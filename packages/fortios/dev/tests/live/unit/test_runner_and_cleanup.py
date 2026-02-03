"""Tests for utility scripts that orchestrate test runs and cleanup.

These do not hit live FortiGate endpoints; we inject fakes to validate
the control flow and filtering logic.
"""

from types import SimpleNamespace
from pathlib import Path

import importlib.util
import importlib

import pytest


def _fake_endpoint(items):
    class Endpoint:
        def __init__(self, items):
            self._items = items
            self.deleted = []

        def get(self):
            return list(self._items)

        def delete(self, **kwargs):
            name = (
                kwargs.get("name")
                or kwargs.get("policyid")
                or kwargs.get("tag")
            )
            # Simulate occasional delete failure
            if name == "raise_me":
                raise RuntimeError("delete failed")
            self.deleted.append(name)

    return Endpoint(items)


def _fake_obj(**kwargs):
    return SimpleNamespace(**kwargs)


def test_cleanup_skips_non_test_objects_and_counts_deletes(monkeypatch):
    # Arrange fake FortiGate client with nested endpoints
    policy = _fake_endpoint([_fake_obj(name="test_policy", policyid=1), _fake_obj(name="keep", policyid=2)])
    addrgrp = _fake_endpoint([_fake_obj(name="test_group"), _fake_obj(name="prod_group")])
    svc_group = _fake_endpoint([_fake_obj(name="test_svcgroup"), _fake_obj(name="other_svcgroup")])
    address = _fake_endpoint([_fake_obj(name="test_addr"), _fake_obj(name="keep_addr")])
    svc_custom = _fake_endpoint([_fake_obj(name="test_service"), _fake_obj(name="keep_service")])
    vip = _fake_endpoint([_fake_obj(name="raise_me")])
    ippool = _fake_endpoint([_fake_obj(name="test_pool"), _fake_obj(name="prod_pool")])
    traffic_shaper = _fake_endpoint([_fake_obj(name="test_shaper")])
    auth_scheme = _fake_endpoint([_fake_obj(name="test_scheme"), _fake_obj(name="keep_scheme")])
    auth_rule = _fake_endpoint([_fake_obj(name="test_rule")])
    av_profile = _fake_endpoint([_fake_obj(name="test_profile")])
    app_list = _fake_endpoint([_fake_obj(name="test_applist")])
    app_custom = _fake_endpoint([_fake_obj(tag="test_tag"), _fake_obj(tag="prod_tag")])
    app_group = _fake_endpoint([_fake_obj(name="test_appgroup"), _fake_obj(name="appgroup_prod")])

    fake_fgt = SimpleNamespace(
        api=SimpleNamespace(
            cmdb=SimpleNamespace(
                firewall=SimpleNamespace(
                    policy=policy,
                    addrgrp=addrgrp,
                    service=SimpleNamespace(group=svc_group, custom=svc_custom),
                    address=address,
                    vip=vip,
                    ippool=ippool,
                    shaper=SimpleNamespace(traffic_shaper=traffic_shaper),
                ),
                authentication=SimpleNamespace(scheme=auth_scheme, rule=auth_rule),
                antivirus=SimpleNamespace(profile=av_profile),
                application=SimpleNamespace(list=app_list, custom=app_custom, group=app_group),
            )
        )
    )

    cleanup_path = Path(__file__).resolve().parent.parent / "cleanup.py"
    spec = importlib.util.spec_from_file_location("hfortix_cleanup", cleanup_path)
    assert spec is not None and spec.loader is not None
    cleanup = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cleanup)  # type: ignore[misc]
    monkeypatch.setattr(cleanup, "fgt", fake_fgt)

    # Act
    deleted_count = cleanup.cleanup_test_objects()

    # Assert: only names starting with test_ (or tag) are deleted; failures are ignored
    assert deleted_count == 13
    assert policy.deleted == [1]  # policyid forwarded
    assert addrgrp.deleted == ["test_group"]
    assert svc_group.deleted == ["test_svcgroup"]
    assert address.deleted == ["test_addr"]
    assert svc_custom.deleted == ["test_service"]
    # vip deletion raises and should be skipped
    assert vip.deleted == []
    assert ippool.deleted == ["test_pool"]
    assert traffic_shaper.deleted == ["test_shaper"]
    assert auth_scheme.deleted == ["test_scheme"]
    assert auth_rule.deleted == ["test_rule"]
    assert av_profile.deleted == ["test_profile"]
    assert app_list.deleted == ["test_applist"]
    assert app_custom.deleted == ["test_tag"]
    assert app_group.deleted == ["test_appgroup"]


def test_discover_test_files_filters_and_includes(tmp_path):
    # Arrange: build a miniature tests tree
    root = tmp_path / "tests"
    root.mkdir()
    (root / "__pycache__").mkdir()
    (root / "x_egde_cases").mkdir()

    # Files that should be excluded
    excluded = {
        "__init__.py": "print('init')",
        "conftest.py": "print('conf')",
        "fgtclient.py": "print('fgt')",
        "cleanup.py": "print('clean')",
        "no_main.py": "print('no main')",
        "x_egde_cases/edge.py": "if __name__ == '__main__': print('edge')",
        "__pycache__/cached.py": "if __name__ == '__main__': print('cache')",
    }

    included = {
        "with_main.py": 'if __name__ == "__main__": print("run")',
        "nested/also_with_main.py": 'if __name__ == "__main__": print("run2")',
    }

    for rel, content in {**excluded, **included}.items():
        dest = root / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)

    import run_tests

    found = run_tests.discover_test_files(root)
    found_rel = {p.relative_to(root).as_posix() for p in found}

    assert found_rel == {"with_main.py", "nested/also_with_main.py"}

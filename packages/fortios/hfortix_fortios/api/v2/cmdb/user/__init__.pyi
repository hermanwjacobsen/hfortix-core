"""Type stubs for USER category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import adgrp
    from . import certificate
    from . import domain_controller
    from . import exchange
    from . import external_identity_provider
    from . import fortitoken
    from . import fsso
    from . import fsso_polling
    from . import group
    from . import krb_keytab
    from . import ldap
    from . import local
    from . import nac_policy
    from . import password_policy
    from . import peer
    from . import peergrp
    from . import pop3
    from . import quarantine
    from . import radius
    from . import saml
    from . import scim
    from . import security_exempt_list
    from . import setting
    from . import tacacs_plus


class User:
    """Type stub for User."""

    adgrp: adgrp.Adgrp
    certificate: certificate.Certificate
    domain_controller: domain_controller.DomainController
    exchange: exchange.Exchange
    external_identity_provider: external_identity_provider.ExternalIdentityProvider
    fortitoken: fortitoken.Fortitoken
    fsso: fsso.Fsso
    fsso_polling: fsso_polling.FssoPolling
    group: group.Group
    krb_keytab: krb_keytab.KrbKeytab
    ldap: ldap.Ldap
    local: local.Local
    nac_policy: nac_policy.NacPolicy
    password_policy: password_policy.PasswordPolicy
    peer: peer.Peer
    peergrp: peergrp.Peergrp
    pop3: pop3.Pop3
    quarantine: quarantine.Quarantine
    radius: radius.Radius
    saml: saml.Saml
    scim: scim.Scim
    security_exempt_list: security_exempt_list.SecurityExemptList
    setting: setting.Setting
    tacacs_plus: tacacs_plus.TacacsPlus

    def __init__(self, client: IHTTPClient) -> None: ...

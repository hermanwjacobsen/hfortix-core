import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from fgtclient import fgt

policies = fgt.api.cmdb.firewall.policy.get()
for policy in policies:
    name = policy.name
    print(f"Policy Name: {name} policyid: {policy.policyid}")   


policy = fgt.api.cmdb.firewall.policy.get(policyid=11)
print(f"Policy ID 1 Name: {policy.name}")


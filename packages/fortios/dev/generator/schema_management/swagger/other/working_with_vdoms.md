ortiOS - Working with VDOMs
Working with VDOMs
If Virtual Domains (VDOMs) are enabled in the FortiGate, queries will by default use the management VDOM. The response will show which VDOM was queried. For example, when the FortiOS REST API for IPv4 firewall policies is queried, the response will end with:

"vdom":"root",
"path":"firewall",
"name":"policy",
"action":"select",
"status":"success",
…
To query a different VDOM (or multiple VDOMs), use the vdom parameter to specify the VDOM(s) from which results are returned or changes are applied to. The URL parameter will be one of:

vdom=root (Single VDOM)

vdom=vdom1,vdom2 (Multiple VDOMs)

vdom=* (All VDOMs)

Examples:

To return results from or apply changes on a specific VDOM (vdom1) use:

GET /api/v2/cmdb/firewall/address/?vdom=vdom1
To return results from or apply changes on multiple VDOMs (vdom1, vdom2) use:

GET /api/v2/cmdb/firewall/address/?vdom=vdom1,vdom2
To return a list of results or to apply changes on all provisioned VDOMs use:

GET /api/v2/cmdb/firewall/address/?vdom=*
Note:

This request is only applicable to VDOMs that the admin has access to. If the admin does not have access to the VDOM, a permission error will be returned.

 Home  FortiOS
FortiOS - Your first REST API request
Your first REST API request
Make your first REST API request from your web browser by using the API token you generated in Generate an API token. All results will be returned. Filter these results in the next two requests by using parameters.

To pass the API token in the request header you will need to use a client tool such as curl or Postman. This example demonstrates the steps for both tools.

Notes:

To ensure maximum security when using API tokens, HTTPS is enforced (HTTP cannot be used).

Also see Using API tokens and REST API administrator best practices for recommended best practices.

Replace the placeholders below with values for your FortiGate:

<YOUR-FORTIGATE-ADDRESS> is the IP address or hostname of your FortiGate as well as the HTTPS port number (default is 443, which does not need to be explicitly specified).
<YOUR-API-TOKEN> is the token you generated in Generate an API token.
Request 1: Return all firewall addresses
Using curl
The backslash (\) allows for multiline commands in curl. You can choose to enter the backslashes or enter the commands into a single wrapping line.

curl --insecure \
  -H "Accept: application/json" \
  -H "Authorization: Bearer <YOUR-API-TOKEN>" https://<YOUR-FORTIGATE-ADDRESS>/api/v2/cmdb/firewall/address
Using Postman
Open the Postman client.
Go to Settings > General and turn off SSL certificate verification.
Click on New and select HTTP
In the new request, click on the Authorization tab, select Type as Bearer Token and enter <YOUR-API-TOKEN> in the Token field.
Enter a URL like the one below:
https://<YOUR-FORTIGATE-ADDRESS>/api/v2/cmdb/firewall/address
Click Send.
Results
curl and Postman will display results that start out similar to the following:

{
    "http_method": "GET",
    "size": 17,
    "limit_reached": false,
    "matched_count": 17,
    "next_idx": 16,
    "revision": "bd002ee1735120907182831e7528dc8b",
    "results": [
        {
            "name": "EMS_ALL_UNKNOWN_CLIENTS",
            "q_origin_key": "EMS_ALL_UNKNOWN_CLIENTS",
            "uuid":"********-****-****-****-************"
            "type": "dynamic",
            "route-tag": 0,
            "sub-type": "ems-tag",
            "clearpass-spt": "unknown",
            "macaddr": [],
            "country": "",
            "cache-ttl": 0,
            "sdn": "",
            "fsso-group": [],
            "interface": "",
            "obj-tag": "",
            "obj-type": "ip",
            "tag-detection-level": "",
            "tag-type": "",
            "dirty": "clean",
            "hw-vendor": "",
            "hw-model": "",
            "os": "",
            "sw-version": "",
            "comment": "",
            "associated-interface": "",
            "color": 0,
            "filter": "",
            "sdn-addr-type": "private",
            "node-ip-only": "disable",
            "obj-id": "",
            "list": [],
            "tagging": [],
            "allow-routing": "disable",
            "fabric-object": "disable"
        },
        {
            "name": "EMS_ALL_UNMANAGEABLE_CLIENTS",
            "q_origin_key": "EMS_ALL_UNMANAGEABLE_CLIENTS",
            "uuid":"********-****-****-****-************",
You can compare these results with what you see in the FortiGate GUI under Policy & Objects > Addresses.

Request 2: Return only the name and comment for all firewall addresses
Using curl
The backslash (\) allows for multiline commands in curl. You can choose to enter the backslashes or enter the commands into a single wrapping line.

curl --insecure \
  -H "Accept: application/json" \
  -H "Authorization: Bearer " https:///api/v2/cmdb/firewall/address?format="name|comment"
Using Postman
Open the Postman client.
Go to Settings > General and turn off SSL certificate verification.
Click on New and select HTTP
In the new request, click on the Authorization tab, select Type as Bearer Token and enter <YOUR-API-TOKEN> in the Token field.
Enter a URL like the one below:
https:///api/v2/cmdb/firewall/address? format=name|comment
Click Send.
Results
curl and Postman will display results that start out similar to the following:

{
    "http_method": "GET",
    "size": 17,
    "limit_reached": false,
    "matched_count": 17,
    "next_idx": 16,
    "revision": "bd002ee1735120907182831e7528dc8b",
    "results": [
        {
            "name": "EMS_ALL_UNKNOWN_CLIENTS",
            "q_origin_key": "EMS_ALL_UNKNOWN_CLIENTS",
            "comment": ""
        },
        {
            "name": "EMS_ALL_UNMANAGEABLE_CLIENTS",
            "q_origin_key": "EMS_ALL_UNMANAGEABLE_CLIENTS",
            "comment": ""
        },
        {
            "name": "FABRIC_DEVICE",
            "q_origin_key": "FABRIC_DEVICE",
            "comment": "IPv4 addresses of Fabric Devices."
        },
Request 3: Return only those entries with "SSLVPN" in the name
Using curl
The backslash (\) allows for multiline commands in curl. You can choose to enter the backslashes or enter the commands into a single wrapping line.

curl --insecure \
  -H "Accept: application/json" \
  -H "Authorization: Bearer " https:///api/v2/cmdb/firewall/address?format="name|comment&filter=name=@SSLVPN"
Using Postman
Open the Postman client.
Go to Settings > General and turn off SSL certificate verification.
Click on New and select HTTP
In the new request, click on the Authorization tab, select Type as Bearer Token and enter <YOUR-API-TOKEN> in the Token field.
Enter a URL like the one below:
https:///api/v2/cmdb/firewall/address? format=name|comment&filter=name=@SSLVPN
Click Send.
Results
curl and Postman will display results that start out similar to the following:

{
    "http_method": "GET",
    "size": 17,
    "limit_reached": false,
    "matched_count": 1,
    "next_idx": 5,
    "revision": "bd002ee1735120907182831e7528dc8b",
    "results": [
        {
            "name": "SSLVPN_TUNNEL_ADDR1",
            "q_origin_key": "SSLVPN_TUNNEL_ADDR1",
            "comment": ""
        }
    ],
    "vdom": "root",
    "path": "firewall",
    "name": "address",
    "status": "success",
    "http_status": 200,
    "serial": "****************",
    "version": "******",
    "build": ****}
FortiOS - Batch transactions
Batch transactions
Batch transaction support was introduced in FortiOS 6.4.0 for Configuration API requests and allows an administrator to submit multiple configuration commands in a single transaction as well as roll back changes (for example if a request fails) prior to committing the transaction.

A batch transaction could be used to create an interface and a DHCP server, where one depends on the other, or it could be used to create a VLAN and then create a policy that references the newly created VLAN.

Multiple batch transactions can run at the same time as long as they do not modify the same tables. For limitations on running multiple batch transactions simultaneously, refer to the Limitations section.

The basic format of a batch transaction is:

Start transaction
Request 1 (e.g. create a VLAN)
Request 2 (e.g. create a policy that references the previously created VLAN)
Before committing the transaction, view the cached commands. (Available with FortiOS 7.4.1 and later)
Commit transaction
 
Note:

Requests in a batch transaction will not be fulfilled if the transaction:

is not committed,
is aborted using transaction-abort, or
expires (based on the timeout set in transaction-start)
 
 
Example workflow for a successful transaction
The example workflow below will use a batch transaction to create a VLAN and then create a policy that references the newly created VLAN. The API request below is in Python using the requests library.

Create a new transaction:
fgt.post('/api/v2/cmdb?action=transaction-start',
   params={'vdom': "root"},
   data={'timeout': 60})
Response from the transaction request:

POST https://172.16.153.93/api/v2/cmdb?action=transaction-start&vdom=root
Succeed status: 200
{u'action': u'transaction-start',
 u'build': 2296,
 u'http_method': u'POST',
 u'http_status': 200,
 u'results': {u'transaction-id': 19},
 u'revision': u'fbfc2b5d6d3f9016dfbbd7dc82c2a044',
 u'revision_changed': False,
 u'serial': u'FG5H1E5818906668',
 u'status': u'success',
 u'vdom': u'root',
 u'version': u'v7.4.1'}
  The response includes the transaction-id of 19. Subsequent requests in this batch must include this transaction-id.

Create a new VLAN and specify the transaction-id (19) in the header of the request:
fgt.post('/api/v2/cmdb/system/interface',
         headers={'X-TRANSACTION-ID': '19'},
         data={'name': 'officeNetwork', 'vdom': 'root', 'vlanid' : '10',
               'mode': 'static', 'ip': '192.168.9.1/24',
               'interface': 'port6'})
 

Create a new policy that uses the newly created VLAN as its source interface. The transaction-id (19) must also be in the header of the request.
fgt.post('/api/v2/cmdb/firewall/policy',
         headers={'X-TRANSACTION-ID': '19'},
         data={'json': {'policyid': 0,
               'srcintf': [{'name': "officeNetwork"}],
               'srcaddr': [{'name': "all"}],
               'dstintf': [{'name': "port3"}],
               'dstaddr': [{'name': "all"}],
               'service': [{'name': "ALL"}],
               'schedule': "always",
               'action': "accept",
               'nat': "enable",
               'utm-status': "enable",
               'application-list': 'default',
               'profile-protocol-options': 'default',
               'logtraffic': "all"}})
 

Before committing the commands, check the cached commands. The transaction-id (19) must be used.
fgt.get('/api/v2/cmdb?action=transaction-show',
         params={'transaction-id': 19})
	
Response from the cached command:

{ 
"http_method":"GET", 
   "revision":"fbfc2b5d6d3f9016dfbbd7dc82c2a044", 
   "results":[ 
      " config vdom", 
      " edit root", 
      "  config system interface", 
      "      edit "officeNetwork"", 
      "          set vdom "root"", 
      "          set ip "192.168.9.1/24"", 
      "          set interface "port6"", 
      "          set "vlanid 10"", 
      "      end", 
      " end", 
      " config vdom", 
      " edit vdom1", 
      "  config firewall policy", 
      "      edit 0", 
      "          set srcintf "officeNetwork"", 
      "          set dstintf "port3""  
      "          set action "accept"", 
      "          set srcaddr "all"", 
      "          set dstaddr "all"", 
      "          set schedule "always"", 
      "          set service "ALL"",     
      "          set nat "enable"",  
      "          set utm-status "enable"", 
      "          set application-list "default"",  
      "          profile-protocol-options "default"", 
      "          logtraffic "all"", 
      "      end", 
      " end" 
 ],   
"vdom":"root",   
"action":"transaction-show", 
 "status":"success", 
  "http_status":200, 
 "serial":"FG5H1E5818906668", 
 "version":"v7.4.1", 
"build":2463 
} 
 

Commit the transaction:
fgt.post('/api/v2/cmdb?action=transaction-commit',
         params={'vdom': "root"},
         data={'transaction-id': 19})
	
Response from the transaction being committed:

POST https://172.16.153.93/api/v2/cmdb?action=transaction-commit&vdom=root
Succeed status: 200
{u'action': u'transaction-commit',
 u'build': 2296,
 u'http_method': u'POST',
 u'http_status': 200,
 u'revision': u'fbfc2b5d6d3f9016dfbbd7dc82c2a044',
 u'revision_changed': False,
 u'serial': u'FG5H1E5818906668',
 u'status': u'success',
 u'vdom': u'root',
 u'version': u'v7.4.1'}
 

Example workflow for a transaction with a request that fails
The example workflow below will use a batch transaction to create a VLAN and then create a policy that references a source interface (homeNetwork) that does not exist. The API request below is in Python using the requests library.

Create a new transaction:
fgt.post('/api/v2/cmdb?action=transaction-start',
   params={'vdom': "root"},
   data={'timeout': 60})
Response from the transaction request:

POST https://172.16.153.93/api/v2/cmdb?action=transaction-start&vdom=root
Succeed status: 200
{u'action': u'transaction-start',
 u'build': 2296,
 u'http_method': u'POST',
 u'http_status': 200,
 u'results': {u'transaction-id': 23},
 u'revision': u'fbfc2b5d6d3f9016dfbbd7dc82c2a044',
 u'revision_changed': False,
 u'serial': u'FG5H1E5818906668',
 u'status': u'success',
 u'vdom': u'root',
 u'version': u'v7.4.1'}
  The response includes the transaction-id of 23. Subsequent requests in this batch must include this transaction-id.

Create a new VLAN and specify the transaction-id (23) in the header of the request:
fgt.post('/api/v2/cmdb/system/interface',
         headers={'X-TRANSACTION-ID': '23'},
         data={'name': 'officeNetwork', 'vdom': 'root', 'vlanid' : '10',
               'mode': 'static', 'ip': '192.168.9.1/24',
               'interface': 'port6'})
Response from the request to create a new VLAN:

POST https://172.16.153.93/api/v2/cmdb/system/interface
Succeed status: 200
{u'build': 2296,
 u'http_method': u'POST',
 u'http_status': 200,
 u'mkey': u'officeNetwork',
 u'name': u'interface',
 u'path': u'system',
 u'revision': u'c63617e0167c28ac6b3dba21da9ffdac',
 u'revision_changed': False,
 u'serial': u'FG5H1E5818906668',
 u'status': u'success',
 u'vdom': u'root',
 u'version': u'v7.4.1'}
Create a new policy that references a source interface (homeNetwork) that does not exist. The transaction-id (23) must also be in the header of the request.
fgt.post('/api/v2/cmdb/firewall/policy',
         headers={'X-TRANSACTION-ID': '23'},
         data={'json': {'policyid': 0,
               'srcintf': [{'name': "homeNetwork"}],
               'srcaddr': [{'name': "all"}],
               'dstintf': [{'name': "officeNetwork"}],
               'dstaddr': [{'name': "all"}],
               'service': [{'name': "ALL"}],
               'schedule': "always",
               'action': "accept",
               'nat': "enable",
               'utm-status': "enable",
               'application-list': 'default',
               'profile-protocol-options': 'default',
               'logtraffic': "all"}})
Response from the request that fails:

POST https://172.16.153.93/api/v2/cmdb/firewall/policy
Fail status: 500
{
  "http_method":"POST",
  "revision":"d9f174eeccad1f0bddaa7e92983f6ce7",
  "revision_changed":false,
  "cli_error":"node_check_object fail! for name homeNetwork\n\nvalue parse error before 'homeNetwork'\nCommand fail. Return code -651\n",
  "error":-651,
  "status":"error",
  "http_status":500,
  "vdom":"root",
  "path":"firewall",
  "name":"policy",
  "serial":"FG5H1E5818906668",
  "version":"v7.4.1",
  "build":2296
}
Abort the transaction:
fgt.post('/api/v2/cmdb?action=transaction-abort',
         params={'vdom': "root"},
         data={'transaction-id': 23})
Response from the transaction being aborted:

POST https://172.16.153.93/api/v2/cmdb?action=transaction-abort&vdom=root
Succeed status: 200
{u'action': u'transaction-abort',
 u'build': 2296,
 u'http_method': u'POST',
 u'http_status': 200,
 u'revision': u'fbfc2b5d6d3f9016dfbbd7dc82c2a044',
 u'revision_changed': False,
 u'serial': u'FG5H1E5818906668',
 u'status': u'success',
 u'vdom': u'root',
 u'version': u'v7.4.1'}
 

As the transaction has been aborted, the "officeNetwork" VLAN and the policy are not created.

Limitations
Multiple batch transactions can run at the same time as long as they do not modify the same tables.

For example, if batch transaction A modifies a firewall table (e.g. it includes requests such as "create a new firewall policy", "edit an existing firewall policy", etc.), then this firewall table is locked until the transaction is committed or aborted. If any other batch transaction includes a request to modify this firewall table before transaction A has been committed or aborted, an error code will be returned.

Some tables do not support transactions. For such tables, an error code will be returned.

Batch transaction options
transaction-list
A GET request that returns a list of all active transactions.

{
   "type":"resource",
   "action":"transaction-list",
   "summary":"List all configuration transaction(s).",
   "request":{
      "http_method":"GET"
   },
   "response":{
   }
},
Example: to return a list of all active transactions, use:

https://<YOUR-FORTGATE-ADDRESS>/api/v2/cmdb?action=transaction-list
 

transaction-start
A POST request that starts a transaction with a specified timeout. It will return a transaction-id. This transaction-id must be included for each subsequent post request in the transaction.

{
   "type":"resource",
   "action":"transaction-start",
   "summary":"Create a new configuration transaction.",
   "request":{
      "http_method":"POST",
      "parameters":[
         {
         "name":"timeout",
         "type":"int",
         "summary":"The transaction timeout in seconds."
         }
      ]
   },
   "response":{
   }
},
 

transaction-show
Available with FortiOS 7.4.1 and later, transaction-show is a GET request that returns the uncommitted, cached changes for a transaction-id.

{
   "type":"resource",
   "action":"transaction-show",
   "summary":"List the operation detail of a transaction.",
   "request":{
      "http_method":"GET"
   },
   "response":{
   }
},
 

transaction-commit
A POST request that commits the transaction. It requires the transaction-id.

{
   "type":"resource",
   "action":"transaction-commit",
   "summary":"Commit a configuration transaction.",
   "request":{
      "http_method":"POST",
       "parameters":[
       {
         "name":"transaction-id",
         "type":"int",
         "summary":"The transaction ID to be committed."
         }
      ]
      },
   "response":{
   }
},
 

transaction-abort
A POST request that aborts a transaction. Once this command is entered, any commands with the same transaction-id will not be committed to the database.

{
   "type":"resource",
   "action":"transaction-abort",
   "summary":"Abort a configuration transaction.",
   "request":{
      "http_method":"POST",
      "parameters":[
         {
            "name":"transaction-id",
            "type":"int",
            "summary":"The transaction ID to be aborted."
         }
      ]
    },
   "response":{
   }
},
FortiOS - Customizing your REST API admin
Customizing your REST API admin
Only an Administrator with a super_admin profile can create a REST API administrator by using the GUI or CLI.

Components of a REST API admin are:

Component

Description

Username

This is the username of the administrator.

Administrator Profile

This is where permissions for the REST API admin are defined.
A REST API admin should have the minimum permissions required to complete the request. For details on permissions, refer to the Administrator profile permissions section below.

PKI Group

Certificate matching is supported as an extra layer of security. Both client certificate and token must match to be granted access to the API.

CORS Allow Origin

Cross Origin Resource Sharing (CORS) allows third-party web apps to make API requests to the FortiGate using the token. To use the FNDN Try it out feature, this option must be enabled to allow requests coming from https://fndn.fortinet.net.

Trusted Hosts

At least one trusted host must be specified to ensure that your localhost can reach the FortiGate:

Multiple trusted hosts/subnets can be configured.

IPv6 hosts are supported.

Allow all (0.0.0.0/0) is not allowed.

You will need your Source Address to create the trusted host. For details on obtaining the Source Address, refer to Tutorial > Generate an API token.

 

Creating a REST API admin using the GUI
Ensure you are an administrator with the super_admin profile.

On the FortiGate GUI, select System > Administrators > Create New > REST API Admin.

Populate the fields as appropriate for your needs.

Click OK and an API token will be generated. Make note of the token as it is only shown once.

 
Creating a REST API admin using the CLI
Ensure you are an administrator with the super_admin profile.
Modify the sample below to create the REST API admin.
config system api-user
   edit "api-admin"
      set comments "admin for API access only"
      set api-key ENC SH23sQt? +/9D9/mKb1oQoDvlP32ggn/cpQeGcY/VGUe5S5WIr5nqU20xcNMYDQE=
      set accprofile "API profile"
      set vdom "root"
      config trusthost
         edit 1
            set ipv4-trusthost 192.168.10.0 255.255.255.0
         next
      end
   next
end
Generate an API token using the CLI command below. Make note of the token as it is only shown once.
execute api-user generate-key <API user name>
In 7.6.3 and above, you may specify the expiry time for the API token using the following option:
execute api-user generate-key <API user name> [expiry in minutes]
 

The API token can also be generated in the GUI or with the following REST API request:

Request

Body data

POST /api/v2/monitor/system/api-user/generate-key?vdom=root

{'api-user':"api-admin"}

 
Administrator profile permissions
After a REST API request is authenticated, the REST API will check if the associated REST API admin has the permissions required to perform the operation. For example, if the REST API admin has the VDOM scope set to "vdom1" and a profile that only has read-only permission to firewall schedules, the REST API admin can only return firewall schedules in “vdom1”, and cannot make changes to them.

Each REST API requires specific group permissions defined in the “Access Group” of the REST API summary table. Requests to the REST API will be checked against this access group to ensure the REST API admin has the required permissions to access the resource.

 

Examples:

A REST API admin with read-only permission to a resource can only send read requests (HTTP GET) to the resource.

A REST API admin with write permission to a resource can send read/write requests (HTTP GET/POST/PUT/DELETE) to the resource.

A REST API admin with no permission to a resource cannot access the resource.

Requests with insufficient profile permissions will return a 403 error.

 

To create an administrator profile:

On the FortiGate GUI, select System > Admin Profile > Create New.

Enter a Name for the New Admin Profile.

Under Access Permissions, select the appropriate permissions.

Click OK.
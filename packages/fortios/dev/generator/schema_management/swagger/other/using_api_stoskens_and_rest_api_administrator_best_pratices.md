FortiOS - Using API tokens and REST API administrator best practices
Using API tokens and REST API administrator best practices
The API token can be included in any REST API request in either the request header or URL parameter. For added security, it is strongly recommended to use API tokens in the request header or transition your applications to include the API token in the request header instead of the URL parameter.

API tokens via request header
To pass the API token in the request header, the user needs to explicitly add the following field to the request header:

Authorization: Bearer <YOUR-API-TOKEN>
API tokens as a URL parameter
To pass the API token as a URL parameter, your FortiGate must first enable this setting. It is recommended to disable this setting when this method is not in use.

config system global
    set rest-api-key-url-query enable
end
Configuring security options when creating a REST API administrator
In addition to using API tokens in the request header, for added security when creating a new REST API administrator, one or more of the following fields should be configured, listed in order of configuration difficulty from easy to difficult:

Trusted Hosts
CORS Allow Origin
PKI Group
See Customizing your REST API admin for detail.

FortiOS - Debugging
Debugging
Verbose output can help with debugging. To enable verbose debugging, use the following commands in the FortiGate CLI:

diagnose debug enable
diagnose debug application httpsd -1
Debug messages will be displayed for 30 minutes and will include debug messages for all requests to/from the FortiOS web interface.

When the REST API for IPv4 policy traffic statistics is queried, REST API related debug messages will be similar to the following:

[httpsd 228 - 1418751787     info] ap_invoke_handler[593] -- new request
    (handler='api_monitor_v2-handler', uri='/api/v2/monitor/firewall/policy/
    select?access_token=******************************', method='GET')

[httpsd 228 - 1418751787     info] ap_invoke_handler[597] -- User-Agent:
    Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,
    like Gecko) Chrome/74.0.3729.131 Safari/537.36

[httpsd 228 - 1418751787     info] ap_invoke_handler[600] -- Source:
    10.100.55.254:57495 Destination: 10.100.55.1:443

[httpsd 228 - 1418751787     info] endpoint_handle_req[625] – received
    api_monitor_v2_request from '10.100.55.254'

[httpsd 228 - 1418751787  warning] api_access_check_for_api_key[965] – API
    Key request authorized for restapiuser from 10.100.55.254.

[httpsd 228 - 1418751787     info] api_store_parameter[241] -- add API
    parameter 'access_token': '********' (type=string)

[httpsd 228 - 1418751787     info] endpoint_process_req_vdom[463] -- new API
    request (action='select',path='firewall',name='policy',vdom='root',
    user='restapiuser')

[httpsd 228 - 1418751787     info] ap_invoke_handler[616] – request
    completed (handler='api_monitor_v2-handler' result==0)
To enable CLI debug, use the command:

diagnose debug cli 8
When CLI debug is enabled, CLI commands for any configuration changes will be logged to the console.

When the Trusted Host is changed in the GUI, the output logged to the console will be similar to the following:

0: config system api-user
0: edit "myapiuser"
0: end
0: config system api-user
0: edit " myapiuser "
0: config trusthost
0: delete 1
0: end
0: end
0: config system api-user
0: edit " myapiuser "
0: config trusthost
0: edit 0
0: set ipv4-trusthost 10.100.55.0 255.255.255.0
0: end
0: end
write config file success, prepare to save in flash
[__create_file_new_version:257] the new version config file
    '/data/./config/sys_global.conf.gz.v000000017' is created
[symlink_config_file:324] a new version of
    '/data/./config/sys_global.conf.gz' is created:
    /data/./config/sys_global.conf.gz.v000000017
[symlink_config_file:367] the old version
    '/data/./config/sys_global.conf.gz.v000000016' is deleted
[symlink_config_file:370] '/data/./config/sys_global.conf.gz' has been
    symlink'ed to the new version
    '/data/./config/sys_global.conf.gz.v000000017'. The old version
    '/data/./config/sys_global.conf.gz.v000000016' has been deleted
zip config file /data/./config/sys_global.conf.gz success!
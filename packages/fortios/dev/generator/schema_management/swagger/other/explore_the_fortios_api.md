FortiOS - Explore the FortiOS REST API
Explore the FortiOS REST API
The FNDN Try it out feature is a specifically designed environment with an easy to use interactive environment that allows you to build requests which you then send to your FortiGate. The Try it out request will come from your (local) browser.

Configure Try it out
Click the gear icon (Config-cps.png) to launch the configuration popup.

Enter information for your FortiGate, as shown below.

TryItOut1.png

Click the Model tab and select your FortiGate model from the dropdown.

TryItOutModel.png

Click OK.

Special considerations
It is recommended to use Chrome to access FNDN to utilize the Try it out feature. Chrome produces more detail errors when Try it out fails.
In case of failure, ensure that:
In the CORS Allow Origin setting on the FortiGate REST API Admin, it is enabled and configured to https://fndn.fortinet.net
The following CLI setting is enabled
config system global
    set rest-api-key-url-query enable
end
The FortiGate HTTPS server certificate is trusted. At minimum, under System > Settings, the HTTPS server certificate should be using Fortinet_GUI_Server instead of the self-signed certificate.
Use Try it out
Tip:

Open a new browser window so you'll have the Tutorial and the Try it out windows side by side.

In the left navigation tree, expand the Configuration API for your version and click firewall.

Scroll down to locate and then click firewall/address.

Tip:

Search for "firewall/address" in the Search box and then select the entry for your version.

Click the entry for GET-firewall-address.png.

Available parameters are listed.

Click Try it out and populate the parameters shown in the image:

TryingItOut-Example.png

Scroll to the end of the parameter list and click Execute.

There will be three responses:

A cURL call

A request URL. This request URL should look familiar as it is for the same request as in the previous step of the tutorial.

Results from querying the API. The results will be identical to those from the previous step of the tutorial.

Now, try using some of the other parameters.
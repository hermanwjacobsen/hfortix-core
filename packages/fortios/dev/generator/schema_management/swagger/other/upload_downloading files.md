FortiOS - Uploading / downloading files
Uploading / downloading files
The monitor API supports the upload and download of files for some endpoints. For example, upload a VM license, download a CA certificate, backup or restore a configuration file.

 
Uploading Files
When uploading a file, the upload file must be stored in the HTTP body. Two methods are supported for uploading a file:

Method

Details

JSON data

The JSON data must be encoded in base64 format.
Encode the file directly into the HTTP body as JSON data using the “file_content” field.

Multi-part file

The multi-part file does not need to be encoded in base64 format.
Include the file in the HTTP body as a multi-part file.

 

Examples:

To upload (restore) a configuration file with JSON data using the Python Requests module, use:

self.session.post(url='/api/v2/monitor/system/config/restore',
     params={"vdom": "vdom1”},
     data={"source": "upload”,
           "scope": "vdom”,
           "file_content": b64encode(open("vd1.conf.txt", "r").read())})
To upload (restore) a configuration file as a multi-part file using the Python Requests module, use:

self.session.post(url='/api/v2/monitor/system/config/restore',
     params={"vdom": "vdom1”},
     data={"source": "upload”,
           "scope": "vdom”,
     files=[('random_name',
           ('random_conf.conf', open("vd1.conf.txt", "r"), 'text/plain'))])
 
Downloading Files
When downloading a file, the downloaded file is stored in the response's raw content, not JSON data. Two methods are supported for downloading a file:

Method

Details

Browser

The browser automatically checks the response header for 'Content-Disposition';: attachment. If present, the browser will download the file to a local directory.

Script

A script will need to be written to check the response header for 'Content-Disposition': attachment. If present, the script will need to write the content to a local file.

 

For example, to use a browser to download a debug report for technical support, use:

https://FortiGateAddress/api/v2/monitor/system/debug/download?access_token=******************************
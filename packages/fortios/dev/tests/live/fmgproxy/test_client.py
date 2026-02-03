from hfortix_fortios import FortiManagerProxy
from hfortix_fortios import FortiOS
import os
from dotenv import load_dotenv

# Load environment variables from .env file in main folder
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

# Connect to FortiManager
fmg = FortiManagerProxy(
    host=os.getenv("FMG_HOST", ""),
    username=os.getenv("FMG_USER", ""),
    password=os.getenv("FMG_PASS", ""),
    verify=False,  # Set True in production with valid certs
    adom="HWJ",  # Default ADOM
)

#Login to FortiManager
fmg.login()

# Proxy to a specific FortiGate device managed by FortiManager
fg = fmg.proxy(device="hwj-fw")

# Example API call through the FortiManager proxy to the FortiGate
response = fg.api.monitor.firmware.extension_device.get(type="fortiswitch")
print(response.json)

logout = fmg.logout()
print(logout.fmg_raw)
                           

"""
Validation helpers for wireless_controller/wids_profile endpoint.

Each endpoint has its own validation file to keep validation logic
separate and maintainable. Use central cmdb._helpers tools for common tasks.

Auto-generated from OpenAPI specification
Customize as needed for endpoint-specific business logic.
"""

from typing import Any, TypedDict, NotRequired, Literal

# Import common validators from central _helpers module
from hfortix_fortios._helpers import (
    validate_enable_disable,
    validate_integer_range,
    validate_string_length,
    validate_port_number,
    validate_ip_address,
    validate_ipv6_address,
    validate_mac_address,
)

# ============================================================================
# Required Fields Validation
# Auto-generated from schema
# ============================================================================

# ⚠️  IMPORTANT: FortiOS schemas have known issues with required field marking:
#
# 1. FALSE POSITIVES: Some fields marked "required" have default values,
#    meaning they're optional (filtered out by generator)
#
# 2. CONDITIONAL REQUIREMENTS: Many endpoints require EITHER field A OR field B:
#    - firewall.policy: requires (srcaddr + dstaddr) OR (srcaddr6 + dstaddr6)
#    - These conditional requirements cannot be expressed in a simple list
#
# 3. SPECIALIZED FEATURES: Fields for WAN optimization, VPN, NAT64, etc.
#    are marked "required" but only apply when using those features
#
# The REQUIRED_FIELDS list below is INFORMATIONAL ONLY and shows fields that:
# - Are marked required in the schema
# - Don't have non-empty default values
# - Aren't specialized feature fields
#
# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "comment": "",
    "sensor-mode": "disable",
    "ap-scan": "disable",
    "ap-bgscan-period": 600,
    "ap-bgscan-intv": 3,
    "ap-bgscan-duration": 30,
    "ap-bgscan-idle": 20,
    "ap-bgscan-report-intv": 30,
    "ap-fgscan-report-intv": 15,
    "ap-scan-passive": "disable",
    "ap-scan-threshold": "-90",
    "ap-auto-suppress": "disable",
    "wireless-bridge": "disable",
    "deauth-broadcast": "disable",
    "null-ssid-probe-resp": "disable",
    "long-duration-attack": "disable",
    "long-duration-thresh": 8200,
    "invalid-mac-oui": "disable",
    "weak-wep-iv": "disable",
    "auth-frame-flood": "disable",
    "auth-flood-time": 10,
    "auth-flood-thresh": 30,
    "assoc-frame-flood": "disable",
    "assoc-flood-time": 10,
    "assoc-flood-thresh": 30,
    "reassoc-flood": "disable",
    "reassoc-flood-time": 10,
    "reassoc-flood-thresh": 30,
    "probe-flood": "disable",
    "probe-flood-time": 1,
    "probe-flood-thresh": 30,
    "bcn-flood": "disable",
    "bcn-flood-time": 1,
    "bcn-flood-thresh": 15,
    "rts-flood": "disable",
    "rts-flood-time": 10,
    "rts-flood-thresh": 30,
    "cts-flood": "disable",
    "cts-flood-time": 10,
    "cts-flood-thresh": 30,
    "client-flood": "disable",
    "client-flood-time": 10,
    "client-flood-thresh": 30,
    "block_ack-flood": "disable",
    "block_ack-flood-time": 1,
    "block_ack-flood-thresh": 50,
    "pspoll-flood": "disable",
    "pspoll-flood-time": 1,
    "pspoll-flood-thresh": 30,
    "netstumbler": "disable",
    "netstumbler-time": 30,
    "netstumbler-thresh": 5,
    "wellenreiter": "disable",
    "wellenreiter-time": 30,
    "wellenreiter-thresh": 5,
    "spoofed-deauth": "disable",
    "asleap-attack": "disable",
    "eapol-start-flood": "disable",
    "eapol-start-thresh": 10,
    "eapol-start-intv": 1,
    "eapol-logoff-flood": "disable",
    "eapol-logoff-thresh": 10,
    "eapol-logoff-intv": 1,
    "eapol-succ-flood": "disable",
    "eapol-succ-thresh": 10,
    "eapol-succ-intv": 1,
    "eapol-fail-flood": "disable",
    "eapol-fail-thresh": 10,
    "eapol-fail-intv": 1,
    "eapol-pre-succ-flood": "disable",
    "eapol-pre-succ-thresh": 10,
    "eapol-pre-succ-intv": 1,
    "eapol-pre-fail-flood": "disable",
    "eapol-pre-fail-thresh": 10,
    "eapol-pre-fail-intv": 1,
    "deauth-unknown-src-thresh": 10,
    "windows-bridge": "disable",
    "disassoc-broadcast": "disable",
    "ap-spoofing": "disable",
    "chan-based-mitm": "disable",
    "adhoc-valid-ssid": "disable",
    "adhoc-network": "disable",
    "eapol-key-overflow": "disable",
    "ap-impersonation": "disable",
    "invalid-addr-combination": "disable",
    "beacon-wrong-channel": "disable",
    "ht-greenfield": "disable",
    "overflow-ie": "disable",
    "malformed-ht-ie": "disable",
    "malformed-auth": "disable",
    "malformed-association": "disable",
    "ht-40mhz-intolerance": "disable",
    "valid-ssid-misuse": "disable",
    "valid-client-misassociation": "disable",
    "hotspotter-attack": "disable",
    "pwsave-dos-attack": "disable",
    "omerta-attack": "disable",
    "disconnect-station": "disable",
    "unencrypted-valid": "disable",
    "fata-jack": "disable",
    "risky-encryption": "disable",
    "fuzzed-beacon": "disable",
    "fuzzed-probe-request": "disable",
    "fuzzed-probe-response": "disable",
    "air-jack": "disable",
    "wpa-ft-attack": "disable",
}

# ============================================================================
# Deprecated Fields
# Auto-generated from schema - warns users about deprecated fields
# ============================================================================

# Deprecated fields with migration guidance
DEPRECATED_FIELDS = {
}

# ============================================================================
# Field Metadata (Type Information & Descriptions)
# Auto-generated from schema - use for IDE autocomplete and documentation
# ============================================================================

# Field types mapping
FIELD_TYPES = {
    "name": "string",  # WIDS profile name.
    "comment": "string",  # Comment.
    "sensor-mode": "option",  # Scan nearby WiFi stations (default = disable).
    "ap-scan": "option",  # Enable/disable rogue AP detection.
    "ap-scan-channel-list-2G-5G": "string",  # Selected ap scan channel list for 2.4G and 5G bands.
    "ap-scan-channel-list-6G": "string",  # Selected ap scan channel list for 6G band.
    "ap-bgscan-period": "integer",  # Period between background scans (10 - 3600 sec, default = 60
    "ap-bgscan-intv": "integer",  # Period between successive channel scans (1 - 600 sec, defaul
    "ap-bgscan-duration": "integer",  # Listen time on scanning a channel (10 - 1000 msec, default =
    "ap-bgscan-idle": "integer",  # Wait time for channel inactivity before scanning this channe
    "ap-bgscan-report-intv": "integer",  # Period between background scan reports (15 - 600 sec, defaul
    "ap-bgscan-disable-schedules": "string",  # Firewall schedules for turning off FortiAP radio background 
    "ap-fgscan-report-intv": "integer",  # Period between foreground scan reports (15 - 600 sec, defaul
    "ap-scan-passive": "option",  # Enable/disable passive scanning. Enable means do not send pr
    "ap-scan-threshold": "string",  # Minimum signal level/threshold in dBm required for the AP to
    "ap-auto-suppress": "option",  # Enable/disable on-wire rogue AP auto-suppression (default = 
    "wireless-bridge": "option",  # Enable/disable wireless bridge detection (default = disable)
    "deauth-broadcast": "option",  # Enable/disable broadcasting de-authentication detection (def
    "null-ssid-probe-resp": "option",  # Enable/disable null SSID probe response detection (default =
    "long-duration-attack": "option",  # Enable/disable long duration attack detection based on user 
    "long-duration-thresh": "integer",  # Threshold value for long duration attack detection (1000 - 3
    "invalid-mac-oui": "option",  # Enable/disable invalid MAC OUI detection.
    "weak-wep-iv": "option",  # Enable/disable weak WEP IV (Initialization Vector) detection
    "auth-frame-flood": "option",  # Enable/disable authentication frame flooding detection (defa
    "auth-flood-time": "integer",  # Number of seconds after which a station is considered not co
    "auth-flood-thresh": "integer",  # The threshold value for authentication frame flooding.
    "assoc-frame-flood": "option",  # Enable/disable association frame flooding detection (default
    "assoc-flood-time": "integer",  # Number of seconds after which a station is considered not co
    "assoc-flood-thresh": "integer",  # The threshold value for association frame flooding.
    "reassoc-flood": "option",  # Enable/disable reassociation flood detection (default = disa
    "reassoc-flood-time": "integer",  # Detection Window Period.
    "reassoc-flood-thresh": "integer",  # The threshold value for reassociation flood.
    "probe-flood": "option",  # Enable/disable probe flood detection (default = disable).
    "probe-flood-time": "integer",  # Detection Window Period.
    "probe-flood-thresh": "integer",  # The threshold value for probe flood.
    "bcn-flood": "option",  # Enable/disable bcn flood detection (default = disable).
    "bcn-flood-time": "integer",  # Detection Window Period.
    "bcn-flood-thresh": "integer",  # The threshold value for bcn flood.
    "rts-flood": "option",  # Enable/disable rts flood detection (default = disable).
    "rts-flood-time": "integer",  # Detection Window Period.
    "rts-flood-thresh": "integer",  # The threshold value for rts flood.
    "cts-flood": "option",  # Enable/disable cts flood detection (default = disable).
    "cts-flood-time": "integer",  # Detection Window Period.
    "cts-flood-thresh": "integer",  # The threshold value for cts flood.
    "client-flood": "option",  # Enable/disable client flood detection (default = disable).
    "client-flood-time": "integer",  # Detection Window Period.
    "client-flood-thresh": "integer",  # The threshold value for client flood.
    "block_ack-flood": "option",  # Enable/disable block_ack flood detection (default = disable)
    "block_ack-flood-time": "integer",  # Detection Window Period.
    "block_ack-flood-thresh": "integer",  # The threshold value for block_ack flood.
    "pspoll-flood": "option",  # Enable/disable pspoll flood detection (default = disable).
    "pspoll-flood-time": "integer",  # Detection Window Period.
    "pspoll-flood-thresh": "integer",  # The threshold value for pspoll flood.
    "netstumbler": "option",  # Enable/disable netstumbler detection (default = disable).
    "netstumbler-time": "integer",  # Detection Window Period.
    "netstumbler-thresh": "integer",  # The threshold value for netstumbler.
    "wellenreiter": "option",  # Enable/disable wellenreiter detection (default = disable).
    "wellenreiter-time": "integer",  # Detection Window Period.
    "wellenreiter-thresh": "integer",  # The threshold value for wellenreiter.
    "spoofed-deauth": "option",  # Enable/disable spoofed de-authentication attack detection (d
    "asleap-attack": "option",  # Enable/disable asleap attack detection (default = disable).
    "eapol-start-flood": "option",  # Enable/disable EAPOL-Start flooding (to AP) detection (defau
    "eapol-start-thresh": "integer",  # The threshold value for EAPOL-Start flooding in specified in
    "eapol-start-intv": "integer",  # The detection interval for EAPOL-Start flooding (1 - 3600 se
    "eapol-logoff-flood": "option",  # Enable/disable EAPOL-Logoff flooding (to AP) detection (defa
    "eapol-logoff-thresh": "integer",  # The threshold value for EAPOL-Logoff flooding in specified i
    "eapol-logoff-intv": "integer",  # The detection interval for EAPOL-Logoff flooding (1 - 3600 s
    "eapol-succ-flood": "option",  # Enable/disable EAPOL-Success flooding (to AP) detection (def
    "eapol-succ-thresh": "integer",  # The threshold value for EAPOL-Success flooding in specified 
    "eapol-succ-intv": "integer",  # The detection interval for EAPOL-Success flooding (1 - 3600 
    "eapol-fail-flood": "option",  # Enable/disable EAPOL-Failure flooding (to AP) detection (def
    "eapol-fail-thresh": "integer",  # The threshold value for EAPOL-Failure flooding in specified 
    "eapol-fail-intv": "integer",  # The detection interval for EAPOL-Failure flooding (1 - 3600 
    "eapol-pre-succ-flood": "option",  # Enable/disable premature EAPOL-Success flooding (to STA) det
    "eapol-pre-succ-thresh": "integer",  # The threshold value for premature EAPOL-Success flooding in 
    "eapol-pre-succ-intv": "integer",  # The detection interval for premature EAPOL-Success flooding 
    "eapol-pre-fail-flood": "option",  # Enable/disable premature EAPOL-Failure flooding (to STA) det
    "eapol-pre-fail-thresh": "integer",  # The threshold value for premature EAPOL-Failure flooding in 
    "eapol-pre-fail-intv": "integer",  # The detection interval for premature EAPOL-Failure flooding 
    "deauth-unknown-src-thresh": "integer",  # Threshold value per second to deauth unknown src for DoS att
    "windows-bridge": "option",  # Enable/disable windows bridge detection (default = disable).
    "disassoc-broadcast": "option",  # Enable/disable broadcast dis-association detection (default 
    "ap-spoofing": "option",  # Enable/disable AP spoofing detection (default = disable).
    "chan-based-mitm": "option",  # Enable/disable channel based mitm detection (default = disab
    "adhoc-valid-ssid": "option",  # Enable/disable adhoc using valid SSID detection (default = d
    "adhoc-network": "option",  # Enable/disable adhoc network detection (default = disable).
    "eapol-key-overflow": "option",  # Enable/disable overflow EAPOL key detection (default = disab
    "ap-impersonation": "option",  # Enable/disable AP impersonation detection (default = disable
    "invalid-addr-combination": "option",  # Enable/disable invalid address combination detection (defaul
    "beacon-wrong-channel": "option",  # Enable/disable beacon wrong channel detection (default = dis
    "ht-greenfield": "option",  # Enable/disable HT greenfield detection (default = disable).
    "overflow-ie": "option",  # Enable/disable overflow IE detection (default = disable).
    "malformed-ht-ie": "option",  # Enable/disable malformed HT IE detection (default = disable)
    "malformed-auth": "option",  # Enable/disable malformed auth frame detection (default = dis
    "malformed-association": "option",  # Enable/disable malformed association request detection (defa
    "ht-40mhz-intolerance": "option",  # Enable/disable HT 40 MHz intolerance detection (default = di
    "valid-ssid-misuse": "option",  # Enable/disable valid SSID misuse detection (default = disabl
    "valid-client-misassociation": "option",  # Enable/disable valid client misassociation detection (defaul
    "hotspotter-attack": "option",  # Enable/disable hotspotter attack detection (default = disabl
    "pwsave-dos-attack": "option",  # Enable/disable power save DOS attack detection (default = di
    "omerta-attack": "option",  # Enable/disable omerta attack detection (default = disable).
    "disconnect-station": "option",  # Enable/disable disconnect station detection (default = disab
    "unencrypted-valid": "option",  # Enable/disable unencrypted valid detection (default = disabl
    "fata-jack": "option",  # Enable/disable FATA-Jack detection (default = disable).
    "risky-encryption": "option",  # Enable/disable Risky Encryption detection (default = disable
    "fuzzed-beacon": "option",  # Enable/disable fuzzed beacon detection (default = disable).
    "fuzzed-probe-request": "option",  # Enable/disable fuzzed probe request detection (default = dis
    "fuzzed-probe-response": "option",  # Enable/disable fuzzed probe response detection (default = di
    "air-jack": "option",  # Enable/disable AirJack detection (default = disable).
    "wpa-ft-attack": "option",  # Enable/disable WPA FT attack detection (default = disable).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "WIDS profile name.",
    "comment": "Comment.",
    "sensor-mode": "Scan nearby WiFi stations (default = disable).",
    "ap-scan": "Enable/disable rogue AP detection.",
    "ap-scan-channel-list-2G-5G": "Selected ap scan channel list for 2.4G and 5G bands.",
    "ap-scan-channel-list-6G": "Selected ap scan channel list for 6G band.",
    "ap-bgscan-period": "Period between background scans (10 - 3600 sec, default = 600).",
    "ap-bgscan-intv": "Period between successive channel scans (1 - 600 sec, default = 3).",
    "ap-bgscan-duration": "Listen time on scanning a channel (10 - 1000 msec, default = 30).",
    "ap-bgscan-idle": "Wait time for channel inactivity before scanning this channel (0 - 1000 msec, default = 20).",
    "ap-bgscan-report-intv": "Period between background scan reports (15 - 600 sec, default = 30).",
    "ap-bgscan-disable-schedules": "Firewall schedules for turning off FortiAP radio background scan. Background scan will be disabled when at least one of the schedules is valid. Separate multiple schedule names with a space.",
    "ap-fgscan-report-intv": "Period between foreground scan reports (15 - 600 sec, default = 15).",
    "ap-scan-passive": "Enable/disable passive scanning. Enable means do not send probe request on any channels (default = disable).",
    "ap-scan-threshold": "Minimum signal level/threshold in dBm required for the AP to report detected rogue AP (-95 to -20, default = -90).",
    "ap-auto-suppress": "Enable/disable on-wire rogue AP auto-suppression (default = disable).",
    "wireless-bridge": "Enable/disable wireless bridge detection (default = disable).",
    "deauth-broadcast": "Enable/disable broadcasting de-authentication detection (default = disable).",
    "null-ssid-probe-resp": "Enable/disable null SSID probe response detection (default = disable).",
    "long-duration-attack": "Enable/disable long duration attack detection based on user configured threshold (default = disable).",
    "long-duration-thresh": "Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200).",
    "invalid-mac-oui": "Enable/disable invalid MAC OUI detection.",
    "weak-wep-iv": "Enable/disable weak WEP IV (Initialization Vector) detection (default = disable).",
    "auth-frame-flood": "Enable/disable authentication frame flooding detection (default = disable).",
    "auth-flood-time": "Number of seconds after which a station is considered not connected.",
    "auth-flood-thresh": "The threshold value for authentication frame flooding.",
    "assoc-frame-flood": "Enable/disable association frame flooding detection (default = disable).",
    "assoc-flood-time": "Number of seconds after which a station is considered not connected.",
    "assoc-flood-thresh": "The threshold value for association frame flooding.",
    "reassoc-flood": "Enable/disable reassociation flood detection (default = disable).",
    "reassoc-flood-time": "Detection Window Period.",
    "reassoc-flood-thresh": "The threshold value for reassociation flood.",
    "probe-flood": "Enable/disable probe flood detection (default = disable).",
    "probe-flood-time": "Detection Window Period.",
    "probe-flood-thresh": "The threshold value for probe flood.",
    "bcn-flood": "Enable/disable bcn flood detection (default = disable).",
    "bcn-flood-time": "Detection Window Period.",
    "bcn-flood-thresh": "The threshold value for bcn flood.",
    "rts-flood": "Enable/disable rts flood detection (default = disable).",
    "rts-flood-time": "Detection Window Period.",
    "rts-flood-thresh": "The threshold value for rts flood.",
    "cts-flood": "Enable/disable cts flood detection (default = disable).",
    "cts-flood-time": "Detection Window Period.",
    "cts-flood-thresh": "The threshold value for cts flood.",
    "client-flood": "Enable/disable client flood detection (default = disable).",
    "client-flood-time": "Detection Window Period.",
    "client-flood-thresh": "The threshold value for client flood.",
    "block_ack-flood": "Enable/disable block_ack flood detection (default = disable).",
    "block_ack-flood-time": "Detection Window Period.",
    "block_ack-flood-thresh": "The threshold value for block_ack flood.",
    "pspoll-flood": "Enable/disable pspoll flood detection (default = disable).",
    "pspoll-flood-time": "Detection Window Period.",
    "pspoll-flood-thresh": "The threshold value for pspoll flood.",
    "netstumbler": "Enable/disable netstumbler detection (default = disable).",
    "netstumbler-time": "Detection Window Period.",
    "netstumbler-thresh": "The threshold value for netstumbler.",
    "wellenreiter": "Enable/disable wellenreiter detection (default = disable).",
    "wellenreiter-time": "Detection Window Period.",
    "wellenreiter-thresh": "The threshold value for wellenreiter.",
    "spoofed-deauth": "Enable/disable spoofed de-authentication attack detection (default = disable).",
    "asleap-attack": "Enable/disable asleap attack detection (default = disable).",
    "eapol-start-flood": "Enable/disable EAPOL-Start flooding (to AP) detection (default = disable).",
    "eapol-start-thresh": "The threshold value for EAPOL-Start flooding in specified interval.",
    "eapol-start-intv": "The detection interval for EAPOL-Start flooding (1 - 3600 sec).",
    "eapol-logoff-flood": "Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable).",
    "eapol-logoff-thresh": "The threshold value for EAPOL-Logoff flooding in specified interval.",
    "eapol-logoff-intv": "The detection interval for EAPOL-Logoff flooding (1 - 3600 sec).",
    "eapol-succ-flood": "Enable/disable EAPOL-Success flooding (to AP) detection (default = disable).",
    "eapol-succ-thresh": "The threshold value for EAPOL-Success flooding in specified interval.",
    "eapol-succ-intv": "The detection interval for EAPOL-Success flooding (1 - 3600 sec).",
    "eapol-fail-flood": "Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable).",
    "eapol-fail-thresh": "The threshold value for EAPOL-Failure flooding in specified interval.",
    "eapol-fail-intv": "The detection interval for EAPOL-Failure flooding (1 - 3600 sec).",
    "eapol-pre-succ-flood": "Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable).",
    "eapol-pre-succ-thresh": "The threshold value for premature EAPOL-Success flooding in specified interval.",
    "eapol-pre-succ-intv": "The detection interval for premature EAPOL-Success flooding (1 - 3600 sec).",
    "eapol-pre-fail-flood": "Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable).",
    "eapol-pre-fail-thresh": "The threshold value for premature EAPOL-Failure flooding in specified interval.",
    "eapol-pre-fail-intv": "The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec).",
    "deauth-unknown-src-thresh": "Threshold value per second to deauth unknown src for DoS attack (0: no limit).",
    "windows-bridge": "Enable/disable windows bridge detection (default = disable).",
    "disassoc-broadcast": "Enable/disable broadcast dis-association detection (default = disable).",
    "ap-spoofing": "Enable/disable AP spoofing detection (default = disable).",
    "chan-based-mitm": "Enable/disable channel based mitm detection (default = disable).",
    "adhoc-valid-ssid": "Enable/disable adhoc using valid SSID detection (default = disable).",
    "adhoc-network": "Enable/disable adhoc network detection (default = disable).",
    "eapol-key-overflow": "Enable/disable overflow EAPOL key detection (default = disable).",
    "ap-impersonation": "Enable/disable AP impersonation detection (default = disable).",
    "invalid-addr-combination": "Enable/disable invalid address combination detection (default = disable).",
    "beacon-wrong-channel": "Enable/disable beacon wrong channel detection (default = disable).",
    "ht-greenfield": "Enable/disable HT greenfield detection (default = disable).",
    "overflow-ie": "Enable/disable overflow IE detection (default = disable).",
    "malformed-ht-ie": "Enable/disable malformed HT IE detection (default = disable).",
    "malformed-auth": "Enable/disable malformed auth frame detection (default = disable).",
    "malformed-association": "Enable/disable malformed association request detection (default = disable).",
    "ht-40mhz-intolerance": "Enable/disable HT 40 MHz intolerance detection (default = disable).",
    "valid-ssid-misuse": "Enable/disable valid SSID misuse detection (default = disable).",
    "valid-client-misassociation": "Enable/disable valid client misassociation detection (default = disable).",
    "hotspotter-attack": "Enable/disable hotspotter attack detection (default = disable).",
    "pwsave-dos-attack": "Enable/disable power save DOS attack detection (default = disable).",
    "omerta-attack": "Enable/disable omerta attack detection (default = disable).",
    "disconnect-station": "Enable/disable disconnect station detection (default = disable).",
    "unencrypted-valid": "Enable/disable unencrypted valid detection (default = disable).",
    "fata-jack": "Enable/disable FATA-Jack detection (default = disable).",
    "risky-encryption": "Enable/disable Risky Encryption detection (default = disable).",
    "fuzzed-beacon": "Enable/disable fuzzed beacon detection (default = disable).",
    "fuzzed-probe-request": "Enable/disable fuzzed probe request detection (default = disable).",
    "fuzzed-probe-response": "Enable/disable fuzzed probe response detection (default = disable).",
    "air-jack": "Enable/disable AirJack detection (default = disable).",
    "wpa-ft-attack": "Enable/disable WPA FT attack detection (default = disable).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 35},
    "comment": {"type": "string", "max_length": 63},
    "ap-bgscan-period": {"type": "integer", "min": 10, "max": 3600},
    "ap-bgscan-intv": {"type": "integer", "min": 1, "max": 600},
    "ap-bgscan-duration": {"type": "integer", "min": 10, "max": 1000},
    "ap-bgscan-idle": {"type": "integer", "min": 0, "max": 1000},
    "ap-bgscan-report-intv": {"type": "integer", "min": 15, "max": 600},
    "ap-fgscan-report-intv": {"type": "integer", "min": 15, "max": 600},
    "ap-scan-threshold": {"type": "string", "max_length": 7},
    "long-duration-thresh": {"type": "integer", "min": 1000, "max": 32767},
    "auth-flood-time": {"type": "integer", "min": 5, "max": 120},
    "auth-flood-thresh": {"type": "integer", "min": 1, "max": 100},
    "assoc-flood-time": {"type": "integer", "min": 5, "max": 120},
    "assoc-flood-thresh": {"type": "integer", "min": 1, "max": 100},
    "reassoc-flood-time": {"type": "integer", "min": 1, "max": 120},
    "reassoc-flood-thresh": {"type": "integer", "min": 1, "max": 65100},
    "probe-flood-time": {"type": "integer", "min": 1, "max": 120},
    "probe-flood-thresh": {"type": "integer", "min": 1, "max": 65100},
    "bcn-flood-time": {"type": "integer", "min": 1, "max": 120},
    "bcn-flood-thresh": {"type": "integer", "min": 1, "max": 65100},
    "rts-flood-time": {"type": "integer", "min": 1, "max": 120},
    "rts-flood-thresh": {"type": "integer", "min": 1, "max": 65100},
    "cts-flood-time": {"type": "integer", "min": 1, "max": 120},
    "cts-flood-thresh": {"type": "integer", "min": 1, "max": 65100},
    "client-flood-time": {"type": "integer", "min": 1, "max": 120},
    "client-flood-thresh": {"type": "integer", "min": 1, "max": 65100},
    "block_ack-flood-time": {"type": "integer", "min": 1, "max": 120},
    "block_ack-flood-thresh": {"type": "integer", "min": 1, "max": 65100},
    "pspoll-flood-time": {"type": "integer", "min": 1, "max": 120},
    "pspoll-flood-thresh": {"type": "integer", "min": 1, "max": 65100},
    "netstumbler-time": {"type": "integer", "min": 1, "max": 120},
    "netstumbler-thresh": {"type": "integer", "min": 1, "max": 65100},
    "wellenreiter-time": {"type": "integer", "min": 1, "max": 120},
    "wellenreiter-thresh": {"type": "integer", "min": 1, "max": 65100},
    "eapol-start-thresh": {"type": "integer", "min": 2, "max": 100},
    "eapol-start-intv": {"type": "integer", "min": 1, "max": 3600},
    "eapol-logoff-thresh": {"type": "integer", "min": 2, "max": 100},
    "eapol-logoff-intv": {"type": "integer", "min": 1, "max": 3600},
    "eapol-succ-thresh": {"type": "integer", "min": 2, "max": 100},
    "eapol-succ-intv": {"type": "integer", "min": 1, "max": 3600},
    "eapol-fail-thresh": {"type": "integer", "min": 2, "max": 100},
    "eapol-fail-intv": {"type": "integer", "min": 1, "max": 3600},
    "eapol-pre-succ-thresh": {"type": "integer", "min": 2, "max": 100},
    "eapol-pre-succ-intv": {"type": "integer", "min": 1, "max": 3600},
    "eapol-pre-fail-thresh": {"type": "integer", "min": 2, "max": 100},
    "eapol-pre-fail-intv": {"type": "integer", "min": 1, "max": 3600},
    "deauth-unknown-src-thresh": {"type": "integer", "min": 0, "max": 65535},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "ap-scan-channel-list-2G-5G": {
        "chan": {
            "type": "string",
            "help": "Channel number.",
            "required": True,
            "default": "",
            "max_length": 3,
        },
    },
    "ap-scan-channel-list-6G": {
        "chan": {
            "type": "string",
            "help": "Channel 6g number.",
            "required": True,
            "default": "",
            "max_length": 3,
        },
    },
    "ap-bgscan-disable-schedules": {
        "name": {
            "type": "string",
            "help": "Schedule name.",
            "required": True,
            "default": "",
            "max_length": 35,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_SENSOR_MODE = [
    "disable",  # Disable the scan.
    "foreign",  # Enable the scan and monitor foreign channels. Foreign channels are all other available channels than the current operating channel.
    "both",  # Enable the scan and monitor both foreign and home channels. Select this option to monitor all WiFi channels.
]
VALID_BODY_AP_SCAN = [
    "disable",  # Disable rogue AP detection.
    "enable",  # Enable rogue AP detection.
]
VALID_BODY_AP_SCAN_PASSIVE = [
    "enable",  # Passive scanning on all channels.
    "disable",  # Passive scanning only on DFS channels.
]
VALID_BODY_AP_AUTO_SUPPRESS = [
    "enable",  # Enable on-wire rogue AP auto-suppression.
    "disable",  # Disable on-wire rogue AP auto-suppression.
]
VALID_BODY_WIRELESS_BRIDGE = [
    "enable",  # Enable wireless bridge detection.
    "disable",  # Disable wireless bridge detection.
]
VALID_BODY_DEAUTH_BROADCAST = [
    "enable",  # Enable broadcast de-authentication detection.
    "disable",  # Disable broadcast de-authentication detection.
]
VALID_BODY_NULL_SSID_PROBE_RESP = [
    "enable",  # Enable null SSID probe resp detection.
    "disable",  # Disable null SSID probe resp detection.
]
VALID_BODY_LONG_DURATION_ATTACK = [
    "enable",  # Enable long duration attack detection.
    "disable",  # Disable long duration attack detection.
]
VALID_BODY_INVALID_MAC_OUI = [
    "enable",  # Enable invalid MAC OUI detection.
    "disable",  # Disable invalid MAC OUI detection.
]
VALID_BODY_WEAK_WEP_IV = [
    "enable",  # Enable weak WEP IV detection.
    "disable",  # Disable weak WEP IV detection.
]
VALID_BODY_AUTH_FRAME_FLOOD = [
    "enable",  # Enable authentication frame flooding detection.
    "disable",  # Disable authentication frame flooding detection.
]
VALID_BODY_ASSOC_FRAME_FLOOD = [
    "enable",  # Enable association frame flooding detection.
    "disable",  # Disable association frame flooding detection.
]
VALID_BODY_REASSOC_FLOOD = [
    "enable",  # Enable reassociation flood detection.
    "disable",  # Disable reassociation flood detection.
]
VALID_BODY_PROBE_FLOOD = [
    "enable",  # Enable probe flood detection.
    "disable",  # Disable probe flood detection.
]
VALID_BODY_BCN_FLOOD = [
    "enable",  # Enable bcn flood detection.
    "disable",  # Disable bcn flood detection.
]
VALID_BODY_RTS_FLOOD = [
    "enable",  # Enable rts flood detection.
    "disable",  # Disable rts flood detection.
]
VALID_BODY_CTS_FLOOD = [
    "enable",  # Enable cts flood detection.
    "disable",  # Disable cts flood detection.
]
VALID_BODY_CLIENT_FLOOD = [
    "enable",  # Enable client flood detection.
    "disable",  # Disable client flood detection.
]
VALID_BODY_BLOCK_ACK_FLOOD = [
    "enable",  # Enable block_ack flood detection.
    "disable",  # Disable block_ack flood detection.
]
VALID_BODY_PSPOLL_FLOOD = [
    "enable",  # Enable pspoll flood detection.
    "disable",  # Disable pspoll flood detection.
]
VALID_BODY_NETSTUMBLER = [
    "enable",  # Enable netstumbler detection.
    "disable",  # Disable netstumbler detection.
]
VALID_BODY_WELLENREITER = [
    "enable",  # Enable wellenreiter detection.
    "disable",  # Disable wellenreiter detection.
]
VALID_BODY_SPOOFED_DEAUTH = [
    "enable",  # Enable spoofed de-authentication attack detection.
    "disable",  # Disable spoofed de-authentication attack detection.
]
VALID_BODY_ASLEAP_ATTACK = [
    "enable",  # Enable asleap attack detection.
    "disable",  # Disable asleap attack detection.
]
VALID_BODY_EAPOL_START_FLOOD = [
    "enable",  # Enable EAPOL-Start flooding detection.
    "disable",  # Disable EAPOL-Start flooding detection.
]
VALID_BODY_EAPOL_LOGOFF_FLOOD = [
    "enable",  # Enable EAPOL-Logoff flooding detection.
    "disable",  # Disable EAPOL-Logoff flooding detection.
]
VALID_BODY_EAPOL_SUCC_FLOOD = [
    "enable",  # Enable EAPOL-Success flooding detection.
    "disable",  # Disable EAPOL-Success flooding detection.
]
VALID_BODY_EAPOL_FAIL_FLOOD = [
    "enable",  # Enable EAPOL-Failure flooding detection.
    "disable",  # Disable EAPOL-Failure flooding detection.
]
VALID_BODY_EAPOL_PRE_SUCC_FLOOD = [
    "enable",  # Enable premature EAPOL-Success flooding detection.
    "disable",  # Disable premature EAPOL-Success flooding detection.
]
VALID_BODY_EAPOL_PRE_FAIL_FLOOD = [
    "enable",  # Enable premature EAPOL-Failure flooding detection.
    "disable",  # Disable premature EAPOL-Failure flooding detection.
]
VALID_BODY_WINDOWS_BRIDGE = [
    "enable",  # Enable windows bridge detection.
    "disable",  # Disable windows bridge detection.
]
VALID_BODY_DISASSOC_BROADCAST = [
    "enable",  # Enable broadcast dis-association detection.
    "disable",  # Disable broadcast dis-association detection.
]
VALID_BODY_AP_SPOOFING = [
    "enable",  # Enable AP spoofing detection.
    "disable",  # Disable AP spoofing detection.
]
VALID_BODY_CHAN_BASED_MITM = [
    "enable",  # Enable channel based mitm detection.
    "disable",  # Disable channel based mitm detection.
]
VALID_BODY_ADHOC_VALID_SSID = [
    "enable",  # Enable adhoc using valid SSID detection.
    "disable",  # Disable adhoc using valid SSID detection.
]
VALID_BODY_ADHOC_NETWORK = [
    "enable",  # Enable adhoc network detection.
    "disable",  # Disable adhoc network detection.
]
VALID_BODY_EAPOL_KEY_OVERFLOW = [
    "enable",  # Enable overflow EAPOL key detection.
    "disable",  # Disable overflow EAPOL key detection.
]
VALID_BODY_AP_IMPERSONATION = [
    "enable",  # Enable AP impersonation detection.
    "disable",  # Disable AP impersonation detection.
]
VALID_BODY_INVALID_ADDR_COMBINATION = [
    "enable",  # Enable invalid address combination detection.
    "disable",  # Disable invalid address combination detection.
]
VALID_BODY_BEACON_WRONG_CHANNEL = [
    "enable",  # Enable beacon wrong channel detection.
    "disable",  # Disable beacon wrong channel detection.
]
VALID_BODY_HT_GREENFIELD = [
    "enable",  # Enable HT greenfield detection.
    "disable",  # Disable HT greenfield detection.
]
VALID_BODY_OVERFLOW_IE = [
    "enable",  # Enable overflow IE detection.
    "disable",  # Disable overflow IE detection.
]
VALID_BODY_MALFORMED_HT_IE = [
    "enable",  # Enable malformed HT IE detection.
    "disable",  # Disable malformed HT IE detection.
]
VALID_BODY_MALFORMED_AUTH = [
    "enable",  # Enable malformed auth frame detection.
    "disable",  # Disable malformed auth frame detection.
]
VALID_BODY_MALFORMED_ASSOCIATION = [
    "enable",  # Enable malformed association request detection.
    "disable",  # Disable malformed association request detection.
]
VALID_BODY_HT_40MHZ_INTOLERANCE = [
    "enable",  # Enable HT 40 MHz intolerance detection.
    "disable",  # Disable HT 40 MHz intolerance detection.
]
VALID_BODY_VALID_SSID_MISUSE = [
    "enable",  # Enable valid SSID misuse detection.
    "disable",  # Disable valid SSID misuse detection.
]
VALID_BODY_VALID_CLIENT_MISASSOCIATION = [
    "enable",  # Enable valid client misassociation detection.
    "disable",  # Disable valid client misassociation detection.
]
VALID_BODY_HOTSPOTTER_ATTACK = [
    "enable",  # Enable hotspotter attack detection.
    "disable",  # Disable hotspotter attack detection.
]
VALID_BODY_PWSAVE_DOS_ATTACK = [
    "enable",  # Enable power save DOS attack detection.
    "disable",  # Disable power save DOS attack detection.
]
VALID_BODY_OMERTA_ATTACK = [
    "enable",  # Enable omerta attack detection.
    "disable",  # Disable omerta attack detection.
]
VALID_BODY_DISCONNECT_STATION = [
    "enable",  # Enable disconnect station detection.
    "disable",  # Disable disconnect station detection.
]
VALID_BODY_UNENCRYPTED_VALID = [
    "enable",  # Enable unencrypted valid detection.
    "disable",  # Disable unencrypted valid detection.
]
VALID_BODY_FATA_JACK = [
    "enable",  # Enable FATA-Jack detection.
    "disable",  # Disable FATA-Jack detection.
]
VALID_BODY_RISKY_ENCRYPTION = [
    "enable",  # Enable Risky Encryption detection.
    "disable",  # Disable Risky Encryption detection.
]
VALID_BODY_FUZZED_BEACON = [
    "enable",  # Enable fuzzed beacon detection.
    "disable",  # Disable fuzzed beacon detection.
]
VALID_BODY_FUZZED_PROBE_REQUEST = [
    "enable",  # Enable fuzzed probe request detection.
    "disable",  # Disable fuzzed probe request detection.
]
VALID_BODY_FUZZED_PROBE_RESPONSE = [
    "enable",  # Enable fuzzed probe response detection.
    "disable",  # Disable fuzzed probe response detection.
]
VALID_BODY_AIR_JACK = [
    "enable",  # Enable AirJack detection.
    "disable",  # Disable AirJack detection.
]
VALID_BODY_WPA_FT_ATTACK = [
    "enable",  # Enable WPA FT attack detection.
    "disable",  # Disable WPA FT attack detection.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_wireless_controller_wids_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate GET request parameters for wireless_controller/wids_profile.

    Args:
        attr: Attribute filter (optional)
        filters: Additional filter parameters
        **params: Other query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Examples:
        >>> # Valid - Get all items
        >>> is_valid, error = validate_wireless_controller_wids_profile_get()
        >>> assert is_valid == True
        
        >>> # Valid - Get specific item by name
        >>> is_valid, error = validate_wireless_controller_wids_profile_get(name="test-item")
        >>> assert is_valid == True
        
        >>> # Valid - With filters
        >>> is_valid, error = validate_wireless_controller_wids_profile_get(
        ...     filters={"format": "name|type"}
        ... )
        >>> assert is_valid == True
    """
    # Validate query parameters if present
    if "action" in params:
        value = params.get("action")
        if value and value not in VALID_QUERY_ACTION:
            return (
                False,
                f"Invalid query parameter 'action'='{value}'. Must be one of: {', '.join(VALID_QUERY_ACTION)}",
            )

    return (True, None)


# ============================================================================
# POST Validation
# ============================================================================


def validate_required_fields(payload: dict) -> tuple[bool, str | None]:
    """
    Validate required fields for wireless_controller/wids_profile.

    This validator checks:
    1. Always-required fields are present
    2. Mutually exclusive groups have at least one field

    Args:
        payload: The request payload to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "test"}
        >>> is_valid, error = validate_required_fields(payload)
    """
    # Check always-required fields
    missing_fields = []
    for field in REQUIRED_FIELDS:
        if field not in payload:
            missing_fields.append(field)
    
    if missing_fields:
        # Build enhanced error message
        error_parts = [f"Missing required field(s): {', '.join(missing_fields)}"]
        
        # Add descriptions for first few missing fields
        for field in missing_fields[:3]:
            desc = FIELD_DESCRIPTIONS.get(field)
            if desc:
                error_parts.append(f"  • {field}: {desc}")
        
        if len(missing_fields) > 3:
            error_parts.append(f"  ... and {len(missing_fields) - 3} more")
        
        return (False, "\n".join(error_parts))

    return (True, None)


def validate_wireless_controller_wids_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate POST request to create new wireless_controller/wids_profile object.

    This validator performs two-stage validation:
    1. Required fields check (schema-based)
    2. Field value validation (enums, ranges, formats)

    Args:
        payload: Request body data with configuration
        **params: Query parameters (vdom, etc.)

    Returns:
        Tuple of (is_valid, error_message)
        - is_valid: True if payload is valid, False otherwise
        - error_message: None if valid, detailed error string if invalid

    Examples:
        >>> # ✅ Valid - Minimal required fields
        >>> payload = {
        ... }
        >>> is_valid, error = validate_wireless_controller_wids_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ✅ Valid - With enum field
        >>> payload = {
        ...     "sensor-mode": "{'name': 'disable', 'help': 'Disable the scan.', 'label': 'Disable', 'description': 'Disable the scan'}",  # Valid enum value
        ... }
        >>> is_valid, error = validate_wireless_controller_wids_profile_post(payload)
        >>> assert is_valid == True
        
        >>> # ❌ Invalid - Wrong enum value
        >>> payload["sensor-mode"] = "invalid-value"
        >>> is_valid, error = validate_wireless_controller_wids_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Invalid value" in error
        
        >>> # ❌ Invalid - Missing required field
        >>> payload = {}  # Empty payload
        >>> is_valid, error = validate_wireless_controller_wids_profile_post(payload)
        >>> assert is_valid == False
        >>> assert "Missing required field" in error
    """
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "sensor-mode" in payload:
        value = payload["sensor-mode"]
        if value not in VALID_BODY_SENSOR_MODE:
            desc = FIELD_DESCRIPTIONS.get("sensor-mode", "")
            error_msg = f"Invalid value for 'sensor-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SENSOR_MODE)}"
            error_msg += f"\n  → Example: sensor-mode='{{ VALID_BODY_SENSOR_MODE[0] }}'"
            return (False, error_msg)
    if "ap-scan" in payload:
        value = payload["ap-scan"]
        if value not in VALID_BODY_AP_SCAN:
            desc = FIELD_DESCRIPTIONS.get("ap-scan", "")
            error_msg = f"Invalid value for 'ap-scan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_SCAN)}"
            error_msg += f"\n  → Example: ap-scan='{{ VALID_BODY_AP_SCAN[0] }}'"
            return (False, error_msg)
    if "ap-scan-passive" in payload:
        value = payload["ap-scan-passive"]
        if value not in VALID_BODY_AP_SCAN_PASSIVE:
            desc = FIELD_DESCRIPTIONS.get("ap-scan-passive", "")
            error_msg = f"Invalid value for 'ap-scan-passive': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_SCAN_PASSIVE)}"
            error_msg += f"\n  → Example: ap-scan-passive='{{ VALID_BODY_AP_SCAN_PASSIVE[0] }}'"
            return (False, error_msg)
    if "ap-auto-suppress" in payload:
        value = payload["ap-auto-suppress"]
        if value not in VALID_BODY_AP_AUTO_SUPPRESS:
            desc = FIELD_DESCRIPTIONS.get("ap-auto-suppress", "")
            error_msg = f"Invalid value for 'ap-auto-suppress': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_AUTO_SUPPRESS)}"
            error_msg += f"\n  → Example: ap-auto-suppress='{{ VALID_BODY_AP_AUTO_SUPPRESS[0] }}'"
            return (False, error_msg)
    if "wireless-bridge" in payload:
        value = payload["wireless-bridge"]
        if value not in VALID_BODY_WIRELESS_BRIDGE:
            desc = FIELD_DESCRIPTIONS.get("wireless-bridge", "")
            error_msg = f"Invalid value for 'wireless-bridge': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WIRELESS_BRIDGE)}"
            error_msg += f"\n  → Example: wireless-bridge='{{ VALID_BODY_WIRELESS_BRIDGE[0] }}'"
            return (False, error_msg)
    if "deauth-broadcast" in payload:
        value = payload["deauth-broadcast"]
        if value not in VALID_BODY_DEAUTH_BROADCAST:
            desc = FIELD_DESCRIPTIONS.get("deauth-broadcast", "")
            error_msg = f"Invalid value for 'deauth-broadcast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DEAUTH_BROADCAST)}"
            error_msg += f"\n  → Example: deauth-broadcast='{{ VALID_BODY_DEAUTH_BROADCAST[0] }}'"
            return (False, error_msg)
    if "null-ssid-probe-resp" in payload:
        value = payload["null-ssid-probe-resp"]
        if value not in VALID_BODY_NULL_SSID_PROBE_RESP:
            desc = FIELD_DESCRIPTIONS.get("null-ssid-probe-resp", "")
            error_msg = f"Invalid value for 'null-ssid-probe-resp': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NULL_SSID_PROBE_RESP)}"
            error_msg += f"\n  → Example: null-ssid-probe-resp='{{ VALID_BODY_NULL_SSID_PROBE_RESP[0] }}'"
            return (False, error_msg)
    if "long-duration-attack" in payload:
        value = payload["long-duration-attack"]
        if value not in VALID_BODY_LONG_DURATION_ATTACK:
            desc = FIELD_DESCRIPTIONS.get("long-duration-attack", "")
            error_msg = f"Invalid value for 'long-duration-attack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_LONG_DURATION_ATTACK)}"
            error_msg += f"\n  → Example: long-duration-attack='{{ VALID_BODY_LONG_DURATION_ATTACK[0] }}'"
            return (False, error_msg)
    if "invalid-mac-oui" in payload:
        value = payload["invalid-mac-oui"]
        if value not in VALID_BODY_INVALID_MAC_OUI:
            desc = FIELD_DESCRIPTIONS.get("invalid-mac-oui", "")
            error_msg = f"Invalid value for 'invalid-mac-oui': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INVALID_MAC_OUI)}"
            error_msg += f"\n  → Example: invalid-mac-oui='{{ VALID_BODY_INVALID_MAC_OUI[0] }}'"
            return (False, error_msg)
    if "weak-wep-iv" in payload:
        value = payload["weak-wep-iv"]
        if value not in VALID_BODY_WEAK_WEP_IV:
            desc = FIELD_DESCRIPTIONS.get("weak-wep-iv", "")
            error_msg = f"Invalid value for 'weak-wep-iv': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WEAK_WEP_IV)}"
            error_msg += f"\n  → Example: weak-wep-iv='{{ VALID_BODY_WEAK_WEP_IV[0] }}'"
            return (False, error_msg)
    if "auth-frame-flood" in payload:
        value = payload["auth-frame-flood"]
        if value not in VALID_BODY_AUTH_FRAME_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("auth-frame-flood", "")
            error_msg = f"Invalid value for 'auth-frame-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AUTH_FRAME_FLOOD)}"
            error_msg += f"\n  → Example: auth-frame-flood='{{ VALID_BODY_AUTH_FRAME_FLOOD[0] }}'"
            return (False, error_msg)
    if "assoc-frame-flood" in payload:
        value = payload["assoc-frame-flood"]
        if value not in VALID_BODY_ASSOC_FRAME_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("assoc-frame-flood", "")
            error_msg = f"Invalid value for 'assoc-frame-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASSOC_FRAME_FLOOD)}"
            error_msg += f"\n  → Example: assoc-frame-flood='{{ VALID_BODY_ASSOC_FRAME_FLOOD[0] }}'"
            return (False, error_msg)
    if "reassoc-flood" in payload:
        value = payload["reassoc-flood"]
        if value not in VALID_BODY_REASSOC_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("reassoc-flood", "")
            error_msg = f"Invalid value for 'reassoc-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_REASSOC_FLOOD)}"
            error_msg += f"\n  → Example: reassoc-flood='{{ VALID_BODY_REASSOC_FLOOD[0] }}'"
            return (False, error_msg)
    if "probe-flood" in payload:
        value = payload["probe-flood"]
        if value not in VALID_BODY_PROBE_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("probe-flood", "")
            error_msg = f"Invalid value for 'probe-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PROBE_FLOOD)}"
            error_msg += f"\n  → Example: probe-flood='{{ VALID_BODY_PROBE_FLOOD[0] }}'"
            return (False, error_msg)
    if "bcn-flood" in payload:
        value = payload["bcn-flood"]
        if value not in VALID_BODY_BCN_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("bcn-flood", "")
            error_msg = f"Invalid value for 'bcn-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BCN_FLOOD)}"
            error_msg += f"\n  → Example: bcn-flood='{{ VALID_BODY_BCN_FLOOD[0] }}'"
            return (False, error_msg)
    if "rts-flood" in payload:
        value = payload["rts-flood"]
        if value not in VALID_BODY_RTS_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("rts-flood", "")
            error_msg = f"Invalid value for 'rts-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RTS_FLOOD)}"
            error_msg += f"\n  → Example: rts-flood='{{ VALID_BODY_RTS_FLOOD[0] }}'"
            return (False, error_msg)
    if "cts-flood" in payload:
        value = payload["cts-flood"]
        if value not in VALID_BODY_CTS_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("cts-flood", "")
            error_msg = f"Invalid value for 'cts-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CTS_FLOOD)}"
            error_msg += f"\n  → Example: cts-flood='{{ VALID_BODY_CTS_FLOOD[0] }}'"
            return (False, error_msg)
    if "client-flood" in payload:
        value = payload["client-flood"]
        if value not in VALID_BODY_CLIENT_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("client-flood", "")
            error_msg = f"Invalid value for 'client-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CLIENT_FLOOD)}"
            error_msg += f"\n  → Example: client-flood='{{ VALID_BODY_CLIENT_FLOOD[0] }}'"
            return (False, error_msg)
    if "block_ack-flood" in payload:
        value = payload["block_ack-flood"]
        if value not in VALID_BODY_BLOCK_ACK_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("block_ack-flood", "")
            error_msg = f"Invalid value for 'block_ack-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BLOCK_ACK_FLOOD)}"
            error_msg += f"\n  → Example: block_ack-flood='{{ VALID_BODY_BLOCK_ACK_FLOOD[0] }}'"
            return (False, error_msg)
    if "pspoll-flood" in payload:
        value = payload["pspoll-flood"]
        if value not in VALID_BODY_PSPOLL_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("pspoll-flood", "")
            error_msg = f"Invalid value for 'pspoll-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PSPOLL_FLOOD)}"
            error_msg += f"\n  → Example: pspoll-flood='{{ VALID_BODY_PSPOLL_FLOOD[0] }}'"
            return (False, error_msg)
    if "netstumbler" in payload:
        value = payload["netstumbler"]
        if value not in VALID_BODY_NETSTUMBLER:
            desc = FIELD_DESCRIPTIONS.get("netstumbler", "")
            error_msg = f"Invalid value for 'netstumbler': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_NETSTUMBLER)}"
            error_msg += f"\n  → Example: netstumbler='{{ VALID_BODY_NETSTUMBLER[0] }}'"
            return (False, error_msg)
    if "wellenreiter" in payload:
        value = payload["wellenreiter"]
        if value not in VALID_BODY_WELLENREITER:
            desc = FIELD_DESCRIPTIONS.get("wellenreiter", "")
            error_msg = f"Invalid value for 'wellenreiter': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WELLENREITER)}"
            error_msg += f"\n  → Example: wellenreiter='{{ VALID_BODY_WELLENREITER[0] }}'"
            return (False, error_msg)
    if "spoofed-deauth" in payload:
        value = payload["spoofed-deauth"]
        if value not in VALID_BODY_SPOOFED_DEAUTH:
            desc = FIELD_DESCRIPTIONS.get("spoofed-deauth", "")
            error_msg = f"Invalid value for 'spoofed-deauth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SPOOFED_DEAUTH)}"
            error_msg += f"\n  → Example: spoofed-deauth='{{ VALID_BODY_SPOOFED_DEAUTH[0] }}'"
            return (False, error_msg)
    if "asleap-attack" in payload:
        value = payload["asleap-attack"]
        if value not in VALID_BODY_ASLEAP_ATTACK:
            desc = FIELD_DESCRIPTIONS.get("asleap-attack", "")
            error_msg = f"Invalid value for 'asleap-attack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ASLEAP_ATTACK)}"
            error_msg += f"\n  → Example: asleap-attack='{{ VALID_BODY_ASLEAP_ATTACK[0] }}'"
            return (False, error_msg)
    if "eapol-start-flood" in payload:
        value = payload["eapol-start-flood"]
        if value not in VALID_BODY_EAPOL_START_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("eapol-start-flood", "")
            error_msg = f"Invalid value for 'eapol-start-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAPOL_START_FLOOD)}"
            error_msg += f"\n  → Example: eapol-start-flood='{{ VALID_BODY_EAPOL_START_FLOOD[0] }}'"
            return (False, error_msg)
    if "eapol-logoff-flood" in payload:
        value = payload["eapol-logoff-flood"]
        if value not in VALID_BODY_EAPOL_LOGOFF_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("eapol-logoff-flood", "")
            error_msg = f"Invalid value for 'eapol-logoff-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAPOL_LOGOFF_FLOOD)}"
            error_msg += f"\n  → Example: eapol-logoff-flood='{{ VALID_BODY_EAPOL_LOGOFF_FLOOD[0] }}'"
            return (False, error_msg)
    if "eapol-succ-flood" in payload:
        value = payload["eapol-succ-flood"]
        if value not in VALID_BODY_EAPOL_SUCC_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("eapol-succ-flood", "")
            error_msg = f"Invalid value for 'eapol-succ-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAPOL_SUCC_FLOOD)}"
            error_msg += f"\n  → Example: eapol-succ-flood='{{ VALID_BODY_EAPOL_SUCC_FLOOD[0] }}'"
            return (False, error_msg)
    if "eapol-fail-flood" in payload:
        value = payload["eapol-fail-flood"]
        if value not in VALID_BODY_EAPOL_FAIL_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("eapol-fail-flood", "")
            error_msg = f"Invalid value for 'eapol-fail-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAPOL_FAIL_FLOOD)}"
            error_msg += f"\n  → Example: eapol-fail-flood='{{ VALID_BODY_EAPOL_FAIL_FLOOD[0] }}'"
            return (False, error_msg)
    if "eapol-pre-succ-flood" in payload:
        value = payload["eapol-pre-succ-flood"]
        if value not in VALID_BODY_EAPOL_PRE_SUCC_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("eapol-pre-succ-flood", "")
            error_msg = f"Invalid value for 'eapol-pre-succ-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAPOL_PRE_SUCC_FLOOD)}"
            error_msg += f"\n  → Example: eapol-pre-succ-flood='{{ VALID_BODY_EAPOL_PRE_SUCC_FLOOD[0] }}'"
            return (False, error_msg)
    if "eapol-pre-fail-flood" in payload:
        value = payload["eapol-pre-fail-flood"]
        if value not in VALID_BODY_EAPOL_PRE_FAIL_FLOOD:
            desc = FIELD_DESCRIPTIONS.get("eapol-pre-fail-flood", "")
            error_msg = f"Invalid value for 'eapol-pre-fail-flood': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAPOL_PRE_FAIL_FLOOD)}"
            error_msg += f"\n  → Example: eapol-pre-fail-flood='{{ VALID_BODY_EAPOL_PRE_FAIL_FLOOD[0] }}'"
            return (False, error_msg)
    if "windows-bridge" in payload:
        value = payload["windows-bridge"]
        if value not in VALID_BODY_WINDOWS_BRIDGE:
            desc = FIELD_DESCRIPTIONS.get("windows-bridge", "")
            error_msg = f"Invalid value for 'windows-bridge': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WINDOWS_BRIDGE)}"
            error_msg += f"\n  → Example: windows-bridge='{{ VALID_BODY_WINDOWS_BRIDGE[0] }}'"
            return (False, error_msg)
    if "disassoc-broadcast" in payload:
        value = payload["disassoc-broadcast"]
        if value not in VALID_BODY_DISASSOC_BROADCAST:
            desc = FIELD_DESCRIPTIONS.get("disassoc-broadcast", "")
            error_msg = f"Invalid value for 'disassoc-broadcast': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DISASSOC_BROADCAST)}"
            error_msg += f"\n  → Example: disassoc-broadcast='{{ VALID_BODY_DISASSOC_BROADCAST[0] }}'"
            return (False, error_msg)
    if "ap-spoofing" in payload:
        value = payload["ap-spoofing"]
        if value not in VALID_BODY_AP_SPOOFING:
            desc = FIELD_DESCRIPTIONS.get("ap-spoofing", "")
            error_msg = f"Invalid value for 'ap-spoofing': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_SPOOFING)}"
            error_msg += f"\n  → Example: ap-spoofing='{{ VALID_BODY_AP_SPOOFING[0] }}'"
            return (False, error_msg)
    if "chan-based-mitm" in payload:
        value = payload["chan-based-mitm"]
        if value not in VALID_BODY_CHAN_BASED_MITM:
            desc = FIELD_DESCRIPTIONS.get("chan-based-mitm", "")
            error_msg = f"Invalid value for 'chan-based-mitm': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_CHAN_BASED_MITM)}"
            error_msg += f"\n  → Example: chan-based-mitm='{{ VALID_BODY_CHAN_BASED_MITM[0] }}'"
            return (False, error_msg)
    if "adhoc-valid-ssid" in payload:
        value = payload["adhoc-valid-ssid"]
        if value not in VALID_BODY_ADHOC_VALID_SSID:
            desc = FIELD_DESCRIPTIONS.get("adhoc-valid-ssid", "")
            error_msg = f"Invalid value for 'adhoc-valid-ssid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADHOC_VALID_SSID)}"
            error_msg += f"\n  → Example: adhoc-valid-ssid='{{ VALID_BODY_ADHOC_VALID_SSID[0] }}'"
            return (False, error_msg)
    if "adhoc-network" in payload:
        value = payload["adhoc-network"]
        if value not in VALID_BODY_ADHOC_NETWORK:
            desc = FIELD_DESCRIPTIONS.get("adhoc-network", "")
            error_msg = f"Invalid value for 'adhoc-network': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ADHOC_NETWORK)}"
            error_msg += f"\n  → Example: adhoc-network='{{ VALID_BODY_ADHOC_NETWORK[0] }}'"
            return (False, error_msg)
    if "eapol-key-overflow" in payload:
        value = payload["eapol-key-overflow"]
        if value not in VALID_BODY_EAPOL_KEY_OVERFLOW:
            desc = FIELD_DESCRIPTIONS.get("eapol-key-overflow", "")
            error_msg = f"Invalid value for 'eapol-key-overflow': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EAPOL_KEY_OVERFLOW)}"
            error_msg += f"\n  → Example: eapol-key-overflow='{{ VALID_BODY_EAPOL_KEY_OVERFLOW[0] }}'"
            return (False, error_msg)
    if "ap-impersonation" in payload:
        value = payload["ap-impersonation"]
        if value not in VALID_BODY_AP_IMPERSONATION:
            desc = FIELD_DESCRIPTIONS.get("ap-impersonation", "")
            error_msg = f"Invalid value for 'ap-impersonation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AP_IMPERSONATION)}"
            error_msg += f"\n  → Example: ap-impersonation='{{ VALID_BODY_AP_IMPERSONATION[0] }}'"
            return (False, error_msg)
    if "invalid-addr-combination" in payload:
        value = payload["invalid-addr-combination"]
        if value not in VALID_BODY_INVALID_ADDR_COMBINATION:
            desc = FIELD_DESCRIPTIONS.get("invalid-addr-combination", "")
            error_msg = f"Invalid value for 'invalid-addr-combination': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_INVALID_ADDR_COMBINATION)}"
            error_msg += f"\n  → Example: invalid-addr-combination='{{ VALID_BODY_INVALID_ADDR_COMBINATION[0] }}'"
            return (False, error_msg)
    if "beacon-wrong-channel" in payload:
        value = payload["beacon-wrong-channel"]
        if value not in VALID_BODY_BEACON_WRONG_CHANNEL:
            desc = FIELD_DESCRIPTIONS.get("beacon-wrong-channel", "")
            error_msg = f"Invalid value for 'beacon-wrong-channel': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_BEACON_WRONG_CHANNEL)}"
            error_msg += f"\n  → Example: beacon-wrong-channel='{{ VALID_BODY_BEACON_WRONG_CHANNEL[0] }}'"
            return (False, error_msg)
    if "ht-greenfield" in payload:
        value = payload["ht-greenfield"]
        if value not in VALID_BODY_HT_GREENFIELD:
            desc = FIELD_DESCRIPTIONS.get("ht-greenfield", "")
            error_msg = f"Invalid value for 'ht-greenfield': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HT_GREENFIELD)}"
            error_msg += f"\n  → Example: ht-greenfield='{{ VALID_BODY_HT_GREENFIELD[0] }}'"
            return (False, error_msg)
    if "overflow-ie" in payload:
        value = payload["overflow-ie"]
        if value not in VALID_BODY_OVERFLOW_IE:
            desc = FIELD_DESCRIPTIONS.get("overflow-ie", "")
            error_msg = f"Invalid value for 'overflow-ie': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERFLOW_IE)}"
            error_msg += f"\n  → Example: overflow-ie='{{ VALID_BODY_OVERFLOW_IE[0] }}'"
            return (False, error_msg)
    if "malformed-ht-ie" in payload:
        value = payload["malformed-ht-ie"]
        if value not in VALID_BODY_MALFORMED_HT_IE:
            desc = FIELD_DESCRIPTIONS.get("malformed-ht-ie", "")
            error_msg = f"Invalid value for 'malformed-ht-ie': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MALFORMED_HT_IE)}"
            error_msg += f"\n  → Example: malformed-ht-ie='{{ VALID_BODY_MALFORMED_HT_IE[0] }}'"
            return (False, error_msg)
    if "malformed-auth" in payload:
        value = payload["malformed-auth"]
        if value not in VALID_BODY_MALFORMED_AUTH:
            desc = FIELD_DESCRIPTIONS.get("malformed-auth", "")
            error_msg = f"Invalid value for 'malformed-auth': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MALFORMED_AUTH)}"
            error_msg += f"\n  → Example: malformed-auth='{{ VALID_BODY_MALFORMED_AUTH[0] }}'"
            return (False, error_msg)
    if "malformed-association" in payload:
        value = payload["malformed-association"]
        if value not in VALID_BODY_MALFORMED_ASSOCIATION:
            desc = FIELD_DESCRIPTIONS.get("malformed-association", "")
            error_msg = f"Invalid value for 'malformed-association': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MALFORMED_ASSOCIATION)}"
            error_msg += f"\n  → Example: malformed-association='{{ VALID_BODY_MALFORMED_ASSOCIATION[0] }}'"
            return (False, error_msg)
    if "ht-40mhz-intolerance" in payload:
        value = payload["ht-40mhz-intolerance"]
        if value not in VALID_BODY_HT_40MHZ_INTOLERANCE:
            desc = FIELD_DESCRIPTIONS.get("ht-40mhz-intolerance", "")
            error_msg = f"Invalid value for 'ht-40mhz-intolerance': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HT_40MHZ_INTOLERANCE)}"
            error_msg += f"\n  → Example: ht-40mhz-intolerance='{{ VALID_BODY_HT_40MHZ_INTOLERANCE[0] }}'"
            return (False, error_msg)
    if "valid-ssid-misuse" in payload:
        value = payload["valid-ssid-misuse"]
        if value not in VALID_BODY_VALID_SSID_MISUSE:
            desc = FIELD_DESCRIPTIONS.get("valid-ssid-misuse", "")
            error_msg = f"Invalid value for 'valid-ssid-misuse': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VALID_SSID_MISUSE)}"
            error_msg += f"\n  → Example: valid-ssid-misuse='{{ VALID_BODY_VALID_SSID_MISUSE[0] }}'"
            return (False, error_msg)
    if "valid-client-misassociation" in payload:
        value = payload["valid-client-misassociation"]
        if value not in VALID_BODY_VALID_CLIENT_MISASSOCIATION:
            desc = FIELD_DESCRIPTIONS.get("valid-client-misassociation", "")
            error_msg = f"Invalid value for 'valid-client-misassociation': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_VALID_CLIENT_MISASSOCIATION)}"
            error_msg += f"\n  → Example: valid-client-misassociation='{{ VALID_BODY_VALID_CLIENT_MISASSOCIATION[0] }}'"
            return (False, error_msg)
    if "hotspotter-attack" in payload:
        value = payload["hotspotter-attack"]
        if value not in VALID_BODY_HOTSPOTTER_ATTACK:
            desc = FIELD_DESCRIPTIONS.get("hotspotter-attack", "")
            error_msg = f"Invalid value for 'hotspotter-attack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_HOTSPOTTER_ATTACK)}"
            error_msg += f"\n  → Example: hotspotter-attack='{{ VALID_BODY_HOTSPOTTER_ATTACK[0] }}'"
            return (False, error_msg)
    if "pwsave-dos-attack" in payload:
        value = payload["pwsave-dos-attack"]
        if value not in VALID_BODY_PWSAVE_DOS_ATTACK:
            desc = FIELD_DESCRIPTIONS.get("pwsave-dos-attack", "")
            error_msg = f"Invalid value for 'pwsave-dos-attack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_PWSAVE_DOS_ATTACK)}"
            error_msg += f"\n  → Example: pwsave-dos-attack='{{ VALID_BODY_PWSAVE_DOS_ATTACK[0] }}'"
            return (False, error_msg)
    if "omerta-attack" in payload:
        value = payload["omerta-attack"]
        if value not in VALID_BODY_OMERTA_ATTACK:
            desc = FIELD_DESCRIPTIONS.get("omerta-attack", "")
            error_msg = f"Invalid value for 'omerta-attack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OMERTA_ATTACK)}"
            error_msg += f"\n  → Example: omerta-attack='{{ VALID_BODY_OMERTA_ATTACK[0] }}'"
            return (False, error_msg)
    if "disconnect-station" in payload:
        value = payload["disconnect-station"]
        if value not in VALID_BODY_DISCONNECT_STATION:
            desc = FIELD_DESCRIPTIONS.get("disconnect-station", "")
            error_msg = f"Invalid value for 'disconnect-station': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_DISCONNECT_STATION)}"
            error_msg += f"\n  → Example: disconnect-station='{{ VALID_BODY_DISCONNECT_STATION[0] }}'"
            return (False, error_msg)
    if "unencrypted-valid" in payload:
        value = payload["unencrypted-valid"]
        if value not in VALID_BODY_UNENCRYPTED_VALID:
            desc = FIELD_DESCRIPTIONS.get("unencrypted-valid", "")
            error_msg = f"Invalid value for 'unencrypted-valid': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_UNENCRYPTED_VALID)}"
            error_msg += f"\n  → Example: unencrypted-valid='{{ VALID_BODY_UNENCRYPTED_VALID[0] }}'"
            return (False, error_msg)
    if "fata-jack" in payload:
        value = payload["fata-jack"]
        if value not in VALID_BODY_FATA_JACK:
            desc = FIELD_DESCRIPTIONS.get("fata-jack", "")
            error_msg = f"Invalid value for 'fata-jack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FATA_JACK)}"
            error_msg += f"\n  → Example: fata-jack='{{ VALID_BODY_FATA_JACK[0] }}'"
            return (False, error_msg)
    if "risky-encryption" in payload:
        value = payload["risky-encryption"]
        if value not in VALID_BODY_RISKY_ENCRYPTION:
            desc = FIELD_DESCRIPTIONS.get("risky-encryption", "")
            error_msg = f"Invalid value for 'risky-encryption': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RISKY_ENCRYPTION)}"
            error_msg += f"\n  → Example: risky-encryption='{{ VALID_BODY_RISKY_ENCRYPTION[0] }}'"
            return (False, error_msg)
    if "fuzzed-beacon" in payload:
        value = payload["fuzzed-beacon"]
        if value not in VALID_BODY_FUZZED_BEACON:
            desc = FIELD_DESCRIPTIONS.get("fuzzed-beacon", "")
            error_msg = f"Invalid value for 'fuzzed-beacon': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FUZZED_BEACON)}"
            error_msg += f"\n  → Example: fuzzed-beacon='{{ VALID_BODY_FUZZED_BEACON[0] }}'"
            return (False, error_msg)
    if "fuzzed-probe-request" in payload:
        value = payload["fuzzed-probe-request"]
        if value not in VALID_BODY_FUZZED_PROBE_REQUEST:
            desc = FIELD_DESCRIPTIONS.get("fuzzed-probe-request", "")
            error_msg = f"Invalid value for 'fuzzed-probe-request': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FUZZED_PROBE_REQUEST)}"
            error_msg += f"\n  → Example: fuzzed-probe-request='{{ VALID_BODY_FUZZED_PROBE_REQUEST[0] }}'"
            return (False, error_msg)
    if "fuzzed-probe-response" in payload:
        value = payload["fuzzed-probe-response"]
        if value not in VALID_BODY_FUZZED_PROBE_RESPONSE:
            desc = FIELD_DESCRIPTIONS.get("fuzzed-probe-response", "")
            error_msg = f"Invalid value for 'fuzzed-probe-response': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FUZZED_PROBE_RESPONSE)}"
            error_msg += f"\n  → Example: fuzzed-probe-response='{{ VALID_BODY_FUZZED_PROBE_RESPONSE[0] }}'"
            return (False, error_msg)
    if "air-jack" in payload:
        value = payload["air-jack"]
        if value not in VALID_BODY_AIR_JACK:
            desc = FIELD_DESCRIPTIONS.get("air-jack", "")
            error_msg = f"Invalid value for 'air-jack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AIR_JACK)}"
            error_msg += f"\n  → Example: air-jack='{{ VALID_BODY_AIR_JACK[0] }}'"
            return (False, error_msg)
    if "wpa-ft-attack" in payload:
        value = payload["wpa-ft-attack"]
        if value not in VALID_BODY_WPA_FT_ATTACK:
            desc = FIELD_DESCRIPTIONS.get("wpa-ft-attack", "")
            error_msg = f"Invalid value for 'wpa-ft-attack': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_WPA_FT_ATTACK)}"
            error_msg += f"\n  → Example: wpa-ft-attack='{{ VALID_BODY_WPA_FT_ATTACK[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_wireless_controller_wids_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """
    Validate PUT request to update wireless_controller/wids_profile.

    Args:
        payload: Request body data
        **params: Query parameters

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> payload = {"name": "updated_item"}
        >>> is_valid, error = validate_wireless_controller_wids_profile_put(payload)
    """
    # Step 1: Validate enum values
    if "sensor-mode" in payload:
        value = payload["sensor-mode"]
        if value not in VALID_BODY_SENSOR_MODE:
            return (
                False,
                f"Invalid value for 'sensor-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SENSOR_MODE)}",
            )
    if "ap-scan" in payload:
        value = payload["ap-scan"]
        if value not in VALID_BODY_AP_SCAN:
            return (
                False,
                f"Invalid value for 'ap-scan'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_SCAN)}",
            )
    if "ap-scan-passive" in payload:
        value = payload["ap-scan-passive"]
        if value not in VALID_BODY_AP_SCAN_PASSIVE:
            return (
                False,
                f"Invalid value for 'ap-scan-passive'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_SCAN_PASSIVE)}",
            )
    if "ap-auto-suppress" in payload:
        value = payload["ap-auto-suppress"]
        if value not in VALID_BODY_AP_AUTO_SUPPRESS:
            return (
                False,
                f"Invalid value for 'ap-auto-suppress'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_AUTO_SUPPRESS)}",
            )
    if "wireless-bridge" in payload:
        value = payload["wireless-bridge"]
        if value not in VALID_BODY_WIRELESS_BRIDGE:
            return (
                False,
                f"Invalid value for 'wireless-bridge'='{value}'. Must be one of: {', '.join(VALID_BODY_WIRELESS_BRIDGE)}",
            )
    if "deauth-broadcast" in payload:
        value = payload["deauth-broadcast"]
        if value not in VALID_BODY_DEAUTH_BROADCAST:
            return (
                False,
                f"Invalid value for 'deauth-broadcast'='{value}'. Must be one of: {', '.join(VALID_BODY_DEAUTH_BROADCAST)}",
            )
    if "null-ssid-probe-resp" in payload:
        value = payload["null-ssid-probe-resp"]
        if value not in VALID_BODY_NULL_SSID_PROBE_RESP:
            return (
                False,
                f"Invalid value for 'null-ssid-probe-resp'='{value}'. Must be one of: {', '.join(VALID_BODY_NULL_SSID_PROBE_RESP)}",
            )
    if "long-duration-attack" in payload:
        value = payload["long-duration-attack"]
        if value not in VALID_BODY_LONG_DURATION_ATTACK:
            return (
                False,
                f"Invalid value for 'long-duration-attack'='{value}'. Must be one of: {', '.join(VALID_BODY_LONG_DURATION_ATTACK)}",
            )
    if "invalid-mac-oui" in payload:
        value = payload["invalid-mac-oui"]
        if value not in VALID_BODY_INVALID_MAC_OUI:
            return (
                False,
                f"Invalid value for 'invalid-mac-oui'='{value}'. Must be one of: {', '.join(VALID_BODY_INVALID_MAC_OUI)}",
            )
    if "weak-wep-iv" in payload:
        value = payload["weak-wep-iv"]
        if value not in VALID_BODY_WEAK_WEP_IV:
            return (
                False,
                f"Invalid value for 'weak-wep-iv'='{value}'. Must be one of: {', '.join(VALID_BODY_WEAK_WEP_IV)}",
            )
    if "auth-frame-flood" in payload:
        value = payload["auth-frame-flood"]
        if value not in VALID_BODY_AUTH_FRAME_FLOOD:
            return (
                False,
                f"Invalid value for 'auth-frame-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_AUTH_FRAME_FLOOD)}",
            )
    if "assoc-frame-flood" in payload:
        value = payload["assoc-frame-flood"]
        if value not in VALID_BODY_ASSOC_FRAME_FLOOD:
            return (
                False,
                f"Invalid value for 'assoc-frame-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_ASSOC_FRAME_FLOOD)}",
            )
    if "reassoc-flood" in payload:
        value = payload["reassoc-flood"]
        if value not in VALID_BODY_REASSOC_FLOOD:
            return (
                False,
                f"Invalid value for 'reassoc-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_REASSOC_FLOOD)}",
            )
    if "probe-flood" in payload:
        value = payload["probe-flood"]
        if value not in VALID_BODY_PROBE_FLOOD:
            return (
                False,
                f"Invalid value for 'probe-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_PROBE_FLOOD)}",
            )
    if "bcn-flood" in payload:
        value = payload["bcn-flood"]
        if value not in VALID_BODY_BCN_FLOOD:
            return (
                False,
                f"Invalid value for 'bcn-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_BCN_FLOOD)}",
            )
    if "rts-flood" in payload:
        value = payload["rts-flood"]
        if value not in VALID_BODY_RTS_FLOOD:
            return (
                False,
                f"Invalid value for 'rts-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_RTS_FLOOD)}",
            )
    if "cts-flood" in payload:
        value = payload["cts-flood"]
        if value not in VALID_BODY_CTS_FLOOD:
            return (
                False,
                f"Invalid value for 'cts-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_CTS_FLOOD)}",
            )
    if "client-flood" in payload:
        value = payload["client-flood"]
        if value not in VALID_BODY_CLIENT_FLOOD:
            return (
                False,
                f"Invalid value for 'client-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_CLIENT_FLOOD)}",
            )
    if "block_ack-flood" in payload:
        value = payload["block_ack-flood"]
        if value not in VALID_BODY_BLOCK_ACK_FLOOD:
            return (
                False,
                f"Invalid value for 'block_ack-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_BLOCK_ACK_FLOOD)}",
            )
    if "pspoll-flood" in payload:
        value = payload["pspoll-flood"]
        if value not in VALID_BODY_PSPOLL_FLOOD:
            return (
                False,
                f"Invalid value for 'pspoll-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_PSPOLL_FLOOD)}",
            )
    if "netstumbler" in payload:
        value = payload["netstumbler"]
        if value not in VALID_BODY_NETSTUMBLER:
            return (
                False,
                f"Invalid value for 'netstumbler'='{value}'. Must be one of: {', '.join(VALID_BODY_NETSTUMBLER)}",
            )
    if "wellenreiter" in payload:
        value = payload["wellenreiter"]
        if value not in VALID_BODY_WELLENREITER:
            return (
                False,
                f"Invalid value for 'wellenreiter'='{value}'. Must be one of: {', '.join(VALID_BODY_WELLENREITER)}",
            )
    if "spoofed-deauth" in payload:
        value = payload["spoofed-deauth"]
        if value not in VALID_BODY_SPOOFED_DEAUTH:
            return (
                False,
                f"Invalid value for 'spoofed-deauth'='{value}'. Must be one of: {', '.join(VALID_BODY_SPOOFED_DEAUTH)}",
            )
    if "asleap-attack" in payload:
        value = payload["asleap-attack"]
        if value not in VALID_BODY_ASLEAP_ATTACK:
            return (
                False,
                f"Invalid value for 'asleap-attack'='{value}'. Must be one of: {', '.join(VALID_BODY_ASLEAP_ATTACK)}",
            )
    if "eapol-start-flood" in payload:
        value = payload["eapol-start-flood"]
        if value not in VALID_BODY_EAPOL_START_FLOOD:
            return (
                False,
                f"Invalid value for 'eapol-start-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_START_FLOOD)}",
            )
    if "eapol-logoff-flood" in payload:
        value = payload["eapol-logoff-flood"]
        if value not in VALID_BODY_EAPOL_LOGOFF_FLOOD:
            return (
                False,
                f"Invalid value for 'eapol-logoff-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_LOGOFF_FLOOD)}",
            )
    if "eapol-succ-flood" in payload:
        value = payload["eapol-succ-flood"]
        if value not in VALID_BODY_EAPOL_SUCC_FLOOD:
            return (
                False,
                f"Invalid value for 'eapol-succ-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_SUCC_FLOOD)}",
            )
    if "eapol-fail-flood" in payload:
        value = payload["eapol-fail-flood"]
        if value not in VALID_BODY_EAPOL_FAIL_FLOOD:
            return (
                False,
                f"Invalid value for 'eapol-fail-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_FAIL_FLOOD)}",
            )
    if "eapol-pre-succ-flood" in payload:
        value = payload["eapol-pre-succ-flood"]
        if value not in VALID_BODY_EAPOL_PRE_SUCC_FLOOD:
            return (
                False,
                f"Invalid value for 'eapol-pre-succ-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_PRE_SUCC_FLOOD)}",
            )
    if "eapol-pre-fail-flood" in payload:
        value = payload["eapol-pre-fail-flood"]
        if value not in VALID_BODY_EAPOL_PRE_FAIL_FLOOD:
            return (
                False,
                f"Invalid value for 'eapol-pre-fail-flood'='{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_PRE_FAIL_FLOOD)}",
            )
    if "windows-bridge" in payload:
        value = payload["windows-bridge"]
        if value not in VALID_BODY_WINDOWS_BRIDGE:
            return (
                False,
                f"Invalid value for 'windows-bridge'='{value}'. Must be one of: {', '.join(VALID_BODY_WINDOWS_BRIDGE)}",
            )
    if "disassoc-broadcast" in payload:
        value = payload["disassoc-broadcast"]
        if value not in VALID_BODY_DISASSOC_BROADCAST:
            return (
                False,
                f"Invalid value for 'disassoc-broadcast'='{value}'. Must be one of: {', '.join(VALID_BODY_DISASSOC_BROADCAST)}",
            )
    if "ap-spoofing" in payload:
        value = payload["ap-spoofing"]
        if value not in VALID_BODY_AP_SPOOFING:
            return (
                False,
                f"Invalid value for 'ap-spoofing'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_SPOOFING)}",
            )
    if "chan-based-mitm" in payload:
        value = payload["chan-based-mitm"]
        if value not in VALID_BODY_CHAN_BASED_MITM:
            return (
                False,
                f"Invalid value for 'chan-based-mitm'='{value}'. Must be one of: {', '.join(VALID_BODY_CHAN_BASED_MITM)}",
            )
    if "adhoc-valid-ssid" in payload:
        value = payload["adhoc-valid-ssid"]
        if value not in VALID_BODY_ADHOC_VALID_SSID:
            return (
                False,
                f"Invalid value for 'adhoc-valid-ssid'='{value}'. Must be one of: {', '.join(VALID_BODY_ADHOC_VALID_SSID)}",
            )
    if "adhoc-network" in payload:
        value = payload["adhoc-network"]
        if value not in VALID_BODY_ADHOC_NETWORK:
            return (
                False,
                f"Invalid value for 'adhoc-network'='{value}'. Must be one of: {', '.join(VALID_BODY_ADHOC_NETWORK)}",
            )
    if "eapol-key-overflow" in payload:
        value = payload["eapol-key-overflow"]
        if value not in VALID_BODY_EAPOL_KEY_OVERFLOW:
            return (
                False,
                f"Invalid value for 'eapol-key-overflow'='{value}'. Must be one of: {', '.join(VALID_BODY_EAPOL_KEY_OVERFLOW)}",
            )
    if "ap-impersonation" in payload:
        value = payload["ap-impersonation"]
        if value not in VALID_BODY_AP_IMPERSONATION:
            return (
                False,
                f"Invalid value for 'ap-impersonation'='{value}'. Must be one of: {', '.join(VALID_BODY_AP_IMPERSONATION)}",
            )
    if "invalid-addr-combination" in payload:
        value = payload["invalid-addr-combination"]
        if value not in VALID_BODY_INVALID_ADDR_COMBINATION:
            return (
                False,
                f"Invalid value for 'invalid-addr-combination'='{value}'. Must be one of: {', '.join(VALID_BODY_INVALID_ADDR_COMBINATION)}",
            )
    if "beacon-wrong-channel" in payload:
        value = payload["beacon-wrong-channel"]
        if value not in VALID_BODY_BEACON_WRONG_CHANNEL:
            return (
                False,
                f"Invalid value for 'beacon-wrong-channel'='{value}'. Must be one of: {', '.join(VALID_BODY_BEACON_WRONG_CHANNEL)}",
            )
    if "ht-greenfield" in payload:
        value = payload["ht-greenfield"]
        if value not in VALID_BODY_HT_GREENFIELD:
            return (
                False,
                f"Invalid value for 'ht-greenfield'='{value}'. Must be one of: {', '.join(VALID_BODY_HT_GREENFIELD)}",
            )
    if "overflow-ie" in payload:
        value = payload["overflow-ie"]
        if value not in VALID_BODY_OVERFLOW_IE:
            return (
                False,
                f"Invalid value for 'overflow-ie'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERFLOW_IE)}",
            )
    if "malformed-ht-ie" in payload:
        value = payload["malformed-ht-ie"]
        if value not in VALID_BODY_MALFORMED_HT_IE:
            return (
                False,
                f"Invalid value for 'malformed-ht-ie'='{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_HT_IE)}",
            )
    if "malformed-auth" in payload:
        value = payload["malformed-auth"]
        if value not in VALID_BODY_MALFORMED_AUTH:
            return (
                False,
                f"Invalid value for 'malformed-auth'='{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_AUTH)}",
            )
    if "malformed-association" in payload:
        value = payload["malformed-association"]
        if value not in VALID_BODY_MALFORMED_ASSOCIATION:
            return (
                False,
                f"Invalid value for 'malformed-association'='{value}'. Must be one of: {', '.join(VALID_BODY_MALFORMED_ASSOCIATION)}",
            )
    if "ht-40mhz-intolerance" in payload:
        value = payload["ht-40mhz-intolerance"]
        if value not in VALID_BODY_HT_40MHZ_INTOLERANCE:
            return (
                False,
                f"Invalid value for 'ht-40mhz-intolerance'='{value}'. Must be one of: {', '.join(VALID_BODY_HT_40MHZ_INTOLERANCE)}",
            )
    if "valid-ssid-misuse" in payload:
        value = payload["valid-ssid-misuse"]
        if value not in VALID_BODY_VALID_SSID_MISUSE:
            return (
                False,
                f"Invalid value for 'valid-ssid-misuse'='{value}'. Must be one of: {', '.join(VALID_BODY_VALID_SSID_MISUSE)}",
            )
    if "valid-client-misassociation" in payload:
        value = payload["valid-client-misassociation"]
        if value not in VALID_BODY_VALID_CLIENT_MISASSOCIATION:
            return (
                False,
                f"Invalid value for 'valid-client-misassociation'='{value}'. Must be one of: {', '.join(VALID_BODY_VALID_CLIENT_MISASSOCIATION)}",
            )
    if "hotspotter-attack" in payload:
        value = payload["hotspotter-attack"]
        if value not in VALID_BODY_HOTSPOTTER_ATTACK:
            return (
                False,
                f"Invalid value for 'hotspotter-attack'='{value}'. Must be one of: {', '.join(VALID_BODY_HOTSPOTTER_ATTACK)}",
            )
    if "pwsave-dos-attack" in payload:
        value = payload["pwsave-dos-attack"]
        if value not in VALID_BODY_PWSAVE_DOS_ATTACK:
            return (
                False,
                f"Invalid value for 'pwsave-dos-attack'='{value}'. Must be one of: {', '.join(VALID_BODY_PWSAVE_DOS_ATTACK)}",
            )
    if "omerta-attack" in payload:
        value = payload["omerta-attack"]
        if value not in VALID_BODY_OMERTA_ATTACK:
            return (
                False,
                f"Invalid value for 'omerta-attack'='{value}'. Must be one of: {', '.join(VALID_BODY_OMERTA_ATTACK)}",
            )
    if "disconnect-station" in payload:
        value = payload["disconnect-station"]
        if value not in VALID_BODY_DISCONNECT_STATION:
            return (
                False,
                f"Invalid value for 'disconnect-station'='{value}'. Must be one of: {', '.join(VALID_BODY_DISCONNECT_STATION)}",
            )
    if "unencrypted-valid" in payload:
        value = payload["unencrypted-valid"]
        if value not in VALID_BODY_UNENCRYPTED_VALID:
            return (
                False,
                f"Invalid value for 'unencrypted-valid'='{value}'. Must be one of: {', '.join(VALID_BODY_UNENCRYPTED_VALID)}",
            )
    if "fata-jack" in payload:
        value = payload["fata-jack"]
        if value not in VALID_BODY_FATA_JACK:
            return (
                False,
                f"Invalid value for 'fata-jack'='{value}'. Must be one of: {', '.join(VALID_BODY_FATA_JACK)}",
            )
    if "risky-encryption" in payload:
        value = payload["risky-encryption"]
        if value not in VALID_BODY_RISKY_ENCRYPTION:
            return (
                False,
                f"Invalid value for 'risky-encryption'='{value}'. Must be one of: {', '.join(VALID_BODY_RISKY_ENCRYPTION)}",
            )
    if "fuzzed-beacon" in payload:
        value = payload["fuzzed-beacon"]
        if value not in VALID_BODY_FUZZED_BEACON:
            return (
                False,
                f"Invalid value for 'fuzzed-beacon'='{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_BEACON)}",
            )
    if "fuzzed-probe-request" in payload:
        value = payload["fuzzed-probe-request"]
        if value not in VALID_BODY_FUZZED_PROBE_REQUEST:
            return (
                False,
                f"Invalid value for 'fuzzed-probe-request'='{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_PROBE_REQUEST)}",
            )
    if "fuzzed-probe-response" in payload:
        value = payload["fuzzed-probe-response"]
        if value not in VALID_BODY_FUZZED_PROBE_RESPONSE:
            return (
                False,
                f"Invalid value for 'fuzzed-probe-response'='{value}'. Must be one of: {', '.join(VALID_BODY_FUZZED_PROBE_RESPONSE)}",
            )
    if "air-jack" in payload:
        value = payload["air-jack"]
        if value not in VALID_BODY_AIR_JACK:
            return (
                False,
                f"Invalid value for 'air-jack'='{value}'. Must be one of: {', '.join(VALID_BODY_AIR_JACK)}",
            )
    if "wpa-ft-attack" in payload:
        value = payload["wpa-ft-attack"]
        if value not in VALID_BODY_WPA_FT_ATTACK:
            return (
                False,
                f"Invalid value for 'wpa-ft-attack'='{value}'. Must be one of: {', '.join(VALID_BODY_WPA_FT_ATTACK)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Provide programmatic access to field metadata for IDE autocomplete,
# documentation generation, and dynamic validation
# ============================================================================


def get_field_description(field_name: str) -> str | None:
    """
    Get description/help text for a field.

    Args:
        field_name: Name of the field

    Returns:
        Description text or None if field doesn't exist

    Example:
        >>> desc = get_field_description("name")
        >>> print(desc)
    """
    return FIELD_DESCRIPTIONS.get(field_name)


def get_field_type(field_name: str) -> str | None:
    """
    Get the type of a field.

    Args:
        field_name: Name of the field

    Returns:
        Field type (e.g., "string", "integer", "option") or None

    Example:
        >>> field_type = get_field_type("status")
        >>> print(field_type)  # "option"
    """
    return FIELD_TYPES.get(field_name)


def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """
    Get constraints for a field (min/max values, string length).

    Args:
        field_name: Name of the field

    Returns:
        Constraint dict or None

    Example:
        >>> constraints = get_field_constraints("port")
        >>> print(constraints)  # {"type": "integer", "min": 1, "max": 65535}
    """
    return FIELD_CONSTRAINTS.get(field_name)


def get_field_default(field_name: str) -> Any | None:
    """
    Get default value for a field.

    Args:
        field_name: Name of the field

    Returns:
        Default value or None if no default

    Example:
        >>> default = get_field_default("status")
        >>> print(default)  # "enable"
    """
    return FIELDS_WITH_DEFAULTS.get(field_name)


def get_field_options(field_name: str) -> list[str] | None:
    """
    Get valid enum options for a field.

    Args:
        field_name: Name of the field

    Returns:
        List of valid values or None if not an enum field

    Example:
        >>> options = get_field_options("status")
        >>> print(options)  # ["enable", "disable"]
    """
    # Construct the constant name from field name
    # Replace all non-alphanumeric characters with underscores for valid Python identifiers
    import re
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', field_name)
    constant_name = f"VALID_BODY_{safe_name.upper()}"
    return globals().get(constant_name)


def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """
    Get schema for nested table/list fields.

    Args:
        field_name: Name of the parent field

    Returns:
        Dict mapping child field names to their metadata

    Example:
        >>> nested = get_nested_schema("members")
        >>> if nested:
        ...     for child_field, child_meta in nested.items():
        ...         print(f"{child_field}: {child_meta['type']}")
    """
    return NESTED_SCHEMAS.get(field_name)


def get_all_fields() -> list[str]:
    """
    Get list of all field names.

    Returns:
        List of all field names in the schema

    Example:
        >>> fields = get_all_fields()
        >>> print(len(fields))
    """
    return list(FIELD_TYPES.keys())


def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """
    Get complete metadata for a field (type, description, constraints, defaults, options).

    Args:
        field_name: Name of the field

    Returns:
        Dict with all available metadata or None if field doesn't exist

    Example:
        >>> meta = get_field_metadata("status")
        >>> print(meta)
        >>> # {
        >>> #   "type": "option",
        >>> #   "description": "Enable/disable this feature",
        >>> #   "default": "enable",
        >>> #   "options": ["enable", "disable"]
        >>> # }
    """
    if field_name not in FIELD_TYPES:
        return None

    metadata = {
        "name": field_name,
        "type": FIELD_TYPES[field_name],
    }

    # Add description if available
    if field_name in FIELD_DESCRIPTIONS:
        metadata["description"] = FIELD_DESCRIPTIONS[field_name]

    # Add constraints if available
    if field_name in FIELD_CONSTRAINTS:
        metadata["constraints"] = FIELD_CONSTRAINTS[field_name]

    # Add default if available
    if field_name in FIELDS_WITH_DEFAULTS:
        metadata["default"] = FIELDS_WITH_DEFAULTS[field_name]

    # Add required flag
    metadata["required"] = field_name in REQUIRED_FIELDS

    # Add options if available
    options = get_field_options(field_name)
    if options:
        metadata["options"] = options

    # Add nested schema if available
    nested = get_nested_schema(field_name)
    if nested:
        metadata["nested_schema"] = nested

    return metadata


def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """
    Validate a single field value against its constraints.

    Args:
        field_name: Name of the field
        value: Value to validate

    Returns:
        Tuple of (is_valid, error_message)

    Example:
        >>> is_valid, error = validate_field_value("status", "enable")
        >>> if not is_valid:
        ...     print(error)
    """
    # Get field metadata
    field_type = get_field_type(field_name)
    if field_type is None:
        return (False, f"Unknown field: '{field_name}' (not defined in schema)")

    # Get field description for better error context
    description = get_field_description(field_name)

    # Validate enum values
    options = get_field_options(field_name)
    if options and value not in options:
        error_msg = f"Invalid value for '{field_name}': {repr(value)}"
        if description:
            error_msg += f"\n  → Description: {description}"
        error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in options)}"
        if options:
            error_msg += f"\n  → Example: {field_name}={repr(options[0])}"
        return (False, error_msg)

    # Validate constraints
    constraints = get_field_constraints(field_name)
    if constraints:
        constraint_type = constraints.get("type")

        if constraint_type == "integer":
            if not isinstance(value, int):
                error_msg = f"Field '{field_name}' must be an integer"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            min_val = constraints.get("min")
            max_val = constraints.get("max")

            if min_val is not None and value < min_val:
                error_msg = f"Field '{field_name}' value {value} is below minimum {min_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if max_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

            if max_val is not None and value > max_val:
                error_msg = f"Field '{field_name}' value {value} exceeds maximum {max_val}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                if min_val is not None:
                    error_msg += f"\n  → Valid range: {min_val} to {max_val}"
                return (False, error_msg)

        elif constraint_type == "string":
            if not isinstance(value, str):
                error_msg = f"Field '{field_name}' must be a string"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → You provided: {type(value).__name__} = {repr(value)}"
                return (False, error_msg)

            max_length = constraints.get("max_length")
            if max_length and len(value) > max_length:
                error_msg = f"Field '{field_name}' length {len(value)} exceeds maximum {max_length}"
                if description:
                    error_msg += f"\n  → Description: {description}"
                error_msg += f"\n  → Your value: {repr(value[:50])}{'...' if len(value) > 50 else ''}"
                return (False, error_msg)

    return (True, None)


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "wireless_controller/wids_profile",
    "category": "cmdb",
    "api_path": "wireless-controller/wids-profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure wireless intrusion detection system (WIDS) profiles.",
    "total_fields": 110,
    "required_fields_count": 0,
    "fields_with_defaults_count": 107,
}


def get_schema_info() -> dict[str, Any]:
    """
    Get information about this endpoint schema.

    Returns:
        Dict with schema metadata

    Example:
        >>> info = get_schema_info()
        >>> print(f"Endpoint: {info['endpoint']}")
        >>> print(f"Total fields: {info['total_fields']}")
    """
    return SCHEMA_INFO.copy()

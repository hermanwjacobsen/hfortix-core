"""Validation helpers for firewall/profile_protocol_options - Auto-generated"""

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

# Do NOT use this list for strict validation - test with the actual FortiOS API!

# Fields marked as required (after filtering false positives)
REQUIRED_FIELDS = [
    "name",  # Name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "replacemsg-group": "",
    "oversize-log": "disable",
    "switching-protocols-log": "disable",
    "rpc-over-http": "disable",
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
    "name": "string",  # Name.
    "comment": "var-string",  # Optional comments.
    "replacemsg-group": "string",  # Name of the replacement message group to be used.
    "oversize-log": "option",  # Enable/disable logging for antivirus oversize file blocking.
    "switching-protocols-log": "option",  # Enable/disable logging for HTTP/HTTPS switching protocols.
    "http": "string",  # Configure HTTP protocol options.
    "ftp": "string",  # Configure FTP protocol options.
    "imap": "string",  # Configure IMAP protocol options.
    "mapi": "string",  # Configure MAPI protocol options.
    "pop3": "string",  # Configure POP3 protocol options.
    "smtp": "string",  # Configure SMTP protocol options.
    "nntp": "string",  # Configure NNTP protocol options.
    "ssh": "string",  # Configure SFTP and SCP protocol options.
    "dns": "string",  # Configure DNS protocol options.
    "cifs": "string",  # Configure CIFS protocol options.
    "mail-signature": "string",  # Configure Mail signature.
    "rpc-over-http": "option",  # Enable/disable inspection of RPC over HTTP.
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Name.",
    "comment": "Optional comments.",
    "replacemsg-group": "Name of the replacement message group to be used.",
    "oversize-log": "Enable/disable logging for antivirus oversize file blocking.",
    "switching-protocols-log": "Enable/disable logging for HTTP/HTTPS switching protocols.",
    "http": "Configure HTTP protocol options.",
    "ftp": "Configure FTP protocol options.",
    "imap": "Configure IMAP protocol options.",
    "mapi": "Configure MAPI protocol options.",
    "pop3": "Configure POP3 protocol options.",
    "smtp": "Configure SMTP protocol options.",
    "nntp": "Configure NNTP protocol options.",
    "ssh": "Configure SFTP and SCP protocol options.",
    "dns": "Configure DNS protocol options.",
    "cifs": "Configure CIFS protocol options.",
    "mail-signature": "Configure Mail signature.",
    "rpc-over-http": "Enable/disable inspection of RPC over HTTP.",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
    "replacemsg-group": {"type": "string", "max_length": 35},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "http": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 80).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "inspect-all": {
            "type": "option",
            "help": "Enable/disable the inspection of all ports for the protocol.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Prevent client timeout.", "label": "Clientcomfort", "name": "clientcomfort"}, {"help": "Prevent server timeout.", "label": "Servercomfort", "name": "servercomfort"}, {"help": "Block oversized file.", "label": "Oversize", "name": "oversize"}, {"help": "Bypass chunked transfer encoded sites.", "label": "Chunkedbypass", "name": "chunkedbypass"}],
        },
        "comfort-interval": {
            "type": "integer",
            "help": "Interval between successive transmissions of data for client comforting (seconds).",
            "default": 10,
            "min_value": 1,
            "max_value": 900,
        },
        "comfort-amount": {
            "type": "integer",
            "help": "Number of bytes to send in each transmission for client comforting (bytes).",
            "default": 1,
            "min_value": 1,
            "max_value": 65535,
        },
        "range-block": {
            "type": "option",
            "help": "Enable/disable blocking of partial downloads.",
            "default": "disable",
            "options": [{"help": "Disable range header blocking (allow partial file downloads)", "label": "Disable", "name": "disable"}, {"help": "Enable range header blocking (treat all partial file downloads as full file download)", "label": "Enable", "name": "enable"}],
        },
        "strip-x-forwarded-for": {
            "type": "option",
            "help": "Enable/disable stripping of HTTP X-Forwarded-For header.",
            "default": "disable",
            "options": [{"help": "Disable changing of HTTP X-Forwarded-For header.", "label": "Disable", "name": "disable"}, {"help": "Enable replacement of X-Forwarded-For value with 1.1.1.1.", "label": "Enable", "name": "enable"}],
        },
        "post-lang": {
            "type": "option",
            "help": "ID codes for character sets to be used to convert to UTF-8 for banned words and DLP on HTTP posts (maximum of 5 character sets).",
            "default": "",
            "options": [{"help": "Japanese Industrial Standard 0201.", "label": "Jisx0201", "name": "jisx0201"}, {"help": "Japanese Industrial Standard 0208.", "label": "Jisx0208", "name": "jisx0208"}, {"help": "Japanese Industrial Standard 0212.", "label": "Jisx0212", "name": "jisx0212"}, {"help": "Guojia Biaozhun 2312 (simplified Chinese).", "label": "Gb2312", "name": "gb2312"}, {"help": "Wansung Korean standard 5601.", "label": "Ksc5601 Ex", "name": "ksc5601-ex"}, {"help": "Extended Unicode Japanese.", "label": "Euc Jp", "name": "euc-jp"}, {"help": "Shift Japanese Industrial Standard.", "label": "Sjis", "name": "sjis"}, {"help": "ISO 2022 Japanese.", "label": "Iso2022 Jp", "name": "iso2022-jp"}, {"help": "ISO 2022-1 Japanese.", "label": "Iso2022 Jp 1", "name": "iso2022-jp-1"}, {"help": "ISO 2022-2 Japanese.", "label": "Iso2022 Jp 2", "name": "iso2022-jp-2"}, {"help": "Extended Unicode Chinese.", "label": "Euc Cn", "name": "euc-cn"}, {"help": "Extended GB2312 (simplified Chinese).", "label": "Ces Gbk", "name": "ces-gbk"}, {"help": "Hanzi simplified Chinese.", "label": "Hz", "name": "hz"}, {"help": "Big-5 traditional Chinese.", "label": "Ces Big5", "name": "ces-big5"}, {"help": "Extended Unicode Korean.", "label": "Euc Kr", "name": "euc-kr"}, {"help": "ISO 2022-3 Japanese.", "label": "Iso2022 Jp 3", "name": "iso2022-jp-3"}, {"help": "ISO 8859 Part 1 (Western European).", "label": "Iso8859 1", "name": "iso8859-1"}, {"help": "Thai Industrial Standard 620.", "label": "Tis620", "name": "tis620"}, {"help": "Code Page 874 (Thai).", "label": "Cp874", "name": "cp874"}, {"help": "Code Page 1252 (Western European Latin).", "label": "Cp1252", "name": "cp1252"}, {"help": "Code Page 1251 (Cyrillic).", "label": "Cp1251", "name": "cp1251"}],
        },
        "streaming-content-bypass": {
            "type": "option",
            "help": "Enable/disable bypassing of streaming content from buffering.",
            "default": "enable",
            "options": [{"help": "Enable bypassing of streaming content from buffering", "label": "Enable", "name": "enable"}, {"help": "Disable bypassing of streaming content from buffering", "label": "Disable", "name": "disable"}],
        },
        "switching-protocols": {
            "type": "option",
            "help": "Bypass from scanning, or block a connection that attempts to switch protocol.",
            "default": "bypass",
            "options": [{"help": "Bypass connections when switching protocols.", "label": "Bypass", "name": "bypass"}, {"help": "Block connections when switching protocols.", "label": "Block", "name": "block"}],
        },
        "unknown-http-version": {
            "type": "option",
            "help": "How to handle HTTP sessions that do not comply with HTTP 0.9, 1.0, or 1.1.",
            "default": "reject",
            "options": [{"help": "Reject or tear down HTTP sessions that do not use HTTP 0.9, 1.0, or 1.1.", "label": "Reject", "name": "reject"}, {"help": "Pass HTTP traffic that does not use HTTP 0.9, 1.0, or 1.1 without applying HTTP protocol optimization, byte-caching, or web caching. TCP protocol optimization is applied.", "label": "Tunnel", "name": "tunnel"}, {"help": "Assume all HTTP sessions comply with HTTP 0.9, 1.0, or 1.1. If a session uses a different HTTP version, it may not parse correctly and the connection may be lost.", "label": "Best Effort", "name": "best-effort"}],
        },
        "http-0.9": {
            "type": "option",
            "help": "Configure action to take upon receipt of HTTP 0.9 request.",
            "default": "allow",
            "options": [{"help": "Allow HTTP 0.9 traffic for web filtering only.", "label": "Allow", "name": "allow"}, {"help": "Block HTTP 0.9 traffic.", "label": "Block", "name": "block"}],
        },
        "tunnel-non-http": {
            "type": "option",
            "help": "Configure how to process non-HTTP traffic when a profile configured for HTTP traffic accepts a non-HTTP session. Can occur if an application sends non-HTTP traffic using an HTTP destination port.",
            "default": "enable",
            "options": [{"help": "Pass non-HTTP sessions through the tunnel without applying protocol optimization, byte-caching, or web caching. TCP protocol optimization is applied.", "label": "Enable", "name": "enable"}, {"help": "Drop or tear down non-HTTP sessions accepted by the profile.", "label": "Disable", "name": "disable"}],
        },
        "h2c": {
            "type": "option",
            "help": "Enable/disable h2c HTTP connection upgrade.",
            "default": "disable",
            "options": [{"help": "Allow h2c HTTP connection upgrades. h2c tunnels do not support content scan.", "label": "Enable", "name": "enable"}, {"help": "Do not allow h2c HTTP connection upgrades.", "label": "Disable", "name": "disable"}],
        },
        "unknown-content-encoding": {
            "type": "option",
            "help": "Configure the action the FortiGate unit will take on unknown content-encoding.",
            "default": "block",
            "options": [{"help": "Block HTTP session when unknown content-encoding is detected.", "label": "Block", "name": "block"}, {"help": "Scan HTTP traffic as plain-text when unknown content-encoding is detected.", "label": "Inspect", "name": "inspect"}, {"help": "Bypass scan when unknown content-encoding is detected.", "label": "Bypass", "name": "bypass"}],
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "stream-based-uncompressed-limit": {
            "type": "integer",
            "help": "Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "verify-dns-for-policy-matching": {
            "type": "option",
            "help": "Enable/disable verification of DNS for policy matching.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "block-page-status-code": {
            "type": "integer",
            "help": "Code number returned for blocked HTTP pages (non-FortiGuard only) (100 - 599, default = 403).",
            "default": 403,
            "min_value": 100,
            "max_value": 599,
        },
        "retry-count": {
            "type": "integer",
            "help": "Number of attempts to retry HTTP connection (0 - 100, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 100,
        },
        "domain-fronting": {
            "type": "option",
            "help": "Configure HTTP domain fronting (default = block).",
            "default": "block",
            "options": [{"help": "Allow domain fronting.", "label": "Allow", "name": "allow"}, {"help": "Allow and log domain fronting.", "label": "Monitor", "name": "monitor"}, {"help": "Block and log domain fronting. Will not block potential matching IP and Domain.", "label": "Block", "name": "block"}, {"help": "Block and log domain fronting. Will block potential matching IP and Domain.", "label": "Strict", "name": "strict"}],
        },
        "tcp-window-type": {
            "type": "option",
            "help": "TCP window type to use for this protocol.",
            "default": "auto-tuning",
            "options": [{"help": "Allow system to auto-tune TCP window size (default).", "label": "Auto Tuning", "name": "auto-tuning"}, {"help": "Use system default TCP window size for this protocol.", "label": "System", "name": "system"}, {"help": "Manually specify TCP window size.", "label": "Static", "name": "static"}, {"help": "Vary TCP window size based on available memory and within limits of tcp-window-minimum and tcp-window-maximum.", "label": "Dynamic", "name": "dynamic"}],
        },
        "tcp-window-minimum": {
            "type": "integer",
            "help": "Minimum dynamic TCP window size.",
            "default": 131072,
            "min_value": 65536,
            "max_value": 1048576,
        },
        "tcp-window-maximum": {
            "type": "integer",
            "help": "Maximum dynamic TCP window size.",
            "default": 8388608,
            "min_value": 1048576,
            "max_value": 16777216,
        },
        "tcp-window-size": {
            "type": "integer",
            "help": "Set TCP static window size.",
            "default": 262144,
            "min_value": 65536,
            "max_value": 16777216,
        },
        "ssl-offloaded": {
            "type": "option",
            "help": "SSL decryption and encryption performed by an external device.",
            "default": "no",
            "options": [{"help": "SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.", "label": "No", "name": "no"}, {"help": "SSL decryption and encryption performed by an external device.", "label": "Yes", "name": "yes"}],
        },
        "address-ip-rating": {
            "type": "option",
            "help": "Enable/disable IP based URL rating.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
    },
    "ftp": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 21).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "inspect-all": {
            "type": "option",
            "help": "Enable/disable the inspection of all ports for the protocol.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Prevent client timeout.", "label": "Clientcomfort", "name": "clientcomfort"}, {"help": "Block oversized file.", "label": "Oversize", "name": "oversize"}, {"help": "Enable splice mode.", "label": "Splice", "name": "splice"}, {"help": "Bypass REST command.", "label": "Bypass Rest Command", "name": "bypass-rest-command"}, {"help": "Bypass MODE command.", "label": "Bypass Mode Command", "name": "bypass-mode-command"}],
        },
        "comfort-interval": {
            "type": "integer",
            "help": "Interval between successive transmissions of data for client comforting (seconds).",
            "default": 10,
            "min_value": 1,
            "max_value": 900,
        },
        "comfort-amount": {
            "type": "integer",
            "help": "Number of bytes to send in each transmission for client comforting (bytes).",
            "default": 1,
            "min_value": 1,
            "max_value": 65535,
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "stream-based-uncompressed-limit": {
            "type": "integer",
            "help": "Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "tcp-window-type": {
            "type": "option",
            "help": "TCP window type to use for this protocol.",
            "default": "auto-tuning",
            "options": [{"help": "Allow system to auto-tune TCP window size (default).", "label": "Auto Tuning", "name": "auto-tuning"}, {"help": "Use system default TCP window size for this protocol.", "label": "System", "name": "system"}, {"help": "Manually specify TCP window size.", "label": "Static", "name": "static"}, {"help": "Vary TCP window size based on available memory and within limits of tcp-window-minimum and tcp-window-maximum.", "label": "Dynamic", "name": "dynamic"}],
        },
        "tcp-window-minimum": {
            "type": "integer",
            "help": "Minimum dynamic TCP window size.",
            "default": 131072,
            "min_value": 65536,
            "max_value": 1048576,
        },
        "tcp-window-maximum": {
            "type": "integer",
            "help": "Maximum dynamic TCP window size.",
            "default": 8388608,
            "min_value": 1048576,
            "max_value": 16777216,
        },
        "tcp-window-size": {
            "type": "integer",
            "help": "Set TCP static window size.",
            "default": 262144,
            "min_value": 65536,
            "max_value": 16777216,
        },
        "ssl-offloaded": {
            "type": "option",
            "help": "SSL decryption and encryption performed by an external device.",
            "default": "no",
            "options": [{"help": "SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.", "label": "No", "name": "no"}, {"help": "SSL decryption and encryption performed by an external device.", "label": "Yes", "name": "yes"}],
        },
        "explicit-ftp-tls": {
            "type": "option",
            "help": "Enable/disable FTP redirection for explicit FTPS.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
    },
    "imap": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 143).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "inspect-all": {
            "type": "option",
            "help": "Enable/disable the inspection of all ports for the protocol.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Pass fragmented email.", "label": "Fragmail", "name": "fragmail"}, {"help": "Block oversized email.", "label": "Oversize", "name": "oversize"}],
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "ssl-offloaded": {
            "type": "option",
            "help": "SSL decryption and encryption performed by an external device.",
            "default": "no",
            "options": [{"help": "SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.", "label": "No", "name": "no"}, {"help": "SSL decryption and encryption performed by an external device.", "label": "Yes", "name": "yes"}],
        },
    },
    "mapi": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 135).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Pass fragmented email.", "label": "Fragmail", "name": "fragmail"}, {"help": "Block oversized email.", "label": "Oversize", "name": "oversize"}],
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
    },
    "pop3": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 110).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "inspect-all": {
            "type": "option",
            "help": "Enable/disable the inspection of all ports for the protocol.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Pass fragmented email.", "label": "Fragmail", "name": "fragmail"}, {"help": "Block oversized email.", "label": "Oversize", "name": "oversize"}],
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "ssl-offloaded": {
            "type": "option",
            "help": "SSL decryption and encryption performed by an external device.",
            "default": "no",
            "options": [{"help": "SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.", "label": "No", "name": "no"}, {"help": "SSL decryption and encryption performed by an external device.", "label": "Yes", "name": "yes"}],
        },
    },
    "smtp": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 25).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "inspect-all": {
            "type": "option",
            "help": "Enable/disable the inspection of all ports for the protocol.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Pass fragmented email.", "label": "Fragmail", "name": "fragmail"}, {"help": "Block oversized email.", "label": "Oversize", "name": "oversize"}, {"help": "Enable splice mode.", "label": "Splice", "name": "splice"}],
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "server-busy": {
            "type": "option",
            "help": "Enable/disable SMTP server busy when server not available.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "ssl-offloaded": {
            "type": "option",
            "help": "SSL decryption and encryption performed by an external device.",
            "default": "no",
            "options": [{"help": "SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.", "label": "No", "name": "no"}, {"help": "SSL decryption and encryption performed by an external device.", "label": "Yes", "name": "yes"}],
        },
    },
    "nntp": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 119).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "inspect-all": {
            "type": "option",
            "help": "Enable/disable the inspection of all ports for the protocol.",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "proxy-after-tcp-handshake": {
            "type": "option",
            "help": "Proxy traffic after the TCP 3-way handshake has been established (not before).",
            "default": "disable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Block oversized file.", "label": "Oversize", "name": "oversize"}, {"help": "Enable splice mode.", "label": "Splice", "name": "splice"}],
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
    },
    "ssh": {
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Block oversized file.", "label": "Oversize", "name": "oversize"}, {"help": "Prevent client timeout.", "label": "Clientcomfort", "name": "clientcomfort"}, {"help": "Prevent server timeout.", "label": "Servercomfort", "name": "servercomfort"}],
        },
        "comfort-interval": {
            "type": "integer",
            "help": "Interval between successive transmissions of data for client comforting (seconds).",
            "default": 10,
            "min_value": 1,
            "max_value": 900,
        },
        "comfort-amount": {
            "type": "integer",
            "help": "Number of bytes to send in each transmission for client comforting (bytes).",
            "default": 1,
            "min_value": 1,
            "max_value": 65535,
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "stream-based-uncompressed-limit": {
            "type": "integer",
            "help": "Maximum stream-based uncompressed data size that will be scanned in megabytes. Stream-based uncompression used only under certain conditions (unlimited = 0, default = 0).",
            "default": 0,
            "min_value": 0,
            "max_value": 4294967295,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "tcp-window-type": {
            "type": "option",
            "help": "TCP window type to use for this protocol.",
            "default": "auto-tuning",
            "options": [{"help": "Allow system to auto-tune TCP window size (default).", "label": "Auto Tuning", "name": "auto-tuning"}, {"help": "Use system default TCP window size for this protocol.", "label": "System", "name": "system"}, {"help": "Manually specify TCP window size.", "label": "Static", "name": "static"}, {"help": "Vary TCP window size based on available memory and within limits of tcp-window-minimum and tcp-window-maximum.", "label": "Dynamic", "name": "dynamic"}],
        },
        "tcp-window-minimum": {
            "type": "integer",
            "help": "Minimum dynamic TCP window size.",
            "default": 131072,
            "min_value": 65536,
            "max_value": 1048576,
        },
        "tcp-window-maximum": {
            "type": "integer",
            "help": "Maximum dynamic TCP window size.",
            "default": 8388608,
            "min_value": 1048576,
            "max_value": 16777216,
        },
        "tcp-window-size": {
            "type": "integer",
            "help": "Set TCP static window size.",
            "default": 262144,
            "min_value": 65536,
            "max_value": 16777216,
        },
        "ssl-offloaded": {
            "type": "option",
            "help": "SSL decryption and encryption performed by an external device.",
            "default": "no",
            "options": [{"help": "SSL decryption and encryption performed by FortiGate when deep-inspection is enabled.", "label": "No", "name": "no"}, {"help": "SSL decryption and encryption performed by an external device.", "label": "Yes", "name": "yes"}],
        },
    },
    "dns": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 53).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
    },
    "cifs": {
        "ports": {
            "type": "integer",
            "help": "Ports to scan for content (1 - 65535, default = 445).",
            "required": True,
            "default": "",
            "min_value": 1,
            "max_value": 65535,
        },
        "status": {
            "type": "option",
            "help": "Enable/disable the active status of scanning for this protocol.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "options": {
            "type": "option",
            "help": "One or more options that can be applied to the session.",
            "default": "",
            "options": [{"help": "Block oversized file.", "label": "Oversize", "name": "oversize"}],
        },
        "oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-oversize-limit": {
            "type": "integer",
            "help": "Maximum in-memory uncompressed file size that can be scanned (MB).",
            "default": 10,
            "min_value": 1,
            "max_value": 4095,
        },
        "uncompressed-nest-limit": {
            "type": "integer",
            "help": "Maximum nested levels of compression that can be uncompressed and scanned (2 - 100, default = 12).",
            "default": 12,
            "min_value": 2,
            "max_value": 100,
        },
        "scan-bzip2": {
            "type": "option",
            "help": "Enable/disable scanning of BZip2 compressed files.",
            "default": "enable",
            "options": [{"help": "Enable setting.", "label": "Enable", "name": "enable"}, {"help": "Disable setting.", "label": "Disable", "name": "disable"}],
        },
        "tcp-window-type": {
            "type": "option",
            "help": "TCP window type to use for this protocol.",
            "default": "auto-tuning",
            "options": [{"help": "Allow system to auto-tune TCP window size (default).", "label": "Auto Tuning", "name": "auto-tuning"}, {"help": "Use system default TCP window size for this protocol.", "label": "System", "name": "system"}, {"help": "Manually specify TCP window size.", "label": "Static", "name": "static"}, {"help": "Vary TCP window size based on available memory and within limits of tcp-window-minimum and tcp-window-maximum.", "label": "Dynamic", "name": "dynamic"}],
        },
        "tcp-window-minimum": {
            "type": "integer",
            "help": "Minimum dynamic TCP window size.",
            "default": 131072,
            "min_value": 65536,
            "max_value": 1048576,
        },
        "tcp-window-maximum": {
            "type": "integer",
            "help": "Maximum dynamic TCP window size.",
            "default": 8388608,
            "min_value": 1048576,
            "max_value": 16777216,
        },
        "tcp-window-size": {
            "type": "integer",
            "help": "Set TCP static window size.",
            "default": 262144,
            "min_value": 65536,
            "max_value": 16777216,
        },
        "server-credential-type": {
            "type": "option",
            "help": "CIFS server credential type.",
            "required": True,
            "default": "none",
            "options": [{"help": "Credential derivation not set.", "label": "None", "name": "none"}, {"help": "Credential derived using Replication account on Domain Controller.", "label": "Credential Replication", "name": "credential-replication"}, {"help": "Credential derived using server keytab.", "label": "Credential Keytab", "name": "credential-keytab"}],
        },
        "domain-controller": {
            "type": "string",
            "help": "Domain for which to decrypt CIFS traffic.",
            "required": True,
            "default": "",
            "max_length": 63,
        },
        "server-keytab": {
            "type": "string",
            "help": "Server keytab.",
        },
    },
    "mail-signature": {
        "status": {
            "type": "option",
            "help": "Enable/disable adding an email signature to SMTP email messages as they pass through the FortiGate.",
            "default": "disable",
            "options": [{"help": "Disable mail signature.", "label": "Disable", "name": "disable"}, {"help": "Enable mail signature.", "label": "Enable", "name": "enable"}],
        },
        "signature": {
            "type": "string",
            "help": "Email signature to be added to outgoing email (if the signature contains spaces, enclose with quotation marks).",
            "default": "",
            "max_length": 1023,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_OVERSIZE_LOG = [
    "disable",  # Disable logging for antivirus oversize file blocking.
    "enable",  # Enable logging for antivirus oversize file blocking.
]
VALID_BODY_SWITCHING_PROTOCOLS_LOG = [
    "disable",  # Disable logging for HTTP/HTTPS switching protocols.
    "enable",  # Enable logging for HTTP/HTTPS switching protocols.
]
VALID_BODY_RPC_OVER_HTTP = [
    "enable",  # Enable inspection of RPC over HTTP.
    "disable",  # Disable inspection of RPC over HTTP.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_firewall_profile_protocol_options_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for firewall/profile_protocol_options."""
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
    """Validate required fields for firewall/profile_protocol_options."""
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


def validate_firewall_profile_protocol_options_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new firewall/profile_protocol_options object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "oversize-log" in payload:
        value = payload["oversize-log"]
        if value not in VALID_BODY_OVERSIZE_LOG:
            desc = FIELD_DESCRIPTIONS.get("oversize-log", "")
            error_msg = f"Invalid value for 'oversize-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OVERSIZE_LOG)}"
            error_msg += f"\n  → Example: oversize-log='{{ VALID_BODY_OVERSIZE_LOG[0] }}'"
            return (False, error_msg)
    if "switching-protocols-log" in payload:
        value = payload["switching-protocols-log"]
        if value not in VALID_BODY_SWITCHING_PROTOCOLS_LOG:
            desc = FIELD_DESCRIPTIONS.get("switching-protocols-log", "")
            error_msg = f"Invalid value for 'switching-protocols-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SWITCHING_PROTOCOLS_LOG)}"
            error_msg += f"\n  → Example: switching-protocols-log='{{ VALID_BODY_SWITCHING_PROTOCOLS_LOG[0] }}'"
            return (False, error_msg)
    if "rpc-over-http" in payload:
        value = payload["rpc-over-http"]
        if value not in VALID_BODY_RPC_OVER_HTTP:
            desc = FIELD_DESCRIPTIONS.get("rpc-over-http", "")
            error_msg = f"Invalid value for 'rpc-over-http': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_RPC_OVER_HTTP)}"
            error_msg += f"\n  → Example: rpc-over-http='{{ VALID_BODY_RPC_OVER_HTTP[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_firewall_profile_protocol_options_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update firewall/profile_protocol_options."""
    # Step 1: Validate enum values
    if "oversize-log" in payload:
        value = payload["oversize-log"]
        if value not in VALID_BODY_OVERSIZE_LOG:
            return (
                False,
                f"Invalid value for 'oversize-log'='{value}'. Must be one of: {', '.join(VALID_BODY_OVERSIZE_LOG)}",
            )
    if "switching-protocols-log" in payload:
        value = payload["switching-protocols-log"]
        if value not in VALID_BODY_SWITCHING_PROTOCOLS_LOG:
            return (
                False,
                f"Invalid value for 'switching-protocols-log'='{value}'. Must be one of: {', '.join(VALID_BODY_SWITCHING_PROTOCOLS_LOG)}",
            )
    if "rpc-over-http" in payload:
        value = payload["rpc-over-http"]
        if value not in VALID_BODY_RPC_OVER_HTTP:
            return (
                False,
                f"Invalid value for 'rpc-over-http'='{value}'. Must be one of: {', '.join(VALID_BODY_RPC_OVER_HTTP)}",
            )

    return (True, None)


# ============================================================================
# Metadata Access Functions
# Imported from central module to avoid duplication across 1,062 files
# ============================================================================

from hfortix_fortios._helpers.metadata import (
    get_field_description as _get_field_description,
    get_field_type as _get_field_type,
    get_field_constraints as _get_field_constraints,
    get_field_default as _get_field_default,
    get_field_options as _get_field_options,
    get_nested_schema as _get_nested_schema,
    get_all_fields as _get_all_fields,
    get_field_metadata as _get_field_metadata,
    validate_field_value as _validate_field_value,
)

# Wrapper functions that bind module-specific data to central functions
def get_field_description(field_name: str) -> str | None:
    """Get description/help text for a field."""
    return _get_field_description(FIELD_DESCRIPTIONS, field_name)

def get_field_type(field_name: str) -> str | None:
    """Get the type of a field."""
    return _get_field_type(FIELD_TYPES, field_name)

def get_field_constraints(field_name: str) -> dict[str, Any] | None:
    """Get constraints for a field (min/max values, string length)."""
    return _get_field_constraints(FIELD_CONSTRAINTS, field_name)

def get_field_default(field_name: str) -> Any | None:
    """Get default value for a field."""
    return _get_field_default(FIELDS_WITH_DEFAULTS, field_name)

def get_field_options(field_name: str) -> list[str] | None:
    """Get valid enum options for a field."""
    return _get_field_options(globals(), field_name)

def get_nested_schema(field_name: str) -> dict[str, Any] | None:
    """Get schema for nested table/list fields."""
    return _get_nested_schema(NESTED_SCHEMAS, field_name)

def get_all_fields() -> list[str]:
    """Get list of all field names."""
    return _get_all_fields(FIELD_TYPES)

def get_field_metadata(field_name: str) -> dict[str, Any] | None:
    """Get complete metadata for a field (type, description, constraints, defaults, options)."""
    return _get_field_metadata(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        FIELDS_WITH_DEFAULTS, REQUIRED_FIELDS, NESTED_SCHEMAS,
        globals(), field_name
    )

def validate_field_value(field_name: str, value: Any) -> tuple[bool, str | None]:
    """Validate a single field value against its constraints."""
    return _validate_field_value(
        FIELD_TYPES, FIELD_DESCRIPTIONS, FIELD_CONSTRAINTS,
        globals(), field_name, value
    )


# ============================================================================
# Schema Information
# Metadata about this endpoint schema
# ============================================================================

SCHEMA_INFO = {
    "endpoint": "firewall/profile_protocol_options",
    "category": "cmdb",
    "api_path": "firewall/profile-protocol-options",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure protocol options.",
    "total_fields": 17,
    "required_fields_count": 1,
    "fields_with_defaults_count": 5,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()

"""Validation helpers for antivirus/profile - Auto-generated"""

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
    "name",  # Profile name.
]

# Fields with defaults (optional)
FIELDS_WITH_DEFAULTS = {
    "name": "",
    "replacemsg-group": "",
    "feature-set": "flow",
    "fortisandbox-mode": "analytics-everything",
    "fortisandbox-max-upload": 10,
    "analytics-ignore-filetype": 0,
    "analytics-accept-filetype": 0,
    "analytics-db": "disable",
    "mobile-malware-db": "enable",
    "outbreak-prevention-archive-scan": "enable",
    "external-blocklist-enable-all": "disable",
    "ems-threat-feed": "disable",
    "fortindr-error-action": "log-only",
    "fortindr-timeout-action": "log-only",
    "fortisandbox-scan-timeout": 60,
    "fortisandbox-error-action": "log-only",
    "fortisandbox-timeout-action": "log-only",
    "av-virus-log": "enable",
    "extended-log": "disable",
    "scan-mode": "default",
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
    "name": "string",  # Profile name.
    "comment": "var-string",  # Comment.
    "replacemsg-group": "string",  # Replacement message group customized for this profile.
    "feature-set": "option",  # Flow/proxy feature set.
    "fortisandbox-mode": "option",  # FortiSandbox scan modes.
    "fortisandbox-max-upload": "integer",  # Maximum size of files that can be uploaded to FortiSandbox i
    "analytics-ignore-filetype": "integer",  # Do not submit files matching this DLP file-pattern to FortiS
    "analytics-accept-filetype": "integer",  # Only submit files matching this DLP file-pattern to FortiSan
    "analytics-db": "option",  # Enable/disable using the FortiSandbox signature database to 
    "mobile-malware-db": "option",  # Enable/disable using the mobile malware signature database.
    "http": "string",  # Configure HTTP AntiVirus options.
    "ftp": "string",  # Configure FTP AntiVirus options.
    "imap": "string",  # Configure IMAP AntiVirus options.
    "pop3": "string",  # Configure POP3 AntiVirus options.
    "smtp": "string",  # Configure SMTP AntiVirus options.
    "mapi": "string",  # Configure MAPI AntiVirus options.
    "nntp": "string",  # Configure NNTP AntiVirus options.
    "cifs": "string",  # Configure CIFS AntiVirus options.
    "ssh": "string",  # Configure SFTP and SCP AntiVirus options.
    "nac-quar": "string",  # Configure AntiVirus quarantine settings.
    "content-disarm": "string",  # AV Content Disarm and Reconstruction settings.
    "outbreak-prevention-archive-scan": "option",  # Enable/disable outbreak-prevention archive scanning.
    "external-blocklist-enable-all": "option",  # Enable/disable all external blocklists.
    "external-blocklist": "string",  # One or more external malware block lists.
    "ems-threat-feed": "option",  # Enable/disable use of EMS threat feed when performing AntiVi
    "fortindr-error-action": "option",  # Action to take if FortiNDR encounters an error.
    "fortindr-timeout-action": "option",  # Action to take if FortiNDR encounters a scan timeout.
    "fortisandbox-scan-timeout": "integer",  # FortiSandbox inline scan timeout in seconds (30 - 180, defau
    "fortisandbox-error-action": "option",  # Action to take if FortiSandbox inline scan encounters an err
    "fortisandbox-timeout-action": "option",  # Action to take if FortiSandbox inline scan encounters a scan
    "av-virus-log": "option",  # Enable/disable AntiVirus logging.
    "extended-log": "option",  # Enable/disable extended logging for antivirus.
    "scan-mode": "option",  # Configure scan mode (default or legacy).
}

# Field descriptions (help text from FortiOS API)
FIELD_DESCRIPTIONS = {
    "name": "Profile name.",
    "comment": "Comment.",
    "replacemsg-group": "Replacement message group customized for this profile.",
    "feature-set": "Flow/proxy feature set.",
    "fortisandbox-mode": "FortiSandbox scan modes.",
    "fortisandbox-max-upload": "Maximum size of files that can be uploaded to FortiSandbox in Mbytes.",
    "analytics-ignore-filetype": "Do not submit files matching this DLP file-pattern to FortiSandbox (post-transfer scan only).",
    "analytics-accept-filetype": "Only submit files matching this DLP file-pattern to FortiSandbox (post-transfer scan only).",
    "analytics-db": "Enable/disable using the FortiSandbox signature database to supplement the AV signature databases.",
    "mobile-malware-db": "Enable/disable using the mobile malware signature database.",
    "http": "Configure HTTP AntiVirus options.",
    "ftp": "Configure FTP AntiVirus options.",
    "imap": "Configure IMAP AntiVirus options.",
    "pop3": "Configure POP3 AntiVirus options.",
    "smtp": "Configure SMTP AntiVirus options.",
    "mapi": "Configure MAPI AntiVirus options.",
    "nntp": "Configure NNTP AntiVirus options.",
    "cifs": "Configure CIFS AntiVirus options.",
    "ssh": "Configure SFTP and SCP AntiVirus options.",
    "nac-quar": "Configure AntiVirus quarantine settings.",
    "content-disarm": "AV Content Disarm and Reconstruction settings.",
    "outbreak-prevention-archive-scan": "Enable/disable outbreak-prevention archive scanning.",
    "external-blocklist-enable-all": "Enable/disable all external blocklists.",
    "external-blocklist": "One or more external malware block lists.",
    "ems-threat-feed": "Enable/disable use of EMS threat feed when performing AntiVirus scan. Analyzes files including the content of archives.",
    "fortindr-error-action": "Action to take if FortiNDR encounters an error.",
    "fortindr-timeout-action": "Action to take if FortiNDR encounters a scan timeout.",
    "fortisandbox-scan-timeout": "FortiSandbox inline scan timeout in seconds (30 - 180, default = 60).",
    "fortisandbox-error-action": "Action to take if FortiSandbox inline scan encounters an error.",
    "fortisandbox-timeout-action": "Action to take if FortiSandbox inline scan encounters a scan timeout.",
    "av-virus-log": "Enable/disable AntiVirus logging.",
    "extended-log": "Enable/disable extended logging for antivirus.",
    "scan-mode": "Configure scan mode (default or legacy).",
}

# Field constraints (string lengths, integer ranges)
FIELD_CONSTRAINTS = {
    "name": {"type": "string", "max_length": 47},
    "replacemsg-group": {"type": "string", "max_length": 35},
    "fortisandbox-max-upload": {"type": "integer", "min": 1, "max": 4095},
    "analytics-ignore-filetype": {"type": "integer", "min": 0, "max": 4294967295},
    "analytics-accept-filetype": {"type": "integer", "min": 0, "max": 4294967295},
    "fortisandbox-scan-timeout": {"type": "integer", "min": 30, "max": 180},
}

# Nested schemas (for table/list fields with children)
NESTED_SCHEMAS = {
    "http": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
        "content-disarm": {
            "type": "option",
            "help": "Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.",
            "default": "disable",
            "options": [{"help": "Disable Content Disarm and Reconstruction when performing AntiVirus scan.", "label": "Disable", "name": "disable"}, {"help": "Enable Content Disarm and Reconstruction when performing AntiVirus scan.", "label": "Enable", "name": "enable"}],
        },
    },
    "ftp": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
    },
    "imap": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
        "executables": {
            "type": "option",
            "help": "Treat Windows executable files as viruses for the purpose of blocking or monitoring.",
            "default": "default",
            "options": [{"help": "Perform standard AntiVirus scanning of Windows executable files.", "label": "Default", "name": "default"}, {"help": "Treat Windows executables as viruses.", "label": "Virus", "name": "virus"}],
        },
        "content-disarm": {
            "type": "option",
            "help": "Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.",
            "default": "disable",
            "options": [{"help": "Disable Content Disarm and Reconstruction when performing AntiVirus scan.", "label": "Disable", "name": "disable"}, {"help": "Enable Content Disarm and Reconstruction when performing AntiVirus scan.", "label": "Enable", "name": "enable"}],
        },
    },
    "pop3": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
        "executables": {
            "type": "option",
            "help": "Treat Windows executable files as viruses for the purpose of blocking or monitoring.",
            "default": "default",
            "options": [{"help": "Perform standard AntiVirus scanning of Windows executable files.", "label": "Default", "name": "default"}, {"help": "Treat Windows executables as viruses.", "label": "Virus", "name": "virus"}],
        },
        "content-disarm": {
            "type": "option",
            "help": "Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.",
            "default": "disable",
            "options": [{"help": "Disable Content Disarm and Reconstruction when performing AntiVirus scan.", "label": "Disable", "name": "disable"}, {"help": "Enable Content Disarm and Reconstruction when performing AntiVirus scan.", "label": "Enable", "name": "enable"}],
        },
    },
    "smtp": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
        "executables": {
            "type": "option",
            "help": "Treat Windows executable files as viruses for the purpose of blocking or monitoring.",
            "default": "default",
            "options": [{"help": "Perform standard AntiVirus scanning of Windows executable files.", "label": "Default", "name": "default"}, {"help": "Treat Windows executables as viruses.", "label": "Virus", "name": "virus"}],
        },
        "content-disarm": {
            "type": "option",
            "help": "Enable/disable Content Disarm and Reconstruction when performing AntiVirus scan.",
            "default": "disable",
            "options": [{"help": "Disable Content Disarm and Reconstruction when performing AntiVirus scan.", "label": "Disable", "name": "disable"}, {"help": "Enable Content Disarm and Reconstruction when performing AntiVirus scan.", "label": "Enable", "name": "enable"}],
        },
    },
    "mapi": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
        "executables": {
            "type": "option",
            "help": "Treat Windows executable files as viruses for the purpose of blocking or monitoring.",
            "default": "default",
            "options": [{"help": "Perform standard AntiVirus scanning of Windows executable files.", "label": "Default", "name": "default"}, {"help": "Treat Windows executables as viruses.", "label": "Virus", "name": "virus"}],
        },
    },
    "nntp": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
    },
    "cifs": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
    },
    "ssh": {
        "av-scan": {
            "type": "option",
            "help": "Enable AntiVirus scan service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the virus infected files.", "label": "Block", "name": "block"}, {"help": "Log the virus infected files.", "label": "Monitor", "name": "monitor"}],
        },
        "outbreak-prevention": {
            "type": "option",
            "help": "Enable virus outbreak prevention service.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "external-blocklist": {
            "type": "option",
            "help": "Enable external-blocklist. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "malware-stream": {
            "type": "option",
            "help": "Enable 0-day malware-stream scanning. Analyzes files including the content of archives.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the matched files.", "label": "Block", "name": "block"}, {"help": "Log the matched files.", "label": "Monitor", "name": "monitor"}],
        },
        "fortindr": {
            "type": "option",
            "help": "Enable scanning of files by FortiNDR.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiNDR detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiNDR detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "fortisandbox": {
            "type": "option",
            "help": "Enable scanning of files by FortiSandbox.",
            "default": "disable",
            "options": [{"help": "Disable.", "label": "Disable", "name": "disable"}, {"help": "Block the FortiSandbox detected infections.", "label": "Block", "name": "block"}, {"help": "Log the FortiSandbox detected infections.", "label": "Monitor", "name": "monitor"}],
        },
        "quarantine": {
            "type": "option",
            "help": "Enable/disable quarantine for infected files.",
            "default": "disable",
            "options": [{"help": "Disable quarantine for infected files.", "label": "Disable", "name": "disable"}, {"help": "Enable quarantine for infected files.", "label": "Enable", "name": "enable"}],
        },
        "archive-block": {
            "type": "option",
            "help": "Select the archive types to block.",
            "default": "",
            "options": [{"help": "Block encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Block corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Block partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Block multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Block nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Block mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Block scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Block archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "archive-log": {
            "type": "option",
            "help": "Select the archive types to log.",
            "default": "",
            "options": [{"help": "Log encrypted archives.", "label": "Encrypted", "name": "encrypted"}, {"help": "Log corrupted archives.", "label": "Corrupted", "name": "corrupted"}, {"help": "Log partially corrupted archives.", "label": "Partiallycorrupted", "name": "partiallycorrupted"}, {"help": "Log multipart archives.", "label": "Multipart", "name": "multipart"}, {"help": "Log nested archives that exceed uncompressed nest limit.", "label": "Nested", "name": "nested"}, {"help": "Log mail bomb archives.", "label": "Mailbomb", "name": "mailbomb"}, {"help": "Log scan timeout.", "label": "Timeout", "name": "timeout"}, {"help": "Log archives that FortiOS cannot open.", "label": "Unhandled", "name": "unhandled"}],
        },
        "emulator": {
            "type": "option",
            "help": "Enable/disable the virus emulator.",
            "default": "enable",
            "options": [{"help": "Enable the virus emulator.", "label": "Enable", "name": "enable"}, {"help": "Disable the virus emulator.", "label": "Disable", "name": "disable"}],
        },
    },
    "nac-quar": {
        "infected": {
            "type": "option",
            "help": "Enable/Disable quarantining infected hosts to the banned user list.",
            "default": "none",
            "options": [{"help": "Do not quarantine infected hosts.", "label": "None", "name": "none"}, {"help": "Quarantine all traffic from the infected hosts source IP.", "label": "Quar Src Ip", "name": "quar-src-ip"}],
        },
        "expiry": {
            "type": "user",
            "help": "Duration of quarantine.",
            "default": "5m",
        },
        "log": {
            "type": "option",
            "help": "Enable/disable AntiVirus quarantine logging.",
            "default": "disable",
            "options": [{"help": "Enable AntiVirus quarantine logging.", "label": "Enable", "name": "enable"}, {"help": "Disable AntiVirus quarantine logging.", "label": "Disable", "name": "disable"}],
        },
    },
    "content-disarm": {
        "analytics-suspicious": {
            "type": "option",
            "help": "Enable/disable using CDR as a secondary method for determining suspicous files for analytics.",
            "default": "enable",
            "options": [{"help": "", "label": "Disable", "name": "disable"}, {"help": "", "label": "Enable", "name": "enable"}],
        },
        "original-file-destination": {
            "type": "option",
            "help": "Destination to send original file if active content is removed.",
            "default": "discard",
            "options": [{"help": "Send original file to configured FortiSandbox.", "label": "Fortisandbox", "name": "fortisandbox"}, {"help": "Send original file to quarantine.", "label": "Quarantine", "name": "quarantine"}, {"help": "Original file will be discarded after content disarm.", "label": "Discard", "name": "discard"}],
        },
        "error-action": {
            "type": "option",
            "help": "Action to be taken if CDR engine encounters an unrecoverable error.",
            "default": "log-only",
            "options": [{"help": "Block file on CDR error.", "label": "Block", "name": "block"}, {"help": "Log CDR error, but allow file.", "label": "Log Only", "name": "log-only"}, {"help": "Do nothing on CDR error.", "label": "Ignore", "name": "ignore"}],
        },
        "office-macro": {
            "type": "option",
            "help": "Enable/disable stripping of macros in Microsoft Office documents.",
            "default": "enable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "office-hylink": {
            "type": "option",
            "help": "Enable/disable stripping of hyperlinks in Microsoft Office documents.",
            "default": "enable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "office-linked": {
            "type": "option",
            "help": "Enable/disable stripping of linked objects in Microsoft Office documents.",
            "default": "",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "office-embed": {
            "type": "option",
            "help": "Enable/disable stripping of embedded objects in Microsoft Office documents.",
            "default": "enable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "office-dde": {
            "type": "option",
            "help": "Enable/disable stripping of Dynamic Data Exchange events in Microsoft Office documents.",
            "default": "",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "office-action": {
            "type": "option",
            "help": "Enable/disable stripping of PowerPoint action events in Microsoft Office documents.",
            "default": "enable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-javacode": {
            "type": "option",
            "help": "Enable/disable stripping of JavaScript code in PDF documents.",
            "default": "",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-embedfile": {
            "type": "option",
            "help": "Enable/disable stripping of embedded files in PDF documents.",
            "default": "enable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-hyperlink": {
            "type": "option",
            "help": "Enable/disable stripping of hyperlinks from PDF documents.",
            "default": "",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-act-gotor": {
            "type": "option",
            "help": "Enable/disable stripping of PDF document actions that access other PDF documents.",
            "default": "enable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-act-launch": {
            "type": "option",
            "help": "Enable/disable stripping of PDF document actions that launch other applications.",
            "default": "enable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-act-sound": {
            "type": "option",
            "help": "Enable/disable stripping of PDF document actions that play a sound.",
            "default": "",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-act-movie": {
            "type": "option",
            "help": "Enable/disable stripping of PDF document actions that play a movie.",
            "default": "",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-act-java": {
            "type": "option",
            "help": "Enable/disable stripping of PDF document actions that execute JavaScript code.",
            "default": "",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "pdf-act-form": {
            "type": "option",
            "help": "Enable/disable stripping of PDF document actions that submit data to other targets.",
            "default": "",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "cover-page": {
            "type": "option",
            "help": "Enable/disable inserting a cover page into the disarmed document.",
            "default": "enable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
        "detect-only": {
            "type": "option",
            "help": "Enable/disable only detect disarmable files, do not alter content.",
            "default": "disable",
            "options": [{"help": "Disable this Content Disarm and Reconstruction feature.", "label": "Disable", "name": "disable"}, {"help": "Enable this Content Disarm and Reconstruction feature.", "label": "Enable", "name": "enable"}],
        },
    },
    "external-blocklist": {
        "name": {
            "type": "string",
            "help": "External blocklist.",
            "default": "",
            "max_length": 79,
        },
    },
}


# Valid enum values from API documentation
VALID_BODY_FEATURE_SET = [
    "flow",  # Flow feature set.
    "proxy",  # Proxy feature set.
]
VALID_BODY_FORTISANDBOX_MODE = [
    "inline",  # FortiSandbox inline scan.
    "analytics-suspicious",  # FortiSandbox post-transfer scan: submit supported files if heuristics or other methods determine they are suspicious.
    "analytics-everything",  # FortiSandbox post-transfer scan: submit supported files for inspection.
]
VALID_BODY_ANALYTICS_DB = [
    "disable",  # Use only the standard AV signature databases.
    "enable",  # Also use the FortiSandbox signature database.
]
VALID_BODY_MOBILE_MALWARE_DB = [
    "disable",  # Do not use the mobile malware signature database.
    "enable",  # Also use the mobile malware signature database.
]
VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN = [
    "disable",  # Analyze files as sent, not the content of archives.
    "enable",  # Analyze files including the content of archives.
]
VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL = [
    "disable",  # Use configured external blocklists.
    "enable",  # Enable all external blocklists.
]
VALID_BODY_EMS_THREAT_FEED = [
    "disable",  # Disable use of EMS threat feed when performing AntiVirus scan.
    "enable",  # Enable use of EMS threat feed when performing AntiVirus scan.
]
VALID_BODY_FORTINDR_ERROR_ACTION = [
    "log-only",  # Log FortiNDR error, but allow the file.
    "block",  # Block the file on FortiNDR error.
    "ignore",  # Do nothing on FortiNDR error.
]
VALID_BODY_FORTINDR_TIMEOUT_ACTION = [
    "log-only",  # Log FortiNDR scan timeout, but allow the file.
    "block",  # Block the file on FortiNDR scan timeout.
    "ignore",  # Do nothing on FortiNDR scan timeout.
]
VALID_BODY_FORTISANDBOX_ERROR_ACTION = [
    "log-only",  # Log FortiSandbox inline scan error, but allow the file.
    "block",  # Block the file on FortiSandbox inline scan error.
    "ignore",  # Do nothing on FortiSandbox inline scan error.
]
VALID_BODY_FORTISANDBOX_TIMEOUT_ACTION = [
    "log-only",  # Log FortiSandbox inline scan timeout, but allow the file.
    "block",  # Block the file on FortiSandbox inline scan timeout.
    "ignore",  # Do nothing on FortiSandbox inline scan timeout.
]
VALID_BODY_AV_VIRUS_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_EXTENDED_LOG = [
    "enable",  # Enable setting.
    "disable",  # Disable setting.
]
VALID_BODY_SCAN_MODE = [
    "default",  # On the fly decompression and scanning of certain archive files.
    "legacy",  # Scan archive files only after the entire file is received.
]
VALID_QUERY_ACTION = ["default", "schema"]

# ============================================================================
# GET Validation
# ============================================================================


def validate_antivirus_profile_get(
    attr: str | None = None,
    filters: dict[str, Any] | None = None,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate GET request parameters for antivirus/profile."""
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
    """Validate required fields for antivirus/profile."""
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


def validate_antivirus_profile_post(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate POST request to create new antivirus/profile object."""
    # Step 1: Validate required fields
    is_valid, error = validate_required_fields(payload)
    if not is_valid:
        return (False, error)

    # Step 2: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            desc = FIELD_DESCRIPTIONS.get("feature-set", "")
            error_msg = f"Invalid value for 'feature-set': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FEATURE_SET)}"
            error_msg += f"\n  → Example: feature-set='{{ VALID_BODY_FEATURE_SET[0] }}'"
            return (False, error_msg)
    if "fortisandbox-mode" in payload:
        value = payload["fortisandbox-mode"]
        if value not in VALID_BODY_FORTISANDBOX_MODE:
            desc = FIELD_DESCRIPTIONS.get("fortisandbox-mode", "")
            error_msg = f"Invalid value for 'fortisandbox-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTISANDBOX_MODE)}"
            error_msg += f"\n  → Example: fortisandbox-mode='{{ VALID_BODY_FORTISANDBOX_MODE[0] }}'"
            return (False, error_msg)
    if "analytics-db" in payload:
        value = payload["analytics-db"]
        if value not in VALID_BODY_ANALYTICS_DB:
            desc = FIELD_DESCRIPTIONS.get("analytics-db", "")
            error_msg = f"Invalid value for 'analytics-db': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_ANALYTICS_DB)}"
            error_msg += f"\n  → Example: analytics-db='{{ VALID_BODY_ANALYTICS_DB[0] }}'"
            return (False, error_msg)
    if "mobile-malware-db" in payload:
        value = payload["mobile-malware-db"]
        if value not in VALID_BODY_MOBILE_MALWARE_DB:
            desc = FIELD_DESCRIPTIONS.get("mobile-malware-db", "")
            error_msg = f"Invalid value for 'mobile-malware-db': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_MOBILE_MALWARE_DB)}"
            error_msg += f"\n  → Example: mobile-malware-db='{{ VALID_BODY_MOBILE_MALWARE_DB[0] }}'"
            return (False, error_msg)
    if "outbreak-prevention-archive-scan" in payload:
        value = payload["outbreak-prevention-archive-scan"]
        if value not in VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN:
            desc = FIELD_DESCRIPTIONS.get("outbreak-prevention-archive-scan", "")
            error_msg = f"Invalid value for 'outbreak-prevention-archive-scan': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN)}"
            error_msg += f"\n  → Example: outbreak-prevention-archive-scan='{{ VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN[0] }}'"
            return (False, error_msg)
    if "external-blocklist-enable-all" in payload:
        value = payload["external-blocklist-enable-all"]
        if value not in VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL:
            desc = FIELD_DESCRIPTIONS.get("external-blocklist-enable-all", "")
            error_msg = f"Invalid value for 'external-blocklist-enable-all': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL)}"
            error_msg += f"\n  → Example: external-blocklist-enable-all='{{ VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL[0] }}'"
            return (False, error_msg)
    if "ems-threat-feed" in payload:
        value = payload["ems-threat-feed"]
        if value not in VALID_BODY_EMS_THREAT_FEED:
            desc = FIELD_DESCRIPTIONS.get("ems-threat-feed", "")
            error_msg = f"Invalid value for 'ems-threat-feed': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EMS_THREAT_FEED)}"
            error_msg += f"\n  → Example: ems-threat-feed='{{ VALID_BODY_EMS_THREAT_FEED[0] }}'"
            return (False, error_msg)
    if "fortindr-error-action" in payload:
        value = payload["fortindr-error-action"]
        if value not in VALID_BODY_FORTINDR_ERROR_ACTION:
            desc = FIELD_DESCRIPTIONS.get("fortindr-error-action", "")
            error_msg = f"Invalid value for 'fortindr-error-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTINDR_ERROR_ACTION)}"
            error_msg += f"\n  → Example: fortindr-error-action='{{ VALID_BODY_FORTINDR_ERROR_ACTION[0] }}'"
            return (False, error_msg)
    if "fortindr-timeout-action" in payload:
        value = payload["fortindr-timeout-action"]
        if value not in VALID_BODY_FORTINDR_TIMEOUT_ACTION:
            desc = FIELD_DESCRIPTIONS.get("fortindr-timeout-action", "")
            error_msg = f"Invalid value for 'fortindr-timeout-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTINDR_TIMEOUT_ACTION)}"
            error_msg += f"\n  → Example: fortindr-timeout-action='{{ VALID_BODY_FORTINDR_TIMEOUT_ACTION[0] }}'"
            return (False, error_msg)
    if "fortisandbox-error-action" in payload:
        value = payload["fortisandbox-error-action"]
        if value not in VALID_BODY_FORTISANDBOX_ERROR_ACTION:
            desc = FIELD_DESCRIPTIONS.get("fortisandbox-error-action", "")
            error_msg = f"Invalid value for 'fortisandbox-error-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTISANDBOX_ERROR_ACTION)}"
            error_msg += f"\n  → Example: fortisandbox-error-action='{{ VALID_BODY_FORTISANDBOX_ERROR_ACTION[0] }}'"
            return (False, error_msg)
    if "fortisandbox-timeout-action" in payload:
        value = payload["fortisandbox-timeout-action"]
        if value not in VALID_BODY_FORTISANDBOX_TIMEOUT_ACTION:
            desc = FIELD_DESCRIPTIONS.get("fortisandbox-timeout-action", "")
            error_msg = f"Invalid value for 'fortisandbox-timeout-action': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_FORTISANDBOX_TIMEOUT_ACTION)}"
            error_msg += f"\n  → Example: fortisandbox-timeout-action='{{ VALID_BODY_FORTISANDBOX_TIMEOUT_ACTION[0] }}'"
            return (False, error_msg)
    if "av-virus-log" in payload:
        value = payload["av-virus-log"]
        if value not in VALID_BODY_AV_VIRUS_LOG:
            desc = FIELD_DESCRIPTIONS.get("av-virus-log", "")
            error_msg = f"Invalid value for 'av-virus-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_AV_VIRUS_LOG)}"
            error_msg += f"\n  → Example: av-virus-log='{{ VALID_BODY_AV_VIRUS_LOG[0] }}'"
            return (False, error_msg)
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            desc = FIELD_DESCRIPTIONS.get("extended-log", "")
            error_msg = f"Invalid value for 'extended-log': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_EXTENDED_LOG)}"
            error_msg += f"\n  → Example: extended-log='{{ VALID_BODY_EXTENDED_LOG[0] }}'"
            return (False, error_msg)
    if "scan-mode" in payload:
        value = payload["scan-mode"]
        if value not in VALID_BODY_SCAN_MODE:
            desc = FIELD_DESCRIPTIONS.get("scan-mode", "")
            error_msg = f"Invalid value for 'scan-mode': '{value}'"
            if desc:
                error_msg += f"\n  → Description: {desc}"
            error_msg += f"\n  → Valid options: {', '.join(repr(v) for v in VALID_BODY_SCAN_MODE)}"
            error_msg += f"\n  → Example: scan-mode='{{ VALID_BODY_SCAN_MODE[0] }}'"
            return (False, error_msg)

    return (True, None)


# ============================================================================
# PUT Validation
# ============================================================================


def validate_antivirus_profile_put(
    payload: dict,
    **params: Any,
) -> tuple[bool, str | None]:
    """Validate PUT request to update antivirus/profile."""
    # Step 1: Validate enum values
    if "feature-set" in payload:
        value = payload["feature-set"]
        if value not in VALID_BODY_FEATURE_SET:
            return (
                False,
                f"Invalid value for 'feature-set'='{value}'. Must be one of: {', '.join(VALID_BODY_FEATURE_SET)}",
            )
    if "fortisandbox-mode" in payload:
        value = payload["fortisandbox-mode"]
        if value not in VALID_BODY_FORTISANDBOX_MODE:
            return (
                False,
                f"Invalid value for 'fortisandbox-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTISANDBOX_MODE)}",
            )
    if "analytics-db" in payload:
        value = payload["analytics-db"]
        if value not in VALID_BODY_ANALYTICS_DB:
            return (
                False,
                f"Invalid value for 'analytics-db'='{value}'. Must be one of: {', '.join(VALID_BODY_ANALYTICS_DB)}",
            )
    if "mobile-malware-db" in payload:
        value = payload["mobile-malware-db"]
        if value not in VALID_BODY_MOBILE_MALWARE_DB:
            return (
                False,
                f"Invalid value for 'mobile-malware-db'='{value}'. Must be one of: {', '.join(VALID_BODY_MOBILE_MALWARE_DB)}",
            )
    if "outbreak-prevention-archive-scan" in payload:
        value = payload["outbreak-prevention-archive-scan"]
        if value not in VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN:
            return (
                False,
                f"Invalid value for 'outbreak-prevention-archive-scan'='{value}'. Must be one of: {', '.join(VALID_BODY_OUTBREAK_PREVENTION_ARCHIVE_SCAN)}",
            )
    if "external-blocklist-enable-all" in payload:
        value = payload["external-blocklist-enable-all"]
        if value not in VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL:
            return (
                False,
                f"Invalid value for 'external-blocklist-enable-all'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTERNAL_BLOCKLIST_ENABLE_ALL)}",
            )
    if "ems-threat-feed" in payload:
        value = payload["ems-threat-feed"]
        if value not in VALID_BODY_EMS_THREAT_FEED:
            return (
                False,
                f"Invalid value for 'ems-threat-feed'='{value}'. Must be one of: {', '.join(VALID_BODY_EMS_THREAT_FEED)}",
            )
    if "fortindr-error-action" in payload:
        value = payload["fortindr-error-action"]
        if value not in VALID_BODY_FORTINDR_ERROR_ACTION:
            return (
                False,
                f"Invalid value for 'fortindr-error-action'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTINDR_ERROR_ACTION)}",
            )
    if "fortindr-timeout-action" in payload:
        value = payload["fortindr-timeout-action"]
        if value not in VALID_BODY_FORTINDR_TIMEOUT_ACTION:
            return (
                False,
                f"Invalid value for 'fortindr-timeout-action'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTINDR_TIMEOUT_ACTION)}",
            )
    if "fortisandbox-error-action" in payload:
        value = payload["fortisandbox-error-action"]
        if value not in VALID_BODY_FORTISANDBOX_ERROR_ACTION:
            return (
                False,
                f"Invalid value for 'fortisandbox-error-action'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTISANDBOX_ERROR_ACTION)}",
            )
    if "fortisandbox-timeout-action" in payload:
        value = payload["fortisandbox-timeout-action"]
        if value not in VALID_BODY_FORTISANDBOX_TIMEOUT_ACTION:
            return (
                False,
                f"Invalid value for 'fortisandbox-timeout-action'='{value}'. Must be one of: {', '.join(VALID_BODY_FORTISANDBOX_TIMEOUT_ACTION)}",
            )
    if "av-virus-log" in payload:
        value = payload["av-virus-log"]
        if value not in VALID_BODY_AV_VIRUS_LOG:
            return (
                False,
                f"Invalid value for 'av-virus-log'='{value}'. Must be one of: {', '.join(VALID_BODY_AV_VIRUS_LOG)}",
            )
    if "extended-log" in payload:
        value = payload["extended-log"]
        if value not in VALID_BODY_EXTENDED_LOG:
            return (
                False,
                f"Invalid value for 'extended-log'='{value}'. Must be one of: {', '.join(VALID_BODY_EXTENDED_LOG)}",
            )
    if "scan-mode" in payload:
        value = payload["scan-mode"]
        if value not in VALID_BODY_SCAN_MODE:
            return (
                False,
                f"Invalid value for 'scan-mode'='{value}'. Must be one of: {', '.join(VALID_BODY_SCAN_MODE)}",
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
    "endpoint": "antivirus/profile",
    "category": "cmdb",
    "api_path": "antivirus/profile",
    "mkey": "name",
    "mkey_type": "string",
    "help": "Configure AntiVirus profiles.",
    "total_fields": 33,
    "required_fields_count": 1,
    "fields_with_defaults_count": 20,
}


def get_schema_info() -> dict[str, Any]:
    """Get information about this endpoint schema."""
    return SCHEMA_INFO.copy()

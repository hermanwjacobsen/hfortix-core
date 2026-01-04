"""Type stubs for WIFI category."""

from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hfortix_core.http.interface import IHTTPClient
    from . import ap_channels
    from . import ap_names
    from . import ap_profile
    from . import ap_status
    from . import client_ns
    from . import euclid
    from . import firmware
    from . import interfering_ap
    from . import managed_ap
    from . import matched_devices
    from . import meta
    from . import nac_device
    from . import network
    from . import region_image
    from . import rogue_ap
    from . import spectrum
    from . import ssid
    from . import station_capability
    from . import statistics
    from . import unassociated_devices
    from . import vlan_probe


class Wifi:
    """Type stub for Wifi."""

    ap_profile: ap_profile.ApProfile
    client: client_ns.Client
    euclid: euclid.Euclid
    firmware: firmware.Firmware
    managed_ap: managed_ap.ManagedAp
    network: network.Network
    region_image: region_image.RegionImage
    rogue_ap: rogue_ap.RogueAp
    spectrum: spectrum.Spectrum
    ssid: ssid.Ssid
    vlan_probe: vlan_probe.VlanProbe
    ap_channels: ap_channels.ApChannels
    ap_names: ap_names.ApNames
    ap_status: ap_status.ApStatus
    interfering_ap: interfering_ap.InterferingAp
    matched_devices: matched_devices.MatchedDevices
    meta: meta.Meta
    nac_device: nac_device.NacDevice
    station_capability: station_capability.StationCapability
    statistics: statistics.Statistics
    unassociated_devices: unassociated_devices.UnassociatedDevices

    def __init__(self, client: IHTTPClient) -> None: ...

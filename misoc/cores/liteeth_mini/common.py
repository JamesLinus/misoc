from migen import *

eth_mtu = 1532
eth_min_len = 46
eth_interpacket_gap = 12
eth_preamble = 0xD555555555555555
buffer_depth = 2**log2_int(eth_mtu, need_pow2=False)


def eth_phy_description(dw):
    return [
        ("data", dw),
        ("last_be", dw//8),
        ("error", dw//8)
    ]

def eth_mac_description(dw):
    return mac_header.get_layout() + [
        ("data", dw),
        ("last_be", dw//8),
        ("error", dw//8)
    ]
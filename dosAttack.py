#! /usr/bin/python3
import multiprocessing
import scapy.all as scapy

def test(source="127.0.01",dest="127.0.01"):
    print("source = " + source)
    print("dest = " + dest)
    packet = scapy.IP(ttl=10)
    packet.src = source
    packet.dst = dest



dest = "192.168.1.111"
test(dest=dest)


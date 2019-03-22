#! /usr/bin/python3
import multiprocessing
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
# import scapy.all as scapy
from scapy.all import *

# def test(source="127.0.01",dest="127.0.01"):
#     print("source = " + source)
#     print("dest = " + dest)
#     packet = scapy.IP(ttl=10)/scapy.TCP()
#     packet.src = source
#     packet.dst = dest
#     return packet

# Source for this text can be found at : 
def TCPScan(dest="127.0.0.1", sourceport=65000,destport=80):
    dst_ip = dest
    src_port = sourceport
    dst_port=destport
    stealth_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S")/"Hello There",timeout=10, verbose=0)
    if(str(type(stealth_scan_resp))=="<class 'NoneType'>"):
        return "Filtered"
    elif(stealth_scan_resp.haslayer(TCP)):
        if(stealth_scan_resp.getlayer(TCP).flags == 0x12):
            send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R")/"Hello There",timeout=10, verbose=0)
            return "Open"
        elif (stealth_scan_resp.getlayer(TCP).flags == 0x14):
            return "Closed"
    elif(stealth_scan_resp.haslayer(ICMP)):
        if(int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            return "Filtered"

def UDPScan(dest="127.0.0.1", sourceport=65000,destport=80):
    dst_ip = dest
    src_port = sourceport
    dst_port=destport
    stealth_scan_resp = sr1(IP(dst=dst_ip)/UDP(sport=src_port,dport=dst_port,flags="S")/"Hello There",timeout=10, verbose=0)
    if(str(type(stealth_scan_resp))=="<class 'NoneType'>"):
        return "Filtered"
    elif(stealth_scan_resp.haslayer(UDP)):
        if(stealth_scan_resp.getlayer(UDP).flags == 0x12):
            send_rst = sr(IP(dst=dst_ip)/UDP(sport=src_port,dport=dst_port,flags="R")/"dosAtackPayload",timeout=10, verbose=0)
            return "Open"
        elif (stealth_scan_resp.getlayer(UDP).flags == 0x14):
            return "Closed"
    elif(stealth_scan_resp.haslayer(ICMP)):
        if(int(stealth_scan_resp.getlayer(ICMP).type)==3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
            return "Filtered"


def RangeScan(dest="127.0.0.1",startPort=1,endPort=8888):
    portDictionary = {}
    # print("dest = " + dest)
    for port in range(startPort,endPort+1): 
        print("Scanning %s:%d" %(dest,port))
        temp = TCPScan(dest=dest,destport=port)
        portDictionary[port] = temp
    return portDictionary


if __name__ == "__main__":
    print(RangeScan(dest="127.0.0.1", startPort=5555,endPort=5555))
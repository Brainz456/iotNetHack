#! /usr/bin/python3
import argparse
import multiprocessing



def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument( "-i",'--ip', default="127.0.0.1", type=str, help="Target IP address ( can also be a URL)")
    parser.add_argument( "-p",'--port-scanner', help="Port Scan Flag",action='store_true')
    parser.add_argument( "-sp", '--start-port', default=1, type=int, help="Starting Port for port scanner")
    parser.add_argument("-ep", '--end-port', default=1, type=int, help="Ending Port for port scanner")
    
    return parser.parse_args()

def main():
    args = parseArgs()
    if args.port_scanner == True:
        import portScanner
        print("Begining Port Scanner on IP: %s" %(args.ip))
        print("Port Range: %d - %d " %(args.start_port,args.end_port))
        portDict = portScanner.RangeScan(args.ip,args.start_port,args.end_port)
        print("")
        for port in portDict:
            print("Port: %d       Status: %s" %(port, portDict[port]))


if __name__ == "__main__":
    main()



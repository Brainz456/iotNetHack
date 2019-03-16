#! /usr/bin/python3
import argparse
import multiprocessing

def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', "-i",default="127.0.0.1", type=str, help="Target IP address")
    # parser.add_argument('--ip', "-i",default="127.0.0.1", type=str, help="Target IP address")
    return parser.parse_args()

def main():
    args = parseArgs()
    print(args.ip)

if __name__ == "__main__":
    main()



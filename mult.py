import argparse
import os
import sys
import platform as p
from modules.crack import crack
from utils import nTools
from utils.colors import (
    white,
    red,
    green,
    yellow,
    end,
    back,
    info,
    que,
    bad,
    good,
    run,
    red_line,
)

# Global Vars

OS = ""
thread_count = 0
ports = []


def scan_nmap(url):
    # Checking network
    nTools.check_network()
    if OS.lower().startswith(("win", "nt")):
        print("Limited features")
    else:
        if os.system(f"nmap -sC -sV {url} -vv"):
            ops = input("Some packages not found. Do you want to install??(Y/N)")
            if ops.lower() == "yes" or ops.lower() == "y":
                os.system("./setup.sh && python3 -m pip install -r requirements.txt")
            elif ops.lower() == "n" or ops.lower() == "no":
                print("Exiting")
                exit()


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-url", help="Specify URL", type=str)
    # parser.add_argument("-p", help="Specific port", type=int)
    parser.add_argument("-c", help="Hash to crack", type=str)
    parser.add_argument("-t", "--threads", help="Specify threads", default=4, type=int)
    parser.add_argument("-o", "--output", help="Save output into a file", type=argparse.FileType("w", encoding="UTF-8"))

    args = parser.parse_args()
    global thread_count
    thread_count = args.threads or 4

    # Call Meths
    print(
        """%s  __  __           _   _   
 |  \/  |         | | | |  
 | \  / |  _   _  | | | |_ 
 | |\/| | | | | | | | | __|
 | |  | | | |_| | | | | |_ 
 |_|  |_|  \__,_| |_|  \__|
                           %s(0.1)%s
                           """
        % (green, red, end))

    # SYSINFO
    print("%sSYSTEM INFO" % (que))
    print(
        f"%s Running on %s{p.system()} {p.release()}%s {p.version()}\n Using %s{args.threads}%s threads. Use -t to specify threads" % (
        info, red, end, yellow, end))
    print(red_line)
    global OS
    OS = p.system()
    # print(red_line)

    # Scanning specific port
    global ports
    if args.url:
        scan_nmap(args.url)

    # Cracking HASHES    
    if args.c:
        crack(args.c)
    print(red_line)


if __name__ == "__main__":
    main()

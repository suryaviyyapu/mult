import argparse
import os
import sys
import platform as p
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

OS = ""


def setup():
    print(f"Running on {p.system()} {p.release()} {p.version()}")
    print(red_line)
    global OS
    OS = p.system()


def scan_nmap(url, port):
    nTools.check_network()
    if OS.lower().startswith(("win", "nt")):
        print("Limited features")
    else:
        if os.system(f"nmap -sC -sV {url} -p {port}"):
            ops = input("Some packages not found. Do you want to install??(Y/N)")
            if ops.lower() == "yes" or ops.lower() == "y":
                os.system("./setup.sh && python3 -m pip install -r requirements.txt")
            elif ops.lower() == "n" or ops.lower() == "no":
                print("Exiting")
                exit()


def Main():
    parser = argparse.ArgumentParser()

    parser.add_argument("url", help="Specify URL", type=str)
    parser.add_argument("-p", help="Specific port", type=int)
    # parser.add_argument()
    parser.add_argument(
        "-o", "--output", help="Save output into a file", action="store_true"
    )

    args = parser.parse_args()

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
    setup()
    if args.p:
        scan_nmap(args.url, args.p)
    print(red_line)


if __name__ == "__main__":
    Main()
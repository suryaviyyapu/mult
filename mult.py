import argparse
from utils.colors import white, red, green, yellow, end, back, info, que, bad, good, run, red_line

def Main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('mode', help="Select Automatic, Manual mode", type=str, choices=['A', 'M'])
    # parser.add_argument("-s", "--shell", help="Specific shell to generate", choices=['web', 'msfvenom'], type=str)
    parser.add_argument("-o", "--output", help="Save output into a file", action="store_true")

    parser.parse_args()

    # Call Meths
    print(red_line)
    print('Init%s Mult %s' %(run, end))

if __name__ == "__main__":
    Main()
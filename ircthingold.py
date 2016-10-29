import time
import sys
import socket
import ssl
import string

HOST="irc.wpc.io"
PORT=6697
NICK="coffee2"
IDENT="coffee"
REALNAME="houseBot"
readbuffer=""
PASS="0xFEE1DEAD"



sock=socket.socket()
wrappedSocket = ssl.wrap_socket(sock)


#s.connect((HOST, PORT))
wrappedSocket.connect((HOST, PORT))
#wrappedSocket.send
wrappedSocket.send("PASS %s\r\n" % PASS)
wrappedSocket.send("NICK %s\r\n" % NICK)
wrappedSocket.send("USER %s 0 * :%s\r\n" % (IDENT, REALNAME))
#wrappedSocket.send("JOIN #cof")

print "connected"
joined=False



while 1:
    readbuffer=readbuffer+wrappedSocket.recv(1024)
    raw=readbuffer
#    print readbuffer
    temp=string.split(readbuffer, "\n")
    readbuffer=temp.pop( )
    
    for line in temp:
        line=string.rstrip(line)
        line=string.split(line)

        if(line[0]!=""):
           print line
	   
	   if(line[0]=="PING"):
              wrappedSocket.send("PONG %s\r\n" % line[1])
	      if(joined==False):
		 wrappedSocket.send("JOIN #")
		 print "join msg sent"
	#	 time.sleep(5)
	
    if raw.find('NAMES') != -1:
#	      time.sleep(2)
	      print "greet"
	      wrappedSocket.send("PRIVMSG # :I'm online\r\n")
    raw=""		

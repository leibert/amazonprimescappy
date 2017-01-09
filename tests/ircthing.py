import time
import sys
import socket
import ssl
import string
import select

HOST="irc.freenode.net"
PORT=6697

NICK="coffeemaker1547"
IDENT="coffeeMaker"
REALNAME="coffeeBot"

readbuffer=""
PASS=""

#HOST="irc.wpc.io"
#PORT=6697
#NICK="coffee2"
#IDENT="coffee"
#REALNAME="houseBot"
#readbuffer=""
#PASS="0xFEE1DEAD"


print "does #work testt"

sock=socket.socket()
sock.settimeout(1)
#sock.setblocking(0)
wrappedSocket = ssl.wrap_socket(sock)
#sock.setblocking(0)


#s.connect((HOST, PORT))
wrappedSocket.connect((HOST, PORT))
#wrappedSocket.send
#wrappedSocket.send("PASS %s\r\n" % PASS)
#wrappedSocket.send("NICK %s\r\n" % NICK)
#wrappedSocket.send("USER %s 0 * :%s\r\n" % (IDENT, REALNAME))
#wrappedSocket.send("JOIN #66Adams")

print "connected"
joined=False
status="none"

timerstart = time.time()
print timerstart

#wait for all the logon bullshit to pass
while 1:
    temp=""
#    ready = select.select([wrappedSocket], [], [], 5)
 #   if ready[0]:
  	#data = mysocket.recv(4096)
    try:
	    readbuffer=readbuffer+wrappedSocket.recv(1024)
	    raw=readbuffer
	
            print readbuffer
	    temp=string.split(readbuffer, "\n")
	    readbuffer=temp.pop( )
    except:
	    print "sock timeout"	
    
#    if(time.time()%5):
    print time.time()


   #     print "attempt join"
    #    wrappedSocket.send("PING")
     #   joined=True;
#	timerstart=time.time()





    for line in temp:
          line=string.rstrip(line)
          line=string.split(line)

#          if(line[0]!=""):
 #       	print line
	  print line		
	   
          if(line[0]=="PING"):
  		print "got PING"
                wrappedSocket.send("PONG %s\r\n" % line[1])
#          if(line[0]=="PING"):
#	        print "got PING"
 #               wrappedSocket.send("PONG %s\r\n" % line[1])
#	      if(joined==False):
#		 wrappedSocket.send("JOIN #")
#		 print "join msg sent on pong"
#		 joined=True
#	#	 time.sleep(5)
	
#    if raw.find('NAMES') != -1:
#	      time.sleep(2)
#	      print "greet"
#	      wrappedSocket.send("PRIVMSG # :I'm online\r\n")
#   raw=""		

    
    if((time.time()-timerstart)>7):
	if(status == "none"):
	        print time.time()
	        print timerstart
		timerstart=time.time()
	        wrappedSocket.send("NICK %s\r\n" % NICK)
#		status="nicksent"
#	elif(status == "nicksent"):
#	        print time.time()
 #       	print timerstart
		time.sleep(2)
	        wrappedSocket.send("USER %s 0 * :%s\r\n" % (IDENT, REALNAME))
        	print "user"
		status="usersent"
	elif(status == "usersent"):
	        print time.time()
	        print timerstart
        	wrappedSocket.send("JOIN #66Adams\r\n")
		print "\"JOIN \#66ADAMS\""
	        print "join"
		status="joined"


	


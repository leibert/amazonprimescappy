import requests
from scapy.all import *
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



    


def arp_display(pkt):

	try:	
		if pkt[ARP].op == 1: #who-has (request)

#		print 'whois'
#		if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
#			print "ARP Probe from: " + pkt[ARP].hwsrc
			if pkt[ARP].hwsrc == '74:c2:46:5b:8b:a4':
				print 'coffee dash!'
				r = requests.post("http://192.168.0.12/coffee.php?potid=fl1", data={'submit': 'randomshit'})
				print(r.status_code, r.reason)
				print(r.text)
				wrappedSocket.send("PRIVMSG # :COFFEE IS BREWING!!!!\r\n")
	except:
		print "something in arp borked"
			



while 1:
#	print sniff(prn=arp_display, filter="arp", store=0, count=2)
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
    if raw.find('NAMES') != -1:
#             time.sleep(2)
        print "greet"
        wrappedSocket.send("PRIVMSG # :I'm online\r\n")

	
    print sniff(prn=arp_display, filter="arp")


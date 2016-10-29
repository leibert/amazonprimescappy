#!/usr/bin/env python

import time
import requests
from scapy.all import *

def arp_display(pkt):

	if pkt[ARP].op == 1: #who-has (request)

#		print 'whois'
#		if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
#			print "ARP Probe from: " + pkt[ARP].hwsrc
		if pkt[ARP].hwsrc == 'a0:02:dc:08:0b:92':
			print time.time()
			print 'other dash'
		if pkt[ARP].hwsrc == '74:c2:46:5b:8b:a4':
			print time.time()
			print 'coffee dash!'
        	        try:
	        	        r = requests.post("http://192.168.0.30/coffee.php?potid=fl1", data={'submit': 'randomshit'})
                                print(r.status_code, r.reason)
                                print(r.text)
                        except:
                                print 'coffee server error'

                        try:
                                r = requests.post("http://192.168.0.50/coffeemadeGOGOGO", data={'submit': 'randomshit'})
                                print(r.status_code, r.reason)
                                print(r.text)
                        except:
                                print 'lightESP error'





print sniff(prn=arp_display, filter="arp", store=0, count=0)


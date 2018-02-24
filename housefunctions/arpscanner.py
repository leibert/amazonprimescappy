#!/usr/bin/env python

import time
import requests
#import scapy.all
from scapy.all import *

import argparse
import sys
import time

# sys.path.append('/home/leibert/pyScripts')
#from datacollectionbot.databot import *


def arp_display(pkt):
  if ARP in pkt:
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            print "ARP Probe from: " + pkt[ARP].hwsrc

while True:
    print sniff(prn=arp_display, filter="arp", store=0, count=30)

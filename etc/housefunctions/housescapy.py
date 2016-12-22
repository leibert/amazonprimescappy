#!/usr/bin/env python

import time
import requests
#import scapy.all
from scapy.all import *

import logging
import logging.handlers
import argparse
import sys
import time

#sys.path.append('/home/leibert/pyScripts')
from datacollectionbot.databot import *


# Deafults
LOG_FILENAME = "/tmp/coffee.log"
LOG_LEVEL = logging.INFO  # Could be e.g. "DEBUG" or "WARNING"

# Define and parse command line arguments
parser = argparse.ArgumentParser(description="My simple Python service")
parser.add_argument("-l", "--log", help="file to write log to (default '" + LOG_FILENAME + "')")

# If the log file is specified on the command line then override the default
args = parser.parse_args()
if args.log:
    LOG_FILENAME = args.log

# Configure logging to log to a file, making a new file at midnight and keeping the last 3 day's data
# Give the logger a unique name (good practice)
logger = logging.getLogger(__name__)
# Set the log level to LOG_LEVEL
logger.setLevel(LOG_LEVEL)
# Make a handler that writes to a file, making a new file at midnight and keeping 3 backups
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
# Format each log message like this
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
# Attach the formatter to the handler
handler.setFormatter(formatter)
# Attach the handler to the logger
logger.addHandler(handler)

# lastminute = 0  # holder for minute timer


# Make a class we can use to capture stdout and sterr in the log
class MyLogger(object):
    def __init__(self, logger, level):
        """Needs a logger and a logger level."""
        self.logger = logger
        self.level = level

    def write(self, message):
        # Only log if there is a message (not just a new line)
        if message.rstrip() != "":
            self.logger.log(self.level, message.rstrip())

# Replace stdout with logging to file at INFO level
sys.stdout = MyLogger(logger, logging.INFO)
# Replace stderr with logging to file at ERROR level
sys.stderr = MyLogger(logger, logging.ERROR)

i = 0

def arp_display(pkt):
    # global lastminute
    # if time.localtime().tm_min != lastminute:
    #     lastminute=time.localtime().tm_min
    #     updateCMDCTRL()

    if pkt[ARP].op == 1:  #who-has (request)

        #		print 'whois'
        if pkt[ARP].psrc == '0.0.0.0':  # ARP Probe
            print "ARP Probe from: " + pkt[ARP].hwsrc

        if pkt[ARP].hwsrc == '00:bb:3a:6f:02:21':
            print time.time()
            print 'ON DASH A'
            try:
                r = requests.post("http://192.168.0.31/cgi-bin/IOS/ios.py?mode=execmacro&macroID=4", data={'submit': 'randomshit'})
                print(r.status_code, r.reason)
                print(r.text)
                time.sleep(5)
            except:
                print 'Backyard light error'

        elif pkt[ARP].hwsrc == '10:ae:60:f0:ce:0a':
            print time.time()
            print 'ON DASH B'
	    updateState("DASHB","TS")
            try:
                r = requests.post("http://192.168.0.0/LIGHTS=TOGGLE", data={'submit': 'randomshit'})
                print(r.status_code, r.reason)
                print(r.text)
                time.sleep(5)
            except:
                print 'Backyard light error'

        elif pkt[ARP].hwsrc == '74:c2:46:5b:8b:a4':
            print time.time()
            print 'coffee dash!'
	    updateState("coffee","TS")
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


# Loop forever, doing something useful hopefully:
# while True:
# program loop continuously running
while True:
    print sniff(prn=arp_display, filter="arp", store=0, count=0)
    # sleep(1000)






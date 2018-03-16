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

sys.path.append('/opt/datacollectionbot/')
from databot import *


# Deafults
LOG_FILENAME = "/var/log/housescapy.log"
LOG_LEVEL = logging.INFO  # Could be e.g. "DEBUG" or "WARNING"

# Define and parse command line arguments
parser = argparse.ArgumentParser(description="My simple Python service")
parser.add_argument(
    "-l", "--log", help="file to write log to (default '" + LOG_FILENAME + "')")

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
handler = logging.handlers.TimedRotatingFileHandler(
    LOG_FILENAME, when="midnight", backupCount=3)
# Format each log message like this
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
# Attach the formatter to the handler
handler.setFormatter(formatter)
# Attach the handler to the logger
logger.addHandler(handler)

lasttrigger = time.time()-5  # holder for last trigger to debounce dash buttons

updateState("test", "TS")


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


def detect_button(pkt):
    global lasttrigger

    # we only care about DHCP packets and if it's been more than 5 seconds from the last Dash push (for debouncing)
    if pkt.haslayer(DHCP) and (time.time()-lasttrigger) > 5:

        #stuff to debug the debouncing stuff
        #print "lasttrigger"
        #print lasttrigger
        #print "currenttime"
        #print time.time()
        #print "delta:"
        #print (time.time()-lasttrigger)

        # start checking source of packets to see if they came from a known dash button
        if pkt[Ether].src == '00:bb:3a:6f:02:21':
            print "DASH 02:21 Detected - TEST"
            print time.time()
            lasttrigger = time.time()

        elif pkt[Ether].src == '10:ae:60:f0:ce:0a':
            print 'DASH f0:ce:0a Detected - TEST BUTTON'
            print time.time()
            lasttrigger = time.time()

        elif pkt[Ether].src == '44:65:0d:d9:c3:97':
            print 'd9:c3:97 Detected - coffee'
            print time.time()
            lasttrigger = time.time()
            updateState("coffee", "TS")
            try:
                r = requests.get("http://192.168.0.15/coffeemadeGOGOGO")
                print(r.status_code, r.reason)
                print(r.text)
            except:
                print 'error contacting 0.15'



        elif pkt[Ether].src == '10:ae:60:f0:ce:0b':
            print 'DASH f0:ce:0b Detected - LOWER PORCH BUTTON'
            print time.time()
            lasttrigger = time.time()
            updateState("DASHB", "TS")

            try:
                r = requests.post("http://192.168.0.0/LIGHTS=TOGGLE", data={'submit': 'randomshit'})
                print(r.status_code, r.reason)
                print(r.text)
        # sleep to debounce
            except:
                print 'IOS Server Error'


        elif pkt[Ether].src == '44:65:0d:26:a9:35':
            print 'DASH 26:a9:35 Detected - test button 3'
            print time.time()
            lasttrigger = time.time()


# Loop forever, doing something useful hopefully:
# while True:
# program loop continuously running
while True:
    sniff(prn=detect_button, filter="(udp and (port 67 or 68))", store=0)
    # sleep(1000)

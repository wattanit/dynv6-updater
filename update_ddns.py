import urllib.request
import requests 
import time
import sys
import logging

'''
MODIFY VARIABLES BELOW
'''
token = YOUR_TOKEN_HERE
zone = YOUR_ZONE_HERE


# logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(fmt="%(asctime)s %(name)s.%(levelname)s: %(message)s", datefmt="%Y.%m.%d %H:%M:%S")

handler = logging.StreamHandler(stream=sys.stdout)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.info("Starting DDNS update")
while True:
    time.sleep(300) # adjust for how long the wait during update checks should be. time is in seconds.
    logger.info("Fetch current IP address")
    ipv4 = urllib.request.urlopen('https://v4.ident.me').read().decode('utf8') #ident.me is a tool for identifiying your ipv4 address
    ipv6 = urllib.request.urlopen('https://v6.ident.me').read().decode('utf8')
    logger.info("Updating DDNS")
    request = urllib.request.urlopen(f"https://ipv4.dynv6.com/api/update?ipv4={ipv4}&token={token}&zone={zone}")
    request = urllib.request.urlopen(f"https://ipv6.dynv6.com/api/update?ipv6prefix={ipv6}&token={token}&zone={zone}")

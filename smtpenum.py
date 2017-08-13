#!/usr/bin/python
import sys
import socket

if len (sys.argv) != 2:
	print "enter username to verify"
	sys.exit(0)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('192.168.43.215',25))
banner=s.recv(1024)
print banner
s.send('VRFY' + sys.argv[1] + '\r\n')
result=s.recv(1024)
print result

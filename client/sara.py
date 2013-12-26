#!/usr/bin/env python

import socket
import urllib

class Sara:
	connected = False
	hash = None # hash, a string given by user, we us no salts now!
	server = "localhost"
	port = 0x7dd
	socket = None
	def __init__(self, server, port=0x7dd):
		self.server = server
		self.port = port
		self.socket = socket.socket()
	
	def hello(self):
		"""call server; request jobs!"""
		# check if connected
		if not self.connected:
			self.connect()
		else:
			self.request()
	def connect(self):
		if self.connected:
			return True
		try:
			self.socket.connect((self.host,self.port))
			self.connected = True
		except:
			return False


if __name__ == '__main__':
	sara = Sara()
	sara.start()


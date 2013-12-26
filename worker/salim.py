#!/usr/bin/env python

import socket
import urllib
import hashlib
from _nimosh import Nimosh

class Salim(object):
	connected = False
	hash = None # hash, a hashlib function.
	server = "localhost"
	port = 0x7c7
	socket = None
	def __init__(self, server, port=0x7c7)
		self.server = server
		self.port = port
		self.socket = socket.socket()
		#self.hello()

	def hello(self):
		"""call server; ask for jobs?"""
		# check if connected
		if not self.connected:
			self.connect()
		else:
			self.ask()
		
	def connect(self):
		if self.connected:
			return True
		try:
			self.socket.connect((self.host,self.port))
			self.connected = True
		except:
			return False

	def start(self):
		pass
if __name__ == '__main__':
	salim = Salim()
	salim.start()


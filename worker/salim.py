#!/usr/bin/env python

import urllib
import urllib2
import hashlib
from _nimosh import Nimosh

class Salim(object):
	hash_t = None # hash, a hashlib function.
	hash_f = None
	server = "localhost"
	port = 5852
	nimo = None
	taken = False
	target = ""
	def __init__(self, server= "localhost", port=5852)
		self.server = server
		self.port = port

	def getTask(self):
		req = urllib2.Request("http://%s:%s/getjob" %(self.server, self.port))
		fd = urllib2.urlopen(req)
		# get result and store them in json object
		try:
			task_info = json.loads(fd.read())
			self.nimo = Nimosh(task_info['start'],task_info['end'])
			if task_info['alphabet'] != 'Default':
				self.nimo.setAlphabet(task_info['alphabet'])
			if task_info['hash_type'] !="Default":
				self.hash_t = task_info['hash_type']
			else:
				self.hash_t = "md5"
			self.target = task_info['hash_data']
			taken = True
		except:
			print "can not load task info"
			pass

	def sendFound(self,plain):
		data = urllib.urlencode([('plain',plain)])
		req = urllib2.Request("http://%s:%s/updatejob?found=true&%s" %(self.server, self.port,data))
		fd = urllib2.urlopen(req)

	def sendNotFound(self):
		req = urllib2.Request("http://%s:%s/updatejob?found=false" %(self.server, self.port))
		fd = urllib2.urlopen(req)

	def start(self):
		if not taken:
			getTask()
		if self.hash_t == "md5":
			self.hash_f = hashlib.md5
		elif self.hash_t == "sha1":
			self.hash_f = hashlib.sha1
		elif self.hash_t == "sha256":
			self.hash_f = hashlib.sha256
		elif self.hash_t == "sha512":
			self.hash_f = hashlib.sha512

		while True:
			if self.hash_f(self.nimo.get_current())==self.target:
				self.sendFound(self.nimosh.get_current())
			else:
				if self.nimo.increment() == False:
					self.sendNotFound()
if __name__ == '__main__':
	salim = Salim()
	salim.start()


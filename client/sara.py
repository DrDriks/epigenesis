#!/usr/bin/env python

import urllib
import urllib2
import json
import sys

class Sara:
	hash = None # hash, a string given by user, we us no salts now!
	server = "localhost"
	port = 5852
	def __init__(self, server= "localhost", port=5852):
		self.server = server
		self.port = port

	def requestJob(self, hash_data, hash_type="md5",salt=None):
		try:
			data = urllib.urlencode([('hashtype',hash_type),('hashdata',hash_data)])
			req = urllib2.Request("http://%s:%s/newjob" %(self.server, self.port),data)

			fd = urllib2.urlopen(req)
			# print fd.code
			# get result and store them in json object
		except:
			print "Catch me if you can"

	def getStats(self):
		req = urllib2.Request("http://%s:%s/stats" %(self.server, self.port))
		fd = urllib2.urlopen(req)
		# get result and store them in json object
		try:
			stats = json.loads(fd.read())
			print "Currently we have %s active worker nodes" %(stats['workers'])
			print "----------------------------------------"
			print "Jobs: %s" %(stats['jobs'])
			print "Cracked Hashes: (%s) " %(len(stats['cracked'])) # cracked is a list of tuples (hash, type, plain)
			print "HASH\t\t\TYPE\t\tPLAIN"
			for h, t, p in stats['cracked']:
				print h,"\t\t",t,"\t\t",p
			
		except:
			print "can not load statistics!"
			pass

	def start(self):
		while True:
			print "Epigenesis Client - Sara"
			print "========================"
			print
			print "1) Request New Job"
			print "2) Statistics"
			print "3) Exit"
			print
			cmd = raw_input("ready> ").strip()[0]
			if cmd == "3":
				sys.exit()
			elif cmd == "2":
				self.getStats()
			elif cmd == "1":
				hash_type = raw_input("Hash Type: ").strip()
				hash_data = raw_input("Hash Data: ").strip()
				self.requestJob(hash_data=hash_data, hash_type=hash_type)
			else:
				continue
if __name__ == '__main__':
	sara = Sara()
	sara.start()


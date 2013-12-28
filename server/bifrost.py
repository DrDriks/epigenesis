#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import cgi
import time, threading, json

class RequestHandler(BaseHTTPRequestHandler):
	"""Definition of the request handler."""

	workers = []
	jobs = [] # (hash_data, hash_type) the zero-indexed one is the highest priority (change to Priority Queue Later)
	cracked = [] # (hash_data, hash_type, plain)
	def _writeheaders(self, doc):
		"""Write the HTTP headers for the document. ...etc"""
		if doc is None:
			self.send_response(404)
		else:
			self.send_response(200)
		# Always serve up json for now
		self.send_header('Server','Epigenesis')
		self.send_header('Content-type', 'text/json')
		self.end_headers()

	def _getdoc(self, filename):
		"""Handles.."""
		global starttime
		if filename == '/':
			return "json string"
		elif filename == '/stats':
			return self.getStats()
		elif filename == "/newjob":
			return 'newjob'
		elif filename == '/getjob':
			return self.getJob()
		elif filename == '/updatejob':
			return 'update'
		else:
			return None
	
	def do_HEAD(self):
		doc = self._getdoc(self.path)
		self._writeheaders(doc)

	def do_GET(self):
		print "Handling with thread", threading.currentThread().getName()
		doc = self._getdoc(self.path)
		self._writeheaders(doc)
		if doc is None:
			self.wfile.write("json not found")
		else:
			self.wfile.write(doc)

	def do_POST(self):
		doc = self._getdoc(self.path)
		self._writeheaders(doc)
		ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
		if ctype == 'multipart/form-data':
			postvars = cgi.parse_multipart(self,rfile, pdict)
		elif ctype == 'application/x-www-form-urlencoded':
			length = int(self.headers.getheader('content-length'))
			postvars = cgi.parse_qs(self.rfile.read(length),keep_blank_values=1)
		else:
			postvars = {}
		print postvars

	def getStats(self):
		return json.dumps([("workers",len(self.workers)),("jobs",len(self.jobs)),("cracked",self.cracked)])
	
	def getJob(self):
		# partition the interval
		return json.dumps([("hash_type","Default"),("hash_data",self.jobs[0][0]),("start",),("end",),("alphabet","Default")]) # get from jobs (list) # hash_type from self.jobs[0][1] later
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
	pass






if __name__ == '__main__':
	serveraddr = ('localhost', 5852)
	srvr = ThreadingHTTPServer(serveraddr, RequestHandler)
	srvr.serve_forever()


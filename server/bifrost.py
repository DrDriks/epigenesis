#!/usr/bin/env python

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import cgi
import time, threading, json

class RequestHandler(BaseHTTPRequestHandler):
	"""Definition of the request handler."""
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
			return ''
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
		return

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
	pass




class Bifrost:
	host = 'localhost'
	port = 5852
	srvr = None
	workers = []

	def __init__(self, host='localhost', port=5852):
		self.host = host
		self.port = port
		srvr = ThreadingHTTPServer(serveraddr, RequestHandler)

	def serve_forever(self):
		if srvr:
			srvr.serve_forever()


if __name__ == '__main__':
	bf = Bifrost()
	bf.serve_forever()


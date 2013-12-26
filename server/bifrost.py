#!/usr/bin/env python

import socket


class Bifrost:
	host = 'localhost'
	worker_interface = 0x7c7
	requester_interface = 0x7dd
	socket = None
	workers = []

	def __init__(self, host, w_iface=0x7c7, r_iface=0x7dd):
		self.host = host
		self.worker_interface = w_iface
		self.requester_interface = r_iface
		self.socket = socket.socket()

	def serve_forever(self):
		pass


if __name__ == '__main__':
	bf = Bifrost()
	bf.serve_forever()


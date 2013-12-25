#!/usr/bin/env python

import string

class Nimosh(object):
	__alphabet__ = string.digits + string.ascii_letters # + "_-!@#$%^&*()=+"
	carry = False
	carryIndex = -1
	carryValue = 1 # nimosh is sequencial
	start = None
	end = None
	current = []
	
	"""
	store ranges and increment
	e.g.:
		start = aaa
		end   = zzz
		running table:
		current = aaa
		next = baa
			   caa
			   zaa
			   aba
			   bba
               zba
			   aca
			   bca
			   zca
			   ...
			   ETC
	"""
	def setAlphabet(self,alpha):
		"""Set the current alphabet"""
		self.__alphabet__ = alpha

	def isSupported(self,s):
		for i in s:
			if (not i in self.__alphabet__):
				return False
		return True

	def checkType(self,t):
		"""supported?"""
		tt = type(t).__name__
		if (tt=='str'):
			pass
		elif (tt=='int'):
			pass
		else:
			pass

	def __init__(self, start, end=None):
		self.current = list(start)[::-1] # reverse order to add right-to-left (in reality left-to-right), no effect but makes me good :)
		self.end = end


	def isOverFlow(self,index):
		"""check if there's any overflow resulting by adding or carrying"""
		idx = self.__alphabet__.index(self.current[index])
		if (idx+1 < len(self.__alphabet__)): # inside the __alphabet__
			# i h t f l
			pass
	
	def isReachedEnd(self):
		"""is this the end?"""		
		pass

	def get_current(self):
		return ''.join(self.current[::-1])

	def increment(self,step=1,idx=0):
		"""Increment current value by `step`. Return False when can not increment"""
		try:
			if(self.end!=None and ''.join(self.current[::-1])==self.end):
				raise IndexError

			if(self.current[idx]==self.__alphabet__[-1]):
				self.current[idx] = self.__alphabet__[0]
				self.increment(step=1,idx=idx+1)
			else:
				self.current[idx] = self.__alphabet__[self.__alphabet__.index(self.current[idx])+1]
		except IndexError:
			return False

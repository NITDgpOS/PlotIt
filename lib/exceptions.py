'''
This module holds custom exceptions created by us

'''

class InvalidFunctionException(Exception):
	def __init__(self, value):
		self.parameter = value

	def __str__(self):
		return repr(self.parameter)

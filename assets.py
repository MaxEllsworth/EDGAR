#!/usr/bin/python

import xml.etree.ElementTree
from analyze import *

class res():
	def __init__(self, web = False, local = False):
		self.name = name
		self.web = web
		self.local = local
 # local or web

class Monthly_Sheet():
	def __init__(self, 
				 resource = False, 
				 month = False,
				 tree = False):
		self.resource = resource
		self.month = month
		self.tree = tree


	def import(self, resource):
		if resource.web == "local":




if __name__ == "__main__":
	feb = Monthly_Sheet(url = "https://www.sec.gov/Archives/edgar/data/1477336/000172782018000015/ex102feb2018aart201811.xml",
							 month = "jan")

	feb.tree = xml.etree.ElementTree.parse("ex102feb2018aart201811.xml").getroot()





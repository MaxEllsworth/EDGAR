import xml.etree.ElementTree
import os
import numpy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import xml.etree.cElementTree as ET
from config import *
import shutil
import subprocess 
from analyze import fixNan
from analyze import getAttributes, selectAttributes, plotRegression

from sys import argv

def r_squared(x, y, degree):

	x = fixNan(x)
	y = fixNan(y)
	
	results = {}
	coeffs = numpy.polyfit(x, y, degree)
	results['polynomial'] = coeffs.tolist()
	correlation = numpy.corrcoef(x, y)[0,1]
	results['correlation'] = correlation
	results['determination'] = correlation**2
	return results

def importer(f, *args):

	print("Importing " + str(args) + " from " + str(f) + " .... " + "\n")
	data = xml.etree.ElementTree.parse(f).getroot()
	# define a function which returns arrays for desired attributes
	saves = {}
	for key in args:
		saves[key] = []
	for asset in data:
		for item in asset._children:
			key = item.tag
			key = "".join([ch for ch in key if ch not in ['{', '}']]	)
			key = key.split('/')[-1]
			key = key.split('assetdata')[-1]
			if key in args:
				saves[key].append(item.text)

	return saves




def getAttributes(e, **kwargs):
	values = []

	for item in e._children:
			key = item.tag
			key = "".join([ch for ch in key if ch not in ['{', '}']]	)
			key = key.split('/')[-1]
			key = key.split('assetdata')[-1]
			stock[key] = item.text


def selectAttributes(stock, attributes):
	values = []
	for key in stock:
		if key in attributes:
			values.append(stock[value])
	return values



		

def fixArray(array):
	ar = numpy.nan_to_num(array)
	for i in range(0, len(ar)):
		try:
			ar[i] = float(ar[i])
		except:
			ar[i] = 0.0
	ar = np.array(ar).astype(np.float)
	return ar


def x(xml):
	True
def y(xml):
	True 
def run_rsquared_on_xml(x, y, xml):
	print("Running r squared test on " + str(xml))
	attributes = [x,y]
	aN = importer(xml, *attributes)
	x, y = aN[aN.keys()[0]], aN[aN.keys()[1]]
	x = fixArray(x)
	y = fixArray(y)
	print("Calculating r squared value ... ")
	print(r_squared(x, y, 1))

if __name__ == "__main__":
	f = argv[1]
	run_rsquared_on_xml(argv[2], argv[3], f)	
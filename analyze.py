#!/usr/bin/python

import xml.etree.ElementTree
import os
import numpy
import matplotlib.pyplot as plt
from matplotlib import rcParams
import xml.etree.cElementTree as ET

rcParams.update({'figure.autolayout': True})

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

assetDirectory = "ally/"
csvDirectory = "csv/"
statsDirectory = "stats/"
graphDirectory = "graphs/"

class loan():
	def __init__(self, assetnumber = "", irp = ""):
		self.assetnumber = assetnumber
		self.irp = irp

def splitXML(xmlFile):
	bulk = xml.etree.ElementTree.parse(xmlFile).getroot()
	ET.register_namespace("",ns0)
	name = xmlFile.rstrip(".xml")
	directory = xmlDirectory + name + "/"
	prepDir(directory)

	for asset in bulk:
		tree = ElementTree(asset)
		name = getAttributes(asset, attribute = "assetNumber")
		tree.write(directory + str(assetNumber) + ".xml")

def getAttributes(e, **kwargs):
	stock = {}
	for item in e._children:
			key = item.tag
			key = "".join([ch for ch in key if ch not in ['{', '}']]	)
			key = key.split('/')[-1]
			key = key.split('assetdata')[-1]
			stock[key] = item.text
	if **kwargs:
		return stock["attribute"]
	else:
		return stock

def selectAttributes(stock, attributes):
	values = []
	for key in stock:
		if key in attributes:
			values.append(stock[value])
	return value


def bulkMax(directory, attribute):
	entries = {}
	assets = os.listdir(directory)
	for a in assets:
		e = xml.etree.ElementTree.parse(directory + "/" + a).getroot()
		asset = getAttributes(e)
		try:
			entries[float(asset[attribute])] = asset["assetNumber"]
		except:
			entries[0] = asset["assetNumber"]
	keys = entries.keys()
	maximum = max(keys)
	return entries[maximum], maximum

def bulkMin(directory, attribute):
	entries = {}
	assets = os.listdir(directory)
	for a in assets:
		e = xml.etree.ElementTree.parse(directory + "/" + a).getroot()
		asset = getAttributes(e)
		try:
			entries[float(asset[attribute])] = asset["assetNumber"]
		except:
			entries[0] = asset["assetNumber"]

	keys = entries.keys()
	minimum = min(keys)
	return entries[minimum], minimum

def fixNames(directory):
	assets = os.listdir(directory)
	
	for a in assets:
		e = xml.etree.ElementTree.parse(directory + "/" + a).getroot()
		assetNumber = getAttributes(e)["assetNumber"]
		xmlfile = open(directory + "/" + a, 'r')
		lines = xmlfile.readlines()
		xmlfile.close()
		f = open(directory + "/" + assetNumber + ".xml", "w+")
		f.writelines(lines)
		f.close()
		os.remove(directory + "/" + a)

def prepDir(directory):
	if os.path.exists(directory):
		print(directory + " exists ...")
		if input((bcolors.WARNING + "Do you want to erase and recreate " + directory + "? [Y/n]: " + bcolors.ENDC)).split()[0].lower() == 'y':
			os.remove(directory)
			os.mkdir(directory)
	else:
		os.mkdir(directory)
		print("Created " + str(directory))
	# consider making this function accept user input for renaming the new directory

def csvAllAssets():
	for f in os.listdir(assetDirectory):
		stock = xml.etree.ElementTree.parse(assetDirectory + f).getroot()
		stock = getAttributes(stock)
		for k in stock.keys():
			dataFile = csvDirectory + k + ".csv"  
			if not os.path.exists(dataFile):
				file = open(dataFile, "w+")
				file.close()
			file = open(dataFile, "a")
			file.write(stock[k] + ",")
			file.close()


def computeStats():
	# max, min standard deviation, median, mean
	prepDir(statsDirectory)
	for csvFile in os.listdir(csvDirectory):
		v = numpy.genfromtxt(open(csvDirectory + csvFile, "rb"), delimiter=",")
		v = v[~numpy.isnan(v)]
		f = open(statsDirectory + csvFile.split('.')[0] + "-stats.txt", "w+")
		try:
			stats = ["MAX: " + str(v.max()) + '\n',
				"MIN: " + str(v.min()) + '\n',
				"STDEV: " + str(v.std()) + '\n',
				"MEDIAN: " + str(numpy.median(v)) + '\n',
				"MEAN: " + str(v.mean())]
		except Exception as e:
			stats = ["FAILED: ", str(e)]	
		f.writelines(stats)
		f.close()

def fixNan(array):
	new = []
	array = numpy.nan_to_num(array)
	return array

def plotRegression(x, y, title):
	x_title = x
	y_title = y

	x = numpy.genfromtxt(open(csvDirectory + x + ".csv", "rb"), delimiter=",")
	y = numpy.genfromtxt(open(csvDirectory + y + ".csv", "rb"), delimiter=",")

	x = fixNan(x)
	y = fixNan(y)

	fit = numpy.polyfit(x,y,1)
	fit_fn = numpy.poly1d(fit)

	plt.plot(x,y, 'yo', x, fit_fn(x), '--k')
	plt.xlim(0, x.max())
	print(fit_fn)
	
	
	plt.suptitle(title)
	plt.xlabel(x_title, fontsize=18)
	plt.ylabel(y_title, fontsize=18)

	plt.ylim(0, y.max())
	plt.tight_layout()
	plt.savefig(graphDirectory + title + ".png")


def polyfit(x, y, degree):
	x = numpy.genfromtxt(open(csvDirectory + x + ".csv", "rb"), delimiter=",")
	y = numpy.genfromtxt(open(csvDirectory + y + ".csv", "rb"), delimiter=",")
	    

	x = fixNan(x)
	y = fixNan(y)
	
	results = {}
	coeffs = numpy.polyfit(x, y, degree)
	results['polynomial'] = coeffs.tolist()
	correlation = numpy.corrcoef(x, y)[0,1]
	results['correlation'] = correlation
	results['determination'] = correlation**2
	return results



if __name__ == "__main__":
	x = "originalLoanAmount"
	y = "originalInterestRatePercentage"
	title = "Linear Regression 2"
	print(polyfit(x, y, 1))
	plotRegression(x,y, title)

'''
	maxLoanAmountAsset, maxLoanAmount = bulkMax("ally/", "repossessedProceedsAmount")
	print(maxLoanAmountAsset)
	print(maxLoanAmount)
	#e = xml.etree.ElementTree.parse("untitled.xml").getroot()
'''
'''	stock = getAttributes(e[0])
	attributes = ["originalInterestRatePercentage", "obligorCreditScore", 
	"obligorIncomeVerificationLevelCode","obligorEmploymentVerificationCode",
	"paymentToIncomePercentage","currentDelinquencyStatus","repossessedIndicator"]
	#print(stock)

	selectAttributes(stock, attributes)
	'''


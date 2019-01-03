#!/usr/bin/python

import xml.etree.ElementTree
import os

assetDirectory = "ally/"
csvOutputDirectory = "csv/"

class loan():
	def __init__(self, assetnumber = "", irp = ""):
		self.assetnumber = assetnumber
		self.irp = irp

def getAttributes(e):
	stock = {}
	for item in e._children:
			key = item.tag
			key = "".join([ch for ch in key if ch not in ['{', '}']]	)
			key = key.split('/')[-1]
			key = key.split('assetdata')[-1]
			stock[key] = item.text
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

def csvAllAssets():
	for f in os.listdir(assetDirectory):
		stock = xml.etree.ElementTree.parse(assetDirectory + f).getroot()
		stock = getAttributes(stock)
		for k in stock.keys():
			dataFile = csvOutputDirectory + k + ".csv"  
			if not os.path.exists(dataFile):
				file = open(dataFile, "w+")
				file.close()
			file = open(dataFile, "a")
			file.write(stock[k] + ",")
			file.close()



if __name__ == "__main__":
		

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


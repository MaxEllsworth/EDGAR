#!/usr/bin/python

import xml.etree.ElementTree
import os

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
	for key in stock:
		print(key)
		if key in attributes:
			print(key + " : " + stock[value])



def bulkMax(directory, attribute):
	entries = {}
	assets = os.listdir(directory)
	for a in assets:
		e = xml.etree.ElementTree.parse(directory + "/" + a).getroot()
		asset = getAttributes(e)
		entries[float(asset[attribute])] = asset["assetNumber"]
	keys = entries.keys()
	maximum = max(keys)
	return entries[maximum], maximum

def bulkMin(directory, attribute):
	entries = {}
	assets = os.listdir(directory)
	for a in assets:
		e = xml.etree.ElementTree.parse(directory + "/" + a).getroot()
		asset = getAttributes(e)
		entries[float(asset[attribute])] = asset["assetNumber"]
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

if __name__ == "__main__":

	maxLoanAmountAsset, maxLoanAmount = bulkMax("ally/", "originalInterestRatePercentage")
	print(maxLoanAmountAsset)
	print(maxLoanAmount)
	#e = xml.etree.ElementTree.parse("untitled.xml").getroot()

'''	stock = getAttributes(e[0])
	attributes = ["originalInterestRatePercentage", "obligorCreditScore", 
	"obligorIncomeVerificationLevelCode","obligorEmploymentVerificationCode",
	"paymentToIncomePercentage","currentDelinquencyStatus","repossessedIndicator"]
	#print(stock)

	selectAttributes(stock, attributes)
	'''


#!/usr/bin/python
from sys import argv
from assets import Monthly_Sheet

def lines(sheet):
	f = open(sheet, "r")
	l = [l.rstrip('\n') for l in f.readlines() if l.split(" ")[0] not in ['#', '\n']]
	f.close()
	return l

def config(lines):
	config = {}
	for l in lines:
		key = l.split('=')[0].rstrip(" ")
		value = "".join(l.split('=')[1:]).lstrip(" ")

		config[key] = value
	return config

def import(sheet):
	l = lines(sheet)
	c = config(l)

	
if __name__ == "__main__":
	sheet = argv[1]
	print(sheet)
	l = lines(sheet)
	print(config(l))
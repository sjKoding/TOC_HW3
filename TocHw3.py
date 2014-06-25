# -*- coding: utf-8 -*-

# Program: TocHw4.py
# Author: sjKoding 林賢哲
# ID: F74001098
# purpose: Theory of Computation Hw4

import sys
import json
import urllib2
import re

# get data from url
# use json.loads() to convert it
def getDataFromURL( url ):
	try:
		response = urllib2.urlopen(urllib2.Request(url))
	except (ValueError, urllib2.URLError) as e:
		print e
		sys.exit(0)
	temp = response.read() 
    ## loads: (load string)deserialize from json string to python obj
	data = json.loads(temp)
	return data

'''
# open an utf-8 json string file
# then get data using json.load()
def getDataFromFile( filename ):
	f = open(filename, 'r')
	data = json.load(f)
	return data

def getTxtFromFile( filename ):
	f = open(filename, 'r')
	data = f.read()
	return data

#data = getDataFromFile( 'housing.txt' )
'''


if len(sys.argv)!=5:
	print "agrv Error."
	print "python TocHw3.py [URL] [region] [road] [year]"
	sys.exit(0)

try:
	int(sys.argv[4])
except ValueError as e:
	print "Error: [year] should be int."
	sys.exit(0)

URL = sys.argv[1]
region = unicode(sys.argv[2], 'utf-8')
road = unicode(sys.argv[3], 'utf-8')
year = unicode(sys.argv[4], 'utf-8')

data = getDataFromURL(URL)

regionHead = unicode("鄉鎮市區", "utf-8")
roadHead = unicode("土地區段位置或建物區門牌", "utf-8")
yearHead = unicode("交易年月", "utf-8")
priceHead = unicode("總價元", "utf-8")

cnt = 0
price = 0
for i in range(len(data)):
	if data[i][regionHead].find(region)>=0 and data[i][roadHead].find(road)>=0 and str(data[i][yearHead]).find(year)>=0:
		cnt = cnt + 1
		price = price + data[i][priceHead]
try:
	price = price / cnt
except ZeroDivisionError:
	price = 0
print price

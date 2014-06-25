# -*- coding: utf-8 -*-

import sys
import json
import urllib2
import re

# get data from url
# use json.loads() to convert it
def getDataFromURL( url ):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	temp = response.read() 
    ## loads: (load string)deserialize from json string to python obj
	data = json.loads(temp)
	return data

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


URL = sys.argv[1] #"http://www.datagarage.io/api/5365dee31bc6e9d9463a0057"
#data = getDataFromFile( 'housing.txt' )
data = getDataFromURL(URL)

regionHead = unicode("鄉鎮市區", "utf-8")
roadHead = unicode("土地區段位置或建物區門牌", "utf-8")
yearHead = unicode("交易年月", "utf-8")
priceHead = unicode("總價元", "utf-8")

region = sys.argv[2] #"文山區"
road = sys.argv[3] #"辛亥路"
year = sys.argv[4] #"103"
region = unicode(sys.argv[2], 'utf-8')
road = unicode(sys.argv[3], 'utf-8')
year = unicode(sys.argv[4], 'utf-8')


cnt = 0
price = 0
for i in range(len(data)):
	if data[i][regionHead].find(region)>=0 and data[i][roadHead].find(road)>=0 and str(data[i][yearHead]).find(year)>=0:
		cnt = cnt + 1
		price = price + data[i][priceHead]
#print "cnt:",cnt ,data[i][regionHead], data[i][roadHead], data[i][yearHead]
price = price / cnt
print price

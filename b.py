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
    ## loads: (load string?)deserializing from json format to string
	data = json.loads(temp)
	return data

def getDataFromURLwithDump( url ):
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	temp = response.read() 
	data = json.dumps(temp)
	return data
	
# open an utf-8 json format file
# then get data using json.load()
def getDataFromFile( filename ):
	f = open(filename, 'r')
	data = json.load(f)
	return data

def getTxtFromFile( filename ):
	f = open(filename, 'r')
	data = f.read()
	return data

addr = "移轉層次"
addr = unicode(addr,'utf-8')

URL = "http://www.datagarage.io/api/5365dee31bc6e9d9463a0057"
'''
'''
f = open('dumpWithLoad.txt','r')
ldata = json.load(f)
#f = open('housing.json','r')
#data2 = json.load(f)
f = open('dumpWithoutLoad.txt','r')
noldata = json.load(f)
f = open('housing.txt','r')
data4 = json.load(f)
f = open('dumpWithdump.txt','r')
ddata = json.load(f)
#print "1:"
#print ldata[0][addr]
#print "2:"
#print data2[0]
#print "\n"
#print "3:"
#print noldata[0]
print "4:"
print data4[0][addr]
print "for:"
for i in data4[0]:
	print i, ":", data4[0][i]
#print "5:"
#print ddata[0]

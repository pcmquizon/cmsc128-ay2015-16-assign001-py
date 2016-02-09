#!/usr/bin/env python

import sys

def numToWords(number):
	"Accepts  a  whole  number from  zero (0)  to  1  million (1000000 ;  without  commas for  example:  1,000,000 two) and #prints  on  screen number  in  word  form"

	million = (number%10000000)/1000000
	hTH = (number%1000000)/100000
	tTH = (number%100000)/10000
	oTH = (number%10000)/1000
	h = (number%1000)/100
	t = (number%100)/10
	o = number%10

	print "m="+str(million)+" hTH="+str(hTH)+" tTH="+str(tTH)+" oTH="+str(oTH)+" h="+str(h)+" t="+str(t)+" o="+str(o)


	if(million>0):
		#print "one million "
		sys.stdout.write('one million ')
		
	if(hTH>0 or tTH>0 or oTH>0):
	
#		if(hTH>0):
#		onesNum(hTH)
#			print "hundred "
#		if(tTH>0 & oTH>0):
#			tensNum(tTH)
#			print "-"
#			onesNum(oTH)
#		elif(oTH>0):
#			onesNum(oTH)
		threePlaces(hTH, tTH, oTH)
		#print "thousand "
		sys.stdout.write('thousand ')

	if(h>0 or t>0 or o>0):
		threePlaces(h, t, o)
	elif(o==0):
		#print "zero"
		sys.stdout.write('zero')
			
#	else:
#		print "Invalid input"

	return None	
	
def onesNum(number):
	""
	if(number==1):
		#print "one "
		sys.stdout.write('one ')
	if(number==2):
		#print "two "
		sys.stdout.write('two ')
	if(number==3):
		#print "three "
		sys.stdout.write('three ')
	if(number==4):
		#print "four "
		sys.stdout.write('four ')
	if(number==5):
		#print "five "
		sys.stdout.write('five ')
	if(number==6):
		#print "six "
		sys.stdout.write('six ')
	if(number==7):
		#print "seven "
		sys.stdout.write('seven ')
	if(number==8):
		#print "eight "
		sys.stdout.write('eight ')
	if(number==9):
		#print "nine "
		sys.stdout.write('nine ')
	return None

	
def tensNum(number):
	if(number==10):
		#print "ten"
		sys.stdout.write('ten')
	if(number==20):
		#print "twenty"
		sys.stdout.write('twenty')
	if(number==30):
		#print "thirty"
		sys.stdout.write('thirty')
	if(number==40):
		#print "forty"
		sys.stdout.write('forty')
	if(number==50):
		#print "fifty"
		sys.stdout.write('fifty')
	if(number==60):
		#print "sixty"
		sys.stdout.write('sixty')
	if(number==70):
		#print "seventy"
		sys.stdout.write('seventy')
	if(number==80):
		#print "eighty"
		sys.stdout.write('eighty')
	if(number==90):
		#print "ninety"
		sys.stdout.write('ninety')
	return None

def lessThanTwenty(number):
	if(number==11):
		sys.stdout.write('eleven ')
	if(number==12):
		sys.stdout.write('twelve ')
	if(number==13):
		sys.stdout.write('thirteen ')
	
def threePlaces(h, t, o):
		if(h>0):
			onesNum(h)
			#print "hundred "
			sys.stdout.write('hundred ')
		if(t==1 and (1 < o < 4) ):
			lessThanTwenty(10+o)
		elif(t==1 and (5 < o < 10) ):
			onesNum(o)
			sys.stdout.write('teen ')
		elif(t>2 and o>0):
			tensNum(t)
			#print "-"
			sys.stdout.write('-')
			onesNum(o)
		elif(t>0):
			tensNum(t)
		elif(o>0):
			onesNum(o)
		return None
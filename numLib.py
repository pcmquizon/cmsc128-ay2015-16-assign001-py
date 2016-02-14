#!/usr/bin/env python

import sys
import re

def numToWords(number):
	"Accepts  a  whole  number from  zero (0)  to  1  million \
	 (1000000 ;  without  commas for  example:  1,000,000 two) and \
	 prints  on  screen number  in  word  form"

	million = (number%10000000)/1000000
	hTH = (number%1000000)/100000
	tTH = (number%100000)/10000
	oTH = (number%10000)/1000
	h = (number%1000)/100
	t = (number%100)/10
	o = number%10

	output=""

	if(million>0):
		output = output + getWordForm(million) + " million "

	if(hTH>0 or tTH>0 or oTH>0):
		output = output + threePlacesNTW(hTH, tTH, oTH) + " thousand "

	if(h>0 or t>0 or o>0):
		output = output + threePlacesNTW(h, t, o)
	elif(o==0 and hTH==0 and tTH==0 and oTH==0 and million==0 and t==0 and h==0):
		output = "zero"

	print output	

def getWordForm(number):
	"Evaluates the parameter number and returns the corresponding word form"
	if(number==1):
		return "one"
	elif(number==2):
		return "two"
	elif(number==3):
		return "three"
	elif(number==4):
		return "four"
	elif(number==5):
		return "five"
	elif(number==6):
		return "six"
	elif(number==7):
		return "seven"
	elif(number==8):
		return "eight"
	elif(number==9):
		return "nine"
	elif(number==10):
		return "ten"
	elif(number==20):
		return "twenty"
	elif(number==30):
		return "thirty"
	elif(number==40):
		return "forty"
	elif(number==50):
		return "fifty"
	elif(number==60):
		return "sixty"
	elif(number==70):
		return "seventy"
	elif(number==80):
		return "eighty"
	elif(number==90):
		return "ninety"
	elif(number==11):
		return "eleven "
	elif(number==12):
		return "twelve "
	elif(number==13):
		return "thirteen "
	elif(number==14):
		return "fourteen "
	elif(number==15):
		return "fifteen"
	elif(number==16):
		return "sixteen"
	elif(number==17):
		return "seventeen"
	elif(number==18):
		return "eighteen"
	elif(number==19):
		return "nineteen"

def threePlacesNTW(h, t, o):
	"Calls the appropriate functions based on the values of h, t and o"
	output = ""
	if(h>0):
		output = output + getWordForm(h) + " hundred "

	if(t==1 and (0 < o < 10) ):
		output = output + getWordForm(10+o)
	elif(t>1 and o>0):
		output = output + getWordForm(t*10) + "-" + getWordForm(o)
	elif(t>0):
		output = output + getWordForm((t*10)+o)
	elif(o>0):
		output = output + getWordForm(o)

	return output

def numberDelimited(number, delimiter, nJump):
	"Accepts three arguments: (1) a number from 0 to 1 million,\
	 (2) single character delimiter to be used, \
	 (3) number of jumps when the delimiter will appear (from rightmost digit)"

	inputNum = str(number)
	r = ""
	i=0

	while(i<len(inputNum)):
		if(i==len(inputNum)-nJump):
			r = r + delimiter + inputNum[i]
		else:
			r = r + inputNum[i]
		i = i + 1
	return r

def wordsToNum(numInWord):
	"Accepts a number in word form and returns it in numerical form"

	#input must be in lowercase, check em!
	if( not(numInWord.islower()) ):
		return "Input word form must be in lower case."

	#output
	total = 0

	#match input using this
	pat = re.compile(r'(.+[ ]+million[ ]*)?(.+[ ]+thousand[ ]*)?((.+[ ]+hundred[ ]*)?.*)?')

	#ones [million]
	#if pat.match(numInWord).group(1) exists, match it with this
	milPat = re.compile(r'(.+)([ ]+million[ ]*)')

	#hundreds-tens-ones [thousand]
	#if pat.match(numInWord).group(2) exists, match it with this
	thouPat = re.compile(r'(.+)([ ]+thousand[ ]*)')

	#hundreds-tens-ones
	#if pat.match(numInWord).group(3) exists, match it with this
	hunPat = re.compile(r'((.+)([ ]+hundred[ ]*))?(.*)')
	tenPat = re.compile(r'(\w*)(-?)(\w*)')

	#see if it has millions(1) and/or thousands(2) and/or hundreds parts(3)
	mainBlock = pat.search(numInWord)

	#in input, get millions, thousands, hundreds
		#in thousands and one hundreds, get	hundreds
			#if thousands, disregard 'thousand'
			#in hundreds, get tens, ones

	if( mainBlock!=None and mainBlock.group(0) ):

		if(mainBlock.group(1)):
			milBlock = milPat.search(mainBlock.group(1))
			if( milBlock!=None and milBlock.group(1) ):
				total = 1000000

		if(mainBlock.group(2)):
			thouBlock = thouPat.search(mainBlock.group(2))
			if( thouBlock!=None and thouBlock.group(1) ):
				total = total + threePlacesWTN(thouBlock.group(1), hunPat, tenPat)*1000

		if(mainBlock.group(3)):
			hunBlock = hunPat.search(mainBlock.group(3))
			if( hunBlock!=None and hunBlock.group(0) ):
				total = total + threePlacesWTN(hunBlock.group(0),hunPat, tenPat)

	return total

def threePlacesWTN(numInWord, hunPat, tenPat):
	"Divides the input numInWord into millions, thousands and hundreds part; \
	 similar to the concept of the function threePlacesNTW;"

	total = 0;

	#hundreds-tens-ones
	#if pat.match(numInWord).group(3) exists, match it with this

	#get hundreds-tens-ones
	hunBlock = hunPat.search(numInWord) #numInWord == mainBlock
	if( hunBlock!=None and hunBlock.group(1) ):

		total = total + getNum(hunBlock.group(2))*100

	if( hunBlock!=None and hunBlock.group(4) ):

		tensOnesBlock = tenPat.search(hunBlock.group(4))
		if( tensOnesBlock!=None and tensOnesBlock.group(1) ):

			total = total + getNum(tensOnesBlock.group(1))

		if( tensOnesBlock!=None and tensOnesBlock.group(3) ):

			total = total + getNum(tensOnesBlock.group(3))

	return total

def getNum(number):
	"Returns corresponding number based on its input word form"
	if(number=="one"):
		return 1
	elif(number=="two"):
		return 2
	elif(number=="three"):
		return 3
	elif(number=="four"):
		return 4
	elif(number=="five"):
		return 5
	elif(number=="six"):
		return 6
	elif(number=="seven"):
		return 7
	elif(number=="eight"):
		return 8
	elif(number=="nine"):
		return 9
	elif(number=="ten"):
		return 10
	elif(number=="twenty"):
		return 20
	elif(number=="thirty"):
		return 30
	elif(number=="forty"):
		return 40
	elif(number=="fifty"):
		return 50
	elif(number=="sixty"):
		return 60
	elif(number=="seventy"):
		return 70
	elif(number=="eighty"):
		return 80
	elif(number=="ninety"):
		return 90
	elif(number=="eleven"):
		return 11
	elif(number=="twelve"):
		return 12
	elif(number=="thirteen"):
		return 13
	elif(number=="fourteen"):
		return 14
	elif(number=="fifteen"):
		return 15
	elif(number=="sixteen"):
		return 16
	elif(number=="seventeen"):
		return 17
	elif(number=="eighteen"):
		return 18
	elif(number=="nineteen"):
		return 19

def wordsToCurrency(numInWord, currency):
	"Accepts two arguments: (1) a number from 0 to 1 million in word form,\
	 (2) any of 'USD', 'JPY' or 'PHP'; Returns number in to its numerical \
	 form with a prefix of the currency "
	return currency + str(wordsToNum(numInWord))

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

	#checker
	print "m="+str(million)+" hTH="+str(hTH)+" tTH="+str(tTH)+" oTH="+str(oTH)+" h="+str(h)+" t="+str(t)+" o="+str(o)

	output=""


	if(million>0):
		#print "one million "
		output = output + onesNum(million) + " million "
		#sys.stdout.write(' million ')
		
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
		output = output + threePlacesNTW(hTH, tTH, oTH) + " thousand "
		#print "thousand "
		#sys.stdout.write(' thousand ')

	if(h>0 or t>0 or o>0):
		output = output + threePlacesNTW(h, t, o)
	elif(o==0 and hTH==0 and tTH==0 and oTH==0 and million==0 and t==0 and h==0):
		#print "zero"
		#sys.stdout.write('zero')
		output = "zero"
			
#	else:
#		print "Invalid input"

	return output	
	
def onesNum(number):
	"Evaluates the parameter number and prints the corresponding word form"
	if(number==1):
		return "one"
		#sys.stdout.write('one')
	if(number==2):
		return "two"
		#sys.stdout.write('two')
	if(number==3):
		return "three"
		#sys.stdout.write('three')
	if(number==4):
		return "four"
		#sys.stdout.write('four')
	if(number==5):
		return "five"
		#sys.stdout.write('five')
	if(number==6):
		return "six"
		#sys.stdout.write('six')
	if(number==7):
		return "seven"
		#sys.stdout.write('seven')
	if(number==8):
		return "eight"
		#sys.stdout.write('eight')
	if(number==9):
		return "nine"
		#sys.stdout.write('nine')
	#return None
	
def tensNum(number):
	"Evaluates the parameter number and prints the corresponding word form; \
	 similar to onesNum() function"
	if(number==10):
		#print "ten"
		#sys.stdout.write('ten')
		return "ten"
	if(number==20):
		#print "twenty"
		#sys.stdout.write('twenty')
		return "twenty"
	if(number==30):
		#print "thirty"
		#sys.stdout.write('thirty')
		return "thirty"
	if(number==40):
		#print "forty"
		#sys.stdout.write('forty')
		return "forty"
	if(number==50):
		#print "fifty"
		#sys.stdout.write('fifty')
		return "fifty"
	if(number==60):
		#print "sixty"
		#sys.stdout.write('sixty')
		return "sixty"
	if(number==70):
		#print "seventy"
		#sys.stdout.write('seventy')
		return "seventy"
	if(number==80):
		#print "eighty"
		#sys.stdout.write('eighty')
		return "eighty"
	if(number==90):
		#print "ninety"
		#sys.stdout.write('ninety')
		return "ninety"
	#return None

def lessThanTwenty(number):
	"Evaluates the parameter number and prints the corresponding word form; \
	 similar to onesNum() and lessThanTwenty() method"
	if(number==11):
		#sys.stdout.write('eleven ')
		return "eleven "
	if(number==12):
		#sys.stdout.write('twelve ')
		return "twelve "
	if(number==13):
		#sys.stdout.write('thirteen ')
		return "thirteen "
	if(number==14):
		#sys.stdout.write('fourteen ')
		return "fourteen "
	if(number==15):
		#sys.stdout.write('fifteen ')
		return "fifteen"
	if(number==16):
		#sys.stdout.write('sixteen ')
		return "sixteen"
	if(number==17):
		#sys.stdout.write('seventeen ')
		return "seventeen"
	if(number==18):
		#sys.stdout.write('eighteen ')
		return "eighteen"
	if(number==19):
		#sys.stdout.write('nineteen ')
		return "nineteen"
	
def threePlacesNTW(h, t, o):
	"Calls the appropriate functions based on the values of h, t and o"
	output = ""
	if(h>0):
		output = output + onesNum(h) + " hundred "
		#print "hundred "
		#sys.stdout.write(' hundred ')
	if(t==1 and (0 < o < 10) ):
		output = output + lessThanTwenty(10+o)
	elif(t>1 and o>0):
		output = output + tensNum(t*10) + "-" + onesNum(o)
		#print "-"
		#sys.stdout.write('-')
		#onesNum(o)
	elif(t>0):
		output = output + tensNum((t*10)+o)
	elif(o>0):
		output = output + onesNum(o)
	return output

def numberDelimited(number, delimiter, nJump):
	"Accepts three arguments: (1) a number from 0 to 1 million,\
	 (2) single character delimiter to be used, \
	 (3) number of jumps when the delimiter will appear (from rightmost digit)"

	#checker
	#print str(number)+" "+delimiter+" "+str(nJump)

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

	#m = pat.match(numInWord).group(1)
	#th = pat.match(numInWord).group(2)
	#h = pat.match(numInWord).group(3)
	#t = tenPat.match( hunPat.group(3) ).group(1)
	#o = tenPat.match( hunPat.group(3) ).group(3)

	#see if it has millions(1) and/or thousands(2) and/or hundreds parts(3)
	mainBlock = pat.search(numInWord)
	#print mainBlock.group(0)
	if( mainBlock!=None and mainBlock.group(0) ):

		if(mainBlock.group(1)):
			milBlock = milPat.search(mainBlock.group(1))
			if( milBlock!=None and milBlock.group(1) ):
				total = 1000000
				#print milBlock.group(1)
				#print "milyones\n\n"

		if(mainBlock.group(2)):
			thouBlock = thouPat.search(mainBlock.group(2))
			if( thouBlock!=None and thouBlock.group(1) ):
				total = total + threePlacesWTN(thouBlock.group(1), hunPat, tenPat)*1000
				#print "libo\n\n"
				

		if(mainBlock.group(3)):
			hunBlock = hunPat.search(mainBlock.group(3))
			if( hunBlock!=None and hunBlock.group(0) ):
				total = total + threePlacesWTN(hunBlock.group(0),hunPat, tenPat)
				#print "daan\n\n"

	
	#print total
	return total
	#if()

	#in input, get millions, thousands, hundreds
		#in thousands and one hundreds, get	hundreds
			#if thousands, disregard 'thousand'

			#in hundreds, get tens, ones

def threePlacesWTN(numInWord, hunPat, tenPat):
	"Divides the input numInWord into millions, thousands and hundreds part; \
	 similar to the concept of the function threePlacesNTW;"

	total = 0;

	#hundreds-tens-ones
	#if pat.match(numInWord).group(3) exists, match it with this

	#get hundreds-tens-ones
	hunBlock = hunPat.search(numInWord) #numInWord == mainBlock
	if( hunBlock!=None and hunBlock.group(1) ):
		#total = total + ()#get appropriate value and expand
		#print hunBlock.group(2)+"<- hundreds"
		total = total + getNum(hunBlock.group(2))*100

	if( hunBlock!=None and hunBlock.group(4) ):
		#total = total + ()#get appropriate value and expand
		#print hunBlock.group(3)+"<- tensones"

		tensOnesBlock = tenPat.search(hunBlock.group(4))
		if( tensOnesBlock!=None and tensOnesBlock.group(1) ):
			#total = total + ()#get appropriate value and expand
			#print tensOnesBlock.group(1)+"<- tens"
			total = total + getNum(tensOnesBlock.group(1))


		if( tensOnesBlock!=None and tensOnesBlock.group(3) ):
			#total = total + ()#get appropriate value and expand
			#print tensOnesBlock.group(3)+"<- ones"
			total = total + getNum(tensOnesBlock.group(3))

	#re.purge()
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

def testWTN():
	sys.stdout.write('1 999 999 vs ')
	wordsToNum('one million nine hundred ninety-nine thousand nine hundred ninety-nine')

	sys.stdout.write('1 000 000 vs ')
	wordsToNum('one million')

	sys.stdout.write('999 000 vs ')
	wordsToNum('nine hundred ninety-nine thousand')

	sys.stdout.write('900 000 vs ')
	wordsToNum('nine hundred thousand')
	
	sys.stdout.write('90 000 vs ')
	wordsToNum('ninety thousand')
	
	sys.stdout.write('9 000 vs ')
	wordsToNum('nine thousand')

	sys.stdout.write('999 vs ')
	wordsToNum('nine hundred ninety-nine')

	sys.stdout.write('900 vs ')
	wordsToNum('nine hundred')
	
	sys.stdout.write('90 vs ')
	wordsToNum('ninety')

	sys.stdout.write('9 vs ')
	wordsToNum('nine')

	sys.stdout.write('1 999 000 vs ')
	wordsToNum('one million nine hundred ninety-nine thousand')
	
	sys.stdout.write('1 900 000 vs ')
	wordsToNum('one million nine hundred thousand')
	
	sys.stdout.write('1 090 000 vs ')
	wordsToNum('one million ninety thousand')
	
	sys.stdout.write('1 009 000 vs ')
	wordsToNum('one million nine thousand')

	sys.stdout.write('1 000 999 vs ')
	wordsToNum('one million nine hundred ninety-nine')
	
	sys.stdout.write('1 000 900 vs ')
	wordsToNum('one million nine hundred')
	
	sys.stdout.write('1 000 090 vs ')
	wordsToNum('one million ninety')

	sys.stdout.write('1 000 009 vs ')
	wordsToNum('one million nine')

def wordsToCurrency(numInWord, currency):
	"Accepts two arguments: (1) a number from 0 to 1 million in word form,\
	 (2) any of 'USD', 'JPY' or 'PHP'; Returns number in to its numerical \
	 form with a prefix of the currency "
	return currency + str(wordsToNum(numInWord))

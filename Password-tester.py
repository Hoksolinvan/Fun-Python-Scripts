#!/usr/bin/env python3

import sys
import re

def main():
	""" This script reads a text from standard input,
	analyzes the validity of a password in each line,
	if valid assesses the strength of the password,
	and writes results of the password analysis into
	the standard output  """

	# if arguments provided, show error message
	if len(sys.argv) != 1:
		print("No arguments should be provided.")
		print("Usage: %s" % sys.argv[0])
		return 1;

	#reads the entire line(s)
	container=sys.stdin.readlines()
	
	#This secondary function will employ input-validation according to the criteria specified
	supportfunction(container)

	return 0





def supportfunction(container):

	
	for i in container:
		#all password-strength is automatically initialized to 1
		pstrength=1	

		#place holder value
		messages=["VALID"]

		#gets rid of the whitespaces
		length=len(i.strip())
	

		if length < 8:
			#This pattern matches everything that is NOT ASCII characters
			firstpattern=re.compile(r"[^\x00-\x7F]+") #Source: I read it from https://www.regular-expressions.info/posixbrackets.html
			validation1=firstpattern.search(str(i))

			if validation1:
				print(0,"INVALID","TOO_SHORT","NONASCII",sep=',')
				#moves to the next iteration of this loop
				continue;
			else:
				print(0,"INVALID","TOO_SHORT",sep=',')
				continue;


		#this other if statement is for the situation where the length of the string is greater than 8 but contains non-ascii characters
		elif length >=8:
			firstv2pattern=re.compile(r"[^\x00-\x7F]+")
			validation1_2=firstv2pattern.search(str(i))
			if validation1_2:
				print(0,"INVALID","NONASCII",sep=',')
				continue;
			
	
		#if the input-validation above is successfully dealt with we move on to the next function which would be responsible for evaluating the strength of the password
		
		secondsupportfunction(i,messages)


def secondsupportfunction(i,messages):

		separator=","
		pstrength=1


		secondpattern=re.compile(r"[A-Z]+")

		thirdpattern=re.compile(r"[a-z]+")

		fourthpattern=re.compile(r"[0-9]+")

		#This pattern matches special characters, basically everything that is not A-Z, a-z, 0-9, \s, and _ 
		fifthpattern=re.compile(r"[^A-Za-z0-9\s_]+")

		#This pattern makes use of backreferencing to detect repetition of characters
		sixthpattern=re.compile(r"(.)\1\1")



		validation3=secondpattern.search(str(i))
		validation4=thirdpattern.search(str(i))
		validation5=fourthpattern.search(str(i))
		validation6=fifthpattern.search(str(i))
		validation7=sixthpattern.search(str(i))

		if validation3:
			pstrength+=1

			messages.append("UPPERCASE")
		if validation4:
			pstrength+=1

			messages.append("LOWERCASE")
		if validation5:
			pstrength+=1

			messages.append("NUMBER")
		if validation6:
			pstrength+=1

			messages.append("SPECIAL")
		if validation7:
			pstrength-=1

			messages.append("sequence")

		#adds the password-strength number at position 0
		messages.insert(0,str(pstrength));

		#replaces "VALID" in position 1 with the following grade
		if pstrength==1:
			messages[1]="VERY_WEAK"
		elif pstrength==2:
			messages[1]="WEAK"
		elif pstrength==3:
			messages[1]="MEDIUM"
		elif pstrength==4:
			messages[1]="STRONG"
		elif pstrength==5:
			messages[1]="VERY_STRONG"

		#prints to stdout with , separator
		print(",".join(messages))
			

			
	
			



	

if __name__ == "__main__":
	main()

def isLine(txt):
	txt = txt.strip()
	if txt[0:2] <> "//" and txt <> "" and txt <>'\n':
		return True
	return False
	
def cleanLine(txt):
	if '//' in txt:
		comStart = txt.find('/')
		return txt[1:comStart].strip()
	else:
		return txt.strip()

def leftOf(txt, c):
	return txt[0:txt.find(c)].strip()
	
def rightOf(txt, c):
	"""returns text to right of symbol"""
	return txt[txt.find(c)+1:].strip()
	
import re  # Regular expressions library

def word(line, n):
	"""returns word n in line, starting at 0"""
	wordList = []
	wordList = re.sub("[^\w]", " ", line).split()
	return wordList[n]
import sys  # For pulling arguments from command line
	
class Parser(object):
	"""Provides convenient access to the symbols in the .asm file"""
	
	def __init__(self, filename):
		"""Opens the input file and gets ready to parse it"""
		self.hasMoreCommands = False  # This should be a method
		
		try:
			self.fin = open(filename)
			print self.fin
		except:
			print 'ERROR opening', filename
			return
			
		# I hate that this code is repeated below but will live with it!
		# Maybe ALED can help with this?
		while True:
			line = self.fin.readline()
			if not line: break
			if isCommand(line):
				self.command = cleanLine(line)
				self.hasMoreCommands = True
				return
		# If we get here there are no commands!
		self.hasMoreCommands = False
		
	def close(self):
		self.fin.close()
		print self.fin
		
	def advance(self):
		"""Reads the next command from the input and makes it the current command"""
		assert self.hasMoreCommands == True
		while True:
			line = self.fin.readline()
			if not line: break
			if isCommand(line):
				self.command = cleanLine(line)
				self.hasMoreCommands = True
				return
		# If we get here there are no more commands!
		self.hasMoreCommands = False
	
	def commandType(self):
		"""Returns the type of the current command"""
		firstChar = self.command[0]
		if firstChar == '@':
			return "A_COMMAND"
		elif firstChar == '(':
			return "L_COMMAND"
		else:
			return "C_COMMAND"
		
	def symbol(self):
		"""Return the symbol or decimal Xxx of the current command @Xxx (or Xxx)"""
		assert self.commandType() == "A_COMMAND" or self.commandType() == "L_COMMAND"
		if self.commandType() == "A_COMMAND":
			return str(self.command[1::])
		else:
			return str(self.command[1:-1])
	
	def dest(self):
		"""Returns the dest mnemonic in the current C-command (8 possibilities)"""
		assert self.commandType() == "C_COMMAND"
		command = self.command
		if '=' in command:
			return leftOf(command, '=')
		elif ';' in command:
			return 'null'  # Not sure this is right
		
	def comp(self):
		"""Returns the comp mnemonic in the current C-command (28 possibilities)"""
		assert self.commandType() == "C_COMMAND"
		command = self.command
		if '=' in command:
			return rightOf(command, '=')
		elif ';' in command:
			return leftOf(command, ';')
	
	def jump(self):
		"""Returns the jump mnemonic in the current C-command (8 possibilities)"""
		assert self.commandType() == "C_COMMAND"
		command = self.command
		if '=' in command:
			return "null"
		elif ';' in command:
			return rightOf(command, ';')

class Code(object):
	"""Provides methods for converting mnemonics into machine code ready for splicing"""
	def dest(self, mnemonic):
		"""Take mnemonic string and returns and returns 3 bits"""
		assert isinstance(mnemonic, str)
		dests = dict()
		dests['null'] = '000'
		dests['M'] = 	'001'
		dests['D'] = 	'010'
		dests['MD'] = 	'011'
		dests['A'] = 	'100'
		dests['AM'] = 	'101'
		dests['AD'] = 	'110'
		dests['AMD'] = 	'111'
		return dests[mnemonic]
	
	def comp(self, mnemonic):
		"""Take mnemonic string and returns and returns 7 bits"""
		assert isinstance(mnemonic, str)
		alucmds = dict()
		alucmds['0'] = 		'0101010'
		alucmds['1'] = 		'0111111'
		alucmds['-1'] = 	'0111010'
		alucmds['D'] = 		'0001100'
		alucmds['A'] = 		'0110000'
		alucmds['!D'] = 	'0001101'
		alucmds['!A'] = 	'0110001'
		alucmds['-D'] = 	'0001111'
		alucmds['-A'] = 	'0110011'
		alucmds['D+1'] = 	'0011111'
		alucmds['A+1'] = 	'0110111'
		alucmds['D-1'] = 	'0001110'
		alucmds['A-1'] = 	'0110010'
		alucmds['D+A'] = 	'0000010'
		alucmds['D-A'] = 	'0010011'
		alucmds['A-D'] = 	'0000111'
		alucmds['D&A'] = 	'0000000'
		alucmds['D|A'] = 	'0010101'
		alucmds['M'] = 		'1110000'
		alucmds['!M'] = 	'1110001'
		alucmds['-M'] = 	'1110011'
		alucmds['M+1'] = 	'1110111'
		alucmds['M-1'] = 	'1110010'
		alucmds['D+M'] = 	'1000010'
		alucmds['D-M'] = 	'1010011'
		alucmds['M-D'] = 	'1000111'
		alucmds['D&M'] = 	'1000000'
		alucmds['D|M'] = 	'1010101'
		return alucmds[mnemonic]
	
	def jump(self, mnemonic):
		"""Take mnemonic string and returns and returns 3 bits"""
		assert isinstance(mnemonic, str)
		jumps = dict()
		jumps['null'] = '000'
		jumps['JGT'] = 	'001'
		jumps['JEQ'] = 	'010'
		jumps['JGE'] = 	'011'
		jumps['JLT'] = 	'100'
		jumps['JNE'] = 	'101'
		jumps['JLE'] = 	'110'
		jumps['JMP'] = 	'111'
		return jumps[mnemonic]

class SymbolTable(object):
	"""Manages system default, and user symbol table.
	Stores symbols and their binary ROM addresses as strings"""
	
	def __init__(self):
		"""Adds system default entries to symbol table,
		and a dictionary for user values."""
		self.user = dict()
		
		self.user["SP"] = 		binTxt(0x0000, 16)
		self.user["LCL"] = 		binTxt(0x0001, 16)
		self.user["ARG"] = 		binTxt(0x0002, 16)
		self.user["THIS"] = 	binTxt(0x0003, 16)
		self.user["THAT"] = 	binTxt(0x0004, 16)
		self.user["R0"] = 		binTxt(0x0000, 16)
		self.user["R1"] = 		binTxt(0x0001, 16)
		self.user["R2"] =	 	binTxt(0x0002, 16)
		self.user["R3"] = 		binTxt(0x0003, 16)
		self.user["R4"] = 		binTxt(0x0004, 16)
		self.user["R5"] = 		binTxt(0x0005, 16)
		self.user["R6"] = 		binTxt(0x0006, 16)
		self.user["R7"] = 		binTxt(0x0007, 16)
		self.user["R8"] = 		binTxt(0x0008, 16)
		self.user["R9"] = 		binTxt(0x0009, 16)
		self.user["R10"] = 		binTxt(0x000a, 16)
		self.user["R11"] = 		binTxt(0x000b, 16)
		self.user["R12"] = 		binTxt(0x000c, 16)
		self.user["R13"] = 		binTxt(0x000d, 16)
		self.user["R14"] = 		binTxt(0x000e, 16)
		self.user["R15"] = 		binTxt(0x000f, 16)
		self.user["SCREEN"] = 	binTxt(0x4000, 16)
		self.user["KBD"] = 		binTxt(0x6000, 16)

	def __str__(self):
		print "Symbol table"
		ret = ""
		for item in self.user:
			ret += item + ','
		return ret
		
	def addEntry(self, symbol, address):
		"""Adds the pair to the table. Symbol is a string, address is int"""
		assert isinstance(symbol, str)
		assert isinstance(address, int)
		self.user[symbol] = binTxt(address, 16)
		
	def contains(self, symbol):
		"""Does the symbol table contain the given symbol?"""
		assert isinstance(symbol, str)
		return symbol in self.user
	
	def getAddress(self, symbol):
		"""Returns the address associated with the symbol"""
		assert isinstance(symbol, str)
		assert isinstance(self.user[symbol], str)
		return self.user[symbol]
		
def isCommand(txt):
	"""Is this line a command line?"""
	# This can be removed once I solve the issue at the top of Parser
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

def binTxt(x, n):
	"""returns n-bit binary text for x"""
	assert isinstance(x, int)
	assert isinstance(n, int)
	binary = bin(x)[2:]
	padding = n - len(binary)
	if padding < 0:
		return False
	return '0' * padding + binary
	
def main(name, filename):

	# First parse through building symbol table
	P1 = Parser(filename)
	SymTable = SymbolTable()
	
	if not P1.hasMoreCommands:
		print "No commands in file!"
		return
	
	print "First parse, building symbol table..."
	address = 0  # Eventual ROM address
	while P1.hasMoreCommands:
		if P1.commandType() == "L_COMMAND":
			SymTable.addEntry(P1.symbol(),address)
			print "Adding symbol", P1.symbol(), 'pointing to ROM', address
		else:
			address += 1	
		P1.advance()
	P1.close()
	print "First parse complete OK :-)"
	print "---"
	print "Starting second parse..."
	# Second parse
	P2 = Parser(filename)
	C = Code()		
	
	fout = open(filename[:-4] + '.hack', 'w')
	print fout

	nextRAM = 16
	if not P2.hasMoreCommands:
		print "No commands in file (how got here?)!"
		fout.close()
	while P2.hasMoreCommands:
		if P2.commandType() == "A_COMMAND":
			symbol = P2.symbol()
			if symbol[0] in '0123456789':
				fout.write(binTxt(int(symbol),16) + '\n')
			elif SymTable.contains(symbol):
				addressBin = SymTable.getAddress(symbol)
				fout.write(addressBin + '\n')
			else:  # We have a new variable to add to RAM
				SymTable.addEntry(symbol,nextRAM)
				print "Added variable", symbol, "at RAM", nextRAM
				fout.write('0' + binTxt(nextRAM,15) + '\n')
				nextRAM += 1
		elif P2.commandType() == "C_COMMAND":
			fout.write('111' + C.comp(P2.comp()) + C.dest(P2.dest()) + C.jump(P2.jump()) + '\n')
		elif P2.commandType() == "L_COMMAND":
			pass
		
		P2.advance()
	
	P2.close()
	fout.close()
	print fout
	
if __name__ == '__main__':
	main(*sys.argv)
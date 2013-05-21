# ALU commands lookup table
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

# Destinations lookup table
dests = dict()
dests['null'] = '000'
dests['M'] = 	'001'
dests['D'] = 	'010'
dests['MD'] = 	'011'
dests['A'] = 	'100'
dests['AM'] = 	'101'
dests['AD'] = 	'110'
dests['AMD'] = 	'111'

# ALU Jump commands lookup table
jumps = dict()
jumps['null'] = '000'
jumps['JGT'] = 	'001'
jumps['JEQ'] = 	'010'
jumps['JGE'] = 	'011'
jumps['JLT'] = 	'100'
jumps['JNE'] = 	'101'
jumps['JLE'] = 	'110'
jumps['JMP'] = 	'111'

def binTxt(x, n):
	"""returns n-bit binary text for x"""
	binary = bin(x)[2:]
	padding = n - len(binary)
	if padding < 0:
		return False
	return '0' * padding + binary

def leftOf(txt, c):
	return txt[0:txt.find(c)]
	
def rightOf(txt, c):
	return txt[txt.find(c)+1:]
	
def parse(file):
	output = ""
	fin = open(file)
	
	for line in fin:
		line = line.strip()
		print line
		if line[0:2] <> "//" and line <> "":
			if line[0] == "@":  # A Command OR LABEL
				num = int(line[1:])  # Strip @
				output += binTxt(num, 16) + '\n'
			elif line[0] == '(':
				output == "Pseudocommand!"
			else:  # C Command
				if '=' in line:
 					dst = leftOf(line, '=')
 					dst = dests[dst] # Convert to binary
 					alucmd = rightOf(line, '=')
 					alucmd = alucmds[alucmd]
					output += '111'	 + alucmd + dst + '000' + '\n'
				if ';' in line:
					jmp = rightOf(line, ';')
					jmp = jumps[jmp]
					alucmd = leftOf(line, ';')
 					alucmd = alucmds[alucmd]
					output += '111'	 + alucmd + '000' + jmp + '\n'
	return output

# output = parse("add.asm")
output = parse("Max.asm")
# output = parse("PongL.asm")
print output

import BenLib
from BenLib import *

def binTxt(x, n):
	"""returns n-bit binary text for x"""
	binary = bin(x)[2:]
	padding = n - len(binary)
	if padding < 0:
		return False
	return '0' * padding + binary
	
# Predefined symbols table
symbols = dict()
symbols['SP'] = 	binTxt(0x0000, 16)
symbols['LCL'] = 	binTxt(0x0001, 16)
symbols['ARG'] = 	binTxt(0x0002, 16)
symbols['THIS'] = 	binTxt(0x0003, 16)
symbols['THAT'] = 	binTxt(0x0004, 16)
symbols['R0'] = 	binTxt(0x0000, 16)
symbols['R1'] = 	binTxt(0x0001, 16)
symbols['R2'] = 	binTxt(0x0002, 16)
symbols['R3'] = 	binTxt(0x0003, 16)
symbols['R4'] = 	binTxt(0x0004, 16)
symbols['R5'] = 	binTxt(0x0005, 16)
symbols['R6'] = 	binTxt(0x0006, 16)
symbols['R7'] = 	binTxt(0x0007, 16)
symbols['R8'] = 	binTxt(0x0008, 16)
symbols['R9'] = 	binTxt(0x0009, 16)
symbols['R10'] = 	binTxt(0x000a, 16)
symbols['R11'] = 	binTxt(0x000b, 16)
symbols['R12'] = 	binTxt(0x000c, 16)
symbols['R13'] = 	binTxt(0x000d, 16)
symbols['R14'] = 	binTxt(0x000e, 16)
symbols['R15'] = 	binTxt(0x000f, 16)
symbols['SCREEN'] = binTxt(0x4000, 16)
symbols['KBD'] = 	binTxt(0x6000, 16)

def parse(line):
	commandType = ""
	symbol = ""
	comp = ""
	dest = ""
	jump = ""
	
	clean = cleanLine(line)
	
	if isLine(line):
		if clean[0] == "@":
			if clean[1] in '0123456789':
				commandType = "A_COMMAND"
				symbol = binTxt(int(clean[1:]), 15)
			else:
				commandType = "L_COMMAND"
				symbol = rightOf(clean, '@')
		elif clean[0] == '(':
			commandType = ""
		else:
			commandType = "C_COMMAND"
			if '=' in line:
				comp = Code.comp(rightOf(clean, '='))
				dest = Code.dest(leftOf(clean, '='))
				jump = "000"
			if ';' in line:
				comp = Code.comp(leftOf(clean, ';'))
				dest = '000'
				jump = Code.jump(rightOf(clean, ';'))
	return [commandType, symbol, comp, dest, jump]

import Code

def assemble(file):
	fin = open(file)
	
	# First Parse
	inst = 0
	for line in fin:
		parseOut = parse(line)
		if line[0] == '(':
			label = line[1:line.find(')')]
			symbols[label] = binTxt(inst,16)
		elif parseOut[0] <> "":
			inst += 1
		
	# SECOND PARSE
	fin = open(file)
	output = ""	
	for line in fin:
		parseOut = parse(line)
		if parseOut[0] == "A_COMMAND":
			output += '0' + parseOut[1] + '\n'
		if parseOut[0] == "C_COMMAND":
			output += '111' + parseOut[2] + parseOut[3] + parseOut[4] + '\n'
		if parseOut[0] == "L_COMMAND":
			output += str(symbols[parseOut[1]]) + '\n'
			print output
	return output


# fn = raw_input("File to assemble: ")
# print "Assembling " + fn + "..."
# output = assemble(fn)

output = assemble("Pong.asm")

output = output[:-1]  # Strip the final newline

fout = open('Prog.hack', 'w')
fout.write(output)
fout.close()

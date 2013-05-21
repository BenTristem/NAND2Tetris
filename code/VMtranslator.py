import BenLib
from BenLib import *

file = ["SimpleAdd", "StackTest", "BasicTest", "PointerTest", "StaticTest"]
file = file + ["BasicLoop", "FibonacciSeries", "SimpleFunction"]
choose = 6
fileName = file[choose]

fin = open(fileName + ".vm")
fout = open(fileName + ".asm", 'w')
	
def output(line):
	fout.write(line + '\n')

def initialise():
# 	set RAM[0] 256
	output('@256')
	output('D=A')
	output('@0')
	output('M=D')
		
# 	set RAM[1] 300,
	output('@300')
	output('D=A')
	output('@1')
	output('M=D')

# 	set RAM[2] 400,
	output('@400')
	output('D=A')
	output('@2')
	output('M=D')
	
# 	set RAM[3] 3000,
	output('@3000')
	output('D=A')
	output('@3')
	output('M=D')
	
# 	set RAM[4] 3010,
	output('@3010')
	output('D=A')
	output('@4')
	output('M=D')
	
def set(d):
	"""Changes the Stack Pointer by d"""
	output('@SP')
	output('D=M')
	output('@' + str(abs(d)))
	if d > 0:
		output('D=D+A')
	else:
		output('D=D-A')
	output('@AP')
	output('M=D')

ranges = dict()
ranges['local'] = '@LCL'
ranges['argument'] = '@ARG'
ranges['this'] = '@THIS'
ranges['that'] = '@THAT'

def push(type, x):
	if type == 'constant':
		output('@' + str(x))  # X into A register
		output('D=A')  # Copy A into D
		output('@SP')  #  or 0 into A register
		output('A=M')  # Set A register to 
		output('M=D')  # Write memory A with D
	elif type == 'temp' or type == 'pointer' or type == "static":
		output('@' + str(x))  # Load offset into A
		output('D=A') # Move offset to D register
		if type == 'temp':
			output('@5')  # Base of temp
			output('A=D+A') # Absolute source in D
		elif type == 'pointer':
			output('@3') # Base of pointer
			output('A=D+A') # Absolute source in D
		else:
			output('@' + fileName + '.' + x)
		output('D=M') # Read from temp into D
		output('@SP') # A register becomes  (i.e 0) 
		output('A=M')  # Set A register to stack top
		output('M=D')  # Write memory with D
	elif type in ranges:
		output('@' + str(x))  # Load offset into A
		output('D=A') # Move offset to D register
		output(ranges[type])  # Load base of range into A
		output('M')  # Lookup memory value
		output('A=D+M') # Calculate absolute source
		output('D=M')
	else:
		print "PUSH ERROR"
		return False
		
	output('@SP')
	output('A=M')
	output('M=D')
	set(1)

def pop(type, x):
	global fileName  # Used for static
	if type in ranges:
		# calculate absolute address of LCL X & store in Temp0
		output('@' + str(x))
		output('D=A')
		output(ranges[type])
		output('A=M')
		output('D=D+A')
		output('@5')
		output('M=D')
		
		# get the value at -1 (top of stack) and put in D
		output('@SP')
		output('A=M-1')
		output('D=M')
		
		# store this value into address specified by Temp0
		output('@5')
		output('A=M')	
	elif type == 'temp' or type=='pointer' or type == 'static':
		# get the value at -1 (top of stack) and put in D
		output('@SP')
		output('A=M-1')
		output('D=M')
		
		# Write this to temp x
		if type == "temp":
			output('@' + str(5+int(x)))
		elif type == "pointer":
			output('@' + str(3+int(x)))
		else:
			output('@' + fileName + '.' + x)
	else:
		print "Help me with POP segment"
		return False
	
	output('M=D')  # Commit to memory
	set(-1)	

def parseLine(line):
	# Dictionary of commands with number of arguments
	cmds = dict()
	cmds['push'] = 'C_PUSH'
	cmds['pop'] = 'C_POP'
	cmds['if'] = 'C_IF'
	cmds['eq'] = 'C_ARITHMETIC'
	cmds['add'] = 'C_ARITHMETIC'
	cmds['sub'] = 'C_ARITHMETIC'
	cmds['lt'] = 'C_ARITHMETIC'
	cmds['gt'] = 'C_ARITHMETIC'
	cmds['neg'] = 'C_ARITHMETIC'
	cmds['and'] = 'C_ARITHMETIC'
	cmds['or'] = 'C_ARITHMETIC'
	cmds['not'] = 'C_ARITHMETIC'
	cmds['label'] = 'C_LABEL'
	cmds['goto'] = 'C_GOTO'
	cmds['function'] = 'C_FUNCTION'
	cmds['call'] = 'C_CALL'
	cmds['return'] = 'C_RETURN'
	oneArgCmds = ['C_LABEL', 'C_GOTO', "C_NOT"]
	twoArgCmds = ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL', 'C_IF']
	
	args = [22,2]
	cmd = word(line, 0)
	cmdType = ""
	if cmd in cmds:
		cmdType = cmds[cmd]
		if cmdType == 'C_ARITHMETIC' or cmdType == 'C_RETURN':
			args = [word(line,0), None]
		elif cmdType == 'C_FUNCTION':
			# Line below makes up for fact word command mishandles .
			args = [(word(line,1) + '.' + word(line,2)), word(line,3)]
		elif cmdType in oneArgCmds:
			args = [word(line,1), None]
		elif cmdType in twoArgCmds:
			args = [word(line,1), word(line,2)]
		else:
			cmdType = "*UNKNOW*"
	else:
		cmdType = "*NOT FOUND*"
	return [cmdType, args[0], args[1]]

def scrapeTwo():
	"""Put top two stack items into D and A"""	
	# Store value at -1 in TEMP 0
	output('@0')
	output('D=M')
	output('@1')
	output('D=D-A')
	output('@5')
	output('M=D')
	
	# Store value at -2 in D register
	output('@0')
	output('D=M')
	output('@2')
	output('A=D-A')
	output('D=M')
	
	# Put value at address in TEMP 0 in A register
	output('@5')
	output('A=M')
	output('A=M')

# WARNING uses Global 
def writeArithmetic(command):
	lookup = dict()
	lookup['add'] = 'D=D+A'
	lookup['sub'] = 'D=D-A'
	lookup['and'] = 'D=D&A'
	lookup['or'] = 'D=D|A'
	
	output('// ' + command)
	
	if command in lookup:
		scrapeTwo()
		output(lookup[command])
		output('@0')
		output('A=M')
		output('M=D')
	elif command == "eq" or command == "lt" or command == "gt":
		CMD = command.upper()
		scrapeTwo()
		output('D=D-A')
		
		# If condition jump to (XX) label
		output('@' + CMD)	
		output('D;J' + CMD)
		
		# Otherwise not condition so set 0
		output('@' + str(-2))
		output('M=0')
		
		# Jump to customised END
		output('@END_' + CMD)
		output('0;JMP')		
		
		# Set -1 if equal
		output('(' + CMD + ')')
		
		# Put SP-2 into A register
		output('@2')
		output('D=A')
		output('@0')
		output('A=M')		
		output('A=A-D')
		
		output('M=-1')
	
		output('(END_' + CMD +')')  # CAUTION NON UNIQUE LABEL!
	elif command == "neg" or command == "not":
		# Take top of stack into D register
		output('@SP')
		output('A=M')
		output('A=M')
		output('D=A')
	
		if command == "neg":
			output('M=-D')
		else:
			output('M=!D')
		
		set(1)	
	else:
		print command, "Write new command!"
		
	set(-1)

def writePushPop(command, segment, index):
	output('// ' + command + segment + str(index))
	if command == "C_PUSH":
		push(segment, index)
	elif command == "C_POP":
		pop(segment, index)
	else:
		print "Unknown command type"

def writeGoto(label):
	output('// ' + 'GOTO ' + label)
	output('@' + label)
	output('0;JMP')

def writeIf(label):
	output('// IF-GOTO ' + label)
	pop('temp', 1)
	output('@6') # Temp 1
	output('D=M')
	output('@' + label)
	output('D;JNE')

def writeLabel(label):
	output('(' + str(lineList[1]) + ')')
	
def writeFunction(functionName, numLocals):
	output('// function ' + functionName + str(numLocals))
	writeLabel(functionName)
	k = 1
	# Set all local variables to 0
	while k <= numLocals:
		writePushPop('C_PUSH','constant', 0)
		k += 1
	return None

def writeReturn():
	output('// return') 
	return None

def writeCall(functionName, numArgs):
	output('// call ' + functionName + str(numArgs))
	return None

# initialise()

# MAIN LOOP BELOW
for line in fin:
	if isLine(line):
		lineList = parseLine(line)
		cType = lineList[0]
		if cType == 'C_ARITHMETIC':
			writeArithmetic(lineList[1])
		elif cType == 'C_PUSH' or cType == 'C_POP':
			writePushPop(cType, lineList[1], int(lineList[2]))
		elif cType == 'C_LABEL':
			writeLabel(lineList[1])
		elif cType == 'C_IF':
			writeIf(lineList[2])
		elif cType == 'C_GOTO':
			writeGoto(lineList[1])
		elif cType == 'C_RETURN':
			writeReturn()
		elif cType == 'C_FUNCTION':
			writeFunction(lineList[1], int(lineList[2]))
		elif cType == 'C_CALL':
			writeCall(lineList[1], int(lineList[2]))
		else:
			print "ERROR: Unkonwn C_TYPE", line.strip()

fout.close()
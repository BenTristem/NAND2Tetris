@256
D=A
@SP
M=D
@17
D=A
@SP
A=M
M=D
@257
D=A
@SP
M=D
@17
D=A
@SP
A=M
M=D
@258
D=A
@SP
M=D
@256
D=M
@257
A=M
D=D-A
@EQ
D;JEQ
@256
M=0
@END_EQ
0;JMP
(EQ)
@256
M=-1
(END_EQ)
@257
D=A
@SP
M=D
@892
D=A
@SP
A=M
M=D
@258
D=A
@SP
M=D
@891
D=A
@SP
A=M
M=D
@259
D=A
@SP
M=D
@257
D=M
@258
A=M
D=D-A
@LT
D;JLT
@257
M=0
@END_LT
0;JMP
(LT)
@257
M=-1
(END_LT)
@258
D=A
@SP
M=D
@32767
D=A
@SP
A=M
M=D
@259
D=A
@SP
M=D
@32766
D=A
@SP
A=M
M=D
@260
D=A
@SP
M=D
@258
D=M
@259
A=M
D=D-A
@GT
D;JGT
@258
M=0
@END_GT
0;JMP
(GT)
@258
M=-1
(END_GT)
@259
D=A
@SP
M=D
@56
D=A
@SP
A=M
M=D
@260
D=A
@SP
M=D
@31
D=A
@SP
A=M
M=D
@261
D=A
@SP
M=D
@53
D=A
@SP
A=M
M=D
@262
D=A
@SP
M=D
@260
D=M
@261
A=M
D=D+A
@260
M=D
@261
D=A
@SP
M=D
@112
D=A
@SP
A=M
M=D
@262
D=A
@SP
M=D
@260
D=M
@261
A=M
D=D-A
@260
M=D
@261
D=A
@SP
M=D
@260
D=M
M=-D
@262
D=A
@SP
M=D
@261
D=A
@SP
M=D
@259
D=M
@260
A=M
D=D&A
@259
M=D
@260
D=A
@SP
M=D
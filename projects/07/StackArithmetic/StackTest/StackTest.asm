// C_PUSH constant 17 SP=256
@17
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@257
D=A
@SP
M=D
// C_PUSH constant 17 SP=257
@17
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@258
D=A
@SP
M=D
// eq SP=258
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
// C_PUSH constant 892 SP=257
@892
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@258
D=A
@SP
M=D
// C_PUSH constant 891 SP=258
@891
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@259
D=A
@SP
M=D
// lt SP=259
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
// C_PUSH constant 32767 SP=258
@32767
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@259
D=A
@SP
M=D
// C_PUSH constant 32766 SP=259
@32766
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@260
D=A
@SP
M=D
// gt SP=260
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
// C_PUSH constant 56 SP=259
@56
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@260
D=A
@SP
M=D
// C_PUSH constant 31 SP=260
@31
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@261
D=A
@SP
M=D
// C_PUSH constant 53 SP=261
@53
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@262
D=A
@SP
M=D
// add SP=262
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
// C_PUSH constant 112 SP=261
@112
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@262
D=A
@SP
M=D
// sub SP=262
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
// neg SP=261
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
// and SP=261
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
// C_PUSH constant 82 SP=260
@82
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@261
D=A
@SP
M=D
// or SP=261
@259
D=M
@260
A=M
D=D|A
@259
M=D
@260
D=A
@SP
M=D
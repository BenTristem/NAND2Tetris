// C_PUSH constant 10 SP=256
@10
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
// C_POP local 0 SP=257
@0
D=A
@LCL
A=M
D=D+A
@5
M=D
@SP
A=M-1
D=M
@5
A=M
M=D
@256
D=A
@SP
M=D
// C_PUSH constant 21 SP=256
@21
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
// C_PUSH constant 22 SP=257
@22
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
// C_POP argument 2 SP=258
@2
D=A
@ARG
A=M
D=D+A
@5
M=D
@SP
A=M-1
D=M
@5
A=M
M=D
@257
D=A
@SP
M=D
// C_POP argument 1 SP=257
@1
D=A
@ARG
A=M
D=D+A
@5
M=D
@SP
A=M-1
D=M
@5
A=M
M=D
@256
D=A
@SP
M=D
// C_PUSH constant 36 SP=256
@36
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
// C_POP this 6 SP=257
@6
D=A
@THIS
A=M
D=D+A
@5
M=D
@SP
A=M-1
D=M
@5
A=M
M=D
@256
D=A
@SP
M=D
// C_PUSH constant 42 SP=256
@42
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
// C_PUSH constant 45 SP=257
@45
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
// C_POP that 5 SP=258
@5
D=A
@THAT
A=M
D=D+A
@5
M=D
@SP
A=M-1
D=M
@5
A=M
M=D
@257
D=A
@SP
M=D
// C_POP that 2 SP=257
@2
D=A
@THAT
A=M
D=D+A
@5
M=D
@SP
A=M-1
D=M
@5
A=M
M=D
@256
D=A
@SP
M=D
// C_PUSH constant 510 SP=256
@510
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
// C_POP temp 6 SP=257
@SP
A=M-1
D=M
@11
M=D
@256
D=A
@SP
M=D
// C_PUSH local 0 SP=256
@0
D=A
@LCL
M
A=D+M
D=M
@SP
A=M
M=D
@257
D=A
@SP
M=D
// C_PUSH that 5 SP=257
@5
D=A
@THAT
M
A=D+M
D=M
@SP
A=M
M=D
@258
D=A
@SP
M=D
// add SP=258
@256
D=M
@257
A=M
D=D+A
@256
M=D
@257
D=A
@SP
M=D
// C_PUSH argument 1 SP=257
@1
D=A
@ARG
M
A=D+M
D=M
@SP
A=M
M=D
@258
D=A
@SP
M=D
// sub SP=258
@256
D=M
@257
A=M
D=D-A
@256
M=D
@257
D=A
@SP
M=D
// C_PUSH this 6 SP=257
@6
D=A
@THIS
M
A=D+M
D=M
@SP
A=M
M=D
@258
D=A
@SP
M=D
// C_PUSH this 6 SP=258
@6
D=A
@THIS
M
A=D+M
D=M
@SP
A=M
M=D
@259
D=A
@SP
M=D
// add SP=259
@257
D=M
@258
A=M
D=D+A
@257
M=D
@258
D=A
@SP
M=D
// sub SP=258
@256
D=M
@257
A=M
D=D-A
@256
M=D
@257
D=A
@SP
M=D
// C_PUSH temp 6 SP=257
@6
D=A
@5
A=D+A
D=M
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
// add SP=258
@256
D=M
@257
A=M
D=D+A
@256
M=D
@257
D=A
@SP
M=D

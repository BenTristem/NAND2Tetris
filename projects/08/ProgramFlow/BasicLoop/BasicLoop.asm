// C_PUSH constant 0
@0
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@SP
D=M
@1
D=D+A
@SP
M=D
// C_POP local 0
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
@SP
D=M
@1
D=D-A
@SP
M=D
(LOOP_START)
// C_PUSH argument 0
@0
D=A
@ARG
M
A=D+M
D=M
@SP
A=M
M=D
@SP
D=M
@1
D=D+A
@SP
M=D
// C_PUSH local 0
@0
D=A
@LCL
M
A=D+M
D=M
@SP
A=M
M=D
@SP
D=M
@1
D=D+A
@SP
M=D
// add
@0
D=M
@1
D=D-A
@5
M=D
@0
D=M
@2
A=D-A
D=M
@5
A=M
A=M
D=D+A
@7
M=A
@5
M=D
@SP
D=M
@2
D=D-A
@6
M=D
@5
D=M
@6
M
A=M
M=D
@7
A=M
@SP
D=M
@1
D=D-A
@SP
M=D
// C_POP local 0
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
@SP
D=M
@1
D=D-A
@SP
M=D
// C_PUSH argument 0
@0
D=A
@ARG
M
A=D+M
D=M
@SP
A=M
M=D
@SP
D=M
@1
D=D+A
@SP
M=D
// C_PUSH constant 1
@1
D=A
@SP
A=M
M=D
@SP
A=M
M=D
@SP
D=M
@1
D=D+A
@SP
M=D
// sub
@0
D=M
@1
D=D-A
@5
M=D
@0
D=M
@2
A=D-A
D=M
@5
A=M
A=M
D=D-A
@7
M=A
@5
M=D
@SP
D=M
@2
D=D-A
@6
M=D
@5
D=M
@6
M
A=M
M=D
@7
A=M
@SP
D=M
@1
D=D-A
@SP
M=D
// C_POP argument 0
@0
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
@SP
D=M
@1
D=D-A
@SP
M=D
// C_PUSH argument 0
@0
D=A
@ARG
M
A=D+M
D=M
@SP
A=M
M=D
@SP
D=M
@1
D=D+A
@SP
M=D
// C_IF goto LOOP_START
@SP
A=M-1
D=M
@6
M=D
@SP
D=M
@1
D=D-A
@SP
M=D
@6
D=M
@LOOP_START
D;JNE
// C_PUSH local 0
@0
D=A
@LCL
M
A=D+M
D=M
@SP
A=M
M=D
@SP
D=M
@1
D=D+A
@SP
M=D
// C_PUSH argument 1
@1
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
// C_POP pointer 1
@SP
A=M-1
D=M
@4
M=D
@SP
D=M
@1
D=D-A
@SP
M=D
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
// C_POP that 0
@0
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
@SP
D=M
@1
D=D-A
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
// C_POP that 1
@1
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
// C_PUSH constant 2
@2
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
(MAIN_LOOP_START)
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
// C_IF goto COMPUTE_ELEMENT
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
@COMPUTE_ELEMENT
D;JNE
// C_GOTO END_PROGRAM
@END_PROGRAM
0;JMP
(COMPUTE_ELEMENT)
// C_PUSH that 0
@0
D=A
@THAT
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
// C_PUSH that 1
@1
D=A
@THAT
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
// C_POP that 2
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
@SP
D=M
@1
D=D-A
@SP
M=D
// C_PUSH pointer 1
@1
D=A
@3
A=D+A
D=M
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
// C_POP pointer 1
@SP
A=M-1
D=M
@4
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
// C_GOTO MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
(END_PROGRAM)

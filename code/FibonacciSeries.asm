// C_PUSHargument1
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
@AP
M=D
// C_POPpointer1
@SP
A=M-1
D=M
@4
M=D
@SP
D=M
@1
D=D-A
@AP
M=D
// C_PUSHconstant0
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
@AP
M=D
// C_POPthat0
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
@AP
M=D
// C_PUSHconstant1
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
@AP
M=D
// C_POPthat1
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
@AP
M=D
// C_PUSHargument0
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
@AP
M=D
// C_PUSHconstant2
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
@AP
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
@0
A=M
M=D
@SP
D=M
@1
D=D-A
@AP
M=D
// C_POPargument0
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
@AP
M=D
(MAIN_LOOP_START)
// C_PUSHargument0
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
@AP
M=D
// IF-GOTO COMPUTE_ELEMENT
@SP
A=M-1
D=M
@6
M=D
@SP
D=M
@1
D=D-A
@AP
M=D
@6
D=M
@COMPUTE_ELEMENT
D;JNE
// GOTO END_PROGRAM
@END_PROGRAM
0;JMP
(COMPUTE_ELEMENT)
// C_PUSHthat0
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
@AP
M=D
// C_PUSHthat1
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
@AP
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
@0
A=M
M=D
@SP
D=M
@1
D=D-A
@AP
M=D
// C_POPthat2
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
@AP
M=D
// C_PUSHpointer1
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
@AP
M=D
// C_PUSHconstant1
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
@AP
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
@0
A=M
M=D
@SP
D=M
@1
D=D-A
@AP
M=D
// C_POPpointer1
@SP
A=M-1
D=M
@4
M=D
@SP
D=M
@1
D=D-A
@AP
M=D
// C_PUSHargument0
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
@AP
M=D
// C_PUSHconstant1
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
@AP
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
@0
A=M
M=D
@SP
D=M
@1
D=D-A
@AP
M=D
// C_POPargument0
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
@AP
M=D
// GOTO MAIN_LOOP_START
@MAIN_LOOP_START
0;JMP
(END_PROGRAM)

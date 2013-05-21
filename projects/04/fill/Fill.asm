// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

@fe // Fill or Empty. 0=Fill, -1=Empty

(START)
// Test if keypress
	@KBD
	D=M
	@NOPRESS
	D;JEQ
	@PRESS
	D;JMP
	
(PRESS)
	@fe
	M=0
	@START2
	D;JMP

(NOPRESS)
	@fe
	M=-1

(START2)
// Load screen start address into i
	@SCREEN

	D=A
	
@i

	M=D



	(LOOP)
	// Check i is still in range
		@i
		D=M
		@24576
		D=D-A
		@START
		D;JEQ
		
	// Choose if fill or blank
		@fe
		D=M
	
	// Go to address stated in i
		@i
		A=M
	
	// Clear or blank based on @fe
		M=!D
		
	// Go to next address
		@i
		M=M+1
		
	// Go back to loop
	@LOOP
	0;JMP
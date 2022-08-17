============  IAS IMPLEMENTATION IN PYTHON  ============

The registers involved in IAS computer are:

AC  : Accumulator
	Accumulate/hold results of an ALU operation

IR  : Instructions Register
	8 bit opcode of the instruction to be executed
	
IBR : Instructions Buffer register
	Holds the RHS instruction temporarily

MQ  : Multiplier/Quotioent Register
	LSB of product

MBR : Memory BUffer register
	Contains a word to be read/stored in memory or I/O

MAR : Memory Adress register
	Specifies the address in memory of the word to be written/read into MBR

PC  : Program Counter
	Holds the next instruction’s address

Instructions being performed by the IAS Architecture:
    LOAD M(X)              
    ADD M(X)             
    SUB M(X)              
    LSH                   
    RSH               
    STOR M(X)        
    LOAD M(Q) M(X)     
    LOAD M(Q)                          
    DIV M(X)              
    JUMP M(X,20:39)         
    NOP---> DENOTED BY 0
---------------------NOTE: This architecture does not handle negative inputs and floating point values.-----------------------------------------------
1. PERIMETER OF RECTANGLE
    LOAD M(X) ADD M(X)
    LSH STOR M(X)
2. SEMI-PERIMETER OF TRIANGLE i.e. s=(a+b+c)/2 
    LOAD M(X) ADD M(X)
    ADD M(X) RSH M(X)
    STOR M(X)-------->If only oneinstruction is present it is treated as RIGHT HAND INSTRUCTION and NOP(no operation)is assigned to LEFT HAND INSTRUCTION.
3. 3x3 MATRIX ADDITION
    For both the matrices,the following operations are being executed times
    LOAD M(X) ADD M(X)
    STOR M(X)
4. SUBTRACT TWO NUMBERS : NUM1-NUM2
    LOAD M(X) SUB M(X)
    STOR M(X)
5. AVERAGE OF 6 POSITIVE NUMBERS
    LOAD M(X) ADD M(X)
    ADD M(X) ADD M(X)
    ADD M(X) ADD M(X)
    STOR M(X) LOAD M(Q) M(X)
    DIV M(X) LOAD M(Q)
    STOR M(X)
6. kth MULTIPLE OF NUMBER 
    LOAD M(X) ADD M(X)
    (k-2) times JUMP M(X,20:39)
    STOR M(X)
0. To STOP the program
--------------------------------------------------------------------
Storing data from 100th memory location
Storing result from 200th memory location
Storing program counter from 1st memory location
Storing extra memory from 300th memory location
M=[0]*1000  #Memory
MAR=0       #MEMORY ADDRESS REGISTER
MBR=''      #MEMORY BUFFER REGISTER
IBR=''      #INSTRUCTION BUFFER REGISTER
IR=''       #INSTRUCTION REGISTER
AC=0        #ACCUMULATOR
PC=1        #PROGRAM COUNTER
MQ=0        #MULTIPLIER/QUOTIENT
extra=300   #EXTRA MEMORY

'''
Storing data from 100th memory location
Storing result from 200th memory location
Storing program counter from 1st memory location
Storing extra memory from 300th memory location
'''

'''

    OPERATION        DECIMAL_DENOTION       OPCODE
-------------------------------------------------------    
    LOAD M(X)                1             00000001
    ADD M(X)                 5             00000101
    SUB M(X)                 6             00000110
    LSH                     20             00010100
    RSH                     21             00010101
    STOR M(X)               33             00100001
    LOAD M(Q) M(X)           9             00001001
    LOAD M(Q)               10             00001010              
    DIV M(X)                12             00001100
    JUMP M(X,20:39)         14             00001110
    NOP                      0             00000000

'''
#----------------------------------------------ASSEMBLER-----------------------------------------------
#function that returns 8 bit binary opcode
def binary_opcode(b):
    binary=bin(b).zfill(8)
    s=str(binary)
    s=s.replace('b','0')
    return s
#function that returns 12 bit binary address
def binary_address(ad):
    bin_ad=bin(ad).zfill(12)
    s=str(bin_ad)
    s=s.replace('b','0')
    return s
#function that returns 40 bit binary instruction
def binary_40bit_instruction(op1,ad1,op2,ad2):
    s=binary_opcode(op1)+binary_address(ad1)+binary_opcode(op2)+binary_address(ad2)
    return s
#function that returns 40 bit binary data
def binary_data(d):
    bin_data=bin(d).zfill(40)
    s=str(bin_data)
    s=s.replace('b','0')
    return s
#------------------------------------------------------------------------------------------------------
#execute cycle
def execute():
    global extra  #extra memory
    global MAR    #Memory Address Register
    global MBR    #Memory Buffer Register
    global IBR    #Instruction Buffer Register
    global IR     #Instruction Register
    global AC     #Accumulator
    global PC     #Program Counter
    global MQ     #Multiplier/Quotient
    #STOR
    if(IR=='00100001'):    
        if(AC>=0):
            MBR=binary_data(AC)
        else:
            MBR='1'+binary_data(AC)[1:]     #handling negative numbers
        M[int(MAR,2)]=MBR
        print("MBR : ",MBR)
        print("AC  : ",AC)   
        print("--------------------------------------------------")
        print("FINAL ANSWER : ",int(MBR,2))
        #exit()
    #LOAD
    if(IR=='00000001'):
        MBR=M[int(MAR,2)]   
        AC=int(MBR,2)
    #ADD
    if(IR=='00000101'):
        MBR=M[int(MAR,2)]  
        AC=AC+int(MBR,2)
    #SUB
    if(IR=='00000110'):
        MBR=M[int(MAR,2)]  
        AC=AC-int(MBR,2)
    #LSH
    if(IR=='00010100'):
        MBR=M[int(MAR,2)]     
        AC=AC<<1
    #RSH
    if(IR=='00010101'):
        MBR=M[int(MAR,2)]     
        AC=AC>>1    
    #LOAD M(Q) M(X)
    if(IR=='00001001'):
        MBR=M[int(MAR,2)]   
        MQ=int(MBR,2)
    #DIV M(X)
    if(IR=='00001100'):
        MBR=M[int(MAR,2)]
        AC=MQ%int(MBR,2)
        MQ=MQ//int(MBR,2)
    #LOAD M(Q)
    if(IR=='00001010'):
        AC=MQ
    #JUMP M(X,20:39}
    if(IR=='00001110'):
        MBR=M[int(MAR,2)]  
        AC=AC+int(MBR,2)

    print("MBR : ",MBR)
    print("MQ  : ",MQ)
    print("AC  : ",AC)    
#fetch and decode cycle
def fetch_decode():
    global extra
    global MAR
    global MBR
    global IBR
    global IR
    global AC
    global PC
    print("PC  : ",PC)
    MAR=PC   
    print("MAR : ",MAR)      
    M[extra]=MAR
    extra+=1
    MBR=M[MAR] #40 BIT INSTRUCTION
    print("MBR : ",MBR)
    IBR=MBR[20:40]   #RIGHT HAND INSTRUCTION
    print("IBR : ",IBR)
    if(MBR[0:8]!='00000000'):  
        IR=MBR[0:8]   #OPCODE
        print("IR  : ",IR)
        MAR=MBR[8:20]  #ADDRESS
        print("MAR : ",MAR)
        M[extra]=MAR
        extra+=1
        execute()
        IR=IBR[0:8]   #OPCODE OF LEFT HAND INSTRUCTION
        print("IR  : ",IR)
        MAR=IBR[8:20]   #ADDRESS OF LEFT HAND INSTRUCTION
        print("MAR : ",MAR)
        M[extra]=MAR
        extra+=1
        execute()
    else:
        IR=IBR[0:8]   #OPCODE OF RIGHT HAND INSTRUCTION
        print("IR  : ",IR)
        MAR=IBR[8:20]       #ADDRESS OF RIGHT HAND INSTRUCTION
        print("MAR : ",MAR)
        M[extra]=MAR
        extra+=1
        execute()

# MAIN
while(1):    
    print("ENTER YOUR CHOICE :1 / 2 / 3 / 4 / 5 / 6")
    print("1 PERIMETER OF RECTANGLE")
    print("2 SEMI-PERIMETER OF TRIANGLE i.e. s=(a+b+c)/2   { NOTE : This operation will give integer result only since ias architecture did not have floating point values.It will round down the decimal value. }")
    print("3 3x3 MATRIX ADDITION")
    print("4 SUBTRACT TWO NUMBERS : NUM1-NUM2")
    print("5 AVERAGE OF 6 POSITIVE NUMBERS")
    print("6 kth MULTIPLE OF NUMBER n")
    print("Enter 0 to STOP the program")
    choice=int(input())
    if(choice==0):
        exit()
    elif(choice==1):
        l=int(input("ENTER LENGTH OF RECTANGLE : "))
        b=int(input("ENTER BREADTH OF RECTANGLE : "))
        M[100]=binary_data(l)
        M[101]=binary_data(b)
        M[PC]=binary_40bit_instruction(1,100,5,101)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(20,0,33,200)
        fetch_decode()
        print("--------------------------------------------------")
    elif(choice==2):
        a=int(input("ENTER SIDE 1 OF TRIANGLE : "))
        b=int(input("ENTER SIDE 2 OF TRIANGLE : "))
        c=int(input("ENTER SIDE 3 OF TRIANGLE : "))
        M[100]=binary_data(a)
        M[101]=binary_data(b)
        M[102]=binary_data(c)
        M[PC]=binary_40bit_instruction(1,100,5,101)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(5,102,21,0)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(0,0,33,200)
        fetch_decode()
        print("--------------------------------------------------")
    elif(choice==3):
        store=200
        print("ENTER ELEMENTS OF 1st MATRIX ROW-WISE")
        ind_1=100
        ind_2=110
        for i in range(0,9):
            inp=int(input(f"ENTER ELEMENT {i+1} : "))
            M[ind_1]=binary_data(inp)
            ind_1+=1
        print("ENTER ELEMENTS OF 2nd MATRIX ROW-WISE")
        for i in range(0,9):
            inp=int(input(f"ENTER ELEMENT {i+1} : "))
            M[ind_2]=binary_data(inp)
            ind_2+=1
        ind_1=100
        ind_2=110
        for i in range(0,9):
            print(f"CALCULATING ELEMENT {i+1} OF RESULTANT MATRIX")
            M[PC]=binary_40bit_instruction(1,ind_1,5,ind_2)
            fetch_decode()
            ind_1+=1
            ind_2+=1
            print("-------------------")
            PC+=1
            M[PC]=binary_40bit_instruction(0,0,33,store)
            fetch_decode()
            print("--------------------------------------------------")
            store+=1
            PC+=1
        matrix_sum=[[int(M[200],2),int(M[201],2),int(M[202],2)],[int(M[203],2),int(M[204],2),int(M[205],2)],[int(M[206],2),int(M[207],2),int(M[208],2)]]
        for m in matrix_sum:
            print(m)
    elif(choice==4):
        a=int(input("ENTER NUMBER 1  : "))
        b=int(input("ENTER NUMBER 2  : "))
        M[100]=binary_data(a)
        M[101]=binary_data(b)
        M[PC]=binary_40bit_instruction(1,100,6,101)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(0,0,33,200)
        fetch_decode()
        print("--------------------------------------------------")
    elif(choice==5):
        a=int(input("ENTER NUMBER 1  : "))
        b=int(input("ENTER NUMBER 2  : "))
        c=int(input("ENTER NUMBER 3  : "))
        d=int(input("ENTER NUMBER 4  : "))
        e=int(input("ENTER NUMBER 5  : "))
        f=int(input("ENTER NUMBER 6  : "))
        M[100]=binary_data(a)
        M[101]=binary_data(b)
        M[102]=binary_data(c)
        M[103]=binary_data(d)
        M[104]=binary_data(e)
        M[105]=binary_data(f)
        M[106]=binary_data(6)
        M[PC]=binary_40bit_instruction(1,100,5,101)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(5,102,5,103)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(5,104,5,105)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(33,200,9,200)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(12,106,10,0)
        fetch_decode()
        print("--------------------------------------------------")
        PC+=1
        M[PC]=binary_40bit_instruction(0,0,33,201)
        fetch_decode()
        print("--------------------------------------------------")
    elif(choice==6):
        n=int(input("ENTER NUMBER n : "))
        k=int(input("ENTER NUMBER k : "))
        M[100]=binary_data(n)
        PC=1
        M[1]=binary_40bit_instruction(1,100,5,100)
        fetch_decode()
        print("--------------------------------------------------")
    
        for a in range(0,k-2):
            PC+=1
            M[PC]=binary_40bit_instruction(0,0,14,100)
            fetch_decode()
            print("--------------------------------------------------")
            PC=1
        PC+=2
        M[PC]=binary_40bit_instruction(0,0,33,200)
        fetch_decode()
        print("--------------------------------------------------")
        


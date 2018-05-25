a0=int(input())
a1=int(input())
a2=int(input())
b0=int(input())
b1=int(input())
b2=int(input())

A=0
B=0

if(a0>b0):
    A=A+1
if(a0<b0):
    B=B+1
    
if(a1>b1):
    A=A+1
if(a1<b1):
    B=B+1
    
if(a2>b2):
    A=A+1
if(a2<b2):
    B=B+1
    
print(A, B)
    
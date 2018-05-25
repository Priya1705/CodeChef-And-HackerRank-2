#pattern 
#incomplete

n=int(input())
for i in range(n):
    for j in range(n-1,0, -1):
        if(i+j>=n):
            print("*")
        else:
            print(" ")
    print(" ")    
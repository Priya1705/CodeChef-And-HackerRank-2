n=int(input())
arr = list(map(int, input().strip().split(' ')))
p=0
ne=0
z=0
for i in range(n):
    if(arr[i]>0):
        p+=1
    elif(arr[i]<0):
        ne+=1
    else:
        z+=1

print(str.format('{0:.6f}', p/n)) 
print(str.format('{0:.6f}',ne/n))
print(str.format('{0:.6f}',z/n))
        


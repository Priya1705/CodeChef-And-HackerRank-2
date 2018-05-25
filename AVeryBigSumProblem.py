n=int(input())
arr=list()
sum=0
for i in range(n):
    arr.append(input())
for i in range(n):
    sum+=int(arr[i])
print(sum)
    
#ar = list(map(int, input().strip().split(' ')))
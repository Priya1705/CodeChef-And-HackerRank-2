n=int(input())
m=int(input())
S=list()
M=list()
for i in range(m):
    M.append(int(0))
for i in range(n):
    S.append(int(input()))
for j in range(m):
    for i in range(n):
        if S[i]==j:
            M[j]=M[j]+1
for i in range(m):
    print(M[i])
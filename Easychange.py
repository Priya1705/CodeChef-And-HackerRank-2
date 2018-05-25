t=int(input())
a=[20,50,100,200,500,1000]
for i in range(t):
    c=int(input())
    p=int(input())
    count=0
    x=p-c
    
    #equal
    if x==0:
        print("0")
        count+=1
        
    #if present
    if count==0:
        if x in a:
            print("0")
            count+=1
     
    #multiple
    if count==0:
        for j in range(6):
            if x%a[j]==0:
                print("0")
                count+=1
        
    #normal
    if count==0:
        for j in range(6):
            k=0
            while a[k]<c:
                k=k+1
            else:
                y=a[k-1]
        #print(y)
        if y-x >9:
            print("-1")
        else:
            print(y-x)
        

        

    
            
    
    

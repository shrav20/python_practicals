#sort array in Ascending order

arr=list(map(int,input().split()))
n=[]
temp=0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i] > arr[j]):    
            temp = arr[i]  
            arr[i] = arr[j]      # swapping the elements
            arr[j] = temp

print(arr)

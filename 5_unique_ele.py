 #Program to Unique number of elements

print("Enter list elements: ")
li=list(map(int,input().split()))
x=len(set(li))
print(x)

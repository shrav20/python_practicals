# Program to print largest and smallest element in an array
l=list(map(int,input("Enter a list: ").split()))
length=len(l)
min=l[0]
max=l[0]
for i in l:
    if i<min:
        min=i
    if i>max:
        max=i

print("The largest element in array is ",max)
print("The smallest element in array is ",min)

d={}
for i in range(10):
    Name=input("Enter Name: ")
    Num=input("Enter Number: ")
    d[Name]=Num
print(d)
print()
N1=input("Enter Name To Find: ")
if N1 in d:
    print(N1,":",d[N1])
else:
    print("Name Not Found")
    
N2=input("Enter Name To Replace: ")
if N2 in d:
    val=input("Enter New Number: ")
    d[N2]=val
else:
    print("Name Not Found")

N3=input("Enter Name To be Deleted: ")
if N3 in d:
    del d[N3]
else:
    print("Name Not Found")

#difference of two lists
n=int(input("enter the length of both lists"))
print("enter list1")
li1=[]
for _ in range(n):
    li1.append(list(map(int,input().split())))
print("enter list2")
li2=[]
for _ in range(n):
    li2.append(list(map(int,input().split())))
final=[]
print("li1-li2 is ")
for i in li1:
    if i not in li2:
        final.append(i)
        
print(final)

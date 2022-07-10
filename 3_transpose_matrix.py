# Program to find transpose of matrix
l=eval(input("Enter a 2-D list"))
print("The given matrix is: ")
for i in l:
    for j in i:
        print(j,end=' ')
    print()
print("Transpose of the above matrix is: ")
rows=len(l)
cols=len(l[0])
for i in range(rows):
    for j in range(cols):
        print(l[j][i],end=' ')
    print()

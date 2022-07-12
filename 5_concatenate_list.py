#Write a python program which concatenenate 2 lists
#if L1=[p,q] L2=[1,2,3,4] O/P:- p1 p2 p3 p4 q1 q2 q3 q4
N=int(input("Enter Number---> "))
y=1
L1=['p','q']
final=[]
while y<N+1:
    for x in L1:    
        final.append(('{}{}'.format(x,y)))
    y+=1
print(final)

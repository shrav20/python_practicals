a=[[12,7],
    [4,5],
    [3,8]]

r= [[0,0,0],
    [0,0,0]]
row=len(a)
col=len(a[0])

for i in range(row):
    for j in range(col):
        r[j][i] = a[i][j]

for i in r:
    print(i)

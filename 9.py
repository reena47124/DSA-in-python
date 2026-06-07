#matrix
#another way to transpose a matrix
a=[[1,8,3],[2,9,7],[5,0,7]]
rows=len(a)
cols=len(a[0])
tr=[[0 for j in range(cols)] for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        tr[j][i]=a[i][j]
print(tr)        

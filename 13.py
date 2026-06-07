#matrix
#addition of 2 matrices.
a=[[1,2,3],[7,8,9],[4,5,6]]
b=[[3,4,5],[0,9,8],[1,6,0]]
rows=len(a)
cols=len(a[0])
c=[[0 for j in range(cols)] for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        c[i][j]=a[i][j]+b[i][j]
print(c)        

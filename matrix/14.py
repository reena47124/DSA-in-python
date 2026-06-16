#matrix
#subtraction of 2 matrices
a=[[6,8,3,7],[5,9,0,3],[12,8,56,0]]
b=[[1,2,3,4],[3,4,5,6],[0,3,7,6]]
rows=len(a)
cols=len(a[0])
c=[[0 for j in range(cols)]for i in range(rows)]
for i in range(rows):
    for j in range(cols):
        c[i][j]=a[i][j]-b[i][j]
print(c)        
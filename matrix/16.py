#matrix
#sort the matrix in strict order.
a=[[5,4,7],[1,3,8],[2,9,6]]
rows=len(a)
cols=len(a[0])
x=[]
for i in range(rows):
    for j in range(cols):
        x.append(a[i][j])
x.sort()
k=0
for i in range(rows):
    for j in range(cols):
        a[i][j]=x[k]
        k+=1
for i in range(rows):
    for j in range(cols):
        print(a[i][j],end=" ")
    print()                 

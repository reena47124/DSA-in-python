#matrix
#sort the matrix column-wise
a=[[1,8,3],[2,9,7],[9,5,4]]
rows=len(a)
cols=len(a[0])
for j in range(cols):
    column=[]
    for i in range(rows):
        column.append(a[i][j])
    column.sort()
    for i in range(rows):
        a[i][j]=column[i] 
print(a)           
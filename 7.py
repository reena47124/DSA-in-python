#matrix
#transpose a matrix
a=[[1,2,3,4],[5,6,7,8]]
rows=len(a)
cols=len(a[0])
tr=[]
for j in range(cols):
    column=[]
    for i in range(rows):
        column.append(a[i][j])
    tr.append(column)
print(f"transpose matrix is:{tr}")
    
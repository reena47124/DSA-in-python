#matrix
#column-wise traversal
a=[[1,8,3],[2,9,7],[5,0,7]]
rows=len(a)
cols=len(a[0])
for j in range(cols):
    for i in range(rows):
        print(a[i][j],end=" ")
    print()    
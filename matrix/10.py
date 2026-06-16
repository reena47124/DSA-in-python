#matrix
#print a matrix
a=[[1,8,3],[2,9,7],[5,0,7]]
rows=len(a)
cols=len(a[0])
for i in range(rows):
    for j in range(cols):
        print(a[i][j],end=" ")
    print()    
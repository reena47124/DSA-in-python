#matrix
#multiplication of 2 matrices
a=[[1,2,3],[4,5,6]]
b=[[7,8],[9,10],[11,12]]
rows_a=len(a)
cols_a=len(a[0])
rows_b=len(b)
cols_b=len(b[0])
product=[[0 for j in range(cols_b)] for i in range(rows_a)]
for i in range(rows_a):
    for j in range(cols_b):
        for k in range(cols_a):
            product[i][j]+=a[i][k]*b[k][j]
print(product)            
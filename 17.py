#matrix
#find determinant of matrix
def determinant(mat):
    n=len(mat)

    if n==1:
        return mat[0][0]
    
    if n==2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    
    det=0
    for col in range(n):
        minor=[]
        for row in range(1,n):
            temp=mat[row][:col]+mat[row][col+1:]
            minor.append(temp)
        det+=((-1)**col)*mat[0][col]*determinant(minor)
    return det

a=[[1,2,3],[4,5,6],[7,8,10]]
print(determinant(a))


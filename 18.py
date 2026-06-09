#matrix
#find the adjoint of a matrix
def determinant(mat):
    n=len(mat)

    if n==1:
        return mat[0][0]
    
    if n==2:
        return mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    
    det=0
    for col in range(n):
        minor=[]
        for row in range(n):
            temp=mat[row][:col]+mat[row][col+1:]
            minor.append(temp)
        det+=((-1)**col)*mat[0][col]*determinant(minor) 
    return det
    
def adjoint(mat):
    n=len(mat)
    cofactor=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            minor=[]
            for row in range(n):
                if row==i:
                    continue
                temp=[]
                for col in range(n):
                    if col!=j:
                        temp.append(mat[row][col])
                minor.append(temp)
            cofactor[i][j]=((-1)**(i+j))*determinant(minor)
    adj=[[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            adj[j][i]=cofactor[i][j]

    return adj

a=[[1,2,3],[4,5,6],[7,8,10]]
print(adjoint(a))



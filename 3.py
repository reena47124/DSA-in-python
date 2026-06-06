#matrix
#search in a matrix
arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
x=int(input("enter the value of x:"))
rows,cols=len(arr),len(arr[0])
for i in range(rows):
    for j in range(cols):
        if arr[i][j]==x:
            print(f"{x} is present at {i}th row and {j}th column")
            break



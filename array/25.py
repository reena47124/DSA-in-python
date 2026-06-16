#array
#modifying elements in an array
a=[1,2,3,4,5]
n=len(a)
for i in range(n):
    a[i]+=5
print("modified array:",end="") 
for i in range(n):
    print(a[i],end=" ")
       
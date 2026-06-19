#array
#reverse the array,naive approach
a=[1,2,3,4,5]
n=len(a)
b=[]
for i in range(n-1,-1,-1):
    b.append(a[i])
print(b)    
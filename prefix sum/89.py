#prefix sum
#equilibrium index,naive approach
def equi_index(a):
    n=len(a)
    for i in range(n):
        sum1=0
        sum2=0
        for j in range(0,i):
            sum1+=a[j]
        for j in range(i+1,n):
            sum2+=a[j]
        if sum1==sum2:
            return i
    return -1
a=[-7,1,5,2,-4,3,0]
print(equi_index(a))
b=[1,1,1,1] 
print(equi_index(b))           
   
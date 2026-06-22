#two-pointers
#move all zeros to the end of the array,naive approach
def move_zeros(a):
    n=len(a)
    i=0
    while i<n:
        if a[i]==0:
            for j in range(i+1,n):
                a[j-1]=a[j]
            a[n-1]=0
            n=n-1
        else:
            i+=1    
    return a
a=[1,2,0,4,3,0,5,0]
print(move_zeros(a))
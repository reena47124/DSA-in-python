#two-pointer
#move all zeros to the end,two-pointer method
def move_zeros(a):
    n=len(a)
    pos=0
    for i in range(n):
        if a[i]!=0:
            a[pos],a[i]=a[i],a[pos]
            pos+=1
    return a
a=[1,2,0,4,3,0,5,0]
print(move_zeros(a))
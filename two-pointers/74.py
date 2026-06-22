#two-pointer
#remove duplicates from a sorted array,two-pointer technique
def remove_dup(a):
    n=len(a)
    if n==0:
        return n
    pos=1
    for i in range(1,n):
        if a[i]!=a[i-1]:
            a[pos]=a[i]
            pos+=1
    return pos
a=[1,2,2,3,4,4,4,5,5]
new_length=remove_dup(a)
print(f"new array:{a[:new_length]}")        

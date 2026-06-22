#two-pointer
#remove all occurrences of an element in an array,two-pointer approach
def remove_ele(a,ele):
    n=len(a)
    pos=0
    for i in range(n):
        if a[i]!=ele:
            a[pos]=a[i]
            pos+=1
    return pos
a=[0,1,3,0,2,2,4,2]
ele=2
new_length=remove_ele(a,ele)
print(f"new lenth:{new_length}")
print(f"new array:{a[:new_length]}")        
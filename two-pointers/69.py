#two-pointer
#remove all occurrences of an element in an array,naive approach
def remove_ele(a,ele):
    n=len(a)
    count=0
    for i in range(n):
        if a[i]!=ele:
            print(a[i])
            count+=1
    return count
a=[0,1,3,0,2,2,4,2]
ele=2
print("total number after removal",remove_ele(a,ele))

#two-pointer
#remove duplicates from a sorted array
def remove_dup(a):
    seen=set()
    for i in range(len(a)):
        if a[i] not in seen:
            seen.add(a[i])
    return list(seen)
a=[1,2,2,3,4,4,4,5,5]
print(remove_dup(a))        
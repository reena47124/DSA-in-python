#array
#binary search
a=[2,5,8,10,12,16,18,33,45,65,98,102]
key=65
low=0
high=(len(a)-1)
found=False
while low<=high:
    mid=(low+high)//2
    if a[mid]==key:
        print(f"element found at {mid}")
        found=True
        break
    elif a[mid]<key:
        low=mid+1
    else:
        high=mid-1
if found:
    print("found")
else:
    print(f"doesnt exist,-1")                    

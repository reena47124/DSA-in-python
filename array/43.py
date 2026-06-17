#array
#check if an array is sorted
a=[1,2,3,3,4,5,5,6,7]
result=True
for i in range(1,len(a)):
    if a[i]<a[i-1]:
        result=False
        break
if result:
    print(f"sorted") 
else:
    print(f"not sorted")           
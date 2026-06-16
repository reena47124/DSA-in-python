#array
#searching element in an array
a=[1,2,3,4,5,6,7]
target=5
found=False
n=len(a)
for i in range(n):
    if a[i]==target:
        found=True
        break
if found:
    print("element found!")
else:
    print("element doesnt find")
            
#array
#delete an element from the end of an array,using built-in method.
a=[1,2,3,4,5,6,7]
print("array before deletion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")
print()
a.pop()
print("array after the deletion:",end="")
for i in range(len(a)):
    print(a[i],end=" ")    
#sorting
#bubble sort
def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[5,6,1,3,2,4,8,0]
print(bubble_sort(a))
            
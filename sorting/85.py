#sorting
#selection sort
def selection_sort(a):
    n=len(a)
    for i in range(n):
        mini=i
        for j in range(i+1,n):
            if a[j]<a[mini]:
                mini=j
        a[i],a[mini]=a[mini],a[i]
    return a
a=[64,25,12,22,11]
print(selection_sort(a))            
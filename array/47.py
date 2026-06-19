#array
#check if an array is sorted or not,using built-in method.
def is_sorted(a):
    return a==sorted(a)
a=[1,3,4,56,78,90]
if is_sorted(a):
    print("true")
else:
    print("false")    
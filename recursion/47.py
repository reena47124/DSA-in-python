#recursion
#print upward right angle triangle with stars.
def fun(n):
    if n>1:
        fun(n-1)
    for i in range(n):
        print("*",end=" ")
    print()
fun(5)            
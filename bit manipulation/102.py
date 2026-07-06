#bit manipulation
#compute XOR from 1 to n,brute force approach
def compute_XOR(n):
    result=0
    for i in range(1,n+1):
        result=result^i
    return result
print(compute_XOR(7))
print(compute_XOR(5))
    
#two-pointer
#reverse a string without altering the position of the space,two-pointer approach
def reverse_string(s):
    chars=[ch for ch in s if ch!=' ']
    j=len(chars)-1
    result=[]
    for ch in s:
        if ch==' ':
            result.append(' ')
        else:
            result.append(chars[j])
            j-=1
    return ''.join(result) 
s="hello there!!!" 
print(reverse_string(s))



#bit manipulation
#checking if the bit at nth position is set or unset.
num=5
pos=0
bit=num&(1<<pos)
if bit==1:
    print(f"bit at {pos}th position is SET that is:{bit}")
else:
    print(f"bit at {pos}th position is UNSET that is:{bit}")

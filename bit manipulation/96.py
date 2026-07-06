#bit manipulation 
#unset a bit at nth position in the number
num=7
pos=1
num=num&(~(1<<pos))
print(f"unset number:{num}")
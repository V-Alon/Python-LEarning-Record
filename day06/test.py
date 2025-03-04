for i in range(8):
    if i % 2!=1:
        continue
    else:
        print(i, end=".")
print()
print('*'*30)
for i in range(-3,4):
    if i<0:
        print(' '*(-i)+'*'*(4+i))
    elif i>0:
        print(' '*3+'*'*(4-i))
    else:
        print('*'*7)
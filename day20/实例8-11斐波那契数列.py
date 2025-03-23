def fbnq(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fbnq(n - 1)+fbnq(n-2)#自己调用自己
print(fbnq(9))#第九位
for i in range(1,10):
    print(fbnq(i))
print()
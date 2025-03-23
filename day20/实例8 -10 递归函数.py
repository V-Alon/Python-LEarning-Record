def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)#自己调用自己
print(fac(5))
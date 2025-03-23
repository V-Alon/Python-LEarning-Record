import random
def getmax(lst):
    x=lst[0]
    for i in range(1,len(lst)):
        if lst[i]>x:
            x=lst[i]
    return x


lst=[ random.randint(1,100) for item  in range(10)]
print(getmax(lst))
print(lst)
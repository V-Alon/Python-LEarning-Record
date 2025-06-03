import re
pattern='\\day86\\.\\day86+'
s='I study python3.12 everday python I love you'
matche=re.search(pattern,s)


s2='4.10 python I study everday'
s3='I study python everday'
matche2=re.search(pattern,s2)
matche3=re.search(pattern,s3)
print(matche)
print(matche2)
print(matche3)

print(matche.group())
print(matche2.group())




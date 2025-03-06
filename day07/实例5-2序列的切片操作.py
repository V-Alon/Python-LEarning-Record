s='HelloWorld'
#切片操作
s1=s[0:5:2]#索引从0开始，到5结束（不包含5）步长为2，
            # 相当于取字符串第1，3，5个字符
print(s1)
#省略开始位置，start从0开始
print(s[:5:1])#hello
print(s[0:5:2])#hlo
#省略开始位置start，省略步长step
print(s[0:5:])#hello,默认步长为1
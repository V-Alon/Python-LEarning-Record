s=0#存储累加和
i=1#初始化变量
while i<11:#条件判断
    #语句块
    s+=i
    if s>20:
        print('累加和大于20当前数字是',i)
        break
    i+=1#改变变量

print('-'*28)
i=0
while i<3:
    user_name=input('请输入用户名')
    pwd=input('请输入密码')
    if user_name=='admin' and pwd=='123456':
        print('正在登陆')
        print('登陆成功')
        break
    else:
        if i<2:
            print('用户名或者密码不正确，还有',2-i,"次机会")
    i+=1
else:
    print('三次全错了')
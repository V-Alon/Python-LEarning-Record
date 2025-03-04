for i in 'hello':
    if i == 'o':
        break
    print(i)
print('-'*50)
for i in range(3):
    user_name = input('请输入用户名')
    pwd = input('请输入密码')
    if user_name == 'admin' and pwd == '123456':
        print('正在登陆','...'*10)
        print('登陆成功')
        break
    else:
        if i < 2:
            print('用户名或者密码不正确，还有', 2 - i, "次机会")
else:
    print('三次全错了')

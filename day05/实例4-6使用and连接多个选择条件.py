user_name=input('请输入你的用户名')
pwd=input('请输入密码')
if user_name=='admin' and pwd=='123456':
    print('登陆成功')
else:
    print('登录失败，重新输入用户名和密码')
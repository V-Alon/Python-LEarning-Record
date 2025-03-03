#初始化变量
import sys

i=0
#条件判断
while i<3:#条件判断0 1 2
    #语句块
    user_name=input('请输入用户名')
    pwd=input('请输入密码')
    #登录操作
    if user_name=='admin' and pwd=='123455':
        print('登录中')
        print('登陆成功')
        i=8#在第三行判断i小于3,8<3 ，false退出循环
    else:
        if i<2:
            print('用户名或者密码不正确，你还有',2-i,'次机会')
        i=i+1#改变变量
if i==3:
    print('对不起，三级机会用完了')
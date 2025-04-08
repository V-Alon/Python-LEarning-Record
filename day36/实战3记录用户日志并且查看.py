import time
def show_info():
    print('输入提示数字，执行相应的操作，0:退出，1:查看登录日志')

def write_loginfo(username):
    with open('logs.txt', 'a', encoding='utf-8') as file:
        s=f'用户名:{username},登录时间:{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}'
        file.write(s)

def raed_loginfo():
    with open('logs.txt', 'r', encoding='utf-8') as file:
        while True:
            line = ''
            line = file.readline()
            if line=='':
                break
            else:
                print(line)


if __name__ == '__main__':
    # write_loginfo('admin')
    username=input('请输入用户名:')
    pwd=input('请输入密码:')
    if username=='admin' and pwd=='admin':
        print('success')

        #
        write_loginfo(username)
        show_info()
        num=eval(input('请输入要操作的数字:'))
        while True:
            if num==0:
                print('退出成功')
                break
            elif num==1:
                print('查看登录日志')
                raed_loginfo()
                show_info()
            else:
                print('error')
                show_info()
            num=eval(input('请输入要操作的数字:'))

    else:
        print('用户名或者密码不正确')
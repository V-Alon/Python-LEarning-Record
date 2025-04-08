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
            

if __name__ == '__main__':
    write_loginfo('admin')
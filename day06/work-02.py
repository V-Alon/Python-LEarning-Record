#实现10086的功能，查询话费，查询剩余通话时长，查询剩余流量，退出
answer='y'
while answer=='y':
    print('欢迎使用查询功能')
    print('1.查询当前余额')
    print('2.查询剩余流量')
    print('3.查询剩余通话时长')
    print('0.退出')
    choice=input('请输入需要的操作')
    if choice=='1':
        print('当前余额是100元')
    elif choice=='2':
        print('当前剩余流量有100GB')
    elif choice=='3':
        print('当前剩余通话时长还有200分钟')
    elif choice=='0':
        break
    else:
        print('请在0——3之间选择')
    answer=input('还要继续查询么，y/n?')
else:
    print('程序退出，谢谢使用')
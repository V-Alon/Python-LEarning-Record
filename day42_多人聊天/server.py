#coding:utf-8
import threading
import time
from socket import socket,AF_INET,SOCK_STREAM
from threading import main_thread

import wx
class KkServer(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,id=1002,title="V-Alon服务器端界面",pos=wx.DefaultPosition,size=wx.Size(400,450))
        #
        pl=wx.Panel(self)
        #
        box=wx.BoxSizer(wx.VERTICAL)
        # 可伸缩的网格布局
        fgz1 = wx.FlexGridSizer(wx.HSCROLL)

        start_server_btn=wx.Button(pl,size=wx.Size(133,40),label='启动服务')
        record_btn=wx.Button(pl,size=wx.Size(133,40),label='保存聊天记录')
        stop_server_btn=wx.Button(pl,size=wx.Size(133,40),label='停止服务')

        #
        fgz1.Add(start_server_btn,1,wx.TOP)
        fgz1.Add(record_btn,1,wx.TOP)
        fgz1.Add(stop_server_btn,1,wx.TOP)

        #
        box.Add(fgz1,1,wx.ALIGN_CENTER)

        # 只读文本框
        self.show_text = wx.TextCtrl(pl, size=wx.Size(400, 410), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.show_text, 1, wx.ALIGN_CENTER)
        #
        pl.SetSizer(box)
        '''------------------------以上的代码都是界面绘制的代码----------------------'''
        '''服务器功能实现必要属性'''
        self.isOn=False#服务器启动状态，默认为0，没有启动
        # 服务器绑定的ip和端口号
        self.host_port=('',8888)#空字符串代表本机所以的IP
        #创建socket对象
        self.server_socket=socket(AF_INET,SOCK_STREAM)
        #绑定IP和端口号
        self.server_socket.bind(self.host_port)
        #监听
        self.server_socket.listen(5)
        #创建字典存储客户端对话线程
        self.session_thread_dict={}#key-value{客户端的名称key:会话线程:value}

        #当鼠标点击按钮执行的操作
        self.Bind(wx.EVT_BUTTON,self.start_server,start_server_btn)


    def start_server(self,event):
        #判断服务器是否已经启动
        if not self.isOn:
            #启动服务器
            self.isOn=True
            #创建主线程对象
            main_thread=threading.Thread(target=self.do_work)
            #设置为守护线程
            main_thread.daemon=True
            #启动主线程
            main_thread.start()


    def do_work(self):
        #判断isOn的值
        while self.isOn:
            #接收客户端链接请求
            session_socket,client_addr=self.server_socket.accept()
            #客户端发送请求之后，发送过来的第一条数据为客户端的名称
            user_name=session_socket.recv(1024).decode('utf-8')
            #创建会话线程
            sesstion_thread=SesstionThread(session_socket,user_name,self)
            #存储在字典中
            self.session_thread_dict[user_name]=sesstion_thread
            #启动会话线程
            sesstion_thread.start()
            #输出服务器的提示信息
            self.show_info_and_show_client('服务器通知',f'欢迎{user_name}进入聊天群！',time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #当self.isOn的值为False的时候，执行关闭socket对象
        self.server_socket.close()

    def show_info_and_show_client(self,data_source,data,date_time):
        #字符串的拼接
        send_data=f'{data_source}:{data}\n时间:{date_time}'
        #只读文本框
        self.show_text.AppendText('-'*40+'\n'+send_data+'\n')
        #每个客户端都发送一次
        for  client in self.session_thread_dict.values():
            #如果当前的会话是开启状态
            if client.isOn:
                client.client_socket.send(send_data.encode('utf-8'))



#服务器 端 会话线程的类

class SesstionThread(threading.Thread):
    def __init__(self,client_socket,user_name,server):
        #调用父类的方法
        threading.Thread.__init__(self)
        self.client_socket=client_socket
        self.user_name=user_name
        self.server=server
        self.isOn=True#会话线程是否启动


    def run(self)->None:
        print(f'客户端:{self.user_name}已经和服务器连接成功，服务器启动一个会话线程')
        while self.isOn:
            data=self.client_socket.recv(1024).decode('utf-8')
            if data=='K-disconnect-K':
                self.isOn=False
            else:
                self.server.show_info_and_show_client(self.user_name,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        #
        self.client_socket.close()

if __name__ == '__main__':
    # 初始化app
    app = wx.App()
    # 创建自己的服务器端界面对象
    client = KkServer()
    client.Show()

    app.MainLoop()

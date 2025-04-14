#coding:utf-8
import threading
from socket import socket,AF_INET,SOCK_STREAM

import wx
class KkClient(wx.Frame):
    def __init__(self, client_name):
        #调用父类的初始化方法
        #None没有父级窗口
        #id表示当前窗口的编号
        #pos：窗体的打开位置
        #size：窗体的大小，单位是像素，400宽，500高度
        wx.Frame.__init__(self,None,id=1001,title=client_name+"的客户端界面",pos=wx.DefaultPosition,size=wx.Size(400,500))
        #创建面板对象
        pl=wx.Panel(self)
        #在面板上放上盒子
        box=wx.BoxSizer(wx.VERTICAL)
        #可伸缩的网格布局
        fgz1=wx.FlexGridSizer(wx.HSCROLL)

        #创建两个按钮
        conn_btn=wx.Button(pl,size=wx.Size(200,40),label='连接')
        dis_conn_btn=wx.Button(pl,size=wx.Size(200,40),label='断开')

        #把两个按钮放到可伸缩的网格布局
        fgz1.Add(conn_btn,1,wx.TOP|wx.LEFT)
        fgz1.Add(dis_conn_btn,1,wx.TOP|wx.RIGHT)
        #可伸缩的网格布局添加到box
        box.Add(fgz1,1,wx.ALIGN_RIGHT)

        #只读文本框
        self.show_text=wx.TextCtrl(pl,size=wx.Size(400,210),style=wx.TE_MULTILINE|wx.TE_READONLY)
        box.Add(self.show_text,1,wx.ALIGN_CENTER)

        #创建聊天框内容的文本框
        self.chat_text = wx.TextCtrl(pl, size=wx.Size(400,120), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.chat_text, 1, wx.ALIGN_CENTER)

        # 可伸缩的网格布局
        fgz2 = wx.FlexGridSizer(wx.HSCROLL)

        # 创建两个按钮
        reset_btn = wx.Button(pl, size=wx.Size(200, 40), label='重置')
        send_btn = wx.Button(pl, size=wx.Size(200, 40), label='发送')
        fgz2.Add(reset_btn,1,wx.TOP|wx.LEFT)
        fgz2.Add(send_btn,1,wx.TOP|wx.RIGHT)
        #
        box.Add(fgz2,1,wx.ALIGN_RIGHT)
        #将盒子放在面板当中
        pl.SetSizer(box)


        '''-------------以上代码是客户端的绘制----------------'''
        self.Bind(wx.EVT_BUTTON,self.connect_to_server,conn_btn)
        #实例属性的设置
        self.client_name=client_name
        self.isConnected=False#存储客户端连接服务器的状态，默认为False
        self.client_socket=None#设置客户端的socket为空



    def connect_to_server(self,event):
        print(f'客户端{self.client_name}连接服务器成功')
        if  not self.isConnected:
            #tcp编程的步骤
            server_host_port=('127.0.0.1',8888)
            #创建socket对象
            self.client_socket = socket(AF_INET,SOCK_STREAM)
            #发送连接请求
            self.client_socket.connect(server_host_port)
            #只要连接成功，发送一条数据
            self.client_socket.send(self.client_name.encode('utf-8'))
            #启动一个线程，客户端线程和服务器端进行对话
            client_thread = threading.Thread(target=self.recv_data)
            #设置守护线程
            client_thread.daemon=True
            self.isConnected=True
            client_thread.start()
    def recv_data(self):
        while self.isConnected:
            data=self.client_socket.recv(1024).decode('utf-8')
            #显示到只读文本框
            self.show_text.AppendText('-'*40+'\n'+data+'\n')



if __name__ == '__main__':
#初始化app
    app=wx.App()
#创建自己的客户端界面对象
    name=input('请输入客户端的名称:')
    # client=KkClient('X-Alon')
    client=KkClient(name)
    client.Show()

    app.MainLoop()
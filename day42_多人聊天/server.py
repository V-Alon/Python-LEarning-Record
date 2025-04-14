#coding:utf-8
from socket import socket,AF_INET,SOCK_STREAM

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
        print('正在启动服务........')
        print('启动完毕')

if __name__ == '__main__':
    # 初始化app
    app = wx.App()
    # 创建自己的服务器端界面对象
    client = KkServer()
    client.Show()

    app.MainLoop()

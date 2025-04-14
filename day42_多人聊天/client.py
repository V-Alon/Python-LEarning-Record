#coding:utf-8
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

if __name__ == '__main__':
#初始化app
    app=wx.App()
#创建自己的客户端界面对象
    client=KkClient('V-Alon')
    client.Show()

    app.MainLoop()
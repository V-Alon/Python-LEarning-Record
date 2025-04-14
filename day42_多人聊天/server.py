#coding:utf-8
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

if __name__ == '__main__':
    if __name__ == '__main__':
        # 初始化app
        app = wx.App()
        # 创建自己的服务器端界面对象
        client = KkServer()
        client.Show()

        app.MainLoop()
        
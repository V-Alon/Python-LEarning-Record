import socket
#创建socket对象
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定主机和IP
socket_obj.bind(('127.0.0.1', 8888))

#设置最大连接数量
socket_obj.listen(5)

#等待客户端的TCP连接
client_socket,client_addr=socket_obj.accept()

#接收数据
info=client_socket.recv(1024).decode('utf-8')

while info!='bye':
    if info!='':
        print('接收到的数据是:',info)
    #准备发送的数据
    data=input('请输入要发送的数据:')
    #服务器端回复客户端
    client_socket.send(data.encode('utf-8'))
    if data=='bye':
        break
    info=client_socket.recv(1024).decode('utf-8')
#关闭
client_socket.close()
socket_obj.close()
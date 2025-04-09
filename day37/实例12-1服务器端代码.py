from socket import socket,AF_INET,SOCK_STREAM
import socket
#AF_INET,用于Internet之间的进程通信
#SOCK_DGRAM 表示的是TCP协议编程
#创建对象
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定端口和IP
ip='127.0.0.1'#local
port=8008
server_socket.bind((ip,port))
#listen()开始监听
server_socket.listen(5)
#打印输出
print('服务器已经启动')
#等待客户端连接
client_socket,client_address = server_socket.accept()#系列解包赋值
#接收客户端数据
data=client_socket.recv(1024)
print('客户端接受的数据为:',data.decode('utf-8'))
#关闭socket
server_socket.close()

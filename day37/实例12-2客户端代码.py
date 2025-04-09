import socket
#创建socket对象
client_socket = socket.socket()

#ip和主机端口，向服务器发送连接请求
ip="127.0.0.1"
port=8008
client_socket.connect((ip,port))
print('-----与服务器连接成功-----')

#发数据
client_socket.send('Hello World!'.encode('utf-8'))

#关闭
client_socket.close()
print('发送完毕')


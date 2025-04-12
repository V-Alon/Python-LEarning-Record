from socket import socket,AF_INET,SOCK_DGRAM
#创建socket对象
recv_socket = socket(AF_INET,SOCK_DGRAM)
#绑定IP和端口
recv_socket.bind(('127.0.0.1',8080))
#接受
recv_data,addr= recv_socket.recvfrom(1024)
print('接收到的数据为:',recv_data.decode('utf-8'))

#准备回复
data=input('请输入要回复的数据:')
#回复
recv_socket.sendto(data.encode('utf-8'),addr)
#关闭对象
recv_socket.close()
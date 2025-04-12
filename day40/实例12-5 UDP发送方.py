from socket import socket,AF_INET,SOCK_DGRAM
#创建对象
send_socket = socket(AF_INET,SOCK_DGRAM)
#准备发送
data=input('请输入要发送的数据')
ip_port=('127.0.0.1',8080)
#发送数据
send_socket.sendto(data.encode('utf-8'),ip_port)
#接受数据
recv_data,addr=send_socket.recvfrom(1024)
print('接收到的数据为:',recv_data.decode('utf-8'))

#关闭
send_socket.close()
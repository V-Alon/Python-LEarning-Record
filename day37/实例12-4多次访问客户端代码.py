import socket

client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 8888))
print('----------已经建立服务器连接----------')
info=''
while info!='bye':
    send_data=input('请输入客户端要发送的数据:')
    client_socket.send(send_data.encode('utf-8'))
    if send_data == 'bye':
        break
    info=client_socket.recv(1024).decode('utf-8')
    print('收到服务器的响应数据',info)


client_socket.close()

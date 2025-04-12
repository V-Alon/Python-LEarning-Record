from socket import socket,AF_INET,SOCK_DGRAM
recv_socket = socket(AF_INET, SOCK_DGRAM)
ip_sort=('127.0.0.1',8888)
recv_socket.bind(ip_sort)
while True:
    recv_data,addr=recv_socket.recvfrom(1024)
    print('客服说:',recv_data.decode('utf-8'))
    if recv_data.decode('utf-8') == 'bye':
        break
    else:
        data=input('客服回复:')

    recv_socket.sendto(data.encode('utf-8'),addr)

recv_socket.close()
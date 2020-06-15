import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input('Enter IP Address: ')
port = int(input('Enter Port Number'))

def portScanner(port):
    if s.connect_ex((host,port)):
        print('Port is Closed')
    else:
        print('Port is OPEN')

portScanner(port)
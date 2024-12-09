import socket

host='www.google.com'
ip=socket.gethostbyname(host)

print(host," has ip address of: ",ip)

port=80
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
result=s.connect_ex((host,port))

print("building connection...")

req="GET/HTTP/1.1\r\nHost%5s\t\n\r\n"% host
s.send(req.encode())

data=s.recv(4096)

print("Data: ",str(bytes(data)))

print("length: ",len(data))

print("closing connection....")

s.close()
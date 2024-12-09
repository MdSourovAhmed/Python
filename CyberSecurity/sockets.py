import socket

host='www.google.com'
ip=socket.gethostbyname(host)

print(host," has ip address of: ",ip)

portlist=[21,22,23,80,443]

for port in portlist:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    result=s.connect_ex((host,port))
    print(port,": ", {True:"open", False:"close"}[result==0])
    s.close()


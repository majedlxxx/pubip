import socket
website="start.parrotsec.org"
ip =socket.gethostbyname(website)
port=80
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((ip,port))
se="GET / HTTP/1.1\nHost: "+ip+"\n\n"
s.send(se.encode('ascii'))
total=""
started=False
while True:
    re=s.recv(1024).decode('ascii')
    total+=re
    if len(re)==0:
        break
result=""
total=total.split("\n")
for line in total:
    if 'Your IP' in line:
        result=line
        break
result=result.split(" ")
ip=result[-1]
ip=ip[:-7]
print(ip)

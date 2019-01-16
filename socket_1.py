import socket
import urllib.request, urllib.parse, urllib.error

url = input('Enter URL: ')
if len(url) < 1 :
    url = 'http://data.py4e.org/romeo.txt'
urlhost = url.split('/')[2]
print(urlhost)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.py4e.org', 80))
cmd = 'GET HTTP/1.0\r\n\r\n'
print(cmd)
mysock.send(cmd.encode())

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()

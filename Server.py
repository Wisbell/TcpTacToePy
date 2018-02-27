import socket
# import socketserver

class TServer:
    
    def getIp(self):
        pass

#gets local ip
# stuff = socket.gethostbyname(socket.gethostname())
# print('stuff', stuff)

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.connect(("8.8.8.8", 80))
# print(s.getsockname()[0])
# print(s.getsockname())
# s.close()

# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])


# from requests import get

# get('https://ipapi.co/ip/').text

# import urllib

# ip = urllib.request.urlopen("http://icanhazip.com").read()
# print(ip)

#Used to make requests
import urllib.request

x = urllib.request.urlopen('http://icanhazip.com')
print(x.read())
import socket
import html
import argparse

import base64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
parser = argparse.ArgumentParser()
# parser.add_argument("--url")
parser.add_argument("--user")
parser.add_argument("--password")
parser.add_argument("--local-file")

args = parser.parse_args()
url =  "blogtest.vnprogramming.com"
# url = args.url

args = parser.parse_args()
user =  "test"
# user = args.user

args = parser.parse_args()
pw =  "test123QWE@AD"
# pw = args.password

args = parser.parse_args()
file =  "/root/test22.png"
# file = args.local_file

s.connect((url, 80))

cotentlength = int(len(pw)) + int(len(user)) + 9
cotentlength = str(cotentlength)
request = b"POST /wp-login.php HTTP/1.1\r\nHost:blogtest.vnprogramming.com\r\nContent-Length: " + cotentlength.encode('utf-8') + b"\r\nContent-Type: application/x-www-form-urlencoded\r\nCookie: wordpress_test_cookie=WP%20Cookie%20check; wp_lang=en_US\r\nConnection: close\r\n\r\nlog=" + user.encode('utf-8') + b"&pwd=" + pw.encode('utf-8') 
s.send(request)
result = s.recv(2000)
s.close()
result = result.decode('utf-8')
# result = html.unescape(result)
# print(result)
result = result.split('Set-Cookie: ')
# print(result)
c1 = result[2].split(' ')[0]
c2 = result[3].split(' ')[0]
c3 = result[4].split('; ')[0]
c4 = result[1].split(' ')[0]

Cookie = b"Cookie: " + c2.encode('utf-8') + b' ' + c3.encode('utf-8') + b'\r\n'
############################################################
request = b'GET /wp-admin/upload.php HTTP/1.1\r\nHost: blogtest.vnprogramming.com\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\n' + Cookie + b'Connection: close\r\n\r\n'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((url, 80))
s.send(request)
result = s.recv(10000)
result = result.decode('utf-8')
# print(result)
c5 = result.split('Set-Cookie: ')[1]
c5 = c5.split(';')[0]
# print(c5)
Cookie = b"Cookie: " + c2.encode('utf-8') + b' ' + c3.encode('utf-8') + b'; ' + c5.encode('utf-8') + b'\r\n'
cnt = False
wp=''
while True:
	result = s.recv(8000)
	result = result.decode('utf-8')
	if('_wpnonce' in result):
		wp = result.split('_wpnonce')[1]
		wp = wp[:14]
		print(wp)
	if len(result) == 0:
		break;

# while True:
# 	result = s.recv(8000)
# 	result = result.decode('utf-8')
# 	if('_wpnonce' in result):
# 		if not cnt:
# 			cnt = True
# 		else:
# 			wp = result.split('_wpnonce\":\"')[1]
# 			wp = wp[:10]
# 	if len(result) == 0:
# 		break;


s.close()
# print(request.decode('utf-8'))
# print('Right here')
# print(result)

b = b''
with open(file, "rb") as image:
  b = image.read()
  # b = base64.b64encode(image.read())


image = b
# image = image.decode('utf-8')
# image = bytes(image)
# print(image)

fil = file.split('/')[-1]

br = b'------WebKitFormBoundaryBHWzGBxshdnCiU7JJ'

name = br + b'\r\nContent-Disposition: form-data; name=\"name\"\r\n\r\n' + fil.encode('utf-8') + b'\r\n'

ua = b'upload-attachment'
action = br + b'\r\n' + b'Content-Disposition: form-data; name=\"action\"\r\n' + b'\r\n' + ua

wpnonce = b'\r\n' + br + b'\r\n' + b'Content-Disposition: form-data; name=\"_wpnonce\"' + b'\r\n' + b'\r\n' + wp.encode('utf-8') + b'\r\n'
# wpnonce = b''


up = br + b'\r\n' + b'Content-Disposition: form-data; name=\"async-upload\"; filename=\"' + fil.encode('utf-8') + b'\"\r\n'
up2 = b'Content-Type: image/png\r\n\r\n'
image = image + b'\r\n' + br + b'--'

cotentlength = len(name) + len(action) + len(image) + len(wpnonce) + len(up) + len(up2)
cotentlength = str(cotentlength)
request = b"POST " + b"/wp-admin/async-upload.php" + b" HTTP/1.1\nHost: blogtest.vnprogramming.com\r\nContent-Length: " + cotentlength.encode('utf-8') + b"\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36\r\nContent-Type: multipart/form-data; boundary=----WebKitFormBoundaryBHWzGBxshdnCiU7JJ\r\nAccept: */*\r\nOrigin: http://blogtest.vnprogramming.com\r\nReferer: http://blogtest.vnprogramming.com/wp-admin/upload.php\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-US,en;q=0.9\r\n" +  Cookie + b"Connection: close\r\n\r\n" + name + action + wpnonce + up + up2
# print(request.decode('utf-8'))
request = request + image
# print(image)
# print(image.decode('utf-8'))
# print(image)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((url, 80))
s.send(request)
result = s.recv(2000)
result = result.decode('utf-8')
result = html.unescape(result)
print(result)
if 'HTTP/1.1 200' in result:
	result=result.split('link\"')[1]
	result=result.split('\"')[0]
	result=result.split('\\')
	result=''.join(result)
	print('Upload success. File upload url:', result, end='')
	print(file)
else: 
	print('Upload failed.')
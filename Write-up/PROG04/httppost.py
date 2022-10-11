import socket
import html
import argparse


parser = argparse.ArgumentParser()
# parser.add_argument("--url")
# args = parser.parse_args()
url =  "blogtest.vnprogramming.com"
# url = args.url

parser.add_argument("--user")
parser.add_argument("--password")
args = parser.parse_args()
user =  "test"
user = args.user

args = parser.parse_args()
pw =  "test123QWE@AD"
pw = args.password

cotentlength = int(len(pw)) + int(len(user)) + 9
cotentlength = str(cotentlength)

request = b"POST /wp-login.php HTTP/1.1\nHost:blogtest.vnprogramming.com\r\nContent-Length: " + cotentlength.encode('utf-8') + b"\r\nContent-Type: application/x-www-form-urlencoded\r\nCookie: wordpress_test_cookie=WP%20Cookie%20check; wp_lang=en_US\r\nConnection: close\r\n\r\nlog=" + user.encode('utf-8') + b"&pwd=" + pw.encode('utf-8') 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((url, 80))

s.send(request)

result = s.recv(80000)
result = result.decode('utf-8')
if 'HTTP/1.1 302' in result:
	print('User', user, 'đăng nhập thành công')
else:
	print('User', user, 'đăng nhập thất bại')

import socket
import html
import argparse

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
parser = argparse.ArgumentParser()
parser.add_argument("--url")
parser.add_argument("--remote-file")
args = parser.parse_args()
url =  "blogtest.vnprogramming.com"
# url =  "www.libpng.org"
url = args.url

args = parser.parse_args()
file =  "/wp-content/uploads/2020/09/greengrass.png"
# file =  "/pub/png/img_png/pass0.png"
file = args.remote_file

request = b"HEAD " + file.encode('utf-8') + b" HTTP/1.1\nHost:" + url.encode('utf-8') + b"\n\n"
# print(request)
s.connect((url, 80))
s.send(request)
result = s.recv(1000)
result = result.decode('utf-8')
# print(result)
if 'HTTP/1.1 200' in result:
	result = result.split('Content-Length: ')[1]
	result = result.split('\r')[0]
	print('Kích thước file ảnh:', result,'bytes')
else:
	print('Không tồn tại file ảnh')

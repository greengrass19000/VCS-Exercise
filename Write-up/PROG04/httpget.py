import socket
import html
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Type --url + the link")
args = parser.parse_args()
url =  "blogtest.vnprogramming.com"
url = args.url
request = b"GET / HTTP/1.1\nHost:" + url.encode('utf-8') + b"\n\n"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((url, 80))
s.send(request)
result = s.recv(20000)
result = result.decode('utf-8')
# print(result)
if '</title>' in result:
	result = result.split('<title>')[1]
	result = result.split('</title>')[0]
elif '</TITLE>' in result:
	result = result.split('<TITLE>')[1]
	result = result.split('</TITLE>')[0]
elif '</Title>' in result:
	result = result.split('<Title>')[1]
	result = result.split('</Title>')[0]
else:
	print('Title not found!!!')
	exit(0)	
result = html.unescape(result)
print(result)

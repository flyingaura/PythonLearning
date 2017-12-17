
from http.server import HTTPServer, CGIHTTPRequestHandler

# port = 8080
#
# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
# print("Starting simple_httpd on port: %d" % httpd.server_port)
# httpd.serve_forever()

# =================设置并启动一个http服务器=================
port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print('启动python自带的简单HTTP服务器，端口为：%d' % httpd.server_port)
httpd.serve_forever()

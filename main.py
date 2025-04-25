from http.server import BaseHTTPRequestHandler, HTTPServer


host_name = 'localhost'
server_port = 8080

class MyServer(BaseHTTPRequestHandler):
     """ Класс для обработки запросов клиентов """
     def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open('pages/contact.html', encoding='utf-8') as f:
            content = f.read()
        self.wfile.write(bytes(content, 'utf-8'))

if __name__ == '__main__':
    web_server = HTTPServer((host_name, server_port),MyServer)
    print("Server started http://%s:%s" % (host_name, server_port))
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print('Server stopped')

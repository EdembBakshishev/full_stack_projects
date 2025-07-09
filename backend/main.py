from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/hello":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")  # <-- Додаємо CORS заголовок
            self.end_headers()
            self.wfile.write("Привіт з простого Python-сервера!".encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ("0.0.0.0", 80)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Сервер запущено на порті 80")
    httpd.serve_forever()

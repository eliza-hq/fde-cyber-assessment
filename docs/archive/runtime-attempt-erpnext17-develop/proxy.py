import select
import socket
import socketserver


class Forward(socketserver.BaseRequestHandler):
    def handle(self):
        with socket.create_connection(("app", 8000), timeout=10) as upstream:
            upstream.settimeout(None)
            sockets = [self.request, upstream]
            while True:
                ready, _, _ = select.select(sockets, [], [], 60)
                if not ready:
                    break
                for source in ready:
                    data = source.recv(65536)
                    if not data:
                        return
                    (upstream if source is self.request else self.request).sendall(data)


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


with Server(("0.0.0.0", 8000), Forward) as server:
    server.serve_forever()

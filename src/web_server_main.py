import sys, signal
import http.server as hs
import socketserver as sv

def set_server_port():
    if sys.argv[1:]:
        return int(sys.argv[1:])
    return 8080

def start_httpreq_serverhandler(port):
    return sv.ThreadingTCPServer(('', port), hs.SimpleHTTPRequestHandler)

def signal_handler(signal, frame, server):
    try:
        if( server ):
            server.server_close()
    finally:
        sys.exit(0)
    
#main
port = set_server_port()
server = start_httpreq_serverhandler(port)
signal.signal(signal.SIGINT, signal_handler)
try:
    while True:
        server.serve_forever()
except KeyboardInterrupt:
    pass
server.server_close()

import sys, signal
import http.server as hs
import socketserver as sv

USR = "web"
PWD = "server"

def login():
    username = input("Inserire il nome ")
    password = input("Inserire la password ")
    return USR == username and \
        PWD == password

def set_server_port(): #sets the port which the server will be listening, port = 1° argument(8080 by default)
    if sys.argv[1:]:
        return int(sys.argv[1])
    return 8080

def start_httpreq_serverhandler(port): #starts the web server, this server will be able to handle multiple http requests.
    return sv.ThreadingTCPServer(('', port), hs.SimpleHTTPRequestHandler)

def signal_handler(signal, frame, server): #exit method, with ctrl + c the server will be shut down
    try:
        if( server ):
            server.server_close()
    finally:
        sys.exit(0)
if login():
    print("Accesso eseguito correttamente")
    port = set_server_port()
    server = start_httpreq_serverhandler(port)
    server.allow_reuse_address = True #this setting allows to reuse the same address
    signal.signal(signal.SIGINT, signal_handler) 
    try:
        while True:
            server.serve_forever() #until the script is running the server will listen to the requests
    except KeyboardInterrupt:
        pass
    server.server_close()
else:
    print("password errata ")

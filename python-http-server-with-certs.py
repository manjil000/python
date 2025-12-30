from http.server import HTTPServer, BaseHTTPRequestHandler 
import ssl
httpd = HTTPServer(('0.0.0.0', 8002), BaseHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile="key.pem",
    certfile='cert.pem',
    server_side=True)
httpd.serve_forever()
"""
HTTPServer: This class is used to create an HTTP server.
BaseHTTPRequestHandler: This class is used to handle HTTP requests.
ssl: This module provides access to Transport Layer Security (previously known as Secure Sockets Layer), which is used to secure communications over computer networks.
Creating the HTTP Server """
httpd = HTTPServer(('0.0.0.0', 8002), BaseHTTPRequestHandler)
#HTTPServer: Here, we are creating an instance of the HTTPServer class.
#('0.0.0.0', 8002): This is a tuple containing the address and port number on which the server will listen.
#'0.0.0.0': This means the server will accept connections on any network interface (i.e., it will be accessible from any IP address).
#8002: This is the port number on which the server will listen for incoming HTTP requests.
#BaseHTTPRequestHandler: This is the request handler class which will be used to handle incoming requests. By default, this doesn't do anything special; it just provides the basic request handling capabilities.
#Adding SSL/TLS Security

httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile="key.pem",
    certfile='cert.pem',
    server_side=True)
#ssl.wrap_socket: This function wraps an existing socket to add SSL/TLS support.
#httpd.socket: The socket object that is being wrapped to add SSL/TLS.
#keyfile="key.pem": The path to the private key file. This file is used by the server to prove its identity 
#to clients.
#certfile='cert.pem': The path to the certificate file. This file is used by the server to authenticate itself to clients.
#server_side=True: This indicates that the socket is for the server side of the SSL/TLS connection.

#Running the Server
httpd.serve_forever()
#serve_forever: This method starts the server and keeps it running, handling requests until it is manually stopped. 
#It enters an infinite loop, waiting for and processing incoming requests.

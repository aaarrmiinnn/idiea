import socket

soc = socket.socket()
print("Socket is created.")

soc.bind(("localhost", 10000))
print("Socket is bound to an address & port number.")

soc.listen(1)
print("Listening for incoming connection ...")

connected = False
accept_timeout = 5
soc.settimeout(accept_timeout)
try:
    connection, address = soc.accept()
    print("Connected to a client: {client_info}.".format(client_info=address))
    connected = True
except socket.timeout:
    print("A socket.timeout exception occurred because the server did not receive any connection for {accept_timeout} seconds.".format(accept_timeout=accept_timeout))

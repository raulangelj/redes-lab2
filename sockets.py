# EMISOR 

import socket

socket_emisor = socket.socket( socket.AF_INET,socket.SOCK_STREAM )

host=socket.gethostname()
puerto = 7634

socket_emisor.bind(( host,puerto ))
socket_emisor.listen(1)

con,addr=socket_emisor.accept()
print("Se establecio una coneccion con: ",addr)

while True:
    messg=input("Enviar una mensaje al receptor: ")
    con.send(messg.encode())
    print("Esperando respuesta...")
    c_messg=con.recv(1024)
    print("Mensaje del receptor: ",c_messg.decode())


# RECEPTOR

import socket

socket_receptor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
puerto = 7634

socket_receptor.connect((host,puerto))

while True:
    print("Esperando mensaje...")
    s_messg=socket_receptor.recv(1024)
    print("Mensaje del emisor: ",s_messg.decode())
    c_messg=input("Enviar mensaje al emisor: ")
    socket_receptor.send(c_messg.encode())
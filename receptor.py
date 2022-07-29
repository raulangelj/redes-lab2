import socket
from recibir_mensaje import Recibir_mensaje
from emisor import PORT_NUMBER

socket_receptor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
puerto = PORT_NUMBER

socket_receptor.connect((host,puerto))

while True:
    print("Esperando mensaje...")
    s_messg=socket_receptor.recv(1024)
    if s_messg == b'':
      socket_receptor.close()
      exit(1)
    recibir_mensaje = Recibir_mensaje(s_messg.decode())
    mensaje = recibir_mensaje.recibir()
    print("Mensaje traducido del receptor: ",mensaje)
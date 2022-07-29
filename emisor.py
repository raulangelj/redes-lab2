import time
import socket
from enviar_mensaje import Enviar_mensaje
PORT_NUMBER = 7634

menu = """\n
\t1. Enviar mensaje\n
\t2. Salir\n
"""

if __name__ == '__main__':
	print('=============================== Bienvenido al emisor de mensajes ===============================')
	option = 0
	socket_emisor = socket.socket( socket.AF_INET,socket.SOCK_STREAM )

	host=socket.gethostname()
	puerto = 7634

	socket_emisor.bind(( host,puerto ))
	socket_emisor.listen(1)

	con,addr=socket_emisor.accept()
	print('host ', host)
	print('puerto ', puerto)
	print("Se establecio una coneccion con: ",addr)
	while True:	
		while option != 2:
			print(menu)
			option = input('¿Que desea hacer?\n>')
			if option == '1':
				mensaje = input('Ingrese el mensaje:\n\t>')
				enviar_mensaje = Enviar_mensaje(mensaje)
				mensaje = enviar_mensaje.transmitir()
				con.send(mensaje.encode())
				time.sleep(2)
			elif option == '2':
				print('=============================== Gracias por usar el emisor de mensajes ===============================')
				exit(1)

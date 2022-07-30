# import math
from copyreg import constructor
import socket
from bitarray import bitarray
from utils import to_binary, findChecksum

class Enviar_mensaje:
	def __init__(self, texto):
		self.texto = texto

	def verificacion(self):
		# TODO algoritmos
		self.bitarrayy = to_binary(self.texto)
		self.binary = ''.join(str(i) for i in self.bitarrayy)
		# find checksum (CREAR FUNCION QUE CAMBIE EL mensaje_enviar PARA QUE SOLO SE TENGO QUE CAMBAIR LA FUNCION)
		self.check_sum()
		
		
	
	def ruido(self):
		# TODO implementar ruido
		print('ruido')
	
	def transmitir(self):
		self.verificacion()
		self.ruido()
		return self.mensaje_enviar

	def check_sum(self):
		print('SE HIZO CHECKSUM')
		self.checksum = findChecksum(self.binary)
		self.mensaje_enviar = f'{self.binary}checksum{self.checksum}'
		# pruab para ver si el checksum funciona con dato incorrectos
		# falsoBinary = list(self.binary)
		# falsoBinary[1] = '0'
		# falsoBinary[2] = '0'
		# falsoBinary[4] = '0'
		# self.checksum = findChecksum(''.join(str(i) for i in falsoBinary))
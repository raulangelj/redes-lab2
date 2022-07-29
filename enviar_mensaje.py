# import math
import socket
from bitarray import bitarray
from utils import to_binary

class Enviar_mensaje:
	def __init__(self, texto):
		self.texto = texto

	def verificacion(self):
		# TODO algoritmos
		self.binary = to_binary(self.texto)
	
	def ruido(self):
		# TODO implementar ruido
		print('ruido')
	
	def transmitir(self):
		self.verificacion()
		self.ruido()
		return ''.join(str(i) for i in self.binary)
from bitarray import bitarray
from utils import to_text

class Recibir_mensaje():
	def __init__(self, binario):
		self.binary = binario

	def codificacion(self):
		# pasar de binario a texto
		self.texto = to_text(self.binary)
	
	def verificacion(self):
		# TODO algoritmo para verificar mensaje
		pass
	
	def recibir(self):
		# TODO recibir de web socket
		self.codificacion()
		self.verificacion()
		return self.texto
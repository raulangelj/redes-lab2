from bitarray import bitarray
from utils import to_text, findChecksum

class Recibir_mensaje():
	def __init__(self, binario):
		data = binario.split('checksum')
		self.binary = data[0]
		self.checksum = data[1]

	def codificacion(self):
		# pasar de binario a texto
		self.texto = to_text(self.binary)
	
	def verificacion(self):
		# TODO algoritmo para verificar mensaje
		# usamos checksum para verificar
		self.check_sum()
	
	def recibir(self):
		# TODO recibir de web socket
		self.codificacion()
		self.verificacion()
		return self.texto
	
	def check_sum(self):  # sourcery skip: raise-specific-error
		self.checksum_calculado = findChecksum(self.binary)
		if self.checksum_calculado == self.checksum:
			print('MENSAJE VERIFICADO')
		else:
			print('MENSAJE NO VERIFICADO')
			# raise Exception('MENSAJE NO VERIFICADO')

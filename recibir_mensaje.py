from bitarray import bitarray
from utils import to_text, findChecksum, detect_error

class Recibir_mensaje():
	def __init__(self, binario):
		# data = binario.split('checksum')
		data = binario.split('hamming')
		self.binary = data[0]
		# self.checksum = data[1]
		self.hamming = data[1]

	def codificacion(self):
		# pasar de binario a texto
		try:
			self.texto = to_text(self.binary)
		except:
			self.texto = 'No se pudo traducir a texto dado a que el ruido aplicado causó caracteres fuera del encode utf-32'
	
	def verificacion(self):
		# TODO algoritmo para verificar mensaje
		# usamos checksum para verificar
		self.check_sum()
	
	def recibir(self):
		# TODO recibir de web socket
		self.codificacion()
		self.verificacion()
		return self.texto
	
	def hamming_func(self):
		correction = detect_error(self.binary, self.hamming)
		if(correction==0):
			print("MENSAJE SIN ERROR")
		else:
			print("MENSAJE CON ERROR")

	def check_sum(self):  # sourcery skip: raise-specific-error
		self.checksum_calculado = findChecksum(self.binary)
		if self.checksum_calculado == self.checksum:
			print('MENSAJE VERIFICADO')
		else:
			print('MENSAJE NO VERIFICADO')
			# raise Exception('MENSAJE NO VERIFICADO')

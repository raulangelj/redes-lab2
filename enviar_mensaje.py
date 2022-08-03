# import math
from copyreg import constructor
import socket
from bitarray import bitarray
from utils import to_binary, findChecksum, simple_parity
import random

class Enviar_mensaje:
	def __init__(self, texto, probabilidad_ruido):
		self.texto = texto
		self.probabilidad_ruido = probabilidad_ruido

	def verificacion(self):
		# TODO algoritmos
		self.bitarrayy = to_binary(self.texto)
		self.binary = ''.join(str(i) for i in self.bitarrayy)
		# find checksum (CREAR FUNCION QUE CAMBIE EL mensaje_enviar PARA QUE SOLO SE TENGO QUE CAMBAIR LA FUNCION)
		self.check_sum()
		# self.simple_parity()
		
		
	
	def ruido(self):
		random_static_num = self.probabilidad_ruido - 1
		new_binary = ''
		for i in self.binary:
			random_num = random.randint(0, self.probabilidad_ruido)
			if random_num == random_static_num:
				binary = int(i)
				if binary == 0:
					new_binary += '1'
				else:
					new_binary += '0'
			else:
				new_binary += i
		self.binary = new_binary
	
	def transmitir(self):
		self.verificacion()
		self.ruido()
		return self.mensaje_enviar
	
	def simple_parity(self):
		self.simpleParity = simple_parity(self.binary)

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
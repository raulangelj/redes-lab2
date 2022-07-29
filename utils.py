from bitarray import bitarray

def to_binary(texto_a_binario):
  ba = bitarray()
  ba.frombytes(texto_a_binario.encode('utf-8'))
  return ba


def to_text(binario_a_texto):
  return bitarray(binario_a_texto).tobytes().decode('utf-8')

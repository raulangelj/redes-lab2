from bitarray import bitarray

def to_binary(texto_a_binario):
  ba = bitarray()
  ba.frombytes(texto_a_binario.encode('utf-8'))
  return ba


def to_text(binario_a_texto):
  return bitarray(binario_a_texto).tobytes().decode('utf-8')


def simple_parity(SentMessage):
  parity_number = SentMessage[-1]
  without_parity = SentMessage[:-1]
  one_count = 0

  for bit in without_parity:
    if (bit == '1'): one_count += 1

  if (parity_number == '1' and one_count % 2 == 1): return True
  if (parity_number == '0' and one_count % 2 == 0): return True

  return False


# Function to find the Checksum of Sent Message
# Extraido de: https://www.geeksforgeeks.org/implementing-checksum-using-python/amp/
def findChecksum(SentMessage):
  k = len(SentMessage) // 8
  # Dividing sent message in packets of k bits.
  c1 = SentMessage[:k]
  c2 = SentMessage[k:2*k]
  c3 = SentMessage[2*k:3*k]
  c4 = SentMessage[3*k:4*k]

  # Calculating the binary sum of packets
  Sum = bin(int(c1, 2)+int(c2, 2)+int(c3, 2)+int(c4, 2))[2:]

  # Adding the overflow bits
  if (len(Sum) > k):
    x = len(Sum)-k
    Sum = bin(int(Sum[:x], 2) + int(Sum[x:], 2))[2:]
  if(len(Sum) < k):
      Sum = '0'*(k-len(Sum))+Sum

  return ''.join('0' if (i == '1') else '1' for i in Sum)
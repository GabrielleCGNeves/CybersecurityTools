from Crypto.Cipher import AES

output_file = 'encrypted.bin'
data = b'gabi noob'
key = b'testando12345678'  # Precisa ser uma senha de 16 ou 32 bytes

cipher = AES.new(key, AES.MODE_CFB)
ciphered_data = cipher.encrypt(data)

with open(output_file, "wb") as file:
  file.write(cipher.iv)
  file.write(ciphered_data)

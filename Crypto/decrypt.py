from Crypto.Cipher import AES

input_file = 'encrypted.bin'
key = b'testando12345678'

with open(input_file, 'rb') as file:
  iv = file.read(16)
  ciphered_data = file.read()

cipher = AES.new(key, AES.MODE_CFB, iv=iv)
original_data = cipher.decrypt(ciphered_data)
print(original_data)

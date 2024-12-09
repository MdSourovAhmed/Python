from Crypto.Cipher import AES

key="secret-key-12345"

encrypt_AES=AES.new(key.encode("utf8"),AES.MODE_CBC,'This is an lV-12'.encode("utf8"))

message= "This is the secret message    ".encode("utf8")

ciphertext=encrypt_AES.encrypt(message)

print("Cipher text: ",ciphertext)

decrypt_AES=AES.new(key.encode("utf8"),AES.MODE_CBC,'This is an lV-12'.encode("utf8"))

message_dec=decrypt_AES.decrypt(ciphertext)

print("Decrypted text: ",message_dec.strip().decode())


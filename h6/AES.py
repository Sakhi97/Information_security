from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Define the plaintext message and encryption key
message = b'This is a plaintext message.'
key = os.urandom(32)  # Generate a 256-bit (32-byte) encryption key

# Create AES cipher object in CBC mode
cipher = AES.new(key, AES.MODE_CBC)

# Encrypt the message
ciphertext = cipher.encrypt(pad(message, AES.block_size))

# Decrypt the ciphertext
decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Plaintext message: ", message)
print("Encryption key: ", key)
print("Ciphertext: ", ciphertext)
print("Decrypted message: ", decrypted_message)

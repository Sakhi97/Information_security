from Crypto.Cipher import ARC4
import os

# Define the plaintext message and encryption key
message = b'This is a plaintext message.'
key = os.urandom(16)  # Generate a 128-bit (16-byte) encryption key

# Create RC4 cipher object
cipher = ARC4.new(key)

# Encrypt the message
ciphertext = cipher.encrypt(message)

# Decrypt the ciphertext
decrypted_message = cipher.decrypt(ciphertext)

print("Plaintext message: ", message)
print("Encryption key: ", key)
print("Ciphertext: ", ciphertext)
print("Decrypted message: ", decrypted_message)

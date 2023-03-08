from Crypto.PublicKey import ECC

# Generate ECC key pair
key = ECC.generate(curve='P-256')

# Get public key
public_key = key.public_key()

# Define plaintext message
message = b'This is a plaintext message.'

# Encrypt message using ECC
ciphertext = public_key.encrypt(message)

# Decrypt ciphertext using ECC
decrypted_message = key.decrypt(ciphertext)

print("Plaintext message: ", message)
print("Ciphertext: ", ciphertext)
print("Decrypted message: ", decrypted_message)

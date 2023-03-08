import hashlib

message = b'This is a message to be hashed'
hash_object = hashlib.sha256(message)
hash_digest = hash_object.hexdigest()

print("Message: ", message)
print("Hash digest (SHA-256): ", hash_digest)

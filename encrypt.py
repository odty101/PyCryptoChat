from cryptography.fernet import Fernet

# Generate a key and encrypt a message symmetrically
key = Fernet.generate_key()
print('Key: {}'.format(key))
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(b'A really secret message')

print('Cipher Text: {}'.format(str(cipher_text)))

# Decrypt the message
plain_text = cipher_suite.decrypt(cipher_text)

print('Plain Text: {}'.format(str(plain_text)))
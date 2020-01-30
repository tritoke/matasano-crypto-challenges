from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import standard_b64decode as b64decode

data = b64decode(open("7.txt", "rb").read())

backend = default_backend()
KEY = b"YELLOW SUBMARINE"

cipher = Cipher(algorithms.AES(KEY), modes.ECB(), backend=backend)
decryptor = cipher.decryptor()
print(decryptor.update(data).decode())
decryptor.finalize()

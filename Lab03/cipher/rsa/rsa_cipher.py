# import rsa
# import os

# class RSACipher:
#     def __init__(self, key_size=2048):
#         self.key_size = key_size
#         self.private_key = None
#         self.public_key = None

#     def generate_keys(self):
#         # Tạo cặp khóa RSA
#         self.public_key, self.private_key = rsa.newkeys(self.key_size)

#     def save_keys(self, private_key_file='cipher/rsa/keys/private_key.pem', public_key_file='cipher/rsa/keys/public_key.pem'):
#         # Lưu khóa bí mật và khóa công khai vào file
#         os.makedirs(os.path.dirname(private_key_file), exist_ok=True)
#         with open(private_key_file, 'wb') as f:
#             f.write(self.private_key.save_pkcs1('PEM'))
#         with open(public_key_file, 'wb') as f:
#             f.write(self.public_key.save_pkcs1('PEM'))

#     def load_keys(self, private_key_file='cipher/rsa/keys/private_key.pem', public_key_file='cipher/rsa/keys/public_key.pem'):
#         # Đọc khóa bí mật và khóa công khai từ file
#         with open(private_key_file, 'rb') as f:
#             self.private_key = rsa.PrivateKey.load_pkcs1(f.read())
#         with open(public_key_file, 'rb') as f:
#             self.public_key = rsa.PublicKey.load_pkcs1(f.read())
#         return self.private_key, self.public_key

#     def encrypt(self, message, key):
#         # Mã hóa thông điệp sử dụng khóa công khai
#         encrypted_message = rsa.encrypt(message.encode(), key)
#         return encrypted_message

#     def decrypt(self, ciphertext, key):
#         # Giải mã thông điệp sử dụng khóa bí mật
#         decrypted_message = rsa.decrypt(ciphertext, key).decode()
#         return decrypted_message

#     def sign(self, message, private_key):
#         # Ký thông điệp sử dụng khóa bí mật
#         signature = rsa.sign(message.encode(), private_key, 'SHA-256')
#         return signature

#     def verify(self, message, signature, public_key):
#         # Xác minh chữ ký sử dụng khóa công khai
#         try:
#             rsa.verify(message.encode(), signature, public_key)
#             return True
#         except rsa.VerificationError:
#             return False
import rsa, os

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass

    def generate_keys(self):
        (public_key, private_key) = rsa.newkeys(1024)
        with open('cipher/rsa/keys/publicKey.pem', 'wb') as p:
            p.write(public_key.save_pkcs1('PEM'))
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key.save_pkcs1('PEM'))

    def load_keys(self):
        with open('cipher/rsa/keys/publicKey.pem', 'rb') as p:
            public_key = rsa.PublicKey.load_pkcs1(p.read())
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            private_key = rsa.PrivateKey.load_pkcs1(p.read())
        return private_key, public_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('ascii'), key)

    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False

    def sign(self, message, key):
        return rsa.sign(message.encode('ascii'), key, 'SHA-1')

    def verify(self, message, signature, key):
        try:
            return rsa.verify(message.encode('ascii'), signature, key,) == 'SHA-1'
        except:
            return False
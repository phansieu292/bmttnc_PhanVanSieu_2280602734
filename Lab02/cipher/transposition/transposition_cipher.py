class TranspositionCipher:
    def __init__(self):
        pass
    
    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            position = col
            while position < len(text):
                encrypted_text += text[position]
                position += key
        return encrypted_text
    
    def decrypt(self, text, key):
        decrypted_text = [''] * len(text)
        row, col = 0, 0
        for symbol in text:
            decrypted_text[row] += symbol
            row += 1
            if row == key or (row == key - 1 and col >= len(text) % key):
                row = 0
                col += 1
        return ''.join(decrypted_text)
class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, key):
        Rails = [[] for _ in range(key)]
        rail_index = 0
        direction = 1
        for char in plain_text:
            Rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction
        cipher_text = ''.join(''.join(rail) for rail in Rails)
        return cipher_text
        
    def rail_fence_decrypt(self, cipher_text, key):
        rail_length = [0] * key
        rail_index = 0
        direction = 1
        
        for _ in range (len(cipher_text)):
            rail_length[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction
            
        Rails = []
        index = 0
        for length in rail_length:
            Rails.append(cipher_text[index:index+length])
            index += length
            
        plain_text = ""
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            plain_text += Rails[rail_index][0]
            Rails[rail_index] = Rails[rail_index][1:]
            if rail_index == 0:
                direction = 1
            elif rail_index == key - 1:
                direction = -1
            rail_index += direction
        return plain_text
        
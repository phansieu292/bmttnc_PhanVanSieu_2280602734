def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("moi ban nhap chuoi can dao nguoc:")
print("chuoi dao nguoc la ", dao_nguoc_chuoi(input_string))    

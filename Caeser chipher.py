def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()  
            
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            
            if is_upper:
                encrypted_char = encrypted_char.upper() 
            
            encrypted_text += encrypted_char
        else:
            encrypted_text += char 
    
    return encrypted_text

text = ""
shift = 4

encrypted_text = caesar_cipher(text, shift)

print("Зашифрований текст:", encrypted_text)
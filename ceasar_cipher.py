import string


"""Encrypted_caesar_cipher Function """
def Encrypted_caesar_cipher(text, shift):
    result1=""
    for char in text:
        
        
        if char in string.ascii_uppercase:
            CE= chr((ord(char) - 65 + shift)%26 + 65 )
            result1 += CE
        elif char in string.ascii_lowercase :
            CE= chr((ord(char) -97  + shift)%26 + 97)
            result1 += CE
        else : result1 += char
    return result1 
"""decrypted_caesar_cipher Function """


def Decrypted_caesar_cipher(text, shift):
    result2 = ""
    for char in text:
        if char in string.ascii_uppercase:
            DE = chr((ord(char) - 65 + (-shift)) % 26 + 65)
            result2 += DE
        elif char in string.ascii_lowercase:
            DE = chr((ord(char) - 97 + (-shift)) % 26 + 97)
            result2 += DE
        else : result2 += char
    return result2
   
while True :
    
    choise = input(" If you want to Encrypte press E , If you want to Decrypte press D ")
    if choise == "E" or  choise == "e" :
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = Encrypted_caesar_cipher(text, shift)
        print("Encrypted message:", encrypted_message)
        
        
    elif choise == "D" or choise == "d" :
        text = input("Enter the encrypted message: ")
        shift = int(input("Enter the shift value: "))
        message = Decrypted_caesar_cipher(text, shift)
        print("message:", message)
        
    elif choise == "exit":
        break
        
    else : print (" If you want to Encrypte press E , If you want to Decrypte press D ")
       









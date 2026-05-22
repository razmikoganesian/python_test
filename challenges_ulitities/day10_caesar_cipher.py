
def encrypt(message, key):
    result = ''

    for char in message:
        if char.isalpha():  # шифруем только буквы
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char
    return result

def decrypt(message, key):
    return encrypt(message, -key)

print("Secret message program")
choise = input("Do you want E or D").strip().lower()

if choise == "e":
    text = input("Entre your message: \n" )
    try:
        key = int(input("Enter a number between 1 and 25: "))
        encrypted = encrypt(text, key)
        print("Encrypted message: ")
        print(encrypted)
    except ValueError:
        print("Invalid key")
elif choise == "d":
    text = input("Entre your encrypted message: \n" )
    try:
        key = int(input("Enter a number between 1 and 25: "))
        decrypted = decrypt(text, key)
        print("Decrypted message: ")
        print(decrypted)
    except ValueError:
        print("Invalid key")
else: 
    print("Invalid choice")

import base64
import os


VAULT_FILE = "vault.txt"

def encode(text):
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64decode(text.encode()).decode()

def password_strength_checker(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in "!@#$%^&*()_+" for char in password)

    score = sum([length > 8, has_upper, has_digit, has_special_char])
    return ["Weak", "Medium", "Strong", "Very Strong"][min(score,3)]

def add_credentials():
    website = input("Website:  ").strip()
    username = input("Username:  ").strip()
    password = input("Password:  ").strip()


    strength = password_strength_checker(password)

    line = f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding='utf-8') as f:
        f.write(encoded_line)
    
    print("Credential saved")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print('File not found')
        return
    with open(VAULT_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split("||")
            hidden_pasword = "*" * len(password)
            print(f"{website} | {username} | {password}")


def main():
    while True:
        print("\n Credential Manager")
        print("1. Add credentials")
        print("2. View credentials")
        print("3. Update password")
        print("3. Exit")

        choise = input("Enter you choise")

        match choise:
            case "1": add_credentials()
            case "2": view_credentials()
            # case "3": add_credentials()
            case "4": break
            case _: print("Invalid choise")


if __name__ == "__main__":
    main()
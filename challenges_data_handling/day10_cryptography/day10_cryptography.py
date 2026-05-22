import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

from cryptography.hazmat import primitives


VAULT_FILE = "notes_vault.json"
KEY_FILE = 'vault.key'

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)

    else:
        with open(KEY_FILE, 'rb') as f:
            key = f.read()
    return Fernet(key)
    
fernet = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        return json.load(f)
    
def save_vault(data):
    with open(VAULT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def add_note():
    title = input("Enter note title:  ").strip()
    content = input("Enter note content:  ").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({
        "title": title,
        "content": encrypted_content,
        "time" : timestamp
    })

    save_vault(data)
    print("Data saved! ")


def list_notes():
    data = load_vault()
    if not data:
        print("No data !!!")
        return
    
    for i, note in enumerate(data,1):
        print(f"{i}. {note['title']} {note['time']}")


def view_note():
    list_notes()
    try:
        index = int(input("Enter note number to view:  ")) -1
        data = load_vault()
        if 0 <= index < len(data):
            encrypted_content = data[index]["content"]
            decrypted = fernet.decrypt(encrypted_content.encode()).decode()
            
            print(f"\n{data[index]['title']} {data[index]['time']}\n{decrypted}")

        else:
            print("Invalid selection")
    except:
        print("Invalid input! ")

def search_note():
    keyword = input("Enter the key word:  to search:   ").strip().lower()
    data = load_vault()
    found =  [note for note in data if keyword in note["title"].lower()]
    if not found: 
        print("Nothing is found")
    else: 
        for note in found:
            print(f"{note["title"]} founded! ")
    

def main():
    while True:
        print("\n 🔐 Offline Notes Locker")
        print("1. Add notes")
        print("2. List notes")
        print("3. View notes")
        print("4. Search notes")
        print("5. Exit")

        choise = input("Enter you choise:  ").strip()

        match choise:
            case "1": add_note()
            case "2": list_notes()
            case "3": view_note()
            case "4": search_note()
            case "5": break
            case _: print("Invalid choise")


if __name__ == "__main__":
    main()
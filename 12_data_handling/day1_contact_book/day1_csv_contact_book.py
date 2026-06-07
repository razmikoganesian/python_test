from ast import withitem
import csv
import os
from pickle import FALSE

FILENAME = 'contacts.csv'

if not os.path.exists(FILENAME):
    with open(FILENAME, 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", 'Phone', 'Email'])


      
def add_contact():
    name =input("Name:  ").strip()
    phone = input("Phone:  ").strip()
    email = input("Email:  ").strip()

    fieldnames = ["Name", "Phone", "Email"]

    # check for duplicates
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists")
                return
            
    file_empty = os.path.getsize(FILENAME) == 0
            
    with open(FILENAME, 'a', encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if file_empty:
            writer.writeheader()
        
        writer.writerow({"Name": name, "Phone": phone, "Email": email})
    print("Contact added")
   
def view_contacts():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 0:
            print("No contacts")
            return
        print("\n Your contacts: \n ")

        for row in rows[1:]:
            print(f"{row[0]} | {row[1]} | {row[2]} ")
        print("\n")

def search_contact():
    term = input("Enter the name to search:  ").strip().lower()
    found = False
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower():
                print(f"{row["Name"]} | ☎️ phone {row['Phone']}")
                found = True
    if not found:
        print("No such contact found")

def delete_contact():
    found = False
    new_rows = []

    name_delete = input("Enter the name to delete:  ").strip().lower()

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames

        for row in reader:
            if row["Name"].strip().lower() == name_delete:
                found = True
                continue

            new_rows.append(row)

    if not found:
        print("No such contact")
        return
    
    with open(FILENAME, 'w', encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_rows)
    
    print("Contact deleted/ You can check it")
            
        


def main():
    while True:
        print("\n Contact book")
        print("1. Add contact")
        print("2. View All Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choise = input("Choose an option 1 to 5:  ").strip()

        if choise == "1":
            add_contact()
        elif choise == "2":
            view_contacts()
        elif choise == "3":
            search_contact()
        elif choise == "4":
            delete_contact()
        
        elif choise == "5":
            print("Thanks for using our software")
            break

        else:
            print("Invalid number")


if __name__ == "__main__":
    main()
        
        


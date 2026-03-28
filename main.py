import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "contacts.json")

class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
class ContactBook:
    def __init__(self):
        self.contacts=[]
    def save_contacts(self):
        data = [{"name": c.name, "phone_number": c.phone_number} 
            for c in self.contacts]
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)
        print("Contacts saved.")

    def load_contacts(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as f:
                data = json.load(f)
            self.contacts = [Contact(d["name"], d["phone_number"]) 
                            for d in data]
    

    def add_contact(self):
        while True:
            name= input("Enter contact name: ")
            phone_number= input("Enter contact phone number, no. of digits is 12 only: ")
            while len(phone_number) != 12 or not phone_number.isdigit():
                print("Invalid phone number. Please enter a 12-digit number.")
                phone_number= input("Enter contact phone number, no. of digits is 12 only: ")
            contact=Contact(name,phone_number)
            self.contacts.append(contact)
            self.save_contacts()
            print("Contact added successfully.")
            return


    def search_contact(self):
        choice= input("Search by name or phone number? (name/phone): ")
        choice= choice.strip().lower()
        if choice=="name":
            name = input("Enter contact name to search: ")
            for contact in self.contacts:
                if contact.name.lower() == name.lower():
                    print(f"Contact found — Name: {contact.name}, Phone: {contact.phone_number}")
                    return
            print("Contact not found.")
        elif choice=="phone":
            phone_number = input("Enter contact phone number to search: ")
            for contact in self.contacts:
                if contact.phone_number == phone_number:
                    print(f"Contact found — Name: {contact.name}, Phone: {contact.phone_number}")
                    return
            print("Contact not found.")
        else:  
            print("Invalid search option.")
        return


    def delete_contact(self):
        name = input("Enter contact name to delete: ")
        name= name.lower()
        for contact in self.contacts:
            if contact.name.lower() == name:
                self.contacts.remove(contact)
                self.save_contacts()
                print("Contact deleted successfully.")
                return
        print("Contact not found.")
    

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the book.")
            return
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}")

contact_book = ContactBook()
contact_book.load_contacts()

while True:
    print("\n1. Add Contact")
    print("\n2. Search Contact")
    print("\n3. Delete Contact")
    print("\n4. Display Contacts")
    print("\n5. Quit")
    choose= input("Enter an option: " )
    choose= choose.strip()
    if choose=="1":
        contact_book.add_contact()
    elif choose=="2":
        contact_book.search_contact()
    elif choose=="3":
        contact_book.delete_contact()
    elif choose=="4":
        contact_book.display_contacts()
    elif choose=="5":
        print("Exiting the contact book. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")
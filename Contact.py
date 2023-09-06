import json

class Contact:
    def init(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def init(self):
        self.contacts = []

    def add_contact(self, id, name, phone, email):
        contact = Contact(id, name, phone, email)
        if not self.is_duplicate(id):
            self.contacts.append(contact)
            print("Done, The contact is added")
        else:
            print("This contact is already exist")

    def is_duplicate(self, id):
        for contact in self.contacts:
            if contact.id == id:
                return True
        return False

    def update_contact(self, id, name, phone, email):
        for contact in self.contacts:
            if contact.id == id:
                contact.name = name
                contact.phone = phone
                contact.email = email
                print("The contact is updated sucssfully")
                return
        print("The contact is not found")

    def delete_contact(self, id):
        for contact in self.contacts:
            if contact.id == id:
                self.contacts.remove(contact)
                print("Delete sucssfully.")
                return
        print("The contact is not found.")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone or keyword.lower() in contact.email.lower():
                found_contacts.append(contact)
        
        if found_contacts:
            print("Conformity contacts:")
            for contact in found_contacts:
                print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("The contact is not found.")

    def save_contacts_to_file(self, file_name):
        data = []
        for contact in self.contacts:
            data.append({
                "id": contact.id,
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email
            })

        with open(file_name, "w") as file:
            json.dump(data, file)
            print("Saved sucssfully.")

    def load_contacts_from_file(self, file_name):
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                self.contacts = [Contact(contact["id"], contact["name"], contact["phone"], contact["email"]) for contact in data]
                print("Contacts uploaded sucssfully from file.")
        except FileNotFoundError:
            print("The file is not found.")

def main():
    contact_manager = ContactManager()
    file_name = "contacts.json"

    while True:
        print("\nOptions:")
        print("1. Add contact")
        print("2. Edit contact")
        print("3. Delete contact")
        print("4. Search about contact")
        print("5. View all")
        print("6. Save contacts in file")
        print("7. Downlaod contacts from file")
        print("8. Exit")

        choice = input("Please choose option: ")

if choice == "1":
            id = input("Enter the ID: ")
            name = input("Enter the Name: ")
            phone = input("Enter the Phone number: ")
            email = input("Enter the Email: ")
            contact_manager.add_contact(id, name, phone, email)
        elif choice == "2":
            id = input("To update plz enter the ID: ")
            name = input("Enter the new Name: ")
            phone = input("Enter the new Phone number: ")
            email = input("Enter the new Email: ")
            contact_manager.update_contact(id, name, phone, email)
        elif choice == "3":
            id = input("To delete plz enter the ID: ")
            contact_manager.delete_contact(id)
        elif choice == "4":
            keyword = input("Enter the search word plz: ")
            contact_manager.search_contact(keyword)
        elif choice == "5":
            print("\nAll contacts:")
            for contact in contact_manager.contacts:
                print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        elif choice == "6":
            contact_manager.save_contacts_to_file(file_name)
        elif choice == "7":
            contact_manager.load_contacts_from_file(file_name)
        elif choice == "8":
            break
        else:
            print("Wrong option, Choose anthor one")

if name == "main":
    main()

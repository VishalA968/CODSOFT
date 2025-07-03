contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    keyword = input("Search by name or phone: ").lower()
    found = False
    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    search = input("Enter name of the contact to update: ").lower()
    for contact in contacts:
        if contact["name"].lower() == search:
            contact["name"] = input("Enter new name: ")
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address: ")
            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    search = input("Enter name of the contact to delete: ").lower()
    for contact in contacts:
        if contact["name"].lower() == search:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def menu():
    while True:
        print("Contact Manager ")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")
        print()
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the program
menu()

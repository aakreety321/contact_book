contacts = []

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    contacts.append({"name": name, "number": number})
    print("Contact added.")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['number']}")

def search_contact():
    name = input("Enter name to search: ")
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found: {contact['name']} - {contact['number']}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    view_contacts()
    num = input("Enter contact number to delete: ")
    if num.isdigit():
        index = int(num) - 1
        if 0 <= index < len(contacts):
            removed = contacts.pop(index)
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid number.")
    else:
        print("Invalid input.")

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")

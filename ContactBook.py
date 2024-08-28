import json
import os

contacts_file = 'contacts.json'

def sort_contacts():
    contacts = load_contacts()
    sorted_contacts = dict(sorted(contacts.items()))
    save_contacts(sorted_contacts)

def load_contacts():
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as file:
            return json.load(file)
    else:
        return {}

def save_contacts(contacts):
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file, indent=4)

def is_valid(phone, email):
    
    if not (phone.isdigit() and len(phone) == 10) :
        print("Invalid phone number. Please enter a 10-digit number.")
    if '@gmail.com' not in email:
        print("Invalid Gmail address. Please enter a valid Gmail address.")
        return False
    return True

def merge_duplicates():
    contacts = load_contacts()
    merged_contacts = {}

    for name, info in contacts.items():
        phone = info['Phone']
        email = info['Email']

        if name in merged_contacts:
            existing_info = merged_contacts[name]
            if phone != existing_info['Phone']:
                print(f"Conflict found for {name}:")
                print(f"1. {existing_info['Phone']}")
                print(f"2. {phone}")
                choice = input("Which phone number do you want to keep? (1/2): ")
                if choice == '2':
                    existing_info['Phone'] = phone

            if email != existing_info['Email']:
                print(f"Conflict found for {name}:")
                print(f"1. {existing_info['Email']}")
                print(f"2. {email}")
                choice = input("Which email do you want to keep? (1/2): ")
                if choice == '2':
                    existing_info['Email'] = email
        else:
            merged_contacts[name] = info
    save_contacts(merged_contacts)
    print("Duplicate contacts have been merged.")

def search_contact_partial(query):
    contacts = load_contacts()
    found_contacts = {}
    
    query = query.lower()
    
    for name, info in contacts.items():
        if query in name.lower():
            found_contacts[name] = info
    
    if found_contacts:
        print("Found contacts:")
        for name, info in found_contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print("--------------------")
    else:
        print("No contacts found matching your search query.")

def add_contact(name, phone, email):
    contacts = load_contacts()

    if not is_valid(phone, email):
        return

    if name in contacts:
        existing_phone = contacts[name]['Phone']
        existing_email = contacts[name]['Email']

        if phone == existing_phone and email == existing_email:
            print(f"Contact '{name}' already exists with the same phone number and email.")
            return
        else:
            print(f"Contact '{name}' already exists but with different details.")
            update_choice = input("Do you want to update the contact with the new details? (y/n): ")
            if update_choice.lower() == 'y':
                contacts[name] = {'Phone': phone, 'Email': email}
                save_contacts(contacts)
                print(f"Contact '{name}' updated successfully.")
            return

    contacts[name] = {'Phone': phone, 'Email': email}
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully.")

    merge_duplicates()

def view_contacts():
    contacts = load_contacts()
    
    if not contacts:
        print("\nNo contacts found.")
        return
    print("")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print("-"*20)  

"""def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        info = contacts[name]
        print(f"\nName: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
    else:
        print(f"\nContact '{name}' not found.")"""

def edit_contact(name):
    contacts = load_contacts()
    
    if name in contacts:
        print(f"\nEditing contact: {name}")
        current_phone = contacts[name]['Phone']
        current_email = contacts[name]['Email']
        
        new_phone = input(f"(current Number: {current_phone}) Enter new phone number : ") or current_phone
        new_email = input(f"(current: {current_email}) Enter new email address : ") or current_email
        
        contacts[name] = {'Phone': new_phone, 'Email': new_email}
        
        save_contacts(contacts)
        
        print(f"\nContact '{name}' updated successfully.")
    else:
        print(f"\nContact '{name}' not found.")

def delete_contact(name):
    contacts = load_contacts()
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"\nContact '{name}' deleted successfully.")
    else:
        print(f"\nContact '{name}' not found.")

def main():
    while True:
        print("\nContact Book Menu:")
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact: Can add partial name too")
        print("4. Delete Contact")
        print("5. Edit Contact")
        print("6. Exit")
        
        choice = input("\nChoose an option (1-6): ")
        
        if choice == '1':
            name = input("\nEnter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_contact(name, phone, email)
        
        elif choice == '2':
            view_contacts()
        
        elif choice == '3':
            query = input("Enter name or email to search: ")
            search_contact_partial(query)
        
        elif choice == '4':
            name = input("\nEnter Contact name to delete: ")
            delete_contact(name)
        
        elif choice == '5':
            name = input("\nEnter Contact name to edit: ")
            edit_contact(name)
        
        elif choice == '6':
            print("\nContact Book.")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
    sort_contacts()
    

import csv
from colours import *

class Contact:
    def __init__(self, name, surname, phone_number, email, address) -> None:
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} {self.surname} (Phone: {self.phone_number}, Email: {self.email}, Address: {self.address})"

class ContactBook:
    def __init__(self) -> None:
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")

    def save_to_csv(self):
        try:
            with open("contacts.csv", "w", newline='') as csv_file:
                fieldnames = ['Name', 'Surname', 'Phone Number', 'Email', 'Address']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()
                for contact in self.contacts:
                    writer.writerow(vars(contact))
            print("Contact list saved to contacts.csv successfully!")
        except Exception as e:
            print(f"Error saving contacts to file: {e}")

    def load_from_csv(self):
        try:
            with open("contacts.csv", "r", newline='') as csv_file:
                reader = csv.DictReader(csv_file)
                self.contacts = [Contact(**row) for row in reader]
            print("Contact list loaded from contacts.csv successfully!")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error loading contacts from file: {e}")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or
                   search_term.lower() in contact.phone_number]
        if results:
            print("Search Results:")
            for result in results:
                print(result)
        else:
            print("No matching contacts found.")

    def update_contact(self, search_term, updated_contact):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone_number:
                contact.name = updated_contact.name
                contact.surname = updated_contact.surname
                contact.phone_number = updated_contact.phone_number
                contact.email = updated_contact.email
                contact.address = updated_contact.address
                print(f"Contact {search_term} updated successfully!")
                return
        print(f"No matching contact found for {search_term}.")

    def delete_contact(self, search_term):
        self.contacts = [contact for contact in self.contacts if
                         search_term.lower() not in contact.name.lower() and
                         search_term.lower() not in contact.phone_number]
        print(f"{GREEN}{BOLD}Contact {search_term} deleted successfully!{RESET}")

def print_menu():
    print(f"""\n{CYAN}{BOLD}===== Contact Book Menu ====={RESET}
1. Add Contact
2. View Contact List
3. Search Contact
4. Update Contact
5. Delete Contact
6. Save and Exit""")

def main():
    contact_book = ContactBook()
    contact_book.load_from_csv()

    while True:
        try:
            print_menu()
            choice = input("Enter your choice (1-6): \n")

            if choice == "1":
                name = input(f"{CYAN}Enter Name:{RESET} ")
                surname = input(f"{CYAN}Enter Surname:{RESET} ")
                phone_number = input(f"{CYAN}Enter Phone Number:{RESET} ")
                email = input(f"{CYAN}Enter Email:{RESET} ")
                address = input(f"{CYAN}Enter Address:{RESET} ")
                new_contact = Contact(name, surname, phone_number, email, address)
                contact_book.add_contact(new_contact)
            elif choice == "2":
                contact_book.display_contacts()
            elif choice == "3":
                search_term = input(f"{CYAN}Enter Name or Phone Number to Search:{RESET} ")
                contact_book.search_contact(search_term)
            elif choice == "4":
                search_term = input(f"{CYAN}Enter Name or Phone Number to Update:{RESET} ")
                updated_name = input(f"{CYAN}Enter Updated Name: ")
                updated_surname = input(f"{CYAN}Enter Updated Surname:{RESET} ")
                updated_phone_number = input(f"{CYAN}Enter Updated Phone Number:{RESET} ")
                updated_email = input(f"{CYAN}Enter Updated Email: ")
                updated_address = input(f"{CYAN}Enter Updated Address:{RESET} ")
                updated_contact = Contact(updated_name, updated_surname, updated_phone_number, updated_email, updated_address)
                contact_book.update_contact(search_term, updated_contact)
            elif choice == "5":
                search_term = input(f"{CYAN}Enter Name or Phone Number to Delete:{RESET} ")
                contact_book.delete_contact(search_term)
            elif choice == "6":
                contact_book.save_to_csv()
                break
            else:
                print(f"{BRIGHT_RED}Invalid choice. Please enter a number between 1 and 6.{RESET}")

        except Exception as e:
            print(f"{BOLD}Error: {e}{RESET}")

if __name__ == "__main__":
    main()

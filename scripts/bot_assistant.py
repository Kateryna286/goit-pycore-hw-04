
def parse_input(user_input):
    """Parses the user's input into a command and its arguments."""
    
    parts = user_input.strip().lower().split()
    if not parts:
        return "", []
    return parts[0], parts[1:]

contacts = {}

def add_contact(args):
    """Adds a new contact with a phone number."""
    
    if len(args) != 2:
        return "Please provide name and phone number."
    
    name, phone = args

    if not name.isalpha():
        return "Name must contain only letters."
    if not phone.isdigit():
        return "Phone number must contain only digits."

    if name in contacts:
        return f"Contact {name.capitalize()} already exists with phone {contacts[name]}."
    
    contacts[name] = phone

    return f"Contact {name.capitalize()} added with phone {phone}."

def change_contact(args):
    """Changes an existing contact's phone number."""
    
    if len(args) != 2:
        return "Please provide name and new phone number."
    
    name, phone = args

    if not name.isalpha():
        return "Name must contain only letters."
    if not phone.isdigit():
        return "Phone number must contain only digits."
    
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name.capitalize()} updated to {phone}."
    else:
        return f"Contact {name.capitalize()} not found."

def show_phone(args):
    """Shows the phone number for a given contact."""
    
    if len(args) != 1:
        return "Please provide a name."
    
    name = args[0]

    if not name.isalpha():
        return "Name must contain only letters."
    
    return contacts.get(name, f"Contact {name.capitalize()} not found.")

def show_all(args):
    """Shows all stored contacts."""
    if not contacts:
        return "No contacts saved yet."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name.capitalize()}: {phone}")
    return "\n".join(result)


def main():
    """Main loop for handling user commands."""
    print("Welcome to your assistant bot!")
    while True:
        user_input = input(">>> ")
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Goodbye!")
            break
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all(args))
        elif command == "hello":
            print("How can I help you?")
        else:
            print("Unknown command. Try again.")


if __name__ == "__main__":
    main()

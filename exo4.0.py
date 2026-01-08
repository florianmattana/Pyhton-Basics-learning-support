# Create a dictionary with 3 contacts:
# Name, phone, email
    # contacts = {"Alice": {"phone": "0601020304", "email": "alice@email.com"}
 # Add 2 more contacts
# Display all information for a specific contact
# Add a new contact
# Modify an existing contact's phone number

contacts = { "Laura":{"phone": "0601020304", "email": "alice@email.com"},
            "Steph":{"phone": "0602030405", "email": "bob@email.com"},
            "Curry": {"phone": "0603040506", "email": "charlie@email.com"}}

contact_name = "Steph"
if contact_name in contacts :
    print(f"Information for {contact_name}:")
    print(f"Phone: {contacts[contact_name]['phone']}")
    print(f"Email: {contacts[contact_name]['email']}")
else:
    print(f"{contact_name} not found in contacts.")
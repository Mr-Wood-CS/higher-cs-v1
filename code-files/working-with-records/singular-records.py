from dataclasses import dataclass

@dataclass
class Contact:
    Name : str = ""
    Age : int = 0
    PhoneNumber : str = ""
    WhatsApp : str = ""
    Rating : float = 0.0

for count in range(4):

    contact = Contact()

    contact.Name = input("Enter name: ")
    contact.Age = int(input("Enter age: "))
    contact.PhoneNumber = input("Enter phone number: ")
    contact.WhatsApp = input("Enter WhatsApp (Yes/No): ")
    contact.Rating = float(input("Enter rating out of 10: "))

    print()
    print("Contact Details")
    print("---------------")
    print("Name:", contact.Name)
    print("Age:", contact.Age)
    print("Phone Number:", contact.PhoneNumber)
    print("WhatsApp:", contact.WhatsApp)
    print("Rating:", contact.Rating)
    print()

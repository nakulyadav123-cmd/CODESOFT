from datetime import datetime
from pickle import dump,load
from os import system

class contact_no:
    def __init__(self,name = "",email = "",mob_no = "",dob = ""):
        self.name = name
        self.email = email
        self.mob_no = mob_no
        self.DOB = dob
        self.createAt = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")


    def __str__(self):
        return(
f"""\033[33m---------------------------------------
Name      : {self.name}
Email Id  : {self.email}
Phone No  : {self.mob_no}
DOB       : {self.DOB}
Create At : {self.createAt}
""")


class contact_book :
    def __init__(self):
        self.list_of_contact = []
    
    def add_contact(self):
        contact = contact_no()
        print("---------------------------------")
        contact.name   = input("Enter Full Name       : ")
        contact.mob_no = input("Enter Phone No        : ")
        contact.email  = input("Enter Email Id        : ")
        contact.DOB    = input("Enter Dob(DD/MM/YYYY) : ")
        
        if contact.mob_no == "":
            print("Phone No is required")
        else:
            if contact.name == "":
                contact.name = contact.mob_no
            
            self.list_of_contact.append(contact)
            print("Contact Adding Successfully")
    
    def delete_contact(self):
        print("---------------------------------")
        name = input("Enter Name For Deleting Contact : ")
        for item in self.list_of_contact:
            if item.name == name:
                self.list_of_contact.remove(item)
                print("Deleting is Successfully")
                print(item)
                break
        else:
            print(f"{name} is not found in the database")

    
    def update_contact(self):
        print("---------------------------------")
        phone_no = input("Enter Phone No For Updating Contact : ")
        index = 0
        while(index < len(self.list_of_contact)):
            Data = self.list_of_contact[index]
            tempData = contact_no()
            if Data.mob_no == phone_no:
                print("---------------------------------")
                tempData.name   = input("Enter Full Name       : ")
                tempData.email  = input("Enter Email Id        : ")
                tempData.DOB    = input("Enter Dob(DD/MM/YYYY) : ")
                if tempData.name == "":
                    tempData.name = Data.name

                if tempData.email == "":
                    tempData.email = Data.email

                if tempData.DOB == "":
                    tempData.DOB = Data.DOB
                
                tempData.mob_no = phone_no
                tempData.createAt = Data.createAt
                print(tempData)
                self.list_of_contact[index] = tempData
                print("Updating is Successfully")
                break
            index += 1
        else:
            print(f"{phone_no} is not found in the database")

    
    def search_by_name(self):
        found = True
        name = input("Enter Name : ")
        for _ in self.list_of_contact:
            if _.name == name:
                print(_)
                found = False
        if found:
            print(f"{name} is not found in the database")

    def search_by_phone_no(self):
        phone_no = input("Enter Phone Number : ")
        for _ in self.list_of_contact:
            if _.mob_no == phone_no:
                print(_)
                break
        else:
            print(f"{phone_no} is not found in the database")

    def sorting_by_name(self):
        self.list_of_contact.sort(key=lambda data: data.name)

    def save_file(self):
        with open("contact_book.pkl", "wb") as file:
            dump(self.list_of_contact, file)

    def load_file(self):
        try:
            with open("contact_book.pkl", "rb") as file:
                self.list_of_contact = load(file)
        except FileNotFoundError:
            print("File not Found...?")

    def print_all_data(self):
        if len(self.list_of_contact):
            for _ in self.list_of_contact:
                print(_)
        else:
            print("No record found in the database")
    
    def home_page(self):
        self.load_file()
        while True:
            print("Welcome to contact book")
            print("------------------------")
            print("Enter 1 for Add Contact")
            print("Enter 2 for Update Contact")
            print("Enter 3 for Delete Contact")
            print("Enter 4 for Search Contact By Name")
            print("Enter 5 for Search Contact By Phone")
            print("Enter 6 for Display All Contacts")
            print("Enter 7 for Sorting Contacts")
            print("Enter 8 for Exit...!")
            choice = int(input("Enter your choice : "))
            system("clear")

            match(choice):
                case 1:
                    self.add_contact()
                    self.save_file()
                case 2:
                    self.update_contact()
                    self.save_file()
                case 3:
                    self.delete_contact()
                    self.save_file()
                case 4:
                    self.search_by_name()
                case 5:
                    self.search_by_phone_no()
                case 6:
                    self.print_all_data()
                case 7:
                    self.sorting_by_name()
                case 8:
                    print("Thank you for using contact book")
                    break
                case _:
                    print("Plzz enter valid choice")


obj = contact_book()

obj.home_page()

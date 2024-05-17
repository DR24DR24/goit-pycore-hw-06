
from collections import UserDict

class PhoneError(Exception):
       pass




class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)



class Name(Field):
    # реалізація класу
		pass



class Phone(Field):
    # реалізація класу
		pass



class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    # реалізація класу   
    def add_phone(self,phone:str):
        if len(phone)!=10 or not phone.isdigit():
               raise PhoneError
        self.phones.append(Phone(phone))

    def edit_phone(self,old_phone,new_phone):
        if len(new_phone)!=10 or not new_phone.isdigit():
               raise PhoneError
        try:
            fo=self.find_phone(old_phone)
            if fo==None:
                raise ValueError
            fo.value=new_phone
        except ValueError:
            print("No such number")
        except PhoneError:
            print("incorrect phone number")
        
    def find_phone(self,phone):
        phone_objects=[x for x in self.phones if x.value==phone]
        return phone_objects[0] if len(phone_objects)>0 else None
    
    def remove_phone(self,phone):
        p=self.find_phone(phone)
        if p:
            self.phones.remove(p)
            print("remove phone number")
        else:
            print("No such number")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"




class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):
        self.data = {}
    
    def add_record(self,record:Record):
        self.data[record.name.value]=record
        
    def find(self,user_name):
        return self.data[user_name]
    
    def delete(self,user_name):
        try:
            del self.data[user_name]
        except KeyError:
            print("no such user")
		


# Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
book.add_record(john_record)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

print(john_record.name.value)
print(list(book.keys()))    

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
john.remove_phone("1234567890")
john.remove_phone("1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
book.delete("Jane")

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)


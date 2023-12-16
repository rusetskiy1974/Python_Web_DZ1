from class_fields.name import Name
from class_fields.phone import Phone
from class_fields.date import Date
from class_fields.address import Address
from class_fields.mail import Mail
from address_book.address_book_record import AddressBookRecord


def input_value(value, clas):
    while True:
        print ('Enter', value,'>>>', end=' ' )
        result = input()
        try:
            result = clas(result)
            return result
        except:
            result


def add_contact(book):

    name = input_value('name', Name)
    date = input_value('date birthday', Date )
    phone = input_value('phone', Phone)
    mail = input_value('email', Mail)
    address = input_value('address', Address)
    record = AddressBookRecord(name, date, phone)
    book.add(record)

    print ('Contact added')



    



# add_contact()    
        


     
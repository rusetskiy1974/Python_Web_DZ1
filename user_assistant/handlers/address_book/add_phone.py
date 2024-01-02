from typing import Type

from user_assistant.address_book.address_book import AddressBook
from user_assistant.class_fields.name import Name
from user_assistant.class_fields.phone import Phone
from user_assistant.storages.storage import Storage
from user_assistant.handlers.input_value import input_value
from user_assistant.console.console import Console
from user_assistant.console.table_format.address_book_table import address_book_titles, get_address_book_row


def add_phone(book: AddressBook, storage: Type[Storage]):
    Console.print_tip('Press “Enter” with empty value to skip')
    prompts = list(el.name.value.casefold().strip() for el in  book.data.values())
   
    while True:
        name = input_value(value='contact name', class_field= Name, is_edit= True, prompts=prompts)


        if not name:
            return
        
        record = book.find(name.value)
        if record:
            break
        else:
            Console.print_error('Input existing name')

    new_phone = input_value('new phone', Phone, placeholder=Phone.PHONE_FORMAT_EXAMPLE)
    record.add_phone(new_phone)
    storage.update(book.data.values()) 

    Console.print_table('Updated contact phone', address_book_titles, [get_address_book_row(record)])

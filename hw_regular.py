import re
import csv
from pprint import pprint

csv_file = 'phonebook_raw.csv'
regular_pattern = '(8|\+7)?\s*(\(*)(\d{3})(\)*)(\s*|-)(\d{3})(\s*|-)(\d{2})(\s*|-)(\d{2})\s*(\(*)(\w\w\w\.)*\s*(\d{4})*(\))*'
mask = r'+7(\3)\6-\8-\10 \12\13'

class Phone_book():
            
      def get_data(self, file):
          self.file = file
          with open(file, encoding='utf-8') as f:
             line = csv.reader(f, delimiter=",")
             contacts_list = list(line)
          return contacts_list
        
      def sort_contact(self, arr):
          contact_arr = list()
          for contact in arr:
              new_contact = list()
              name = ",".join(contact[:3])
              result = re.findall(r'(\w+)', name)
              while len(result) < 3:
                  result.append('')
              new_contact += result
              new_contact.append(contact[3])
              new_contact.append(contact[4])
              phone_pattern = re.compile(regular_pattern)
              changed_phone = phone_pattern.sub(mask, contact[5])
              new_contact.append(changed_phone)
              contact_arr.append(new_contact)
          return  contact_arr
        
      def fix_contact(self, fix_arr):
          phone_book = dict()
          for contact in fix_arr:
            if contact[0] in phone_book:
               contact_v = phone_book[contact[0]]
               for i in range(len(contact_v)):
                  if contact[i]:
                     contact_v[i] = contact[i]
            else:
              phone_book[contact[0]] = contact
              
          return list(phone_book.values())
              
      def write_file(self, arr):
          with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
               writer = csv.writer(f, delimiter=',')
               writer.writerows(arr)
            

phone_book = Phone_book()

main_list_csv = phone_book.get_data(csv_file)

new_parsed_list = phone_book.sort_contact(main_list_csv)

clear_contact = phone_book.fix_contact(new_parsed_list)

phone_book.write_file(clear_contact)
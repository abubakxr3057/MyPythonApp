print('Contact Book')
contact_list={}
while True:
  print('1 to Add phone and number ')
  print('2 to View Contacts')
  print('3 to Search Contacts')
  print('4 to Remove Contacts')
  print('5 to Quit Program')
  choice=int(input('Enter your choice : '))
  if choice==1:
    while True:
      name=input('Enter contact name : ').capitalize()
      phone=input('Enter phone number : ')
      contact_list[name]=phone
      choice_1=input('Want to add more contact yes/no : ').capitalize()
      if choice_1=='No':
        print('Okay')
        break
  elif choice==2:
    print(contact_list)
  elif choice==3:
    search=input('Enter a contact name : ').capitalize()
    for key in contact_list.keys():
      if search in key:
        print('Number of ',search,' is : ',contact_list[search])
      else:
        print('Contact not found')
  elif choice==4:
    delete_contact=input('Enter contact name you want to remove : ').capitalize()
    if delete_contact in contact_list:
      contact_list.pop(delete_contact)
      print('Contact removed')
    else:
      print('Contact not founded')
  elif choice==5:
    print('Goodbye')
    break
print('TO - DO - APP')
item=[]
while True:
  print('Press 1 to add item')
  print('Press 2 to view list of items')
  print('Press 3 to Delete  item')
  print('Press 4 to quit program')
  user_choice=int(input('Enter your choice : '))
  if user_choice==1:
   while True :
      item_1=input('Enter an item : ').capitalize()
      item.append(item_1)
      select=input('want to add another item : yes/no : ').capitalize()
      if select=='No':
        print('OKAY')
        break
  elif user_choice==2:
    for i,char in enumerate(item,1):
        print(i,char)
  elif user_choice==3:
    deleting=input('Enter item you want to remove : ').capitalize()
    try:
         item.remove(deleting)
         print('Item removed')
    except:
      print('Wrong input')
  elif user_choice==4:
     print('Okay')
     break
  else :
    print('You make a wrong choice...')
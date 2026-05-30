print('Daily Expense Tracker')
expenses={}
while True:
 print('1 to add expense : ')
 print('2 to view expenses :')
 print('3 to remove expense :')
 print('4 to see total amount of expenses:')
 print('5 to quit program')
 choose=int(input('Enter your choice :'))
 if choose==1:
  while True:
    expense_name=input('Enter name of thing where you spend : ').capitalize()
    expense_amount=int(input('Enter amount you spend on  : '))
    expenses[expense_name]=expense_amount
    again=input('Want to add more? yes/no : ').capitalize()
    if again=='No':
      print('Okay')
      break
 elif choose==2:
     for key,value in expenses:
        print(key,value)
 elif choose==5:
     print('Okay')
     break

 elif choose==3:
     removal=input('Enter expense name you want to remove : ').capitalize()
     if removal in expenses:
         expenses.pop(removal)
         print('Removed successfully')
     else:
        print('Not removed')
 elif choose==4:
   total=0
   for i in expenses.values():
     total+=i
   print(total,' rupees')
 else:
  print('Wrong choice')
  
     

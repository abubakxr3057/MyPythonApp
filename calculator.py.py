print('Assalam-U-Alaikum')
while True :

      number_1=int(input('Enter 1st number : '))
      number_2=int(input('Enter 2nd number : '))
      print('which operation you want to perform?')
      print('Enter 1 for +')
      print('Enter 2 for -')
      print('Enter 3 for /')
      print('Enter 4 for *')
      select=int(input('Enter your choice : '))
      if select==1 : 
          print(number_1+number_2)
      elif select==2 :
          if number_1>number_2 :
              print(number_1-number_2)
          else:
              print(number_2-number_1)
      elif select==3 :
          if number_1==0 or number_2==0:
              print('This cannot divided by 0')
          elif number_1>number_2 :
              print(int(number_1/number_2))
          elif number_2>number_1 :
              print(int(number_2/number_1))
      elif select==4 :
          print(number_1*number_2)
      select_1=input('Want to perform operation again? yes/no : ').capitalize()
      if select_1=='No':
          print('OKAY')
          break
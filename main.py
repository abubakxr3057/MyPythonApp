print('NUMBER GUESSING GAME')
import random
while True:
    total=0
    nums=random.randint(1,100)
    while True:
        total+=1
        choice=int(input('Guess the number : '))
        if choice==nums:
            print('You won the game')
            print('Total guesses : ',total)
            break
        elif choice>nums:
            print('TOO high')
        elif choice<nums:
            print('Too low')
    answer=input('Play again?(yes/no) : ')
    if answer=='no':
        print('Thanks for playing')
        break
from random import randrange

sum = 0
while sum < 21:
    print('You have', sum, 'points.')
    answer = input('Turn card? ')
    if answer == 'Yes':
        Card = randrange(2, 11)
        print("You've got number", card)
        sum = sum + card
    elif answer == 'no':
         break
    else:
        print('I do not understand! Answer "yes" or "no"'  

if sum == 21:
    print('Congratulations! You won!')
elif sum > 21:
    print('Bad luck!', sum, 'points is too much!')
else:
    print('So close! You missed', 21 - sum, 'points!')i


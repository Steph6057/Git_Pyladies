pc_choice = 'rock'
user_choice = input('rock, paper, or scissors?')

if user_choice == 'rock':
    if pc_choice == 'rock':
        print('draw.')
    elif pc_choise == 'scissors':
        print('you win!')
    elif pc_choice == 'paper':
        print('computer won!')
elif user_choice == 'scisssors':
    if pc_choice == 'rock':
        print('computer won!')
    elif pc_choice == 'scissors':
          print('draw')
    elif pc_choice == 'paper':
          print('you win!')
elif user_choice == 'paper':
    if pc_choice == 'rock':
        print('you win!')
    elif pc_choice == 'scissors':
          print('computer won!')
    elif pc_choice == 'paper':
          print('draw')
else:
    print('I dont understand .')



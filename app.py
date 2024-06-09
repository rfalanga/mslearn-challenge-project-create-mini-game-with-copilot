# write 'Hello World' to the console
# print('Hello World')

# accept input from user. The input must be either rock, paper or scissors. If the input is not any of the three, print 'Invalid input'
input = input('Enter rock, paper or scissors: ')
if input == 'rock' or input == 'paper' or input == 'scissors':
    print('Valid input')
else:
    print('Invalid input')

# Choose, at random, either rock, paper or scissors. Print the computer's choice
import random
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
print(f'Computer choice: {computer_choice}')

# Compare input to computer's choice. Print 'You win' if you win, 'You lose' if you lose, 'It\'s a draw' if it's a draw
if input == computer_choice:
    print('It\'s a draw')
elif input == 'rock' and computer_choice == 'scissors':
    print('You win')
elif input == 'paper' and computer_choice == 'rock':
    print('You win')
elif input == 'scissors' and computer_choice == 'paper':
    print('You win')
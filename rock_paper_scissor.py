import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_of_images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for paper 2 for scissors.\n"))
if user_input < 0 or user_input > 2:
  print("You have entered an invalid number. You lose")
else:
  print(list_of_images[user_input])

  computer_input = random.randint(0, 2)
  print("Computer chose:")
  print(list_of_images[computer_input])

  if user_input == computer_input:
    print("It's a draw")
  elif user_input == 2 and computer_input == 0:
    print("You lose")
  elif user_input == 0 and computer_input == 2:
    print("You win!")
  elif user_input < computer_input:
    print("You lose")
  elif user_input > computer_input:
    print("You win!")

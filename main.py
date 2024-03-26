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

#Write your code below this line 👇
game_image = [rock, paper, scissors]
import random

you = int(input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if you >= 0 and you <= 2:
    print(game_image[you])
    computer = random.randint(0, 2)
    print("computer chose:")
    print(game_image[computer])
    outcome = [you, computer]
    if outcome == [0, 1] or outcome == [1, 2] or outcome == [2, 0]:
        print("you lose")

    elif outcome == [0, 2] or outcome == [1, 0] or outcome == [2, 1]:
        print("you win")

    else:
        print("it's a draw")

else:
    print("you chose an invalid number you lose")
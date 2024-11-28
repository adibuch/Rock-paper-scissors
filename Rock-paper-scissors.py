import random

option = {
    0 : "Rock",
    1 : "Paper",
    2 : "Scissors"
}

choise = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''','''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
          ''']

your_choise = int(input("Enter 0 to rock, enter 1 to paper or enter 2 to scissors "))
computer_choise = random.randint(0,2)
print(choise[your_choise])
print(choise[computer_choise])
if option[your_choise] == "Rock":

    if option[computer_choise] == "Rock":
        print("Try again.")
    elif option[computer_choise] == "Paper":
        print("You are lose:(")
    elif option[computer_choise] == "Scissors":
        print("You are win!!")
elif option[your_choise] == "Paper":
    if option[computer_choise] == "Rock":
        print("You are win!!")
    elif option[computer_choise] == "Paper":
        print("Try again.")
    elif option[computer_choise] == "Scissors":
        print("You are lose:(")
elif option[your_choise] == "Scissors":
    if option[computer_choise] == "Rock":
        print("You are lose:(")
    elif option[computer_choise] == "Paper":
        print("You are win!!")
    elif option[computer_choise] == "Scissors":
        print("Try again.")
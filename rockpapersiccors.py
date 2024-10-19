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
random_toss = random.choice(["rock", "paper", "scissors"])
if random_toss == "rock":
    print(rock)
elif random_toss == "paper":
    print(rock)
else:
    print(scissors)
print(random_toss)

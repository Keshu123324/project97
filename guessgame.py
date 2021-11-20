import random
number=random.randint(1,9)
guess=int(input("Guess a number (between 1 and 9):"))
chances=1
while chances<5:
 guess=int(input("Guess a number (between 1 and 9):"))
 if guess==number:
     print("Congratulations you won!!!")
     break
 elif(guess>number):
     print("Your guess was too high guess a number lower than ",guess)
 else:
     print("Your guess was too low guess a number higher than ",guess)
 chances=chances+1
 if not chances<5:
  print("You lose!!! The number is ",number)

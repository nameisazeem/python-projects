"""import random
print("Welcome to the number guessing game")

#rand int function to generate the random number b/w 1 to 100
number = random.randint(1,100)

#number of chances to be given to the user to guess the number or it is the
#inputs given by user into input box here no.of chances are 5
chances = 0
print("Guess a number (b/w 1 to 100): ")
#while loop to count the number of chances
while chances < 5:
    #Enter a number 1 to 100
    guess = int(input())

    #compare the user entered number with the number to be guessed
    if guess == number:
        print("Congratulation, YOU WIN!!!")
        break
    elif guess<number:
        print("Your guess was too low",guess)
    else:
        print("Your guess was too high",guess)
    chances += 1

if not chances < 5:
    print("YOU LOSE!!! The number is: ",number)

print("Thanks for playing. Come Again!!")    """



import random
print("\nWelcome To The Game\n")
number = random.randint(1,100)
chances = 0
print("Guess a number b/w 1 to 100 : ")
while chances < 5:
    guess = int(input())
    if guess == number:
        print("Hurray!! You Win!!!")
    elif guess < number:
        print("Your guess is too low: ")
    else:
        print("Your guess is too high: ")
    chances +=1

if not chances < 5:
    print("You Lose!!! The number is:", number)

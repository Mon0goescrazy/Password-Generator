import random
import sys

chars = input("Enter 15 characters you would like your password to have (use 6 letters, 3 capital letters, 3 symbols and 3 numbers for better generation): ")

password = ''
for x in range(8):
    password += random.choice(chars)

password2 = ''
for x in range(8):
    password2 += random.choice(chars)

password3 = ''
for x in range(8):
    password3 += random.choice(chars)
    

print("here is your password: " + password )
answer = input("Generate again? (y or n)")
if answer.lower() == 'y':
    print("here is your password: " + password2 )
if answer.lower() == 'n':
    print("Thanks for using")
    sys.exit()
answer2 = input("Generate again? (y or n)")
if answer2.lower() == 'y' :
    print("here is your password: " + password3 )
    print("Thanks for using")
if answer2.lower() == 'n' :
    print("Thanks for using")
    sys.exit()

    

        











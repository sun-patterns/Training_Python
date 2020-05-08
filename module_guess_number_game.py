#Guess the number game

import random

def get_numberRange(start_num, end_num):
    start_num = int(input("Enter the starting number "))
    end_num = int(input("Enter the ending number "))
    if start_num > end_num:
        print("Starting number is greater than ending number. Please enter once again")
        get_numberRange(start_num, end_num) 
    return(start_num, end_num)




glmt = int(input("Enter a guess limit - Number of times you would like to guess the number "))
a_num =0
e_num =0

a_num,e_num = get_numberRange(a_num,e_num)

number = random.randrange(a_num, e_num)

i=0
while i<glmt:
    g_number=int(input("Guess the number"))
    if g_number == number:
        print("Congratulations ! You have won the game")
        break
    if g_number < number:
        print("You guessed the wrong number and it is low")
    elif g_number > number:
        print("You guessed the wrong number and it is high")
    i=i+1
    if i == glmt:
        print ("Guess limit is over")
    


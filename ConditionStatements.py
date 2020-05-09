
'''#A3 Q1
name = input('What is your name?\n')
age = int(input('What is your age?\n'))

if age < 25:
    print('You are young!\n')
else:
    print ('You are old!\n')


#A3 Q2

amount=int(input('Amount to withdraw:'))

if amount>2000:
    print('Insufficient Balance')

  
#A3 Q3
print('Program to find the largest number among the three input numbers\n')
n1 = int(input('Enter the first number\n'))
n2 = int(input('Enter the second number\n'))
n3 = int(input('Enter the third number\n'))

if n1 > n2:
    if n1 > n3:
        n4 = n1
    else:
        n4=n3
elif n2>n3:
    n4 = n2
else:
    n4 = n3
  
print('The largest number between %s, %s and %s is %s\n' %(n1,n2,n3,n4))

'''
#A3 Q4
print('Ask for time and wish Good Morning, Afternoon, Evening or Night (Use 24 hours time) Morning - 5am to 12pm Afternoon - 12pm to 4pm Evening - 4pm to 7pm Night - 7pm to 11pm\n')
morlist = [5,6,7,8,9,10,11]
aftlist = [12,13,14,15]
evelist = [16,17,18]
ngtlist = [19,20,21,22,23,24]

tmp =float(input('Enter your time:\n'))

if (tmp >5 and tmp < 12):
    wish = "Good Morning"

if tmp in aftlist:
    wish ="Good Afternoon"

if tmp in evelist:
    wish = "Good Evening"

if tmp in ngtlist:
    wish = "Good Night"

print("Hi,%s" %(wish))

'''
#A3 Q5
print('Welcome to the quiz. You will be asked 3 questions. If you answer all the 3 correctly, then you win the quiz')

a1 = int(input('How many colours are there in Indian National Flag?\n'))
a2 = input('Who is the current President of India?\n')
a3 = int(input('How many states are there in India in 2020?\n'))

if a1 == 4 and a2 == "Ram Nath Kovind" and a3 == 28:
      print("Winner")
else:
    print ('Better luck next time')

'''



















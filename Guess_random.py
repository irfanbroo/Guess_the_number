import random
guess = 0
upper_bound = input("Enter the upper Bound: ")
if upper_bound.isdigit():
    upper_bound = int(upper_bound)
    if upper_bound <0:
        print("enter a value greater than 0 ")
        quit()
else:
    print("Please type a number :) ")    
    quit()
r = random.randint(0,upper_bound)
while True:
    guess +=1
    answ = input("Enter the number you guessed: ")
    if answ.isdigit():
        answ = int(answ)
    else:
        print("Please type a valid number :) ")    
        continue
    if answ == r:
        print("yipee!")
        break
    elif answ>r:
        print("its smaller than the number u entered")
    else:
        print("Its greater than the number you  entered ")
print("You made it in " + str(guess) +"guesses " )
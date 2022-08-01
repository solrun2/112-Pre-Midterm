target = 72
cnt = 0
while True :
    guess = int(input("Enter your guess: "))
    cnt += 1
    if guess < 0 or guess > 100 :
        print("Sorry, your guess is out of range.")
    elif guess < target :
        print("Sorry, your guess is too low.")
    elif guess > target :
        print("Sorry, your guess is too high.")
    else : 
        print("Congratulations, your guess is correct.")
        print("Total number of guesses is {}.".format(cnt))
        break
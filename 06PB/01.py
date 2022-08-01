target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))
x, y = target, guess
post_cnt = 0
while True :
    if y == 0 :
        break
    if x % 10 == y % 10 :
        post_cnt += 1
    x = x // 10
    y = y // 10
if post_cnt == 4 :
    print("Congratulations, you just mastered my mind!!")
else :
    digit_cnt = 0
    x, y = target, guess
    i = 0
    while i<4 :
        d = x % 10
        j = 0
        while j<4 :
            c = y % 10
            if c == d :
                digit_cnt += 1
            y = y // 10
            j += 1
        y = guess
        x = x // 10
        i += 1
    digit_cnt = digit_cnt - post_cnt
    if post_cnt == 0 :
        post = "No positions correct, "
    elif post_cnt == 1 :
        post = "One position correct, "
    elif post_cnt == 2 :
        post = "Two positions correct, "
    elif post_cnt == 3 :
        post = "Three positions correct, "
    if digit_cnt == 0 :
        digit = "no digits correct"
    elif digit_cnt == 1 :
        digit = "one digit correct"
    elif digit_cnt == 2 :
        digit = "two digits correct"
    elif digit_cnt == 3 :
        digit = "three digits correct"
    elif digit_cnt == 4 :
        digit = "four digits correct"
    print(post + digit)
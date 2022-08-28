str_day = input()
num_day = int(input())
i = 0
if str_day == 'Monday' and (num_day > 0 and num_day <= 31):
    i = 1
    f = (num_day-1) % 7 
    fd = i + f
    if fd == 1 :
        print('Monday')
    elif fd == 2 :
        print('Tuesday')
    elif fd == 3 :
        print('Wednesday')
    elif fd == 4 :
        print('Thursday')
    elif fd == 5 :
        print('Friday')
    elif fd == 6 :
        print('Saturday')
    elif fd == 0 :
        print('Sunday')
    
elif str_day == 'Tuesday'and (num_day > 0 and num_day <= 31):
    i = 2
    f = (num_day-1) % 7 
    fd = i + f
    if fd == 1 :
        print('Monday')
    elif fd == 2 :
        print('Tuesday')
    elif fd == 3 :
        print('Wednesday')
    elif fd == 4 :
        print('Thursday')
    elif fd == 5 :
        print('Friday')
    elif fd == 6 :
        print('Saturday')
    elif fd == 0 :
        print('Sunday') 
elif str_day == 'Wednesday'and (num_day > 0 and num_day <= 31):
    i = 3
    f = (num_day-1) % 7 
    fd = i + f
    if fd == 1 :
        print('Monday')
    elif fd == 2 :
        print('Tuesday')
    elif fd == 3 :
        print('Wednesday')
    elif fd == 4 :
        print('Thursday')
    elif fd == 5 :
        print('Friday')
    elif fd == 6 :
        print('Saturday')
    elif fd == 0 :
        print('Sunday') 
elif str_day == 'Thursday'and (num_day > 0 and num_day <= 31):
    i = 4
    f = (num_day-1) % 7 
    fd = i + f
    if fd == 1 :
        print('Monday')
    elif fd == 2 :
        print('Tuesday')
    elif fd == 3 :
        print('Wednesday')
    elif fd == 4 :
        print('Thursday')
    elif fd == 5 :
        print('Friday')
    elif fd == 6 :
        print('Saturday')
    elif fd == 0 :
        print('Sunday')
elif str_day == 'Friday'and (num_day > 0 and num_day <= 31):
    i = 5
    f = (num_day-1) % 7 
    fd = i + f
    if fd == 1 :
        print('Monday')
    elif fd == 2 :
        print('Tuesday')
    elif fd == 3 :
        print('Wednesday')
    elif fd == 4 :
        print('Thursday')
    elif fd == 5 :
        print('Friday')
    elif fd == 6 :
        print('Saturday')
    elif fd == 0 :
        print('Sunday')
elif str_day == 'Saturday'and (num_day > 0 and num_day <= 31):
    i = 6
    f = (num_day-1) % 7 
    fd = i + f
    if fd == 1 :
        print('Monday')
    elif fd == 2 :
        print('Tuesday')
    elif fd == 3 :
        print('Wednesday')
    elif fd == 4 :
        print('Thursday')
    elif fd == 5 :
        print('Friday')
    elif fd == 6 :
        print('Saturday')
    elif fd == 0 :
        print('Sunday')
 
elif str_day == 'Sunday'and (num_day > 0 and num_day <= 31):
    i = 7
    f = (num_day-1) % 7 
    fd = i + f
    if fd == 1 :
        print('Monday')
    elif fd == 2 :
        print('Tuesday')
    elif fd == 3 :
        print('Wednesday')
    elif fd == 4 :
        print('Thursday')
    elif fd == 5 :
        print('Friday')
    elif fd == 6 :
        print('Saturday')
    elif fd == 0 :
        print('Sunday')
else :
    print('ERROR')
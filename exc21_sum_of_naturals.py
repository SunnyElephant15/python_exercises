while True:
    number = int(input('Enter your number: '))
    y = 0
    for x in range(number + 1):
        y = x + y
    print(f'Sum of {number} is: {y} ')

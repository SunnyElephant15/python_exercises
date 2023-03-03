import math
numbers = []
while True:
    number = (input('Enter your number: '))
    if number == '':
        LCM = math.lcm(numbers)
        print(f'Your LCM is: {LCM}')
    else:
        numbers.append(int(number))

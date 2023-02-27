while True:
    num = int(input('Input number: '))
    fact = float(1)
    numbers = ''
    separator = '*'
    i = 1
    while i <= num:
        fact *= i
        numbers += str(i)
        i += 1
    new_numbers = separator.join(numbers)
    print(f'factorial = {new_numbers} = {fact}')

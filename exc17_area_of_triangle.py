import math

numbers = input('Enter your numbers, separating them with comas: \n')
numbers_split = numbers.split(',')
s = (0.5 * (int(numbers_split[0]) + int(numbers_split[1]) + int(numbers_split[2])))
sa = (s - int(numbers_split[0]))
sb = (s - int(numbers_split[1]))
sc = (s - int(numbers_split[2]))
multiple = sa * sb * sc
multiples = multiple * s
area = math.sqrt(multiples)
print(f'Area of your triangle is: {area}')

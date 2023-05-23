number1 = int(input('Enter your first number: '))
number2 = int(input('Enter your second number: '))


def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


print("The H.C.F. is", compute_hcf(number1, number2))

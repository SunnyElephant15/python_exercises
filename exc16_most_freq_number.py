from collections import Counter

while True:
    numbers = input('Enter your numbers, separating them with comas: ')
    numbers_split = numbers.split(',')
    occurence_count = Counter(numbers_split)
    most_common = occurence_count.most_common(1)[0][0]
    print(f'Most frequent is: {most_common}')
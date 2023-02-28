while True:
    letters = input('Enter your letters, separating them with comas: ')
    letters_split = letters.split(',')
    letters_sorted = sorted(letters_split)
    print(f'Your letters sorted: {letters_sorted}')
    
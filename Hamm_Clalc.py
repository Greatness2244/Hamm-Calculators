bot: str = 'hamm'
print(f'supp chikko i\'m {bot}best driver in world')

while True:
    user: str = input('Greatness: ').lower()

    if user == 'quit':
        print(f'{bot}: byeee')
        break
    elif user in ['sup','hello','mylord']:
        print(f'{bot}:what??')
    elif user in ['wanna do basic maths']:
        print(f'{bot}: Sure why not?!!')

        try:
            num1: float = (float(input('gimme the 1st: ')))
            num2: float = (float(input('gimme the 2nd: ')))
            print(f'{bot}: What do you want to do with {num1} and {num2}??')

            opp = input('opp: ').lower()

            if opp == 'add':
                print(f'{bot}:dats: {num1 + num2}')
            elif opp == 'sub':
                print(f'{bot}:dats: {num1 - num2}')
            elif opp == 'mult':
                print(f'dats: {num1 * num2}')
            elif opp == 'div':
                print(f'dats: {num1/num2}')

        except ValueError:
            print(f'{bot}: These aint numbers')
    else:
        print(f'{bot}: English Mister!!')

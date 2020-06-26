from random import randint

answer = randint(1, 10)

'''Running using terminal: import sys
    answer = randint(int(sys.argv[1]), int(sys.argv[2]))
    in while loop:
    guess = int(input(f'guess a number {sys.argv[1]}~{sys.argv[2]}:  '))
 '''

while True:
    guess = int(input('Guess a number between 1-10:  '))
    try:
        if 0 < guess < 11:
            if guess == answer:
                print('Guessing Matched!!')
                break
        else:
            print('hey bozo, I said 1 to 10!!?')

    except ValueError:
        print('Please enter a number')
        continue

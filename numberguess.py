import random
print('Number Guessing Game')
number = random.randint(1,20)
chances = 0
print('Guess a number between 1 and 20!')

while chances < 5:
    ans = int(input('Enter your guess : '))
    if ans == number:
        print('Congratulations, You Won!')
        break

    elif ans < number:
        print('You guess was too low , try guessing a number higher than', ans)

    elif ans > number:
        print('You guess was too high, try guessing a number lower than' , ans)

    chances +=1

if not chances < 5:
    print('You Lost!Try again later')
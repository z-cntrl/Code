###############################################################################
# Author: Chloe Weber
# Date: 3/9/21
# Description A program that returns two series of numbers on separate lines
#and asks the user to give the correct answer, if they pass it says one thing if they don't it says wrong
###############################################################################
import random as r

def random_number(digit):

    if digit == 2:
        num = r.randrange(10,100,1)
        return num
    if digit == 3:
        num = r.randrange(100, 1000, 1)
        return num

def main():
    fig_one = random_number(2) #Sending 2 across as digit, which returns as num = fig_one
    print(f'{fig_one: 5d}')
    fig_two = random_number(3) #Sending 3 to random_number as digit, returns as num which is = to fig_two
    print(f'+{fig_two: 3d}') #rewatchin 'passing arguments' lecture
    print('-----')

    ans = int(input('= '))
    correct_answer = fig_one + fig_two
    if ans != correct_answer:
        print(f'Incorrect. The correct answer is {correct_answer}.')
    else:
        print('Correct -- Good Work!')    # Write your mainline logic here ------------------------------------------

# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()

################################################################################
# Author: Chloe Weber
# Date: 3/2/2021
# Description program that checks if a user inputted number is prime or not
################################################################################
def main():
    while True:
        n = int(input(f'Enter a positive integer (-1 to quit): '))
        if n == -1:
            break
        if n <= 0:
            print(f'Invalid input.')
        elif is_prime(n) == False:
            print(f'{n} is not a prime number.')
        elif is_prime(n) == True:
            print(f'{n} is a prime number.')
            #is_prime(n)
#    n = int(input(f'Enter a positive integer (-1 to quit): '))# Write your 'mainline logic' here
    #print(f'{is_prime(n): } is a prime number.')
#    print(f'{is_prime(int):} is not a prime number.')
def is_prime(n):# Write function(s) here
    #while True:
    #    n =int(input(f'Enter a positive integer (-1 to quit): '))
    #    if n <= 1:
    #        print(f'Invalid input.') #no prints only true or false
    n_sq= int(n**(1/2)) +1
    if n == 1:
        return False
    for i in range(2,n_sq):
        if n%i == 0:
            return False
    return True
#    elif (n%2 == 0):
#        return True
#    else:
#        return False

if __name__ == '__main__':
    main()

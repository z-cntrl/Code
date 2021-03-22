################################################################################
# Author: Chloe Weber
# Date: 3/2/21
# Description Builds from prime_numbers to list all numbers between 2 and user
# max input to
################################################################################

## Write function(s) below

def main():

    n = int(input('Enter a positive integer: '))
    prime_list = [] #super confused how to make this list
#    for num in range(2,n+1)
#    count = 0
#    for i in range(1,num+1):
#        if is_prime(n) == True:

    print(f'The primes up to {n} are: ', end='')
    for n in prime_list:
#        while True:
#            n = int(input('Enter a positive integer: '))
        print(*prime_list, sep=', ')


def is_prime(n): # Write function(s) here
        n_sq= int(n**(1/2)) +1
        if n == 1:
            return False
        for i in range(2,n_sq):
            if n%i == 0:
                return False
        return True

if __name__ == '__main__':
    main()

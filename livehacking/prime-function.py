import sys

numbers = [int(sn) for sn in sys.argv[1:]]

def is_prime(number):
    if number == 1:
        return False

    for divisor_candidate in range(2, number):
        if number % divisor_candidate == 0:
            return False

    return True

for number in numbers:
    if is_prime(number):
        print(number, 'prime')
    else:
        print(number, 'not prime')

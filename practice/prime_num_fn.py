# Check whether number is prime 
def is_prime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # number is not a prime
        divisor += 1

    return True  # number is prime

def print_prime_numbers(number_of_primes):
    number_of_primes_per_line = 10  # Display 10 per line
    count = 0  # Count the number of prime numbers
    number = 2  # A number to be tested for primeness

    # Repeatedly find prime numbers
    while count < number_of_primes:
        # Print the prime number and increase the count
        if is_prime(number):
            count += 1  # Increase the count

            print(number, end=' ')
            if count % number_of_primes_per_line == 0:
                # Print the number and advance to the new line
                print()

        # Check if the next number is prime
        number += 1


def main():
    print('The first 50 prime numbers are')
    print_prime_numbers(50)


main()  # Call the main function

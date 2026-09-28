from NUMBER_THEORY.Learn.gcd_learning_mod import gcd_learning
from NUMBER_THEORY.Learn.Prime_number_learning import check_prime
from NUMBER_THEORY.Learn.Prime_factor_learning import prime_factors

from NUMBER_THEORY.common_c.common_codes_main_page_working import *


def gcd():

    print("\n\tGCD\n")

    fst = option_input("Enter first number: ")
    sec = option_input("Enter second number: ")

    print("\nStarting GCD algorithm...")
    press_enter()

    result = gcd_learning(fst, sec)

    print("\nResult:")
    print("GCD =", result)


def prime_num():

    print("\n\tPRIME NUMBER\n")

    number = option_input("Enter a number: ")

    print("\nStarting prime number algorithm...")
    press_enter()

    result = check_prime(number)

    print("\nResult:")

    if result:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")


def prime_factor():

    print("\n\tPRIME FACTORIZATION\n")

    number = option_input("Enter a number: ")

    if number <= 0:
        print("Please enter a positive number.")
        return

    print("\nStarting prime factorization...")
    press_enter()

    Factors = prime_factors(number)

    print("\nPrime Factors:", Factors)


def main():

    programming = True

    while programming:

        print("""
        
      
              PYTHON ALGORITHM LEARNING
       

        NUMBER THEORY

            1. GCD
            2. Prime Number
            3. Prime Factorization
            0. Main Page
            4. Exit


                """)

        option = option_input("Enter your requirement: ")

        if option == 1:
            programming = start_lesson(gcd)

        elif option == 2:
            programming = start_lesson(prime_num)

        elif option == 3:
            programming = start_lesson(prime_factor)

        elif option == 0:
            return

        elif option == 4:

            print("""
            
            Thank you for joining us.

            Keep Learning and Enjoying!
            """)

            programming = False

        else:
            print("\nPlease enter a number from 0 to 4.")
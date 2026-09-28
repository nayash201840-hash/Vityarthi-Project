from SEQUENCES.Learn.Fibonic_series_learning import fibonacci_series
from SEQUENCES.Learn.factoral import factorial_series

from SEQUENCES.common_c.common_codes_main_page_working import *


def fibonacci():

    print("\n\tFIBONACCI SERIES\n")

    terms = option_input("Enter number of terms: ")

    if terms <= 0:
        print("Number of terms should be greater than 0.")
        return

    print("\nStarting Fibonacci algorithm...")
    press_enter()

    fibonacci_series(terms)


def factorial():

    print("\n\tFACTORIAL SERIES\n")

    n = option_input("Enter number of terms: ")

    if n < 1:
        print("Please enter a positive number of terms.")
    else:
        factorial_series(n)


def main():

    programming = True

    while programming:

        print("""

                
              PYTHON ALGORITHM LEARNING


        SEQUENCES

            1. Fibonacci Series
            2. Factorial Series
            0. Main Page
            3. Exit


                """)

        option = option_input("Enter your requirement: ")

        if option == 1:
            programming = start_lesson(fibonacci)

        elif option == 2:
            programming = start_lesson(factorial)

        elif option == 0:
            return

        elif option == 3:

            print("""
            
            Thank you for joining us.

            Keep Learning and Enjoying!
            """)

            programming = False

        else:
            print("\nPlease enter a number from 0 to 3.")
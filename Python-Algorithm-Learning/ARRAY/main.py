from ARRAY.Learn.Array_count import count_occurrences
from ARRAY.Learn.Array_revesel import array_reverse
from ARRAY.Learn.Kth_smallest import kth_smallest

from ARRAY.common_c.common_codes_main_page_working import *


def reversal():

    print("\n\tARRAY REVERSAL\n")

    numbers = list_of_values()

    print("\nOriginal array:", numbers)

    print("\nStarting array reversal...")
    press_enter()

    result = array_reverse(numbers)

    print("\nReversed array:", result)


def counting():

    print("\n\tARRAY OCCURRENCE COUNT\n")

    numbers = list_of_values()

    print("\nArray:", numbers)

    element = option_input("Enter element to count: ")

    print("\nStarting counting...")
    press_enter()

    result = count_occurrences(numbers, element)

    print("\nResult:")
    print(element, "occurs", result, "time(s).")


def kth():

    print("\n\tKTH SMALLEST ELEMENT\n")

    numbers = list_of_values()

    print("\nArray:", numbers)

    while True:

        k = option_input("Enter the value of K: ")

        if 1 <= k <= len(numbers):
            break

        print("K should be between 1 and", len(numbers))

    print("\nStarting Kth smallest algorithm...")
    press_enter()

    result = kth_smallest(numbers, k)

    print("\nResult:")
    print("Kth smallest element =", result)


def main():

    programming = True

    while programming:

        print("""
        
        
              PYTHON ALGORITHM LEARNING
        

        ARRAY ALGORITHMS

            1. Array Reversal
            2. Array Occurrence Counting
            3. Kth Smallest Element
            0. Main Page
            4. Exit

        
        """)

        option = option_input("Enter your requirement: ")

        if option == 1:
            programming = start_lesson(reversal)

        elif option == 2:
            programming = start_lesson(counting)

        elif option == 3:
            programming = start_lesson(kth)

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
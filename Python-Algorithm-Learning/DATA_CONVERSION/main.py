from DATA_CONVERSION.Learn.Hex_to_Dec import dec_to_hex
from DATA_CONVERSION.Learn.binay_to_dec import binary_to_decimal

from DATA_CONVERSION.common_c.common_codes_main_page_working import *


def dec_to_hex_run():

    print("\n\tDECIMAL TO HEXADECIMAL\n")

    number = option_input("Enter a decimal number: ")

    print("\nOriginal Decimal:", number)

    print("\nStarting Decimal conversion...")
    press_enter()

    result = dec_to_hex(number)

    print("\nHexadecimal:", result)


def binary_to_integer_run():

    print("\n\tBINARY TO DECIMAL\n")

    number = input("Enter a binary number: ")

    print("\nOriginal Binary:", number)

    print("\nStarting Binary conversion...")
    press_enter()

    result = binary_to_decimal(number)

    print("\nDecimal:", result)


def main():

    programming = True

    while programming:

        print("""
        
       
              PYTHON ALGORITHM LEARNING

              
        DATA CONVERSION

            1. Decimal to Hexadecimal
            2. Binary to Decimal
            0. Main Page
            3. Exit

        
        """)

        option = option_input("Enter your requirement: ")

        if option == 1:
            programming = start_lesson(dec_to_hex_run)

        elif option == 2:
            programming = start_lesson(binary_to_integer_run)

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
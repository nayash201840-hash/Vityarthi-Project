from NUMBER_THEORY.main import main as number_main
from ARRAY.main import main as array_main
from SEQUENCES.main import main as sequence_main
from DATA_CONVERSION.main import main as data_conversion_main


def main():

    programming = True

    while programming:

        print("""
        
        
              PYTHON ALGORITHM LEARNING
      
              

            1. Number Theory
            2. Array Algorithms
            3. Sequences
            4. Data Conversion
            5. Exit

        
        """)

        option = input("Enter your requirement: ")

        if option == "1":
            number_main()

        elif option == "2":
            array_main()

        elif option == "3":
            sequence_main()

        elif option == "4":
            data_conversion_main()

        elif option == "5":

            print("""
            
            Thank you for joining us.

            Keep Learning and Enjoying!
            """)

            programming = False

        else:
            print("\nPlease enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
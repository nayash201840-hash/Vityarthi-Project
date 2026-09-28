def converter(data):

    numbers = []

    for i in data.split():
        numbers.append(int(i))

    return numbers


def list_of_values():

    while True:

        values = input("Enter numbers separated by spaces: ")

        if values == "":
            print("Please enter some numbers.")
            continue

        numbers = converter(values)

        return numbers


def option_input(message):

    while True:

        number = input(message)

        if number == "":
            print("Please enter something.")
            continue

        if number.isdigit():
            return int(number)

        print("Please enter a number.")


def press_enter():

    input("\nPress Enter to continue...")


def lesson_finished():

    while True:

        print("""
            1. Repeat lesson
            2. Main menu
            3. Exit
        """)

        option = input("\nEnter a number: ")

        if option == "1":
            return "repeat"

        elif option == "2":
            return "menu"

        elif option == "3":
            return "exit"

        else:
            print("\nSelect from given option")


def start_lesson(lesson):

    while True:

        lesson()

        To_do = lesson_finished()

        if To_do == "repeat":
            continue

        elif To_do == "menu":
            return True

        elif To_do == "exit":
            return False
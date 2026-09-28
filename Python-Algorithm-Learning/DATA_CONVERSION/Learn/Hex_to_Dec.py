def dec_to_hex(number):

    digits = "0123456789ABCDEF"

    print("\nStarting Decimal to Hexadecimal Conversion")
    print("Given decimal number:", number)

    step = 1
    dec_num = number
    hex_num = []

    while dec_num > 0:

        remain_digit = dec_num // 16
        convert_digit = dec_num % 16

        print(f"""
        
        Step: {step}
        
        ---> Division: {dec_num} // 16 = {remain_digit}
        ---> Remainder: {dec_num} % 16 = {convert_digit}
        """)

        hex_digit = digits[convert_digit]

        print("Hexadecimal digit:", hex_digit)

        hex_num.append(hex_digit)

        dec_num = remain_digit

        print("New number:", dec_num)

        input("\nPress Enter to continue...")

        step += 1

    print("\nAll divisions completed!")

    print("Collected digits:", hex_num)

    hexadecimal = ""

    print("\nReading remainders in reverse order...")

    for digit in reversed(hex_num):

        hexadecimal = hexadecimal + digit

        print("Current hexadecimal:", hexadecimal)

        input("\nPress Enter to continue...")

    print("\nConversion completed!")
    print("Hexadecimal number:", hexadecimal)

    return hexadecimal
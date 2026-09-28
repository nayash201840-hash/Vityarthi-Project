def binary_to_decimal(binary):

    decimal = 0
    power = 0

    print("\nStarting Binary to Decimal Conversion")
    print("Binary number:", binary)

    if not binary or any(digit not in "01" for digit in binary):
        print("Invalid binary number!")
        return None

    for digit in reversed(binary):

        value = int(digit)
        position_value = value * (2 ** power)

        print(f"""
        -----------------------------
        Digit: {digit}
        Position: {power}
        -----------------------------

        Calculation: {digit} * 2 ** {power}
        Position value: {position_value}
        """)

        decimal = decimal + position_value

        print("Current decimal value:", decimal)

        input("\nPress Enter to continue...")

        power += 1

    print("\nConversion completed!")
    print("Decimal number:", decimal)

    return decimal
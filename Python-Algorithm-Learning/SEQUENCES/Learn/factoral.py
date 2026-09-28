def factorial_series(terms):

    factorial = 1

    print("\nStarting Factorial Series")
    print("Number of terms:", terms)

    for i in range(1, terms + 1):

        factorial = factorial * i

        print(f"""
        -----------------------------
        Term: {i}
        -----------------------------

        Previous factorial: {factorial // i}
        Multiplication: {factorial // i} * {i}
        New factorial: {factorial}
        """)

        print("Factorial:", i, "! =", factorial)

        input("\nPress Enter to continue...")

    print("\nFactorial series completed!")
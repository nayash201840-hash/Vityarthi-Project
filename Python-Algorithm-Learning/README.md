# Python Algorithm Learning

Python Algorithm Learning is a menu-driven program for students who want to study common algorithms through small examples. It groups number theory, array algorithms, sequences, and data conversion in one application. Students can run algorithms, answer topic or mixed practice questions, and review session accuracy and topic results.

## Main features

- Four categories with independent menus.
- Number theory: GCD, prime check, prime factorization, and LCM.
- Arrays: reversal, occurrence counting, kth smallest, linear search, and bubble sort.
- Sequences: Fibonacci series, factorial, and string to integer list.
- Conversions: decimal to hexadecimal and binary to decimal.
- Topic and randomized mixed practice with session performance summaries.

## Run the program

Install Python 3.10 or later. No third-party packages are needed to run the application.

`python main.py`

Choose a category from the main menu. Enter `0` in a category menu to return to the main menu. Enter `0` at the main menu to exit.

## Test

Run the built-in checks with:

`python -m unittest discover -s tests -v`

## Project structure

```text
main.py                    Main navigation
practice.py                Shared quiz and session summary
1.NUMBER THEORY/           Number theory menu
2.ARRAY_ALGORITHMS/        Array menu
3.SEQUENCES/               Sequence menu
4.DATA CONVERSION/         Conversion menu
tests/                     Automated checks
assets/diagrams/           Architecture and workflow images
screenshots/               Screenshot availability note
```

The computer-use environment did not expose a desktop application for full-screen capture. The screenshots folder explains this limitation and includes supplementary test evidence instead.

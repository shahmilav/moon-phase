"""This module contains a method that prints out the moon phase.

Based on the user_input, the information printed is different.

Using the moon phase provided by AgeToPhase.get_moon_phase, it prints out
the moon phase.
"""
from termcolor import colored


class PrintResult:
    """This class contains the PRINT_RESULT method."""

    def __init__(self):
        pass

    def print_result(user_input, month, day_of_month, year, moon_phase):
        """Print out the moon phase using the information provided."""
        if user_input == 'today':
            print("\nThe phase today is ", end="")
            print(colored(moon_phase, 'green'), end=".\n\n")

        elif user_input == 'date':
            print("The phase on ", end="")
            print(int(month), end="/")
            print(int(day_of_month), end="/")
            print(int(year), end=" is ")
            print(colored(
                moon_phase,
                'green',
            ), end=".\n\n")

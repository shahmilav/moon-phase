"""This module contains a method that prints out the moon phase.
It does not calculate anything, it is just a helper method to print out the
phase provided by AgeToPhase.get_moon_phase()."""
from termcolor import colored


class PrintResult:
    """This class contains the print_result method"""

    def print_result(self, user_input, month, day_of_month, year, moon_phase):
        """This method prints out the moon phase
        using the information provided."""

        if user_input == 'today':
            print("\nThe phase today is ", end="")
            print(colored(moon_phase, 'green'), end=".\n\n")
        elif user_input == 'date':
            print("The phase on ", end="")
            print(int(month), end="/")
            print(int(day_of_month), end="/")
            print(int(year), end=" is ")
            print(colored(moon_phase, 'green', ), end=".\n\n")

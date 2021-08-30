"""Contains a method that converts the Julian Day into the moon age.

The possible ages are not 100% accurate. The moon age is
always < 0 and > 29.5306.

Using Julian Day, the method runs through a series of calculations to
determine the moon age.
"""
from termcolor import colored


class FindMoonAge:
    """Has the function to find the moon age."""

    def find_moon_age(self, user_input, julian_day):
        """Use a julian day, this function returns the moon age.

        If the user inputted 'age', it also prints out the result,
        the moon age.
        """
        lunar_cycle = 29.5306

        days_since_new_moon = julian_day - 2451549.5
        new_moons = days_since_new_moon / lunar_cycle
        moon_age = (new_moons - int(new_moons)) * lunar_cycle

        if user_input == 'age':
            print("\nThe moon age is", end=" ")
            print(colored(moon_age, 'green'), end=" days\n\n")

        return moon_age

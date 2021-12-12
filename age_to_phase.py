"""This module contains a method that converts the moon age into a phase.

The phases are ['New Moon', 'Waxing Cresent', 'First Quarter',
                'Waxing Gibbous', 'Full Moon', 'Waning Gibbous',
                'Last Quarter', 'Waning Crescent']

Using the moon age, the method runs through a series of if-statements to
determine the moon phase.

"""
from termcolor import cprint


# Takes the moon age and converts it into the phase of the moon.
class AgeToPhase:
    """Contains the method that gets the moon phase."""

    def get_moon_phase(self, moon_age):
        """Take in the moon age, and convert it into the moon phase."""
        if 0 <= moon_age <= 1:
            moon_phase = "New Moon 🌑"
        elif 1 < moon_age < 7:
            moon_phase = "Waxing Crescent 🌒"
        elif 7 <= moon_age <= 8:
            moon_phase = "First Quarter 🌓"
        elif 8 < moon_age < 15:
            moon_phase = "Waxing Gibbous 🌔"
        elif 15 <= moon_age <= 16:
            moon_phase = "Full Moon 🌕"
        elif 16 < moon_age < 22:
            moon_phase = "Waning Gibbous 🌖"
        elif 22 <= moon_age <= 23:
            moon_phase = "Last Quarter 🌗"
        elif 23 < moon_age < 29.5306:
            moon_phase = "Waning Crescent 🌘"
        else:
            # In case of an invalid date. Anything before 1/6/2000.
            cprint(
                "Given date is invalid. Only dates after " "1/6/2000 work.",
                "red",
                attrs=["blink"],
            )
            return 0

        return moon_phase

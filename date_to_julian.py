"""This module contains a method that converts the date into a Julian Day.

The date is provided in 3 variables, 'day_of_month', 'month', and 'year'.

Using the date, the method runs through a series of calculations provided
by https://www.subsystems.us/uploads/9/8/9/4/98948044/moonphase.pdf
to determine the Julian Day.
"""


class DateToJulian:
    """Contains a method that takes the date, and converts into Julian Date."""

    def date_to_julian(self, day_of_month, month, year):
        """Convert a given date into a Julian Day.
        You are not expected to understand this. 
        """
        if month in (1, 2):
            year = year - 1
            month = month + 12

        v = (year / 100)
        w = v / 4
        x = 2 - v + w
        year = 365.25 * (year + 4716)
        z = 30.6001 * (month + 1)
        julian_day = x + day_of_month + year + z - 1524.5

        return julian_day

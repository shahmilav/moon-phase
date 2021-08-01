class DateToJulian():

    # Converts any date into Julian format.

    def dateToJulian(day_of_month, month, year):

        if (month == 1 or month == 2):
            year = year - 1
            month = month + 12

        v = (year / 100)
        w = v / 4
        x = 2 - v + w
        year = 365.25 * (year + 4716)
        z = 30.6001 * (month + 1)
        julian_day = x + day_of_month + year + z - 1524.5

        return julian_day

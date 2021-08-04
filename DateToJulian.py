class DateToJulian():


    # Handles calculations that convert a given date into a Julian Day.
    
    def dateToJulian(dayOfMonth, month, year):

        if (month == 1 or month == 2):
            year = year - 1
            month = month + 12

        v = (year / 100)
        w = v / 4
        x = 2 - v + w
        year = 365.25 * (year + 4716)
        z = 30.6001 * (month + 1)
        julianDay = x + dayOfMonth + year + z - 1524.5

        return julianDay

class DateToJulian():

    # Converts any date into Julian format.

    def dateToJulian(d, m, y):

        if (m == 1 or m == 2):
            y = y - 1
            m = m + 12

        v = (y / 100)
        w = v / 4
        x = 2 - v + w
        y = 365.25 * (y + 4716)
        z = 30.6001 * (m + 1)
        julianDay = x + d + y + z - 1524.5

        return julianDay

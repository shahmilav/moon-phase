class FindMoonAge():

    # Takes today's julian_day and converts it into the moon_age.

    def findMoonAge(julian_day):
        lunar_cycle = 29.5306

        days_since_new_moon = julian_day - 2451549.5
        new_moons = days_since_new_moon / lunar_cycle
        moon_age = (new_moons - int(new_moons)) * lunar_cycle

        return moon_age

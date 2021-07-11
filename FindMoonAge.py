class FindMoonAge():

    # Takes today's julianDay and converts it into the moonAge.

    def findMoonAge(julianDay):
        lunarCycle = 29.5306

        daysSinceNewMoon = julianDay - 2451549.5
        newMoons = daysSinceNewMoon / lunarCycle
        moonAge = (newMoons - int(newMoons)) * lunarCycle

        return moonAge

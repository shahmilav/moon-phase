class AgeToPhase():

    # Takes the moonAge and converts it into the currentPhase of the moon.

    def getMoonPhase(moonAge):

        if (0 <= moonAge and 1 >= moonAge):
            currentPhase = 'New Moon'
        elif (1 < moonAge and moonAge < 7):
            currentPhase = 'Waxing Cresent'
        elif (7 <= moonAge and 8 >= moonAge):
            currentPhase = 'First Quarter'
        elif (8 < moonAge and moonAge < 15):
            currentPhase = 'Waxing Gibbous'
        elif (15 <= moonAge and 16 >= moonAge):
            currentPhase = 'Full Moon'
        elif (16 < moonAge and moonAge < 22):
            currentPhase = 'Waning Gibbous'
        elif (22 <= moonAge and 23 >= moonAge):
            currentPhase = 'Last Quarter'
        elif (23 < moonAge and moonAge < 29.5306):
            currentPhase = 'Waning Gibbous'
        else:
            print("error, moon age is invalid")
            return

        print("The current phase is " + currentPhase)
        print(round(moonAge, 2))

        return currentPhase

class AgeToPhase():

    # Takes the moonAge and converts it into the currentPhase of the moon.

    def getMoonPhase(moon_age, yes_no, day_of_month, month, year):

        if (0 <= moon_age and 1 >= moon_age):
            moon_phase = 'New Moon'
        elif (1 < moon_age and moon_age < 7):
            moon_phase = 'Waxing Cresent'
        elif (7 <= moon_age and 8 >= moon_age):
            moon_phase = 'First Quarter'
        elif (8 < moon_age and moon_age < 15):
            moon_phase = 'Waxing Gibbous'
        elif (15 <= moon_age and 16 >= moon_age):
            moon_phase = 'Full Moon'
        elif (16 < moon_age and moon_age < 22):
            moon_phase = 'Waning Gibbous'
        elif (22 <= moon_age and 23 >= moon_age):
            moon_phase = 'Last Quarter'
        elif (23 < moon_age and moon_age < 29.5306):
            moon_phase = 'Waning Gibbous'
        else:
            print("error, moon age is invalid")
            return

        if(yes_no == 'n'):
            print("The phase today is " + moon_phase)
        elif(yes_no == 'y'):
            print("The phase on ", end="")
            print(int(month), end="/")
            print(int(day_of_month), end="/")
            print(int(year), end=" ")
            print("is " + moon_phase)

        return moon_phase

from termcolor import colored


class AgeToPhase():

    # Takes the moon age and converts it into the phase of the moon.

    def getMoonPhase(moonAge, userInput, dayOfMonth, month, year):

        if (0 <= moonAge and 1 >= moonAge):
            moonPhase = 'New Moon'
        elif (1 < moonAge and moonAge < 7):
            moonPhase = 'Waxing Cresent'
        elif (7 <= moonAge and 8 >= moonAge):
            moonPhase = 'First Quarter'
        elif (8 < moonAge and moonAge < 15):
            moonPhase = 'Waxing Gibbous'
        elif (15 <= moonAge and 16 >= moonAge):
            moonPhase = 'Full Moon'
        elif (16 < moonAge and moonAge < 22):
            moonPhase = 'Waning Gibbous'
        elif (22 <= moonAge and 23 >= moonAge):
            moonPhase = 'Last Quarter'
        elif (23 < moonAge and moonAge < 29.5306):
            moonPhase = 'Waning Gibbous'
        else:
            # In case of and invalid moon age.
            print("error, moon age is invalid")
            return

        if(userInput == 'today'):
            print("\nThe phase today is ", end = "")
            print(colored(moonPhase, 'green'))
        elif(userInput == 'date'):
            print("The phase on ", end="")
            print(int(month), end="/")
            print(int(dayOfMonth), end="/")
            print(int(year), end=" is ")
            print(colored(moonPhase, 'green'))

        return moonPhase

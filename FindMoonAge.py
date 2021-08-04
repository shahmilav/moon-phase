from termcolor import colored

class FindMoonAge():

    # Takes a given dates Julian Day and converts it into the moon aage.

    def findMoonAge(julianDay, userInput):
        lunarCycle = 29.5306

        daysSinceNewMoon = julianDay - 2415020    
        newMoons = daysSinceNewMoon / lunarCycle
        moonAge = (newMoons - int(newMoons)) * lunarCycle

        if(userInput == 'age'):
            print("\nThe moon age is", end = " ")
            print(colored(moonAge, 'green') , end = " days\n")

        return moonAge

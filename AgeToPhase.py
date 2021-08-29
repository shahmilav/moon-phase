from termcolor import colored


# Takes the moon age and converts it into the phase of the moon.

class AgeToPhase():
    def get_moon_phase(moon_age, user_input, day_of_month, month, year):

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
            # In case of an invalid date. Anything before 1/6/2000.
            print(colored("Error, given date is invalid. Only dates after "
                          "1/6/2000 work.", 'red', attrs=['blink']))
            return

        if(user_input == 'today'):
            print("\nThe phase today is ", end="")
            print(colored(moon_phase, 'green'), end=".\n")
        elif(user_input == 'date'):
            print("The phase on ", end="")
            print(int(month), end="/")
            print(int(day_of_month), end="/")
            print(int(year), end=" is ")
            print(colored(moon_phase, 'green', ), end=".\n")

        return moon_phase

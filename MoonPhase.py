from termcolor import colored

from AgeToPhase import AgeToPhase
from DateToJulian import DateToJulian
from FindMoonAge import FindMoonAge
from datetime import datetime


class MoonPhase():

    # Starting screen: options are displayed.
    print(colored("\nMOON PHASE CALCULATOR", 'magenta', attrs=['bold']))

    # User types 'date' to pass a date.
    print("\nTo pass a date, enter", end=" ")
    print(colored("\'date\'", 'cyan'))

    # User enters 'today' to get today's moon phase.
    print("To get today's phase, enter", end=" ")
    print(colored("\'today\'", 'cyan'))

    # User enters 'age' to get current moon age
    print("To get the moon age, enter", end=" ")
    print(colored("\'age\'", 'cyan'))

    # Get user input
    user_input = input('Which action would you like to take: ')

    # Assigning functions local names
    date_to_julian = DateToJulian.date_to_julian
    get_moon_phase = AgeToPhase.get_moon_phase
    find_moon_age = FindMoonAge.find_moon_age

    if(user_input == 'date'):

        # Date entered in string format is converted into datetime format.
        date_time_string = input('\nEnter any date (mm/dd/yy): ')
        date_time = datetime.strptime(date_time_string, '%m/%d/%y')

        # Getting day of month, month, and year of date passed.
        # Used for calculations.
        day_of_month = date_time.day
        year = date_time.year
        month = date_time.month

        # Passes information into DateToJulian class,
        # in turn passed to FindMoonAge, in turn passed to AgeToPhase.
        get_moon_phase(
            find_moon_age(
                date_to_julian(
                    day_of_month, month, year),
                user_input),
            user_input, day_of_month, month, year)

    elif(user_input == 'today'):

        # Today's date info is converted into three seperate variables/
        day_of_month = float(datetime.now().day)
        month = float(datetime.now().month)
        year = float(datetime.now().year)

        # Passes information into DateToJulian class,
        # in turn passed to FindMoonAge, in turn passed to AgeToPhase.
        get_moon_phase(
            find_moon_age(
                date_to_julian(
                    day_of_month, month, year),
                user_input),
            user_input, day_of_month, month, year)

    elif(user_input == 'age'):

        # Gets current info using datetime.now(),
        # and converts date into three seperate variables.
        day_of_month = float(datetime.now().day)
        month = float(datetime.now().month)
        year = float(datetime.now().year)

        # Information is passed into DateToJulian class,
        # which passes it to FindMoonAge. Class AgeToPhase is not needed.
        find_moon_age(
            date_to_julian(
                day_of_month, month, year),
            user_input)

    # In case the user did not enter a valid input ('date', 'today', or 'age').
    else:
        print(colored(
            "Please enter a valid input", 'red'))

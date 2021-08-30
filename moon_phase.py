"""This module is the main module for the Moon Phases project. When you need to
find the Moon phase for any day, or moon age for today, run this file."""
from datetime import datetime
from termcolor import colored
from age_to_phase import AgeToPhase
from date_to_julian import DateToJulian
from print_result import PrintResult
from find_moon_age import FindMoonAge


class MoonPhase:
    """Main class, run when you need to find the moon phase"""
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

    # Assigning local names to functions
    date_to_julian = DateToJulian.date_to_julian
    get_moon_phase = AgeToPhase.get_moon_phase
    find_moon_age = FindMoonAge.find_moon_age
    print_result = PrintResult.print_result

    if user_input == 'date':

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
        # Printed using print_result.
        julian_day = date_to_julian(DateToJulian, day_of_month, month, year)
        moon_age = find_moon_age(FindMoonAge, user_input, julian_day)
        moon_phase = get_moon_phase(AgeToPhase, moon_age)
        print_result(PrintResult, user_input,
                     month, day_of_month, year, moon_phase)

    elif user_input == 'today':

        # Today's date info is converted into three seperate variables/
        day_of_month = float(datetime.now().day)
        month = float(datetime.now().month)
        year = float(datetime.now().year)

        # Passes information into DateToJulian class,
        # in turn passed to FindMoonAge, in turn passed to AgeToPhase.
        # Printed using print_result.
        julian_day = date_to_julian(DateToJulian, day_of_month, month, year)
        moon_age = find_moon_age(FindMoonAge, user_input, julian_day)
        moon_phase = get_moon_phase(AgeToPhase, moon_age)
        print_result(PrintResult, user_input,
                     month, day_of_month, year, moon_phase)

    elif user_input == 'age':

        # Gets current info using datetime.now(),
        # and converts date into three seperate variables.
        day_of_month = float(datetime.now().day)
        month = float(datetime.now().month)
        year = float(datetime.now().year)

        # Information is passed into DateToJulian class,
        # which passes it to FindMoonAge. Class AgeToPhase is not needed.

        julian_day = date_to_julian(DateToJulian, day_of_month, month, year)
        moon_age = find_moon_age(FindMoonAge, user_input, julian_day)

    # In case the user did not enter a valid input ('date', 'today', or 'age').
    else:
        print(colored(
            "Please enter a valid input", 'red'))

from AgeToPhase import *
from DateToJulian import *
from FindMoonAge import *
from datetime import datetime

from termcolor import colored


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

    userInput = input('Which action would you like to take: ')


    if(userInput == 'date'):

        # Date entered in string format is converted into datetime format.
        dateTimeStr = input('\nEnter any date (mm/dd/yy): ')
        dateTimeObj = datetime.strptime(dateTimeStr, '%m/%d/%y')

        # Getting day of month, month, and year of date passed. Used for calculations.
        dayOfMonth = dateTimeObj.day
        year = dateTimeObj.year
        month = dateTimeObj.month

        # Passes information into DateToJulian class, in turn passed to FindMoonAge, in turn passed to AgeToPhase.
        AgeToPhase.getMoonPhase(
            FindMoonAge.findMoonAge(
                DateToJulian.dateToJulian(dayOfMonth, month, year), userInput), userInput, dayOfMonth, month, year)

    elif(userInput == 'today'):

        # Today's date info is converted into three seperate variables/
        dayOfMonth = float(datetime.now().day)
        month = float(datetime.now().month)
        year = float(datetime.now().year)

        # Passes information into DateToJulian class, in turn passed to FindMoonAge, in turn passed to AgeToPhase.
        AgeToPhase.getMoonPhase(
            FindMoonAge.findMoonAge(
                DateToJulian.dateToJulian(dayOfMonth, month, year), userInput), userInput, dayOfMonth, month, year)

    elif(userInput == 'age'):

        # Gets current info using datetime.now(), and converts date into three sepeate variables.
        dayOfMonth = float(datetime.now().day)
        month = float(datetime.now().month)
        year = float(datetime.now().year)

        # Information is passed into DateToJulian class, which passes it to FindMoonAge. Class AgeToPhase is not needed.
        FindMoonAge.findMoonAge(
                DateToJulian.dateToJulian(dayOfMonth, month, year), userInput)

    # In case the user did not enter a valid input ('date', 'today', or 'age').
    else:
        print(colored("Please enter a valid input", 'red'))

from AgeToPhase import *
from DateToJulian import *
from FindMoonAge import *
from datetime import datetime


class MoonPhase():

    day_of_month = float(datetime.now().day)
    month = float(datetime.now().month)
    year = float(datetime.now().year)

    yes_no = input('Would you like to pass a date? y/n: ')

    if(yes_no == 'y'):

        month = float(input('enter month: '))
        day_of_month = float(input('enter day of month: '))
        year = float(input('enter year: '))

    AgeToPhase.getMoonPhase(
        FindMoonAge.findMoonAge(
            DateToJulian.dateToJulian(day_of_month, month, year)), yes_no, day_of_month, month, year)

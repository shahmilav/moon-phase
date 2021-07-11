from AgeToPhase import *
from DateToJulian import *
from FindMoonAge import *
from datetime import datetime


class MoonPhase():

    d = float(datetime.now().day)
    m = float(datetime.now().month)
    y = float(datetime.now().year)

    AgeToPhase.getMoonPhase(
        FindMoonAge.findMoonAge(
            DateToJulian.dateToJulian(d, m, y)))

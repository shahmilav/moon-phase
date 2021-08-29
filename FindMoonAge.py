from termcolor import colored


# Takes a given dates Julian Day and converts it into the moon age.
class FindMoonAge():

    def find_moon_age(julian_day, user_input):
        lunar_cycle = 29.5306

        days_since_new_moon = julian_day - 2451549.5
        new_moons = days_since_new_moon / lunar_cycle
        moon_age = (new_moons - int(new_moons)) * lunar_cycle

        if(user_input == 'age'):
            print("\nThe moon age is", end=" ")
            print(colored(moon_age, 'green'), end=" days\n")

        return moon_age

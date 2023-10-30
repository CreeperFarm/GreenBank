# Import of libraries
import tkinter as tk
from tkinter import ttk


# Calulate grade by vehicule type


def grade_vehicule(vehicule_type):

    # If vehicule type is citadine, the eco note is 8/10
    if (vehicule_type == "citadine"):
        # Print the eco note on the terminal
        print("The eco note is 8/10 for a citadine")

        # Define the grade of the vehicule (8/10)
        grade_eco_vehicule = 8

    # If vehicule type is cabriolet, the eco note is 6/10
    elif (vehicule_type == "cabriolet"):

        # Print the eco note on the terminal
        print("The eco note is 6/10 for a cabriolet")

        # Define the grade of the vehicule (6/10)
        grade_eco_vehicule = 6

    # If vehicule type is berline, the eco note is 6.5/10
    elif (vehicule_type == "berline"):

        # Print the eco note on the terminal
        print("The eco note is 6.5/10 for a berline")

        # Define the grade of the vehicule (6.5/10)
        grade_eco_vehicule = 6.5

    # If vehicule type is suv or 4x4, the eco note is 4/10
    elif (vehicule_type == "suv" or vehicule_type == "4x4"):

        # Print the eco note on the terminal
        print("The eco note is 4/10 for a suv or 4x4")

        # Define the grade of the vehicule (4/10)
        grade_eco_vehicule = 4

    # If vehicule type is not recognized, the eco note is 'err'
    else:

        # Print the error message on the terminal
        print("The type of vehicule is not recognized, the existing one are : citadine, cabriolet, berline, suv, 4x4")

        # Define and error as grade of the vehicule ('err')
        grade_eco_vehicule = "err-unknown"

    # Return the grade of the vehicule to the main program
    return grade_eco_vehicule

# Calculate grade by energy type of the car


def grade_energy(energy_type):

    # If energy type of the car is electric, the eco note is 9/10
    if (energy_type == "electrique"):

        # Print the eco note on the terminal
        print("The eco note is 9/10 for an electric car")

        # Define the grade of the energy (9/10)
        grade_eco_energy = 9

    # If energy type of the car is hybrid, the eco note is 7/10
    elif (energy_type == "hybrid"):

        # Print the eco note on the terminal
        print("The eco note is 7/10 for a hybrid car")

        # Define the grade of the energy (7/10)
        grade_eco_energy = 7

    # If energy type of the car is gas, the eco note is 6/10
    elif (energy_type == "gaz"):

        # Print the eco note on the terminal
        print("The eco note is 6/10 for a gas car")

        # Define the grade of the energy (6/10)
        grade_eco_energy = 6

    # If energy type of the car is essence, the eco note is 5/10
    elif (energy_type == "essence"):

        # Print the eco note on the terminal
        print("The eco note is 5/10 for an essence car")

        # Define the grade of the energy (5/10)
        grade_eco_energy = 5

    # If energy type of the car is diesel, the eco note is 4/10
    elif (energy_type == "diesel"):

        # Print the eco note on the terminal
        print("The eco note is 4/10 for a diesel car")

        # Define the grade of the energy (4/10)
        grade_eco_energy = 4
    
    else:

        # Print the error message on the terminal
        print("The type of energy is not recognized, the existing one are : electric, hybrid, gaz, essence, diesel")

        # Define and error as grade of the energy ('err')
        grade_eco_energy = "err-unknown"

    # Return the grade of the energy to the main program
    return grade_eco_energy

# Calculate grade by number of kilometers of the car (mileage per year)


def grade_mileage(mileage):

    # If mileage is under 5000 km per year, the eco note is 10/10 (This wasn't define on the subject but it's logic)
    if (mileage >= 0 and mileage < 5000):

        # Print the eco note on the terminal
        print("The eco note is 10/10 for a mileage under 5000 km per year")

        # Define the grade of the mileage (10/10)
        grade_eco_mileage = 10

    # If mileage is between 5000 and 10000 km per year, the eco note is 9/10
    elif (mileage >= 5000 and mileage < 10000):

        # Print the eco note on the terminal
        print("The eco note is 9/10 for a milage between 5000 and 10000 km per year")

        # Define the grade of the mileage (9/10)
        grade_eco_mileage = 9

    # If mileage is between 10000 and 15000 km per year, the eco note is 7/10
    elif (mileage >= 10000 and mileage < 15000):

        # Print the eco note on the terminal
        print("The eco note is 7/10 for a milage between 10000 and 15000 km per year")

        # Define the grade of the mileage (7/10)
        grade_eco_mileage = 7

    # If mileage is between 15000 and 20000 km per year, the eco note is 5/10
    elif (mileage >= 15000 and mileage < 20000):

        # Print the eco note on the terminal
        print("The eco note is 5/10 for a milage between 15000 and 20000 km per year")

        # Define the grade of the mileage (5/10)
        grade_eco_mileage = 5
    
    # If mileage is between 20000 and 25000 km per year, the eco note is 3/10
    elif (mileage >= 20000 and mileage < 25000):

        # Print the eco note on the terminal
        print("The eco note is 3/10 for a milage between 20000 and 25000 km per year")

        # Define the grade of the mileage (3/10)
        grade_eco_mileage = 3

    # If mileage is between 25000 and 30000 km per year, the eco note is 1/10
    elif (mileage >= 25000 and mileage < 30000):

        # Print the eco note on the terminal
        print("The eco note is 1/10 for a milage between 25000 and 30000 km per year")

        # Define the grade of the mileage (1/10)
        grade_eco_mileage = 1

    # If mileage is over 30000 km per year, the eco note is 0/10
    elif (mileage >= 30000):

        # Print the eco note on the terminal
        print("The eco note is 0/10 for a milage over 30000 km per year")

        # Define the grade of the mileage (0/10)
        grade_eco_mileage = 0

    # If mileage is negative, the eco note is 'err' because it's not possible
    elif (mileage < 0):

        # Print the error message on the terminal
        print("The mileage is not possible, it can't be negative")

        # Define and error as grade of the mileage ('err')
        grade_eco_mileage = "err-negative"

    # If mileage is not recognized, the eco note is 'err'
    else:
            
        # Print the error message on the terminal
        print("The mileage is not recognized")
    
        # Define and error as grade of the mileage ('err')
        grade_eco_mileage = "err-unknown"
    
    # Return the grade of the mileage to the main program
    return grade_eco_mileage

# Calculate grade by year of the car


def grade_year(year):

    # If year of the car is between 2010 and 2025, the eco note is 7/10
    if (year >= 2010 and year <= 2025):

        # Print the eco note on the terminal
        print("The eco note of 7/10")

        # Define the grade of the year (7/10)
        grade_eco_year = 7

    # If year of the car is between 2000 and 2010, the eco note is 5/10
    elif (year >= 2000 and year < 2010):

        # Print the eco note on the terminal
        print("The eco note of 5/10")

        # Define the grade of the year (5/10)
        grade_eco_year = 5
    
    # If year of the car is between 1990 and 2000, the eco note is 4/10
    elif (year >= 1990 and year < 2000):

        # Print the eco note on the terminal
        print("The eco note of 4/10")

        # Define the grade of the year (4/10)
        grade_eco_year = 4

    # If year of the car is between 1980 and 1990, the eco note is 3/10 (This wasn't define on the subject)
    elif (year >= 1980 and year < 1990):

        # Print the eco note on the terminal
        print("The eco note of 3/10")

        # Define the grade of the year (3/10)
        grade_eco_year = 3

    # If year of the car is between 1970 and 1980, the eco note is 2/10
    elif (year >= 1970 and year < 1980):

        # Print the eco note on the terminal
        print("The eco note of 2/10")

        # Define the grade of the year (2/10)
        grade_eco_year = 2

    # If year of the car is between 1960 and 1970, the eco note is 1/10
    elif (year >= 1960 and year < 1970):

        # Print the eco note on the terminal
        print("The eco note of 1/10")

        # Define the grade of the year (1/10)
        grade_eco_year = 1

    # If year of the car is between 1908 and 1960, the eco note is 0/10 (1908 is the year of the first car)
    elif (year >= 1908 and year < 1960):
            
            # Print the eco note on the terminal
            print("The eco note of 0/10")
    
            # Define the grade of the year (0/10)
            grade_eco_year = 0

    # If year of the car is before 1908, the eco note is 'err' because it's not possible
    elif (year < 1908):

        # Print the error message on the terminal
        print("The year of the car is not possible, the first car was created in 1908")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-under"

    # If year of the car is after 2025, the eco note is 'err' because the preorder don't go this far
    elif (year > 2025):

        # Print the error message on the terminal
        print("The year of the car is not possible, the preorder don't go this far")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-over"

    # If year of the car is not recognized, the eco note is 'err'
    else:

        # Print the error message on the terminal
        print("The year of the car is not recognized")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-unknown"

    # Return the grade of the year to the main program
    return grade_eco_year


# Calculate bonus / manus by number of passenger of the car

def bonus_passenger(passenger):

    # If number of passenger is 1, the malus is 0.11%
    if (passenger == 1):

        # Print the bonus on the terminal
        print("The malus is 0.11% for 1 passenger")

        # Define the bonus (0.11%)
        bonus_passenger = 0.11/10**-2

    # If number of passenger is 2, the bonus is 0.17%
    elif (passenger == 2):

        # Print the bonus on the terminal
        print("The bonus is 0.17% for 2 passengers")

        # Define the bonus (-0.17%)
        bonus_passenger = -0.17/10**-2

    # If number of passenger is 3, the bonus is 0.29%
    elif (passenger == 3):

        # Print the bonus on the terminal
        print("The bonus is 0.29% for 3 passengers")

        # Define the bonus (-0.29%)
        bonus_passenger = -0.29/10**-2

    # If number of passenger is 4, the bonus is 0.53%
    elif (passenger == 4):
            
        # Print the bonus on the terminal
        print("The bonus is 0.53% for 4 passengers")
    
        # Define the bonus (-0.53%)
        bonus_passenger = -0.53/10**-2

    # If number of passenger over 5, the bonus is not defined
    elif (passenger >= 5):

        # Print the error message on the terminal
        print("The bonus is not defined for more than 4 passengers")

        # Define and error as bonus ('err-over')
        bonus_passenger = "err-over"

    # If number of passenger is negative, the bonus is not defined
    elif (passenger < 0):

        # Print the error message on the terminal
        print("The bonus is not defined for negative passengers")

        # Define and error as bonus ('err-negative')
        bonus_passenger = "err-negative"

    # If number of passenger is not recognized, the bonus is not defined
    else:

        # Print the error message on the terminal
        print("The bonus is not recognized")

        # Define and error as bonus ('err-unknown')
        bonus_passenger = "err-unknown"

    # Return the bonus to the main program
    return bonus_passenger

# Calculate persentage of borrowing rate for the loan
def borrowing_rate(grade_eco_vehicule, grade_eco_energy, grade_eco_mileage, grade_eco_year):

    # Define the grade of the car by adding the grades of the vehicule, energy, mileage and year
    grade_eco_car = grade_eco_vehicule + grade_eco_energy + grade_eco_mileage + grade_eco_year

    # If the grade of the car is between 0 and 10, the borrowing rate is 3%
    if (grade_eco_car >= 0 and grade_eco_car <= 10):

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 3%")

        # Define the borrowing rate (3%)
        borrowing_rate = 3/10**2

    # If the grade of the car is between 11 and 15, the borrowing rate is 2.74%
    elif (grade_eco_car >= 11 and grade_eco_car <= 15):

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.74%")

        # Define the borrowing rate (2.74%)
        borrowing_rate = 2.74/10**2

    # If the grade of the car is between 21 and 30, the borrowing rate is 2.52%
    elif (grade_eco_car >= 16 and grade_eco_car <= 25):

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.52%")

        # Define the borrowing rate (2.52%)
        borrowing_rate = 2.52/10**2

    # If the grade of the car is between 26 and 33, the borrowing rate is 2.10%
    elif (grade_eco_car >= 26 and grade_eco_car <= 33):

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.10%")

        # Define the borrowing rate (2.10%)
        borrowing_rate = 2.10/10**2
    
    # If the grade of the car is between 34 and 40, the borrowing rate is 1.85%
    elif (grade_eco_car >= 34 and grade_eco_car <= 40):

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 1.85%")

        # Define the borrowing rate (1.85%)
        borrowing_rate = 1.85/10**2

    # If the grade of the car is over 40 it's not possible because max grade is 40
    elif (grade_eco_car > 40):

        # Print the error message on the terminal
        print("The borrowing rate is not possible, the max grade is 40")

        # Define and error as borrowing rate ('err-over')
        borrowing_rate = "err-over"

    # If the grade of the car is negative it's not possible because min grade is 0
    elif (grade_eco_car < 0):

        # Print the error message on the terminal
        print("The borrowing rate is not possible, the min grade is 0")

        # Define and error as borrowing rate ('err-negative')
        borrowing_rate = "err-negative"

    else:
            
        # Print the error message on the terminal
        print("The borrowing rate is not recognized")
    
        # Define and error as borrowing rate ('err-unknown')
        borrowing_rate = "err-unknown"

    # Return the borrowing rate to the main program
    return borrowing_rate

# Main Program
def main():

    

# Launch main program
main()
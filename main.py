# Import of libraries
import tkinter as tk
from tkinter import ttk

# Import the Gui
from gui import final_gui, loan_info_gui
from grade import vehicule_grade, energy_grade

# Calculate grade by year of the car


def grade_year(year):
    # If the year of the car is between 2010 and 2025, the eco note is 7/10
    if 2010 <= year <= 2025:

        # Print the eco note on the terminal
        print("The eco note of 7/10")

        # Define the grade of the year (7/10)
        grade_eco_year = 7

    # If the year of the car is between 2000 and 2010, the eco note is 5/10
    elif 2000 <= year < 2010:

        # Print the eco note on the terminal
        print("The eco note of 5/10")

        # Define the grade of the year (5/10)
        grade_eco_year = 5

    # If the year of the car is between 1990 and 2000, the eco note is 4/10
    elif 1990 <= year < 2000:

        # Print the eco note on the terminal
        print("The eco note of 4/10")

        # Define the grade of the year (4/10)
        grade_eco_year = 4

    # If the year of the car is between 1980 and 1990, the eco note is 3/10 (This wasn't defined on the subject)
    elif 1980 <= year < 1990:

        # Print the eco note on the terminal
        print("The eco note of 3/10")

        # Define the grade of the year (3/10)
        grade_eco_year = 3

    # If the year of the car is between 1970 and 1980, the eco note is 2/10
    elif 1970 <= year < 1980:

        # Print the eco note on the terminal
        print("The eco note of 2/10")

        # Define the grade of the year (2/10)
        grade_eco_year = 2

    # If the year of the car is between 1960 and 1970, the eco note is 1/10
    elif 1960 <= year < 1970:

        # Print the eco note on the terminal
        print("The eco note of 1/10")

        # Define the grade of the year (1/10)
        grade_eco_year = 1

    # If the year of the car is between 1908 and 1960, the eco note is 0/10 (1908 is the year of the first car)
    elif 1908 <= year < 1960:

        # Print the eco note on the terminal
        print("The eco note of 0/10")

        # Define the grade of the year (0/10)
        grade_eco_year = 0

    # If the year of the car is before 1908, the eco note is 'err' because it's not possible
    elif year < 1908:

        # Print the error message on the terminal
        print("The year of the car is not possible, the first car was created in 1908")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-under"

    # If the year of the car is after 2025, the eco note is 'err' because the preorder doesn't go this far
    elif year > 2025:

        # Print the error message on the terminal
        print("The year of the car is not possible, the preorder don't go this far")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-over"

    # If the year of the car is not recognized, the eco note is 'err'
    else:

        # Print the error message on the terminal
        print("The year of the car is not recognized")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-unknown"

    # Return the grade of the year to the main program
    return grade_eco_year


# Calculate bonus / manus by number of passengers of the car

def bonus_passenger_function(passenger):
    # If the number of passengers is 1, the malus is 0.11%
    if passenger == 1:

        # Print the bonus on the terminal
        print("The malus is 0.11% for 1 passenger")

        # Define the bonus (0.11%)
        bonus_passenger = 0.11 * 0.01

    # If the number of passengers is 2, the bonus is 0.17%
    elif passenger == 2:

        # Print the bonus on the terminal
        print("The bonus is 0.17% for 2 passengers")

        # Define the bonus (-0.17%)
        bonus_passenger = -0.17 * 0.01

    # If the number of passengers is 3, the bonus is 0.29%
    elif passenger == 3:

        # Print the bonus on the terminal
        print("The bonus is 0.29% for 3 passengers")

        # Define the bonus (-0.29%)
        bonus_passenger = -0.29 * 0.01

    # If the number of passengers is 4, the bonus is 0.53%
    elif passenger == 4:

        # Print the bonus on the terminal
        print("The bonus is 0.53% for 4 passengers")

        # Define the bonus (-0.53%)
        bonus_passenger = -0.53 * 0.01

    # If number of passenger over 5, the bonus is not defined
    elif passenger >= 5:

        # Print the error message on the terminal
        print("The bonus is not defined for more than 4 passengers")

        # Define and error as bonus ('err-over')
        bonus_passenger = "err-over"

    # If the number of passengers is negative, the bonus is not defined
    elif passenger < 0:

        # Print the error message on the terminal
        print("The bonus is not defined for negative passengers")

        # Define and error as bonus ('err-negative')
        bonus_passenger = "err-negative"

    # If the number of passengers is not recognized, the bonus is not defined
    else:

        # Print the error message on the terminal
        print("The bonus is not recognized")

        # Define and error as bonus ('err-unknown')
        bonus_passenger = "err-unknown"

    # Return the bonus to the main program
    return bonus_passenger


# Calculate persentage of borrowing rate for the loan
def borrowing_rate_function(grade_eco_vehicule, grade_eco_energy, grade_eco_mileage, grade_eco_year):
    # Define the grade of the car by adding the grades of the vehicule, energy, mileage and year
    grade_eco_car = grade_eco_vehicule + grade_eco_energy + grade_eco_mileage + grade_eco_year

    # If the grade of the car is between 0 and 10, the borrowing rate is 3%
    if 0 <= grade_eco_car <= 10:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 3%")

        # Define the borrowing rate (3%)
        borrowing_rate = 3 * 0.01

    # If the grade of the car is between 11 and 15, the borrowing rate is 2.74%
    elif 11 <= grade_eco_car <= 15:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.74%")

        # Define the borrowing rate (2.74%)
        borrowing_rate = 2.74 * 0.01

    # If the grade of the car is between 21 and 30, the borrowing rate is 2.52%
    elif 16 <= grade_eco_car <= 25:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.52%")

        # Define the borrowing rate (2.52%)
        borrowing_rate = 2.52 * 0.01

    # If the grade of the car is between 26 and 33, the borrowing rate is 2.10%
    elif 26 <= grade_eco_car <= 33:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.10%")

        # Define the borrowing rate (2.10%)
        borrowing_rate = 2.10 * 0.01

    # If the grade of the car is between 34 and 40, the borrowing rate is 1.85%
    elif 34 <= grade_eco_car <= 40:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 1.85%")

        # Define the borrowing rate (1.85%)
        borrowing_rate = 1.85 * 0.01

    # If the grade of the car is over 40, it's not possible because max grade is 40
    elif grade_eco_car > 40:

        # Print the error message on the terminal
        print("The borrowing rate is not possible, the max grade is 40")

        # Define and error as borrowing rate ('err-over')
        borrowing_rate = "err-over"

    # If the grade of the car is negative, it's not possible because min grade is 0
    elif grade_eco_car < 0:

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


# Get information for the loan Gui
def get_loan_info_gui(entry_energy_type, entry_vehicule_type, entry_mileage, entry_year, entry_passenger):
    # Vérification des entrées pour voir si les cases sont bien remplies
    if entry_energy_type is "" or entry_vehicule_type is "" or entry_mileage is "" or entry_year is "" or entry_passenger is "":
        print("Il y a une erreur, toutes les cases ne sont pas remplies")

        # Define the window error and show it
        window_error = tk.Tk()
        window_error.title("Il y a quelque erreur")

        # Define the label for the error message and the position
        ttk.Label(window_error, text="Il y a une erreur, toutes les cases ne sont pas remplies").grid(row=0, column=0)

        # Define the button to close the window error and the position
        ttk.Button(window_error, text="Fermer", command=window_error.quit).grid(row=1, column=0)

        window_error.mainloop()

    # Convert the entry to lower cases
    try:
        entry_vehicule_type = str(entry_vehicule_type.lower())
    # If the vehicule type is not a string, define it as an error
    except AttributeError:
        print("The vehicule type is not a string")
        entry_vehicule_type = "err-notstring"

    # Convert the entry to lower cases
    try:
        entry_energy_type = str(entry_energy_type.lower())
    # If the energy type is not a string, define it as an error
    except AttributeError:
        print("The energy type is not a string")
        entry_energy_type = "err-notstring"

    # Convert the entry to int
    try:
        entry_mileage = int(entry_mileage)
    # If the mileage is not a number, define it as an error
    except ValueError:
        print("The mileage is not a number")
        entry_mileage = "err-notnumber"

    # Convert the entry to int
    try:
        entry_year = int(entry_year)
    # If the year is not a number, define it as an error
    except ValueError:
        print("The year is not a number")
        entry_year = "err-notnumber"

    # Convert the entry to int
    try:
        entry_passenger = int(entry_passenger)
    # If the number of passengers is not a number, define it as an error
    except ValueError:
        print("The number of passenger is not a number")
        entry_passenger = "err-notnumber"

    # If there is an error, define the window error and show it
    if entry_mileage is "err-notnumber" or entry_year is "err-notnumber" or entry_passenger is "err-notnumber" or entry_vehicule_type is "err-notstring" or entry_energy_type is "err-notstring":
        window_error = tk.Tk()
        window_error.title("Il y a quelque erreur")
        return window_error.mainloop()
    else:
        # Return the information to the main program
        return entry_vehicule_type, entry_energy_type, entry_mileage, entry_year, entry_passenger


# Main Program
def main():
    # Get information for the loan Gui
    loan_info = loan_info_gui.loan_info()

    # Define the variables from the Gui
    entry_energy_type = loan_info[0]
    entry_vehicule_type = loan_info[1]
    entry_mileage = loan_info[2]
    entry_year = loan_info[3]
    entry_passenger = loan_info[4]

    # Verify the entries

    # Get the grade to the vehicule type
    grade_vehicule_get = vehicule_grade.grade_vehicule(entry_vehicule_type)

    # Get the grade to the energy type
    grade_energy_get = energy_grade.grade_energy(entry_energy_type)

    # Get the grade to the mileage
    grade_mileage_get = mileage_grade.grade_mileage(entry_mileage)

    # Get the grade to the year
    grade_year_get = grade_year(entry_year)

    # Get the bonus to the number of passengers
    bonus_passenger_get = bonus_passenger_function(entry_passenger)

    # Get the borrowing rate
    borrowing_rate_get = borrowing_rate_function(grade_vehicule_get, grade_energy_get, grade_mileage_get,
                                                 grade_year_get)

    borrowing_rate_percentage = borrowing_rate_get + bonus_passenger_get

    final_gui.final_gui(borrowing_rate_percentage)


# Launch the main program
main()

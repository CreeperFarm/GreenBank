# Import of libraries
import tkinter as tk
from tkinter import ttk

# Define the variables (The int values are by default -1 and not 0 because 0 is a possible value for each int variable)

# Define the variables from the subject

"""vehicule_type = ""
energy_type = ""
mileage = -1
year = -1
passenger = -1

    # Define the variables for the eco grade

grade_vehicule = -1
grade_energy = -1
grade_mileage = -1
grade_year = -1"""

# Define the variables for the bonus

"""bonus_passenger = -1
borrowing_rate = -1

    # Define the variables from the Gui
entry_vehicule_type = ""
entry_energy_type = ""
entry_mileage = -1
entry_year = -1
entry_passenger = -1"""


# Calculate grade by vehicule type


def grade_vehicule(vehicule_type):
    vehicule_type = str(vehicule_type)

    # If vehicule type is citadine, the eco note is 8/10
    if vehicule_type is "citadine":
        # Print the eco note on the terminal
        print("The eco note is 8/10 for a citadine")

        # Define the grade of the vehicule (8/10)
        grade_eco_vehicule = 8

    # If vehicule type is cabriolet, the eco note is 6/10
    elif vehicule_type is "cabriolet":

        # Print the eco note on the terminal
        print("The eco note is 6/10 for a cabriolet")

        # Define the grade of the vehicule (6/10)
        grade_eco_vehicule = 6

    # If vehicule type is berline, the eco note is 6.5/10
    elif vehicule_type is "berline":

        # Print the eco note on the terminal
        print("The eco note is 6.5/10 for a berline")

        # Define the grade of the vehicule (6.5/10)
        grade_eco_vehicule = 6.5

    # If vehicule type is suv or a 4x4, the eco note is 4/10
    elif vehicule_type is "suv" or "4x4":

        # Print the eco note on the terminal
        print("The eco note is 4/10 for a suv or a 4x4")

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
    # If the energy type of the car is electric, the eco note is 9/10
    if energy_type is "electrique" or "electric" or "électrique" or "électric":

        # Print the eco note on the terminal
        print("The eco note is 9/10 for an electric car")

        # Define the grade of the energy (9/10)
        grade_eco_energy = 9

    # If the energy type of the car is hybrid, the eco note is 7/10
    elif energy_type is "hybrid":

        # Print the eco note on the terminal
        print("The eco note is 7/10 for a hybrid car")

        # Define the grade of the energy (7/10)
        grade_eco_energy = 7

    # If the energy type of the car is gas, the eco note is 6/10
    elif energy_type is "gaz":

        # Print the eco note on the terminal
        print("The eco note is 6/10 for a gas car")

        # Define the grade of the energy (6/10)
        grade_eco_energy = 6

    # If the energy type of the car is essence, the eco note is 5/10
    elif energy_type is "essence":

        # Print the eco note on the terminal
        print("The eco note is 5/10 for an essence car")

        # Define the grade of the energy (5/10)
        grade_eco_energy = 5

    # If the energy type of the car is diesel, the eco note is 4/10
    elif energy_type is "diesel":

        # Print the eco note on the terminal
        print("The eco note is 4/10 for a diesel car")

        # Define the grade of the energy (4/10)
        grade_eco_energy = 4

    else:

        # Print the error message on the terminal
        print("The type of energy is not recognized, the existing one are : electrique, hybrid, gaz, essence, diesel")

        # Define and error as grade of the energy ('err')
        grade_eco_energy = "err-unknown"

    # Return the grade of the energy to the main program
    return grade_eco_energy


# Calculate grade by number of kilometers of the car (mileage per year)


def grade_mileage(mileage):
    # If mileage is under 5000 km per year, the eco note is 10/10 (This wasn't defined on the subject, but it's logic)
    if 0 <= mileage < 5000:

        # Print the eco note on the terminal
        print("The eco note is 10/10 for a mileage under 5000 km per year")

        # Define the grade of the mileage (10/10)
        grade_eco_mileage = 10

    # If mileage is between 5000 and 10000 km per year, the eco note is 9/10
    elif 5000 <= mileage < 10000:

        # Print the eco note on the terminal
        print("The eco note is 9/10 for a milage between 5000 and 10000 km per year")

        # Define the grade of the mileage (9/10)
        grade_eco_mileage = 9

    # If mileage is between 10000 and 15000 km per year, the eco note is 7/10
    elif 10000 <= mileage < 15000:

        # Print the eco note on the terminal
        print("The eco note is 7/10 for a milage between 10000 and 15000 km per year")

        # Define the grade of the mileage (7/10)
        grade_eco_mileage = 7

    # If mileage is between 15000 and 20000 km per year, the eco note is 5/10
    elif 15000 <= mileage < 20000:

        # Print the eco note on the terminal
        print("The eco note is 5/10 for a milage between 15000 and 20000 km per year")

        # Define the grade of the mileage (5/10)
        grade_eco_mileage = 5

    # If mileage is between 20000 and 25000 km per year, the eco note is 3/10
    elif 20000 <= mileage < 25000:

        # Print the eco note on the terminal
        print("The eco note is 3/10 for a milage between 20000 and 25000 km per year")

        # Define the grade of the mileage (3/10)
        grade_eco_mileage = 3

    # If mileage is between 25000 and 30000 km per year, the eco note is 1/10
    elif 25000 <= mileage < 30000:

        # Print the eco note on the terminal
        print("The eco note is 1/10 for a milage between 25000 and 30000 km per year")

        # Define the grade of the mileage (1/10)
        grade_eco_mileage = 1

    # If mileage is over 30000 km per year, the eco note is 0/10
    elif mileage >= 30000:

        # Print the eco note on the terminal
        print("The eco note is 0/10 for a milage over 30000 km per year")

        # Define the grade of the mileage (0/10)
        grade_eco_mileage = 0

    # If mileage is negative, the eco note is 'err' because it's not possible
    elif mileage < 0:

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
def get_loan_info_gui():
    # Define the window and the title
    window = tk.Tk()
    window.title("Eco Note Calculator")

    # Define the label for the vehicule type, the entry and the position
    ttk.Label(window, text="Type de véhicule : ").grid(row=0, column=0)
    entry_vehicule_type = ttk.Entry(window, width=30)
    entry_vehicule_type.grid(row=0, column=1)

    # Define the label for the energy type, the entry and the position
    ttk.Label(window, text="Type d'énergie : ").grid(row=1, column=0)
    entry_energy_type = ttk.Entry(window, width=30)
    entry_energy_type.grid(row=1, column=1)

    # Define the label for the mileage, the entry and the position
    ttk.Label(window, text="Kilométrage par an : ").grid(row=2, column=0)
    entry_mileage = ttk.Entry(window, width=30)
    entry_mileage.grid(row=2, column=1)

    # Define the label for the year, the entry and the position
    ttk.Label(window, text="Année : ").grid(row=3, column=0)
    entry_year = ttk.Entry(window, width=30)
    entry_year.grid(row=3, column=1)

    # Define the label for the number of passengers, the entry and the position
    ttk.Label(window, text="Nombre de passagers : ").grid(row=4, column=0)
    entry_passenger = ttk.Entry(window, width=30)
    entry_passenger.grid(row=4, column=1)

    # Define the label for the cost of the car, the entry and the position
    ttk.Label(window, text="Valeur de l'emprunt : ").grid(row=5, column=0)
    entry_loan_value = ttk.Entry(window, width=30)
    entry_loan_value.grid(row=5, column=1)

    # Define the button to calculate the eco note and the position
    ttk.Button(window, text="Calculer l'éco note", command=window.quit).grid(row=6, column=0)

    # Create the window 
    window.mainloop()

    # Get the information from the entry
    entry_vehicule_type = entry_vehicule_type.get()
    entry_energy_type = entry_energy_type.get()
    entry_mileage = entry_mileage.get()
    entry_year = entry_year.get()
    entry_passenger = entry_passenger.get()
    entry_loan_value = entry_loan_value.get()

    # Vérification des entrées pour voir si les cases sont bien remplies
    if entry_energy_type is "" or entry_vehicule_type is "" or entry_mileage is "" or entry_year is "" or entry_passenger is "" or entry_loan_value is "":
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

    # Remove '€' or '$' from the entry
    try:
        entry_loan_value = entry_loan_value.replace("€", "")
        entry_loan_value = entry_loan_value.replace("$", "")
        entry_loan_value = int(entry_loan_value.replace(" ", ""))
    except ValueError:
        print("The loan value is not a number")
        entry_loan_value = "err-notnumber"

    # If there is an error, define the window error and show it
    if entry_mileage is "err-notnumber" or entry_year is "err-notnumber" or entry_passenger is "err-notnumber" or entry_vehicule_type is "err-notstring" or entry_energy_type is "err-notstring" or entry_loan_value is "err-notnumber":
        window_error = tk.Tk()
        window_error.title("Il y a quelque erreur")
        return window_error.mainloop()
    else:
        # Return the information to the main program
        return entry_vehicule_type, entry_energy_type, entry_mileage, entry_year, entry_passenger, entry_loan_value


# Final Gui to show the result

def final_gui(borrowing_rate_percentage, entry_loan_value):
    # Define the window and the title
    window_final = tk.Tk()
    window_final.title("Résultat du prêt")

    # Show the borrowing rate
    ttk.Label(window_final, text="Le taux d'emprunt est de : " + str(borrowing_rate_percentage * 100) + "%").grid(row=0,
                                                                                                                  column=0)

    # Show the loan value
    ttk.Label(window_final, text="Le montant de l'emprunt est de : " + str(entry_loan_value) + "€").grid(row=1,
                                                                                                         column=0)

    # Show the total payment with borrowing rate
    ttk.Label(window_final, text="Le montant total à payer est de : " + str(entry_loan_value * (1 + borrowing_rate_percentage)) + "€").grid(row=2, column=0)

    # Show the window
    window_final.mainloop()


# Main Program
def main():
    # Get information for the loan Gui
    loan_info = get_loan_info_gui()

    # Define the variables from the Gui
    entry_energy_type = loan_info[0]
    entry_vehicule_type = loan_info[1]
    entry_mileage = loan_info[2]
    entry_year = loan_info[3]
    entry_passenger = loan_info[4]
    entry_loan_value = loan_info[5]

    # Get the grade to the vehicule type
    grade_vehicule_get = grade_vehicule(entry_vehicule_type)

    # Get the grade to the energy type
    grade_energy_get = grade_energy(entry_energy_type)

    # Get the grade to the mileage
    grade_mileage_get = grade_mileage(entry_mileage)

    # Get the grade to the year
    grade_year_get = grade_year(entry_year)

    # Get the bonus to the number of passengers
    bonus_passenger_get = bonus_passenger_function(entry_passenger)

    # Get the borrowing rate
    borrowing_rate_get = borrowing_rate_function(grade_vehicule_get, grade_energy_get, grade_mileage_get,
                                                 grade_year_get)

    borrowing_rate_percentage = borrowing_rate_get + bonus_passenger_get

    final_gui(borrowing_rate_percentage, entry_loan_value)


# Launch the main program
main()

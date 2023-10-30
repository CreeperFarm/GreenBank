# Import of libraries
import tkinter as tk
from tkinter import ttk

# Import the Gui
from gui import final_gui, loan_info_gui
from grade import vehicule_grade, energy_grade, mileage_grade, year_grade
from bonus import bonus_passenger, borrowing_rate

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

    # Get all the grade of the vehicule
    grade_vehicule_get = vehicule_grade.grade_vehicule(entry_vehicule_type)
    grade_energy_get = energy_grade.grade_energy(entry_energy_type)
    grade_mileage_get = mileage_grade.grade_mileage(entry_mileage)
    grade_year_get = year_grade.grade_year(entry_year)

    # Get the bonus to the number of passengers
    bonus_passenger_get = bonus_passenger.bonus_passenger_function(entry_passenger)

    # Get the borrowing rate
    borrowing_rate_get = borrowing_rate.borrowing_rate_function(grade_vehicule_get, grade_energy_get, grade_mileage_get, grade_year_get)

    # Calculate the borrowing rate percentage
    borrowing_rate_percentage = borrowing_rate_get + bonus_passenger_get

    final_gui.final_gui(borrowing_rate_percentage)


# Launch the main program
main()

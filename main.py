# Import of libraries
import tkinter as tk
from tkinter import ttk

# Import the Gui
from gui import final_gui, loan_info_gui
from grade import vehicule_grade, energy_grade, mileage_grade, year_grade
from bonus import bonus_passenger, borrowing_rate


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
    borrowing_rate_get = borrowing_rate.borrowing_rate_function(grade_vehicule_get, grade_energy_get, grade_mileage_get,
                                                                grade_year_get)

    # Calculate the borrowing rate percentage
    borrowing_rate_percentage = borrowing_rate_get + bonus_passenger_get

    final_gui.final_gui(borrowing_rate_percentage)


# Launch the main program
main()

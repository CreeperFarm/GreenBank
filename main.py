# Import the Gui
from components.gui import final_gui, loan_info_gui
from components.grade import energy_grade, mileage_grade, year_grade, vehicule_grade
from components.bonus import borrowing_rate, bonus_passenger
from components.verifier import entry_verifier


# Main Program
def main():
    # Get information for the loan Gui
    loan_info_list = None
    while loan_info_list is None:
        loan_info_list = loan_info_gui.loan_info()

    # Define the variables from the Gui
    entry_energy_type = loan_info_list[0]
    entry_vehicule_type = loan_info_list[1]
    entry_mileage = loan_info_list[2]
    entry_year = loan_info_list[3]
    entry_passenger = loan_info_list[4]

    # Verify the entries
    entry_verify = entry_verifier.verifier_entry(entry_energy_type, entry_vehicule_type, entry_mileage, entry_year, entry_passenger)

    if entry_verify is not None:
        # Define the variables from the verifier
        entry_energy_type = entry_verify[0]
        entry_vehicule_type = entry_verify[1]
        entry_mileage = entry_verify[2]
        entry_year = entry_verify[3]
        entry_passenger = entry_verify[4]

        # Get all the grade of the vehicule
        grade_vehicule_get = vehicule_grade.grade_vehicule(entry_vehicule_type)
        grade_energy_get = energy_grade.grade_energy(entry_energy_type)
        grade_mileage_get = mileage_grade.grade_mileage(entry_mileage)
        grade_year_get = year_grade.grade_year(entry_year)

        # Get the bonus to the number of passengers
        bonus_passenger_get = bonus_passenger.bonus_passenger_function(entry_passenger)

        # If the bonus is not null, run what's next
        if bonus_passenger_get is not None:
            # Get the borrowing rate
            borrowing_rate_get = borrowing_rate.borrowing_rate_function(grade_vehicule_get, grade_energy_get, grade_mileage_get, grade_year_get)

            # If the borrowing rate is not null, run what's next
            if borrowing_rate_get is not None:
                # Calculate the borrowing rate percentage
                borrowing_rate_percentage = borrowing_rate_get + bonus_passenger_get

                final_gui.final_gui(borrowing_rate_percentage, borrowing_rate_get, bonus_passenger_get)


# Launch the main program
main()

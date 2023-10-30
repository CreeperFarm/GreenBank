# Import the error gui
from components.gui import error_gui

# Define the error map
error = []
error_by = []


# Verify the entries got from loan_info_gui.py

def verifier_entry(entry_energy_type, entry_vehicule_type, entry_mileage, entry_year, entry_passenger):

    # Convert the entry to lower cases
    try:
        entry_vehicule_type = str(entry_vehicule_type.lower())
    # If the vehicule type is not a string, define it as an error
    except AttributeError:
        # Print the error message on the terminal
        print("The vehicule type is not a string")

        # Define the vehicule type as an error
        entry_vehicule_type = "err-not-string"
        error.append(entry_vehicule_type)
        error_by.append("vehicule")

    # Convert the entry to lower cases
    try:
        entry_energy_type = str(entry_energy_type.lower())
    # If the energy type is not a string, define it as an error
    except AttributeError:
        # Print the error message on the terminal
        print("The energy type is not a string")

        # Define the energy type as an error
        entry_energy_type = "err-not-string"
        error.append(entry_energy_type)
        error_by.append("energy")

    # Convert the entry to int
    try:
        # If the mileages contain a "k" or a "K", remove it and multiply the number by 1000
        entry_mileage = entry_mileage.replace("k", "")
        entry_mileage = entry_mileage.replace("K", "")
        entry_mileage = entry_mileage.replace(" ", "")
        entry_mileage = int(entry_mileage) * 1000
    # If the mileage is not a number, define it as an error
    except ValueError:
        # Print the error message on the terminal
        print("The mileage is not a number")

        # Define the mileage as an error
        entry_mileage = "err-not-number"
        error.append(entry_mileage)
        error_by.append("mileage")

    # Convert the entry to int
    try:
        entry_year = int(entry_year)
    # If the year is not a number, define it as an error
    except ValueError:
        # Print the error message on the terminal
        print("The year is not a number")

        # Define the year as an error
        entry_year = "err-not-number"
        error.append(entry_year)
        error_by.append("year")

    # Convert the entry to int
    try:
        entry_passenger = int(entry_passenger)
    # If the number of passengers is not a number, define it as an error
    except ValueError:
        # Print the error message on the terminal
        print("The number of passenger is not a number")
        # Define the number of passengers as an error
        entry_passenger = "err-not-number"
        error.append(entry_passenger)
        error_by.append("passenger")

    print(error)
    # If everything is good, return the information to the main program
    if not error:
        # Return the information to the main program
        return entry_vehicule_type, entry_energy_type, entry_mileage, entry_year, entry_passenger
    # If there is an error, show the error gui
    else:
        # Show the error gui
        error_gui.error_gui(error, error_by)

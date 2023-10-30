# Import the error gui
from gui import error_gui

# Define the error map
error = []


# Verify the entries got from loan_info_gui.py

def verifier_entry(entry_energy_type, entry_vehicule_type, entry_mileage, entry_year, entry_passenger):
    # Vérification des entrées pour voir si les cases sont bien remplies
    if entry_energy_type is "" or entry_vehicule_type is "" or entry_mileage is "" or entry_year is "" or entry_passenger is "":
        print("Il y a une erreur, toutes les cases ne sont pas remplies")
        error_gui.error_gui("err-not-filled")
    elif entry_energy_type is not "" and entry_vehicule_type is not "" and entry_mileage is not "" and entry_year is not "" and entry_passenger is not "":
        # Convert the entry to lower cases
        try:
            entry_vehicule_type = str(entry_vehicule_type.lower())
        # If the vehicule type is not a string, define it as an error
        except AttributeError:
            print("The vehicule type is not a string")
            entry_vehicule_type = "err-not-string"
            error.add(entry_vehicule_type)

        # Convert the entry to lower cases
        try:
            entry_energy_type = str(entry_energy_type.lower())
        # If the energy type is not a string, define it as an error
        except AttributeError:
            print("The energy type is not a string")
            entry_energy_type = "err-notstring"
            error.add(entry_energy_type)

        # Convert the entry to int
        try:
            entry_mileage = int(entry_mileage)
        # If the mileage is not a number, define it as an error
        except ValueError:
            print("The mileage is not a number")
            entry_mileage = "err-notnumber"
            error.add(entry_mileage)

        # Convert the entry to int
        try:
            entry_year = int(entry_year)
        # If the year is not a number, define it as an error
        except ValueError:
            print("The year is not a number")
            entry_year = "err-notnumber"
            error.add(entry_year)

        # Convert the entry to int
        try:
            entry_passenger = int(entry_passenger)
        # If the number of passengers is not a number, define it as an error
        except ValueError:
            print("The number of passenger is not a number")
            entry_passenger = "err-notnumber"
            error.add(entry_passenger)

        # If there is an error, show the error gui
        if error is not {}:
            error_gui.error_gui(error)
        # If everything is good, return the information to the main program
        else:
            # Return the information to the main program
            return entry_vehicule_type, entry_energy_type, entry_mileage, entry_year, entry_passenger

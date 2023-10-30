import tkinter as tk
from tkinter import ttk

# Import the error_gui function
from components.gui import error_gui


def loan_info():
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

    # Define the button to calculate the eco note and the position
    ttk.Button(window, text="Calculer l'éco note", command=window.quit).grid(row=5, column=0)

    # Create the window
    window.mainloop()

    # Get the information from the entry
    entry_vehicule_type = entry_vehicule_type.get()
    entry_energy_type = entry_energy_type.get()
    entry_mileage = entry_mileage.get()
    entry_year = entry_year.get()
    entry_passenger = entry_passenger.get()

    window.destroy()

    # Vérification des entrées pour voir si les cases sont bien remplies
    if entry_energy_type is "" or entry_vehicule_type is "" or entry_mileage is "" or entry_year is "" or entry_passenger is "":
        print("Il y a une erreur, toutes les cases ne sont pas remplies")
        error_gui.error_gui("err-not-filled", "")
    else:
        return entry_vehicule_type, entry_energy_type, entry_mileage, entry_year, entry_passenger

import tkinter as tk
from tkinter import ttk

error_map = {
    "err-not-filled": "Toutes les cases ne sont pas remplies",
    "err-not-string": " n'est pas une chaîne de caractère",
    "err-not-number": " n'est pas un nombre",
    "err-negative": " est négatif",
    "err-over": " est trop grand",
    "err-unknown": " est inconnu",
}
error_by_map = {
    "vehicule": "Le type de véhicule entré",
    "energy": "Le type d'énergie entré",
    "mileage": "Le kilométrage entré",
    "year": "L'année entrée",
    "passenger": "Le nombre de passagers entré",
    "borrowing": "Le taux d'emprunt calculé",
}


def error_gui(error_list, error_by):
    # Define the window and the title
    window_error = tk.Tk()
    window_error.title("Il y a quelque erreur")

    # Show the error message
    ttk.Label(window_error, text="Il y a quelque erreur, ce sont celle-ci:").grid(row=0, column=0)
    rowNumber = 1
    for error in error_list:
        ttk.Label(window_error, text=error_by_map[error_by[rowNumber-1]] + error_map[error]).grid(row=rowNumber, column=0)
        rowNumber += 1

    # Show the button to close the window
    ttk.Button(window_error, text="Fermer", command=window_error.quit).grid(row=rowNumber, column=0)

    window_error.mainloop()

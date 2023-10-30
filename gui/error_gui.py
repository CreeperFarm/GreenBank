import tkinter as tk
from tkinter import ttk

error_map = {
    "err-not-filled": "Toutes les cases ne sont pas remplies",
    "err-not-string": " n'est pas une chaîne de caractère",
    "err-not-number": " n'est pas un nombre",
}


def error_gui(error_list):
    # Define the window and the title
    window_error = tk.Tk()
    window_error.title("Il y a quelque erreur")

    # Show the error message
    ttk.Label(window_error, text="Il y a quelque erreur, ce sont celle-ci:").grid(row=0, column=0)
    rowNumber = 1
    for error in error_list:
        ttk.Label(window_error, text=error_map[error]).grid(row=rowNumber, column=0)
        rowNumber += 1

    # Show the button to close the window
    ttk.Button(window_error, text="Fermer", command=window_error.quit).grid(row=rowNumber, column=0)

    window_error.mainloop()

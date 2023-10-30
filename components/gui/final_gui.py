# Import Librairies
import tkinter as tk
from tkinter import ttk

# Define style for the text
fontStyle = ("Arial", 20)


# Final Gui to show the result

def final_gui(borrowing_rate_percentage, borrowing_rate, bonus_passenger):
    # Define the window and the title
    window_final = tk.Tk()
    window_final.title("Résultat du prêt")

    # Show the bonus passenger
    if bonus_passenger < 0:
        bonus_passenger = str(bonus_passenger)
        bonus_passenger = bonus_passenger.replace("-", "0")
        ttk.Label(window_final, text="Le bonus avec le nombre de passagers est : " + bonus_passenger + "%", font=fontStyle).grid(row=0, column=0)
    # Show the malus passenger
    else:
        ttk.Label(window_final, text="Le malus avec le nombre de passagers est : " + str(bonus_passenger) + "%", font=fontStyle).grid(row=0, column=0)

    # Show the borrowing rate
    ttk.Label(window_final,
              text="Le taux d'emprunt avec le critère de la voiture est : " + str(borrowing_rate) + "%", font=fontStyle).grid(row=1, column=0)

    # Show the borrowing rate total
    ttk.Label(window_final, text="Le taux d'emprunt est de : " + str(borrowing_rate_percentage) + "%", font=fontStyle).grid(row=2, column=0)

    # Show the button to close the window
    ttk.Button(window_final, text="Fermer", command=window_final.destroy).grid(row=3, column=0)

    # Show the window
    window_final.mainloop()

    window_final.destroy()

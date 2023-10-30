import tkinter as tk
from tkinter import ttk


# Final Gui to show the result

def final_gui(borrowing_rate_percentage):
    # Define the window and the title
    window_final = tk.Tk()
    window_final.title("Résultat du prêt")

    # Show the borrowing rate
    ttk.Label(window_final, text="Le taux d'emprunt est de : " + str(float(borrowing_rate_percentage * 100)) + "%").grid(row=0, column=0)

    # Show the button to close the window
    ttk.Button(window_final, text="Fermer", command=window_final.destroy).grid(row=1, column=0)

    # Show the window
    window_final.mainloop()

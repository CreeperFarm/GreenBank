# Calculate grade by energy type of the car


def grade_energy(energy_type):
    # If the energy type of the car is electric, the eco note is 9/10
    if energy_type is "electrique" or "electric" or "électrique" or "électric":

        # Print the eco note on the terminal
        print("The eco note is 9/10 for an electric car")

        # Define the grade of the energy (9/10)
        grade_eco_energy = 9

    # If the energy type of the car is hybrid, the eco note is 7/10
    elif energy_type is "hybrid" or "hybride":

        # Print the eco note on the terminal
        print("The eco note is 7/10 for a hybrid car")

        # Define the grade of the energy (7/10)
        grade_eco_energy = 7

    # If the energy type of the car is gas, the eco note is 6/10
    elif energy_type is "gaz":

        # Print the eco note on the terminal
        print("The eco note is 6/10 for a gas car")

        # Define the grade of the energy (6/10)
        grade_eco_energy = 6

    # If the energy type of the car is essence, the eco note is 5/10
    elif energy_type is "essence":

        # Print the eco note on the terminal
        print("The eco note is 5/10 for an essence car")

        # Define the grade of the energy (5/10)
        grade_eco_energy = 5

    # If the energy type of the car is diesel, the eco note is 4/10
    elif energy_type is "diesel":

        # Print the eco note on the terminal
        print("The eco note is 4/10 for a diesel car")

        # Define the grade of the energy (4/10)
        grade_eco_energy = 4

    else:

        # Print the error message on the terminal
        print("The type of energy is not recognized, the existing one are : electrique, hybrid, gaz, essence, diesel")

        # Define and error as grade of the energy ('err')
        grade_eco_energy = "err-unknown"

    # Return the grade of the energy to the main program
    return grade_eco_energy

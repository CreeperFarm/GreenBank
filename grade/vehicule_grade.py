# Calculate grade by vehicule type


def grade_vehicule(vehicule_type):
    # If vehicule type is citadine, the eco note is 8/10
    if vehicule_type is "citadine" or "citadin":
        # Print the eco note on the terminal
        print("The eco note is 8/10 for a citadine")

        # Define the grade of the vehicule (8/10)
        grade_eco_vehicule = 8

    # If vehicule type is cabriolet, the eco note is 6/10
    elif vehicule_type is "cabriolet":

        # Print the eco note on the terminal
        print("The eco note is 6/10 for a cabriolet")

        # Define the grade of the vehicule (6/10)
        grade_eco_vehicule = 6

    # If vehicule type is berline, the eco note is 6.5/10
    elif vehicule_type is "berline":

        # Print the eco note on the terminal
        print("The eco note is 6.5/10 for a berline")

        # Define the grade of the vehicule (6.5/10)
        grade_eco_vehicule = 6.5

    # If vehicule type is suv or a 4x4, the eco note is 4/10
    elif vehicule_type is "suv" or "4x4":

        # Print the eco note on the terminal
        print("The eco note is 4/10 for a suv or a 4x4")

        # Define the grade of the vehicule (4/10)
        grade_eco_vehicule = 4

    # If vehicule type is not recognized, the eco note is 'err'
    else:

        # Print the error message on the terminal
        print("The type of vehicule is not recognized, the existing one are : citadine, cabriolet, berline, suv, 4x4")

        # Define and error as grade of the vehicule ('err')
        grade_eco_vehicule = "err-unknown"

    # Return the grade of the vehicule to the main program
    return grade_eco_vehicule

# Calculate grade by number of kilometers of the car (mileage per year)


def grade_mileage(mileage):
    # If mileage is under 5000 km per year, the eco note is 10/10 (This wasn't defined on the subject, but it's logic)
    if 0 <= mileage < 5000:

        # Print the eco note on the terminal
        print("The eco note is 10/10 for a mileage under 5000 km per year")

        # Define the grade of the mileage (10/10)
        grade_eco_mileage = 10

    # If mileage is between 5000 and 10000 km per year, the eco note is 9/10
    elif 5000 <= mileage < 10000:

        # Print the eco note on the terminal
        print("The eco note is 9/10 for a milage between 5000 and 10000 km per year")

        # Define the grade of the mileage (9/10)
        grade_eco_mileage = 9

    # If mileage is between 10000 and 15000 km per year, the eco note is 7/10
    elif 10000 <= mileage < 15000:

        # Print the eco note on the terminal
        print("The eco note is 7/10 for a milage between 10000 and 15000 km per year")

        # Define the grade of the mileage (7/10)
        grade_eco_mileage = 7

    # If mileage is between 15000 and 20000 km per year, the eco note is 5/10
    elif 15000 <= mileage < 20000:

        # Print the eco note on the terminal
        print("The eco note is 5/10 for a milage between 15000 and 20000 km per year")

        # Define the grade of the mileage (5/10)
        grade_eco_mileage = 5

    # If mileage is between 20000 and 25000 km per year, the eco note is 3/10
    elif 20000 <= mileage < 25000:

        # Print the eco note on the terminal
        print("The eco note is 3/10 for a milage between 20000 and 25000 km per year")

        # Define the grade of the mileage (3/10)
        grade_eco_mileage = 3

    # If mileage is between 25000 and 30000 km per year, the eco note is 1/10
    elif 25000 <= mileage < 30000:

        # Print the eco note on the terminal
        print("The eco note is 1/10 for a milage between 25000 and 30000 km per year")

        # Define the grade of the mileage (1/10)
        grade_eco_mileage = 1

    # If mileage is over 30000 km per year, the eco note is 0/10
    elif mileage >= 30000:

        # Print the eco note on the terminal
        print("The eco note is 0/10 for a milage over 30000 km per year")

        # Define the grade of the mileage (0/10)
        grade_eco_mileage = 0

    # If mileage is negative, the eco note is 'err' because it's not possible
    elif mileage < 0:

        # Print the error message on the terminal
        print("The mileage is not possible, it can't be negative")

        # Define and error as grade of the mileage ('err')
        grade_eco_mileage = "err-negative"

    # If mileage is not recognized, the eco note is 'err'
    else:

        # Print the error message on the terminal
        print("The mileage is not recognized")

        # Define and error as grade of the mileage ('err')
        grade_eco_mileage = "err-unknown"

    # Return the grade of the mileage to the main program
    return grade_eco_mileage

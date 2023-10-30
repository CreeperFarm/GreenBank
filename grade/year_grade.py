# Calculate grade by year of the car


def grade_year(year):
    # If the year of the car is between 2010 and 2025, the eco note is 7/10
    if 2010 <= year <= 2025:

        # Print the eco note on the terminal
        print("The eco note of 7/10")

        # Define the grade of the year (7/10)
        grade_eco_year = 7

    # If the year of the car is between 2000 and 2010, the eco note is 5/10
    elif 2000 <= year < 2010:

        # Print the eco note on the terminal
        print("The eco note of 5/10")

        # Define the grade of the year (5/10)
        grade_eco_year = 5

    # If the year of the car is between 1990 and 2000, the eco note is 4/10
    elif 1990 <= year < 2000:

        # Print the eco note on the terminal
        print("The eco note of 4/10")

        # Define the grade of the year (4/10)
        grade_eco_year = 4

    # If the year of the car is between 1980 and 1990, the eco note is 3/10 (This wasn't defined on the subject)
    elif 1980 <= year < 1990:

        # Print the eco note on the terminal
        print("The eco note of 3/10")

        # Define the grade of the year (3/10)
        grade_eco_year = 3

    # If the year of the car is between 1970 and 1980, the eco note is 2/10
    elif 1970 <= year < 1980:

        # Print the eco note on the terminal
        print("The eco note of 2/10")

        # Define the grade of the year (2/10)
        grade_eco_year = 2

    # If the year of the car is between 1960 and 1970, the eco note is 1/10
    elif 1960 <= year < 1970:

        # Print the eco note on the terminal
        print("The eco note of 1/10")

        # Define the grade of the year (1/10)
        grade_eco_year = 1

    # If the year of the car is between 1908 and 1960, the eco note is 0/10 (1908 is the year of the first car)
    elif 1908 <= year < 1960:

        # Print the eco note on the terminal
        print("The eco note of 0/10")

        # Define the grade of the year (0/10)
        grade_eco_year = 0

    # If the year of the car is before 1908, the eco note is 'err' because it's not possible
    elif year < 1908:

        # Print the error message on the terminal
        print("The year of the car is not possible, the first car was created in 1908")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-under"

    # If the year of the car is after 2025, the eco note is 'err' because the preorder doesn't go this far
    elif year > 2025:

        # Print the error message on the terminal
        print("The year of the car is not possible, the preorder don't go this far")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-over"

    # If the year of the car is not recognized, the eco note is 'err'
    else:

        # Print the error message on the terminal
        print("The year of the car is not recognized")

        # Define and error as grade of the year ('err')
        grade_eco_year = "err-unknown"

    # Return the grade of the year to the main program
    return grade_eco_year

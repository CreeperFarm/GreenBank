# Calculate persentage of borrowing rate for the loan
def borrowing_rate_function(grade_eco_vehicule, grade_eco_energy, grade_eco_mileage, grade_eco_year):
    # Define the grade of the car by adding the grades of the vehicule, energy, mileage and year
    grade_eco_car = grade_eco_vehicule + grade_eco_energy + grade_eco_mileage + grade_eco_year

    # If the grade of the car is between 0 and 10, the borrowing rate is 3%
    if 0 <= grade_eco_car <= 10:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 3%")

        # Define the borrowing rate (3%)
        borrowing_rate = 3 * 0.01

    # If the grade of the car is between 11 and 15, the borrowing rate is 2.74%
    elif 11 <= grade_eco_car <= 15:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.74%")

        # Define the borrowing rate (2.74%)
        borrowing_rate = 2.74 * 0.01

    # If the grade of the car is between 21 and 30, the borrowing rate is 2.52%
    elif 16 <= grade_eco_car <= 25:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.52%")

        # Define the borrowing rate (2.52%)
        borrowing_rate = 2.52 * 0.01

    # If the grade of the car is between 26 and 33, the borrowing rate is 2.10%
    elif 26 <= grade_eco_car <= 33:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 2.10%")

        # Define the borrowing rate (2.10%)
        borrowing_rate = 2.10 * 0.01

    # If the grade of the car is between 34 and 40, the borrowing rate is 1.85%
    elif 34 <= grade_eco_car <= 40:

        # Print the borrowing rate on the terminal
        print("The borrowing rate is 1.85%")

        # Define the borrowing rate (1.85%)
        borrowing_rate = 1.85 * 0.01

    # If the grade of the car is over 40, it's not possible because max grade is 40
    elif grade_eco_car > 40:

        # Print the error message on the terminal
        print("The borrowing rate is not possible, the max grade is 40")

        # Define and error as borrowing rate ('err-over')
        borrowing_rate = "err-over"

    # If the grade of the car is negative, it's not possible because min grade is 0
    elif grade_eco_car < 0:

        # Print the error message on the terminal
        print("The borrowing rate is not possible, the min grade is 0")

        # Define and error as borrowing rate ('err-negative')
        borrowing_rate = "err-negative"

    else:

        # Print the error message on the terminal
        print("The borrowing rate is not recognized")

        # Define and error as borrowing rate ('err-unknown')
        borrowing_rate = "err-unknown"

    # Return the borrowing rate to the main program
    return borrowing_rate
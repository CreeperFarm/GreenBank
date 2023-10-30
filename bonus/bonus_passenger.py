# Calculate bonus / manus by number of passengers of the car

def bonus_passenger_function(passenger):
    # If the number of passengers is 1, the malus is 0.11%
    if passenger == 1:

        # Print the bonus on the terminal
        print("The malus is 0.11% for 1 passenger")

        # Define the bonus (0.11%)
        bonus_passenger = 0.11 * 0.01

    # If the number of passengers is 2, the bonus is 0.17%
    elif passenger == 2:

        # Print the bonus on the terminal
        print("The bonus is 0.17% for 2 passengers")

        # Define the bonus (-0.17%)
        bonus_passenger = -0.17 * 0.01

    # If the number of passengers is 3, the bonus is 0.29%
    elif passenger == 3:

        # Print the bonus on the terminal
        print("The bonus is 0.29% for 3 passengers")

        # Define the bonus (-0.29%)
        bonus_passenger = -0.29 * 0.01

    # If the number of passengers is 4, the bonus is 0.53%
    elif passenger == 4:

        # Print the bonus on the terminal
        print("The bonus is 0.53% for 4 passengers")

        # Define the bonus (-0.53%)
        bonus_passenger = -0.53 * 0.01

    # If number of passenger over 5, the bonus is not defined
    elif passenger >= 5:

        # Print the error message on the terminal
        print("The bonus is not defined for more than 4 passengers")

        # Define and error as bonus ('err-over')
        bonus_passenger = "err-over"

    # If the number of passengers is negative, the bonus is not defined
    elif passenger < 0:

        # Print the error message on the terminal
        print("The bonus is not defined for negative passengers")

        # Define and error as bonus ('err-negative')
        bonus_passenger = "err-negative"

    # If the number of passengers is not recognized, the bonus is not defined
    else:

        # Print the error message on the terminal
        print("The bonus is not recognized")

        # Define and error as bonus ('err-unknown')
        bonus_passenger = "err-unknown"

    # Return the bonus to the main program
    return bonus_passenger
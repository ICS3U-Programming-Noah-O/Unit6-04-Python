#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Feb. 1, 2022
# This program find the average of numbers in a 2 dimensional array


import random
import constants


def calc_average(row_array):
    # This function calculates the average
    total = 0
    # Loop that calculates the average value
    for col_array in (row_array):
        for element in (col_array):
            total = total + element
    average = total / (len(row_array) * len(row_array[0]))
    return average


def main():
    # This function creates the array and
    # fills the array
    row_array = []
    user_row_choice = input("How many rows would you like? : ")
    user_col_choice = input("How many columns would you like? : ")
    try:
        # Make sure that the user inputted an integer
        user_row_choice_int = int(user_row_choice)

        try:
            # Make sure that the user inputted an integer
            user_col_choice_int = int(user_col_choice)
            for loop_counter_rows in range(0, user_row_choice_int):
                temp_column = []
                for loop_counter_columns in range(0, user_col_choice_int):
                    a_random_number = random.randint(constants.MIN,
                                                     constants.MAX)
                    temp_column.append(a_random_number)

                row_array.append(temp_column)
                print("")
            # Call a function to calculate the average
            final_average = calc_average(row_array)
            print(row_array)
            print(" ")
            # Print the final average
            print("The final average is: {}".format(final_average))

        except Exception:
            print("Your input must be an integer.")

    except Exception:
        print("Your input must be an integer.")


if __name__ == "__main__":
    main()

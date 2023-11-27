#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Nov 25, 2023
# This program will ask user for temp in celsius
# and display it in fahrenheit


def fahrenheit():
    # Get temperature in Celsius from the user and display message
    print("This program will ask user for temp in celsius")
    print("and display it in fahrenheit.")
    user_celsius_str = input("Enter temperature in degrees Celsius: ")

    # Catch if the temp is something wrong
    try:
        # Convert temp as a string to int
        user_celsius_int = int(user_celsius_str)

        # calculation cel to fah
        fahrenheit_temp = (user_celsius_int * 9 / 5) + 32

        # Display the Converted temp
        print(f"Temperature in Fahrenheit: {fahrenheit_temp}°F")

    except Exception:
        # Message for invalid user number
        print("\n{} is not a valid temp.".format(user_celsius_str))


def main():
    # Call the fahrenheit function
    fahrenheit()


if __name__ == "__main__":
    main()

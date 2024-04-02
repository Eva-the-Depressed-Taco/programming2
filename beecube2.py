
import sys

# Conversion factors.
# These are separate from the code, given helpful names, and are written in ALL_CAPS.
# The ALL_CAPS names are because these are constant values that do not change.
# This is a common naming convention you will see in many different programming languages.
BEES_PER_MM: int = 30
MM_PER_M: int = 1000
MM_PER_KM: int = 1000 * 1000
KM_PER_LIGHTYEAR: int = 9_460_730_472_600

input_type = input("would you like to enter a base length or number of bees? length/bees: ")
if input_type == "length":
    unit = input("Enter a unit, millimeters, meters, kilometers, lightyears: ")
    if unit == "millimeters":
        millimeters = int(input("Enter Length: "))
        length_in_bees = millimeters / BEES_PER_MM
    elif unit == "meters":
        meters = int(input("Enter Length: "))
        length_in_bees = (meters * MM_PER_M) / BEES_PER_MM
    elif unit == "kilometers":
        kilometers = int(input("Enter Length: "))
        length_in_bees = (kilometers * MM_PER_KM) / BEES_PER_MM
    elif unit == "lightyears":
        lightyears = int(input("Enter Length: "))
        length_in_bees = (lightyears * KM_PER_LIGHTYEAR * MM_PER_KM) / BEES_PER_MM
    else:
        print(f'Error: unexpected input type. Expected one of ["millimeters", "meters", "kilometers", "lightyears"], got {unit}.')
        sys.exit()  # Exit the program early if you gave a bad input.

    total_number_of_bees = length_in_bees ** 3
    print(f"Number of bees: {total_number_of_bees:,.0f}")
    #print("Cubed bees:", beeL)
elif input_type == "bees":
    total_number_of_bees = int(input("Number of bees: "))
    cube_root_of_bees = total_number_of_bees ** (1 / 3)
    length_in_millimeters = (cube_root_of_bees * BEES_PER_MM)
    length_in_meters = (cube_root_of_bees * BEES_PER_MM) / MM_PER_M
    length_in_kilometers = (cube_root_of_bees * BEES_PER_MM) / MM_PER_KM
    length_in_lightyears = (cube_root_of_bees * BEES_PER_MM) / (MM_PER_KM * KM_PER_LIGHTYEAR)
    # Determine the appropriate unit based on the magnitude of length
    if length_in_lightyears >= 1:
        print(f"The cube would be {length_in_lightyears:.10f} lightyears by {length_in_lightyears:.10f} lightyears by {length_in_lightyears:.10f} lightyears")
    elif length_in_kilometers >= 1:
        print(f"The cube would be {length_in_kilometers:.10f} kilometers by {length_in_kilometers:.10f} kilometers by {length_in_kilometers:.10f} kilometers")
    elif length_in_meters >= 1:
        print(f"The cube would be {length_in_meters:.2f} meters by {length_in_meters:.2f} meters by {length_in_meters:.2f} meters")
    else:
        print(f"The cube would be {length_in_millimeters:.2f} millimeters by {length_in_millimeters:.2f} millimeters by {length_in_millimeters:.2f} millimeters")
# Handle errors instead of simply not doing anything if the user inputs something wrong
else:
    print(f'Error: unexpected input type. Expected one of ["length", "bees"], got {input_type}.')
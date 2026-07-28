# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def print_single_table():
    # Ask the user for the number
    num = int(input("Enter a number for the table: "))
    
    # Requirement: Must be a positive integer
    if num <= 0:
        print("Error: Please enter a positive integer.")
    else:
        print()
        print("Multiplication Table for", num, ":")
        
        # Loop from 1 to 12
        for i in range(1, 13):
            answer = num * i
            print(num, " x ", i, " = ", answer)


def print_multiple_tables():
    # Ask the user for the limit N
    n = int(input("Enter a number N for tables 1 to N: "))
    
    # Requirement: Must be a positive integer
    if n <= 0:
        print("Error: Please enter a positive integer.")
    else:
        # Outer loop controls which table we are printing
        for current_num in range(1, n + 1):
            print()
            print("Multiplication Table for", current_num, ":")
            
            # Inner loop prints 1 to 12 for the current table
            for i in range(1, 13):
                answer = current_num * i
                print(current_num, " x ", i, " = ", answer)
            
            # Print a separator line after each table
            print("---------------------------")


# --- Main Program ---
print("--- PART A: Single Table ---")
print_single_table()

print("\n--- PART B: Tables from 1 to N ---")
print_multiple_tables()
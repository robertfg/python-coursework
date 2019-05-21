# Imports
import math

# Function
def split_check(total, num_people):
    # cost_per_person = math.ceil(total / num_people)
    # return cost_per_person
    # Raise exception
    if num_people < 1:
        raise ValueError("More than one person is required to split a check.")
    return math.ceil(total / num_people)

# Call function
# amount_due = split_check(84.97, 4)

# Catch exceptions:
try:
    # Take user input
    total_due = float(input("What's the total?  "))
    num_people = int(input("How many people?  "))
    amount_due = split_check(total_due, num_people)
# except ValueError:
#     # Error
#     print("Invalid entry.")
except ValueError as err:
    # Error
    print("Invalid entry.  {}".format(err))
else:
    # Entry okay
    # amount_due = split_check(total_due, num_people)
    print("Each person owes ${}".format(amount_due))

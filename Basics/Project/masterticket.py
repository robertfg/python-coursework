# START VARIABLES
TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100


# Calculate the price of the block of tickets
def calculate_price(num_tickets):
    return ( num_tickets * TICKET_PRICE ) + SERVICE_CHARGE


# Run code continuously until no more tickets
while tickets_remaining >= 1:
    # Output how many tickets remaining
    print("There are {} tickets remaining.".format(tickets_remaining))

    # Gather user name and assign to variable
    name = input("What is your name?  ")

    # Prompt user for no. of tickets.
    num_tickets = input("How many tickets would you like, {}?  ".format(name))

    # Expect a ValueError if the value is not an integer
    try:
        num_tickets = int(num_tickets)

        # Raise error if user requests more tickets than available
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        # Include error text in output.
        print("Invalid entry.  {}.  Please try again.".format(err))
    else:
        # Calculate price
        amount_due = calculate_price(num_tickets)

        # Output price to screen
        print("Total due is ${} ".format(amount_due))

        # Prompt user to proceed: Y/N
        proceed = input("Do you want to proceed (Y/N)?  ")

        # If they want to proceed
        if proceed.lower() == 'y':
            # Print "Sold"
            print("Sold!")

            # TODO: Gether credit card info. and process.

            # Decrement tickets remaining
            tickets_remaining -= num_tickets

        # Otherwise
        else:
            # Thank them
            print("Thanks anyway, {}.".format(name))

# Notify user there are no more tickets
print("Sorry, sold out.")

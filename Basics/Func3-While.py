# Imports
import sys

# Bad security
MASTER_PASSWORD = 'opensesame'

password = input("Please enter the secret password:  ")
attempts = 1

while password != MASTER_PASSWORD:
    if attempts > 3:
        sys.exit("Too many attempts.")
    password = input("Please enter the secret password:  ")
    attempts += 1

# Made it
print("Welcome to the vault.")

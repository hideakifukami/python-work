"""Birthday Paradox Simulation, by Hideaki Fukami
Explore the surprising probabilities of the 'Birthday Paradox'."""

import datetime, random

def getBirthdays(numberOfBirthdays):
    # Returns a list of number random date objects for birthdays.
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant.
        startOfYear = datetime.date(2022, 1, 1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randinte(0, 364))    
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMath(birthdays):
    # Returns the date object of a birthday that occurs more than once in the birthdays list.
    if len(birthdays) == len(set(birthdays)):
        return None

    # Compare each birthday to every other.
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA

# Display the intro:
print('''Birthday Paradox!
by Hideaki Fukami

The Birthday Paradox show us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.

(It's not actually a paradox, it's just surprising result.)
''') 

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

# Generate and display the birthdays:
print(f'Here are {numBDays} birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName}, birthday.day'
    print(dateText, end='')
print()
print()


favorite_fruits = ['banana', 'melon', 'watermelon', 'papaya', 'avocado', 'apple', 'pineapple']

fruit = input("Choose a fruit.")

if fruit.lower() in favorite_fruits:
    print("Congratulations! You choose a correct fruit!")
else:
    print("Sorry! You choose an incorrect fruit.")
alien_color = input("Choose the alien color:\nGreen\nYellow\nRed\n")

score = ''

if alien_color.lower() == 'green':
    score = 5
elif alien_color.lower() == 'yellow':
    score = 10
elif alien_color.lower() == 'red':
    score = 15
else:
    score =0
    print('You need to choose one of the options.')

print(f'You make {score} points.')
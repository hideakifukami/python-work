"""Bitmap Message, by Hideaki Fukami
Display a text message according to the provided bitmap image."""

import sys

bitmap = '''
                                               **
                                              ****
                                            *******
                                          ***********
                                         **************
          *********        *********  **************
       *************** **************************
     *******     *******************************
    *****    *************************** *****
  *****  *******************************
  ***************************************
  ***************************************
  ***************************************
  ***************************************
  ***************************************
   *************************************
   ************************************
    **********************************
      *******************************
   *   *****************************
  **     *** *********************
  ***   ** *********************
  * **** **  *****************
  *  *  **     *************
 *     ***        *******
*        ***        **
*************'''

print('''Bitmap Message, by Hideaki Fukami
Enter the message to display with the bitmap.''')
message = input('> ')
if message == '':
    sys.exit()

# Loop over each line in the bitmap:
for line in bitmap.splitlines():
    # Loop over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            print(' ', end='')
        else:
            print(message[i % len(message)], end='')
    print()

print()
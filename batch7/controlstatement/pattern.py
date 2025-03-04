

for x in range(1, 11):  # Loop for each row
    for y in range(x):  # Loop to print stars in each row
        print(" ","*",end="")  # Print stars without moving to the next line
    print()  # Move to the next line after printing all stars for the current row


for x in range(11, 1, -1):  # Start from 10 and decrement down to 1
    for y in range(x):  # Loop to print stars in each row
        print(" ","*", end="")  # Print stars without moving to the next line
    print()  # Move to the next line after printing all stars for the current row


for x in range(1, 11):  # Loop for each row
    print(" " * (10 - x) + "*" * (2 * x - 1))  # Print spaces followed by stars


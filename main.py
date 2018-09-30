# first round
userin1 = int(input('We start with 13 chocolates and 1 chili pepper. Who has to eat the chili pepper? Enter 1,2 or 3: '));
if userin1 >= 4:
    int(input('Needs to be 1, 2, or 3: '))
chili1 = int(4 - userin1)
chococounter = 13 - 4
print('You picked ', userin1, 'computer chose', chili1)
print('Chococounter:', chococounter)

# second round
userin2 = int(input('Go again and pick 1, 2, or 3: '))
if userin2 >= 4:
    int(input('Needs to be 1, 2, or 3: '))
chili2 = int(4 - userin2)
chococounter2 = chococounter - 4
print('You picked ', userin2, 'computer chose', chili2)
print('Chocounter:', chococounter2)

# third round
userin3 = int(input('Go again and pick 1, 2, or 3: '))
if userin1 >= 4:
    int(input('Needs to be 1, 2, or 3: '))
chili3 = int(4 - userin2)
chococounter3 = chococounter2 - 4
print('You pick ', userin3)
print('Chocounter:', chococounter3)

# pepeer round
userin4 = int(input('Last round. You pick: '))

print('COMPUTER EATS THE PEPPER! Lucky you')



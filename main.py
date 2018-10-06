# first round

userin1 = int(input('We start with 13 chocolates and 1 chili pepper. Who has to eat the chili pepper? Enter 1,2 or 3: '));
while userin1 >= 4:
    userin1 = int(input('Needs to be 1, 2, or 3: '))
    if userin1 <= 3:
        break

chili1 = int(4 - userin1)
chococounter = 13 - 4
print('You picked ', userin1, 'computer chose', chili1)
print('Chococounter:', chococounter)

# second round
userin2 = int(input('We start with 13 chocolates and 1 chili pepper. Who has to eat the chili pepper? Enter 1,2 or 3: '));
while userin2 >= 4:
    userin2 = int(input('Needs to be 1, 2, or 3: '))
    if userin2 <= 3:
        break

chili2 = int(4 - userin2)
chococounter2 = chococounter - 4
print('You picked ', userin2, 'computer chose', chili2)
print('Chocounter:', chococounter2)

# third round
userin3 = int(input('We start with 13 chocolates and 1 chili pepper. Who has to eat the chili pepper? Enter 1,2 or 3: '));
while userin3 >= 4:
    userin3 = int(input('Needs to be 1, 2, or 3: '))
    if userin3 <= 3:
        break

userin3 = int(input('Needs to be 1, 2, or 3: '))
chili3 = int(4 - userin2)
chococounter3 = chococounter2 - 4
print('You picked ', userin3, 'computer chose', chili3)
print('Chocounter:', chococounter3)

# pepeer round
userin4 = int(input('Last round. You pick: '))

print('COMPUTER EATS THE PEPPER! Lucky you')


year = 0  # Year 0
tuition = 12000  # Year 1

while tuition < 20000:
    year += 1
    tuition = tuition * 1.07

print('Tuition will be doubled in', year, 'years')
print('Tuition will be $' + format(tuition, '.2f'), 'in', year, 'years')
print('Tuition will be ${:.2f} in {:d} years'.format(tuition, year))

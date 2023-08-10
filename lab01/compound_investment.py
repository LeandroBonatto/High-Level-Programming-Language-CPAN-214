saving = float(input('Enter the monthly saving amount: '))

totalsav1 = saving * (1 + 0.005)
totalsav2 = (saving + totalsav1) * (1 + 0.005)
totalsav3 = (saving + totalsav2) * (1 + 0.005)
totalsav4 = (saving + totalsav3) * (1 + 0.005)
totalsav5 = (saving + totalsav4) * (1 + 0.005)
totalsav6 = (saving + totalsav5) * (1 + 0.005)

print('After the sixth month, the account value is {:.2f}'.format(totalsav6))
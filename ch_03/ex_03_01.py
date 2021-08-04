# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

hrs = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
ot = hrs - 40
ot_rate = rate * 1.5
if ot > 0 :
    pay = 40 * rate + ot * ot_rate
else :
    pay = hrs * rate

print('Pay:',pay)

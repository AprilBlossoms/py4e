# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay
# which takes two parameters (hours and rate).

hrs = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))

def computepay(hours, rate):
    ot = hrs - 40
    ot_rate = rate * 1.5
    if ot > 0 :
        pay = 40 * rate + ot * ot_rate
    else :
        pay = hrs * rate

    return pay

print('Pay:', computepay(hrs, rate))

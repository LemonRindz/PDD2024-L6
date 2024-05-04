totalLbs = float(input('Enter Total Weight (lbs): '))

def totalCost(lbs):
    if lbs <= 2:
        print(f'The package weighs {lbs} lbs')
        print(f'Rate Per Pound: $1.10')
        print(f'Shipping Cost: ${lbs * 1.1:.2f}')
    elif 2 < lbs <= 6:
        print(f'The package weighs {lbs} lbs')
        print(f'Rate Per Pound: $2.20')
        print(f'Shipping Cost: ${lbs * 2.2:.2f}')
    elif 6 < lbs <= 10:
        print(f'The package weighs {lbs} lbs')
        print(f'Rate Per Pound: $3.70')
        print(f'Shipping Cost: ${lbs * 3.7:.2f}')
    elif 10 < lbs:
        print(f'The package weighs {lbs} lbs')
        print(f'Rate Per Pound: $3.80')
        print(f'Shipping Cost: ${lbs * 3.8:.2f}')
    else:
        print('ERROR! Enter total weight in pounds (lbs)')

totalCost(totalLbs)
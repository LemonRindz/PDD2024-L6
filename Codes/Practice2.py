#Imani Hollie 02/07/2024
#This program is a repitition structure

#fourlegs is not defined
while dog < fourlegs:
    print('The dog has less than 4 legs.')

#fourlegs is now a literal (integer)
#BUT! dog is not defined
fourlegs = 5
while dog < fourlegs:
    print('The dog has less than 4 legs.')

#dog is now an integer
#BUT! The loop is infinite
fourlegs = 5
dog = 0
while dog < fourlegs:
    print('The dog has less than 4 legs.')

#This loop works
#BUT! It prints 5 over and over
fourlegs = 5
dog = 0
while dog < fourlegs:
    print('The dog has less than 4 legs.')
    dog = dog + 1

#This is correct
fourlegs = 5
dog = 0
while dog < fourlegs:
    print(f'The dog has less {dog} legs.')
    dog = dog + 1
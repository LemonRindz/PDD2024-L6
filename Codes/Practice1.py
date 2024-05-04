#Imani Hollie 02/07/2024
#This program outputs commission rate

#Input-------------------------------------------
sales = float(input('Enter the total sales: $'))

#Calculations------------------------------------
COM_RATE = 0.10
comTotal = sales * COM_RATE

#Output------------------------------------------
#Use 'f' and the curly brackets {} when inserting
#variables in string
print(f'The commission is ${comTotal}')
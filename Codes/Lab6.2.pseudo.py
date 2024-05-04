#Imani Hollie 02.10.2024
#This program will collect package weight
#(package weight, rate per lbs, and final sale)

#Declare the main module [Inputs and Calls totalCost()]
#1. main()
    #Declare local variables
    #a. Declare Float totalLbs
    
    #Input for total seats sold per class
    #b. Display "Enter the total weight (in pounds) of the package: "
    #c. Input totalLbs

    #Call the totalCost module and pass totalLbs as reference
    #d. Call totalCost(totalLbs)
#1. End Module

#Output is then printed to the screen.

#Declare the totalCost module [Calculates and Outputs]
#2. Module totalCost(Float Ref lbs)

    #Calculate the cost of shipping with an IF-THEN-ELSE decision structure
    #Display package weight, shipping rate, and total cost or error message
    #Limit decimal places to two for total cost

    #IF lbs > 2 THEN Display package weight, shipping rate, and total cost
    #e. IF lbs > 2 
        #f. THEN Display "The package weighs", lbs, "lbs."
        #g. THEN Display "Cost Per Pound: $1.10"
        #h. THEN Display "Shipping Cost: $", (lbs * 1.1)

        #IF 2 < lbs > 6 THEN Display package weight, shipping rate, and total cost
        #i. ELSE IF 2 < lbs > 6
            #j. THEN Display "The package weighs", lbs, "lbs."
            #k. THEN Display "Cost Per Pound: $2.20"
            #l. THEN Display "Shipping Cost: $", (lbs * 2.2)

            #IF 6 < lbs > 10 THEN Display package weight, shipping rate, and total cost
            #m. ELSE IF 6 < lbs > 10
                #n. THEN Display "The package weighs", lbs, "lbs."
                #o. THEN Display "Cost Per Pound: $3.70"
                #p. THEN Display "Shipping Cost: $", (lbs * 3.7)

                #IF 10 < lbs THEN Display package weight, shipping rate, and total cost
                #q. ELSE IF 10 < lbs
                    #r. THEN Display "The package weighs", lbs, "lbs."
                    #s. THEN Display "Cost Per Pound: $3.80"
                    #t. THEN Display "Shipping Cost: $", (lbs * 3.8)
                #If argument passes through - display error message
                #u. ELSE Display "ERROR! Enter total weight in pounds (lbs)"
                #v. End If
            #w. End If
        #x. End If
    #y. End If
#2. End Module
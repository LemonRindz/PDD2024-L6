#Imani Hollie 02.10.2024
#This program takes two primary colors and calculates
#the color mixed or displays an error message.

#Declare the main module [Inputs and Calls mixColor()]
#1. main()
    #Declare local variables
    #a. Declare Float priColor1
    #b. Declare Float priColor2
    
    #Input for total seats sold per class
    #c. Display "Enter a primary color: "
    #d. Input priColor1
    #e. Display "Enter a different primary color: "
    #f. Input priColor2

    #Call the mixColor module and pass priColor1 and
    #priColor2 as reference
    #g. Call mixColor(priColor1, priColor2)
#1. End Module

#Output is then printed to the screen.

#Declare the mixColor module [Calculates and Outputs]
#2. Module mixColor(Float Ref color1, Float Ref color2)

    #Calculate the color mixed with an IF-THEN-ELSE decision structure
    #Display primary colors and color mixed or error message

    #IF color1 == RED and IF color2 == YELLOW/BLUE THEN Display ORANGE/PURPLE
    #a. IF color1 == 'RED', 'red', 'red' THEN
        #b. IF color2 == 'YELLOW', 'Yellow', 'yellow'
            #c. THEN Display color1, "mixed with", color2, "makes ORANGE."
        #d. ELSE IF color2 == 'BLUE', 'Blue', 'blue'
            #e. THEN Display color1, "mixed with", color2, "makes PURPLE."

        #IF color1 == YELLOW and IF color2 == RED/BLUE THEN Display ORANGE/GREEN
        #f. ELSE IF color1 == 'YELLOW', 'Yellow', 'yellow' THEN
            #g. IF color2 == 'RED', 'red', 'red'
                #h. THEN Display color1, "mixed with", color2, "makes ORANGE."
            #i. ELSE IF color2 == 'BLUE', 'Blue', 'blue'
                #j. THEN Display color1, "mixed with", color2, "makes GREEN."

            #IF color1 == BLUE and IF color2 == RED/YELLOW THEN Display PURPLE/GREEN
            #k. ELSE IF color1 == 'BLUE', 'Blue', 'blue' THEN
            #l. IF color2 == 'RED', 'red', 'red'
                #m. THEN Display color1, "mixed with", color2, "makes PURPLE."
            #n. ELSE IF color2 == 'YELLOW', 'Yellow', 'yellow'
                #o. THEN Display color1, "mixed with", color2, "makes GREEN."
            #If argument passes through - display error message
            #p. ELSE Display "ERROR! Vaild entries include: RED, Red, red,
                            #YELLOW, Yellow, yellow, BLUE, BLue, blue."
            #r. End If
        #s. End If
    #t. End If
#2. End Module
#Programmed by Blake Emal
#January 22, 2017
#Miles Per Gallon Calculator

#Welcome users to MPG Calculator
print("Welcome to the Miles Per Gallon Calculator!")

#Prompt user to enter in number of miles traveled
milesTraveled = float(input("Please enter the amount of miles you have traveled."))
print("You have traveled",format(milesTraveled, '.2f'),"miles.")

#Prompt user to enter in number of gallons used
gallonsUsed = float(input("Please enter the amount of gallons you have used."))
print("You have used",format(gallonsUsed, '.2f'),"gallons.")

#Calculate MPG
milesPerGallon = milesTraveled/gallonsUsed

#Display MPG to user
print("Your miles per gallon is currently at", format(milesPerGallon, '.2f'))



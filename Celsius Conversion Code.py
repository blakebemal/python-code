#Programmed by Blake Emal
#January 22, 2017
#Celsius to Fahrenheit Conversion App


#Welcome user to the application
print("Welcome to the Celsius-to-Fahrenheit Conversion App!")

#Ask user to enter the temperature in Celsius
tempCelsius = float(input("Please enter the current temperature in Celsius"))

#Convert the Celsius temperature into Fahrenheit
tempFahrenheit = (tempCelsius*1.8)+32

#Display temperature in Fahrenheit
print("Your current temperature in Fahrenheit is ",format(tempFahrenheit, '.2f'))


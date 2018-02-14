#Programmed by Blake Emal
#January 24, 2017
#Sweater Weather
#This program tells you if you need to wear a sweater today

#Welcome screen
print("Want to know if you need to wear a sweater today? We'll help you out.")

#Name
firstName = input("What is your name?")
print('Nice to meet you, ' + str(firstName) + '.')

#What is the temperature?
temp = float(input("Ok, " + " " + str(firstName) + "What is the current temperature where you are?"))
if(not(temp>0)) :
   print("You need to move. It is way too cold up there.")
else:
    if(not(temp<110)) :
        print("You are going to melt if you don't get some shade.")
    else:
        #Do you get cold easily?
        sensitivity = input("Would you say that you get cold very easily, " + str(firstName) + "?")

        #Variables
        Yes = ("Yes")
        No = ("No")

        #Calculate if sweater is needed
        #Display result
        if (temp>70) and (sensitivity==No):
            print("You will be just fine with no sweater, ",firstName,".")

        else:
            print("Looks like you should play it safe and wear a sweater, ",firstName,".")



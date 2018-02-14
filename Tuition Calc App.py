#Tuition Increase Program
#Programmed by Blake Emal
#February 12, 2018

# 1)	Welcome the user to the program
print("Thank you for using the Gulf Coast Tuition Increase Notifier.")



# 2)	Make user aware of upcoming tuition increases

print("Please note that tuition will increase each year by 3%, starting next year and ending in 2023.")



# 3)	Compute the original tuition (counter at 1)

tuition = 8000
percentIncrease = 0.03

# 4) Loop the counter until Year 5
for yearOfTuition in [1,2,3,4,5]:
    tuition = (tuition*percentIncrease) + tuition
    print(yearOfTuition,"\t",tuition)


# 8)	End program 

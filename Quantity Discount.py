#Programmed by Blake Emal
#January 31, 2018
#Computer Software Quantity Discount Calculator


#Welcome user to Quantity Discount App
print("Thank you for buying software with us. Let's see if you qualify for discounts.") 


#Prompt user to input numPackages
numPackages = int(input("How many packages of software did you purchase?"))


#Compute totalSale before discount applied
totalSale = numPackages * 99

#Determine packageDiscount
if (numPackages <=0):
    discountPercent = 0
elif (numPackages <=10):
    discountPercent = 0.10
elif (numPackages <=20):
    discountPercent= 0.20
elif (numPackages <=50):
    discountPercent = 0.30
elif (numPackages <=100):
    discountPercent = 0.40

#Compute the packageDiscount
packageDiscount =  totalSale * discountPercent


#Compute the finalPrice
finalPrice = totalSale  - packageDiscount 


#Display the packageDiscount and finalPrice
print("You purchased ",numPackages,"packages."'\n'
      "This means you qualify for a: ",discountPercent*10,"% discount."'\n'
      "With the discount, your new total is: ",finalPrice)


#Harvard Personality Test and Results Application
#Programmed by Blake Emal
#February 18, 2018


#Set preliminary variables
pointsCounter = 0 
runAgain = "Y" or "y"

#Allow for a runAgain function that loops back to the start without having to restart the entire program
while ((runAgain == "Y") or (runAgain =="y")):
    readyToStart = input("\nPress ENTER to begin the Harvard Personality Test.")
#Validate that the user hit ENTER and not an invalid response
    while (readyToStart != ""):
        print("\nThis was an invalid response.")
        readyToStart = input("\nPress ENTER to begin the Harvard Personality Test.")
        
#Ask Question 1
    question1 = input("\n1. When you get up in the morning, what do you usually have for breakfast? \nA. Eggs and toast \nB. Cereal \nC. Pop Tart \nD. Nothing\n")
    validate1 = ((question1 == "A") or (question1 == "B") or (question1 == "C") or (question1 == "D") or (question1 == "a") or (question1 == "b") or (question1 == "c") or (question1 == "d"))
    points1 = 0
#Set the weighted points parameters for Question 1
    if((question1 == "A") or (question1 == "a")):
        points1 = 3
    elif((question1 == "B") or (question1 == "b")):
        points1 = 1
    elif((question1 == "C") or (question1 == "c")):
        points1 = 6
    elif((question1 == "D") or (question1 == "d")):
        points1 = 2
#Add points to the counter from Question 1
    pointsCounter += points1
#Validate Answer 1
    while not(validate1):
        print("Invalid response. Please select A, B, C, or D.")
        question1 = input("\n1. When you get up in the morning, what do you usually have for breakfast? \nA. Eggs and toast \nB. Cereal \nC. Pop Tart \nD. Nothing\n")
        validate1 = ((question1 == "A") or (question1 == "B") or (question1 == "C") or (question1 == "D") or (question1 == "a") or (question1 == "b") or (question1 == "c") or (question1 == "d"))
        if((question1 == "A") or (question1 == "a")):
            points1 = 3
        elif((question1 == "B") or (question1 == "b")):
            points1 = 1
        elif((question1 == "C") or (question1 == "c")):
            points1 = 6
        elif((question1 == "D") or (question1 == "d")):
            points1 = 2
        pointsCounter += points1

#Ask Question 2
    question2 = input("\n2. If you could have anything you desired, what would you have for breakfast? \nA.Eggs and toast \nB. Something else \nC. Pop Tart \nD. Cake\n")
    validate2 = ((question2 == "A") or (question2 == "B") or (question2 == "C") or (question2 == "D") or (question2 == "a") or (question2 == "b") or (question2 == "c") or (question2 == "d"))
    points2 = 0
#Set the weighted points parameters for Question 2
    if((question2 == "A") or (question2 == "a")):
        points2 = 2
    elif((question2 == "B") or (question2 == "b")):
        points2 = 1
    elif((question2 == "C") or (question2 == "c")):
        points2 = 3
    elif((question2 == "D") or (question2 == "d")):
        points2 = 4
#Add points to the counter from Question 2
    pointsCounter += points2
#Validate Answer 2
    while not(validate2):
        print("Invalid response. Please select A, B, C, or D.")
        question2 = input("\n2. If you could have anything you desired, what would you have for breakfast? \nA.Eggs and toast \nB. Something else \nC. Pop Tart \nD. Cake\n")
        validate2 = ((question2 == "A") or (question2 == "B") or (question2 == "C") or (question2 == "D") or (question2 == "a") or (question2 == "b") or (question2 == "c") or (question2 == "d"))
        if((question2 == "A") or (question2 == "a")):
            points2 = 2
        elif((question2 == "B") or (question2 == "b")):
            points2 = 1
        elif((question2 == "C") or (question2 == "c")):
            points2 = 3
        elif((question2 == "D") or (question2 == "d")):
            points2 = 4
        pointsCounter += points2

#Ask Question 3
    question3 = input("\n3. It's lunch time. You: \nA. Skip a meal because you are too busy or worried about your weight \nB. Get what you have spent all morning thinking about \nC. Eat the food you brought with you \nD. Find out what your friends are having and tag along\n")
    validate3 = ((question3 == "A") or (question3 == "B") or (question3 == "C") or (question3 == "D") or (question3 == "a") or (question3 == "b") or (question3 == "c") or (question3 == "d"))
    points3 = 0
#Set the weighted points parameters for Question 3
    if((question3 == "A") or (question3 == "a")):
        points3 = 2
    elif((question3 == "B") or (question3 == "b")):
        points3 = 1
    elif((question3 == "C") or (question3 == "c")):
        points3 = 3
    elif((question3 == "D") or (question3 == "d")):
        points3 = 4
#Add points to the counter from Question 3
    pointsCounter += points3
#Validate Answer 3
    while not(validate3):
        print("Invalid response. Please select A, B, C, or D.")
        question3 = input("\n3. It's lunch time. You: \nA. Skip a meal because you are too busy or worried about your weight \nB. Get what you have spent all morning thinking about \nC. Eat the food you brought with you \nD. Find out what your friends are having and tag along\n")
        validate3 = ((question3 == "A") or (question3 == "B") or (question3 == "C") or (question3 == "D") or (question3 == "a") or (question3 == "b") or (question3 == "c") or (question3 == "d"))
        if((question3 == "A") or (question3 == "a")):
            points3 = 2
        elif((question3 == "B") or (question3 == "b")):
            points3 = 1
        elif((question3 == "C") or (question3 == "c")):
            points3 = 3
        elif((question3 == "D") or (question3 == "d")):
            points3 = 4
        pointsCounter += points3
    


#Ask Question 4
    question4 = input("\n4. A friend offers you some of his/her food. You:\nA. Take a bite because you are starving \nB. Take a bite to be polite \nC. Refuse because you are watching your weight \nD. Take 2 bites instead of just 1\n")
    validate4 = ((question4 == "A") or (question4 == "B") or (question4 == "C") or (question4 == "D") or (question4 == "a") or (question4 == "b") or (question4 == "c") or (question4 == "d"))
    points4 = 0
#Set the weighted points parameters for Question 4
    if((question4 == "A") or (question4 == "a")):
        points4 = 3
    elif((question4 == "B") or (question4 == "b")):
        points4 = 1
    elif((question4 == "C") or (question4 == "c")):
        points4 = 2
    elif((question4 == "D") or (question4 == "d")):
        points4 = 6
#Add points to the counter from Question 4
    pointsCounter += points4
#Validate Answer 4
    while not(validate4):
        print("Invalid response. Please select A, B, C, or D.")
        question4 = input("\n4. A friend offers you some of his/her food. You:\nA. Take a bite because you are starving \nB. Take a bite to be polite \nC. Refuse because you are watching your weight \nD. Take 2 bites instead of just 1\n")
        validate4 = ((question4 == "A") or (question4 == "B") or (question4 == "C") or (question4 == "D") or (question4 == "a") or (question4 == "b") or (question4 == "c") or (question4 == "d"))
        if((question4 == "A") or (question4 == "a")):
            points4 = 3
        elif((question4 == "B") or (question4 == "b")):
            points4 = 1
        elif((question4 == "C") or (question4 == "c")):
            points4 = 2
        elif((question4 == "D") or (question4 == "d")):
            points4 = 6
        pointsCounter += points4

#Ask Question 5
    question5 = input("\n5. Your future boyfriend/girlfriend offers you something to eat. It is:\nA. A cookie\nB. An apple\nC. A slice of pizza\nD. A carrot\n")
    validate5 = ((question5 == "A") or (question5 == "B") or (question5 == "C") or (question5 == "D") or (question5 == "a") or (question5 == "b") or (question5 == "c") or (question5 == "d"))
    points5 = 0
#Set the weighted points parameters for Question 5
    if((question5 == "A") or (question5 == "a")):
        points5 = 1
    elif((question5 == "B") or (question5 == "b")):
        points5 = 2
    elif((question5 == "C") or (question5 == "c")):
        points5 = 5
    elif((question5 == "D") or (question5 == "d")):
        points5 = 3
#Add points to the counter from Question 5
    pointsCounter += points5
#Validate Answer 5
    while not(validate5):
        print("Invalid response. Please select A, B, C, or D.")
        question5 = input("\n5. Your future boyfriend/girlfriend offers you something to eat. It is:\nA. A cookie\nB. An apple\nC. A slice of pizza\nD. A carrot\n")
        validate5 = ((question5 == "A") or (question5 == "B") or (question5 == "C") or (question5 == "D") or (question5 == "a") or (question5 == "b") or (question5 == "c") or (question5 == "d"))
        if((question5 == "A") or (question5 == "a")):
            points5 = 1
        elif((question5 == "B") or (question5 == "b")):
            points5 = 2
        elif((question5 == "C") or (question5 == "c")):
            points5 = 5
        elif((question5 == "D") or (question5 == "d")):
            points5 = 3
        pointsCounter += points5


#Ask Question 6
    question6 = input("\n6. Your dog is begging you for a treat. You give him:\nA. A dog biscuit\nB. Some cake\nC. Nothing, but you pet him\nD. Nothing and you push him away. Treats are bad for him.\n")
    validate6 = ((question6 == "A") or (question6 == "B") or (question6 == "C") or (question6 == "D") or (question6 == "a") or (question6 == "b") or (question6 == "c") or (question6 == "d"))
    points6 = 0
#Set the weighted points parameters for Question 6
    if((question6 == "A") or (question6 == "a")):
        points6 = 3
    elif((question6 == "B") or (question6 == "b")):
        points6 = 1
    elif((question6 == "C") or (question6 == "c")):
        points6 = 4
    elif((question6 == "D") or (question6 == "d")):
        points6 = 2
#Add points to the counter from Question 6
    pointsCounter += points6
#Validate Answer 6
    while not(validate6):
        print("Invalid response. Please select A, B, C, or D.")
        question6 = input("\n6. Your dog is begging you for a treat. You give him:\nA. A dog biscuit\nB. Some cake\nC. Nothing, but you pet him\nD. Nothing and you push him away. Treats are bad for him.\n")
        validate6 = ((question6 == "A") or (question6 == "B") or (question6 == "C") or (question6 == "D") or (question6 == "a") or (question6 == "b") or (question6 == "c") or (question6 == "d"))
        if((question6 == "A") or (question6 == "a")):
            points6 = 3
        elif((question6 == "B") or (question6 == "b")):
            points6 = 1
        elif((question6 == "C") or (question6 == "c")):
            points6 = 4
        elif((question6 == "D") or (question6 == "d")):
            points6 = 2
        pointsCounter += points6


#Ask Question 7
    question7 = input("\n7. In a dream, you are in the world's best restaurant. You order:\nA. Everything on the menu. It's a dream, right?\nB. A salad. A big one with everything in it.\nC. Steak.\nD. A rich dessert\n")
    validate7 = ((question7 == "A") or (question7 == "B") or (question7 == "C") or (question7 == "D") or (question7 == "a") or (question7 == "b") or (question7 == "c") or (question7 == "d"))
    points7 = 0
#Set the weighted points parameters for Question 7
    if((question7 == "A") or (question7 == "a")):
        points7 = 2
    elif((question7 == "B") or (question7 == "b")):
        points7 = 1
    elif((question7 == "C") or (question7 == "c")):
        points7 = 3
    elif((question7 == "D") or (question7 == "d")):
        points7 = 4
#Add points to the counter from Question 7
    pointsCounter += points7
#Validate Answer 7
    while not(validate7):
        print("Invalid response. Please select A, B, C, or D.")
        question7 = input("\n7. In a dream, you are in the world's best restaurant. You order:\nA. Everything on the menu. It's a dream, right?\nB. A salad. A big one with everything in it.\nC. Steak.\nD. A rich dessert\n")
        validate7 = ((question7 == "A") or (question7 == "B") or (question7 == "C") or (question7 == "D") or (question7 == "a") or (question7 == "b") or (question7 == "c") or (question7 == "d"))
        if((question7 == "A") or (question7 == "a")):
            points7 = 2
        elif((question7 == "B") or (question7 == "b")):
            points7 = 1
        elif((question7 == "C") or (question7 == "c")):
            points7 = 3
        elif((question7 == "D") or (question7 == "d")):
            points7 = 4
        pointsCounter += points7


#Ask Question 8
    question8 = input("\n8. You are stranded alone on a tropical island. What are the foods you have to have with you?\nA. Fruits and vegetables\nB. Meat and potatoes\nC. Ice cream, chocolate, and cake\nD. Chinese food\n")
    validate8 = ((question8 == "A") or (question8 == "B") or (question8 == "C") or (question8 == "D") or (question8 == "a") or (question8 == "b") or (question8 == "c") or (question8 == "d"))
    points8 = 0
#Set the weighted points parameters for Question 8
    if((question8 == "A") or (question8 == "a")):
        points8 = 4
    elif((question8 == "B") or (question8 == "b")):
        points8 = 3
    elif((question8 == "C") or (question8 == "c")):
        points8 = 2
    elif((question8 == "D") or (question8 == "d")):
        points8 = 5
#Add points to the counter from Question 8
    pointsCounter += points8
#Validate Answer 8
    while not(validate8):
        print("Invalid response. Please select A, B, C, or D.")
        question8 = input("\n8. You are stranded alone on a tropical island. What are the foods you have to have with you?\nA. Fruits and vegetables\nB. Meat and potatoes\nC. Ice cream, chocolate, and cake\nD. Chinese food\n")
        validate8 = ((question8 == "A") or (question8 == "B") or (question8 == "C") or (question8 == "D") or (question8 == "a") or (question8 == "b") or (question8 == "c") or (question8 == "d"))
        if((question8 == "A") or (question8 == "a")):
            points8 = 4
        elif((question8 == "B") or (question8 == "b")):
            points8 = 3
        elif((question8 == "C") or (question8 == "c")):
            points8 = 2
        elif((question8 == "D") or (question8 == "d")):
            points8 = 5
        pointsCounter += points8


#Ask Question 9
    question9 = input("\n9. You are an infant and your mother is feeding you:\nA. Baby Cereal or formula\nB. Broccoli\nC. A cookie\nD. Nothing, she is doing something else\n")
    validate9 = ((question9 == "A") or (question9 == "B") or (question9 == "C") or (question9 == "D") or (question9 == "a") or (question9 == "b") or (question9 == "c") or (question9 == "d"))
    points9 = 0
#Set the weighted points parameters for Question 9
    if((question9 == "A") or (question9 == "a")):
        points9 = 6
    elif((question9 == "B") or (question9 == "b")):
        points9 = 4
    elif((question9 == "C") or (question9 == "c")):
        points9 = 8
    elif((question9 == "D") or (question9 == "d")):
        points9 = 2
#Add points to the counter from Question 9
    pointsCounter += points9
#Validate Answer 9
    while not(validate9):
        print("Invalid response. Please select A, B, C, or D.")
        question9 = input("\n9. You are an infant and your mother is feeding you:\nA. Baby Cereal or formula\nB. Broccoli\nC. A cookie\nD. Nothing, she is doing something else\n")
        validate9 = ((question9 == "A") or (question9 == "B") or (question9 == "C") or (question9 == "D") or (question9 == "a") or (question9 == "b") or (question9 == "c") or (question9 == "d"))
        if((question9 == "A") or (question9 == "a")):
            points9 = 6
        elif((question9 == "B") or (question9 == "b")):
            points9 = 4
        elif((question9 == "C") or (question9 == "c")):
            points9 = 8
        elif((question9 == "D") or (question9 == "d")):
            points9 = 2
        pointsCounter += points9


#Ask Question 10
    question10 = input("\n10. You are 6 years old. Your dad is feeding you:\nA. Pizza\nB. Spaghetti-Os\nC. Bubble gum\nD. Carrots\n")
    validate10 = ((question10 == "A") or (question10 == "B") or (question10 == "C") or (question10 == "D") or (question10 == "a") or (question10 == "b") or (question10 == "c") or (question10 == "d"))
    points10 = 0
#Set the weighted points parameters for Question 10
    if((question10 == "A") or (question10 == "a")):
        points10 = 7
    elif((question10 == "B") or (question10 == "b")):
        points10 = 5
    elif((question10 == "C") or (question10 == "c")):
        points10 = 1
    elif((question10 == "D") or (question10 == "d")):
        points10 = 3
#Add points to the counter from Question 10
    pointsCounter += points10
#Validate Answer 10
    while not(validate10):
        print("Invalid response. Please select A, B, C, or D.")
        question10 = input("\n10. You are 6 years old. Your dad is feeding you:\nA. Pizza\nB. Spaghetti-Os\nC. Bubble gum\nD. Carrots\n")
        validate10 = ((question10 == "A") or (question10 == "B") or (question10 == "C") or (question10 == "D") or (question10 == "a") or (question10 == "b") or (question10 == "c") or (question10 == "d"))
        if((question10 == "A") or (question10 == "a")):
            points10 = 7
        elif((question10 == "B") or (question10 == "b")):
            points10 = 5
        elif((question10 == "C") or (question10 == "c")):
            points10 = 1
        elif((question10 == "D") or (question10 == "d")):
            points10 = 3
        pointsCounter += points10

#Display the total number of points and summary to user
    print("\nYour total number of points is: ",pointsCounter)
    
#Categorize the user into the proper summary group according to final total of pointsCounter
#Print the user's summary
    if ((pointsCounter >= 12) and (pointsCounter <= 20)):
        print("\nHere's your summary:\n \nYou tend to be a shy person. You may feel uncomfortable with a lot of other people. You sometimes think that you were given a body that does not fit your mind, and perhaps you were born in the wrong year. You are much smarter than most people think you are and you do not let other people know about it. You have a giant heart that gets crushed all the time. You tend to have an artistic flair. Music you like: songs about love, lost love, and heartbreak. Your favorite movie: Titanic. There are days when you would rather stay home and enjoy time to yourself than to go out and deal with annoying people. Cupid has toyed with you. Someone you loved has hurt you. Your parents fought when you were small. You have thought about getting a tattoo.")
    elif ((pointsCounter >= 21) and (pointsCounter <= 30)):
        print("\nHere's your summary:\n \nYou made your way in this world in spite of all the obstacles you have faced. You have seen a lot more troubles than most people. You have had to deal with difficult people, ridiculous rules, and tempestuous relationships. Love for you can be as intense as the fire on the face of the sun. You are either very calm on the inside when there is a lot of insanity around you or you shut people up and take charge. You can go to a movie by yourself without the need for someone to go with you. You are as comfortable alone as you are with others. You are angry at your parents and you can't change them. You are a great lover when you find that rare mate who is your equal, but otherwise your relationships have been short or frustrating. You have stayed too long with a partner you did not like. Life is a roller coaster, and you are finding ways to make the good times better. You LOVE sports or have taken drugs.")
    elif ((pointsCounter >= 31) and (pointsCounter <= 42)):
        print("\nHere's your summary:\n \nYou generally are a calm person. You get excited when your favorite band is in town, when you are going on a date with your partner, and when you and your friends are dancing. For you, your friends mean everything to you. You hate it when the summer is over. You like art, and some poetry. You can throw a party, or help a friend put one together. You usually have no trouble finding dates, but you occasionally hit a dry spell. You like the outdoors, usually, and rainy weather doesn't bother you. You sometimes get jealous of people who are smarter or better looking than you, but you wouldn't hold it against them if you got to know them. You are on good terms with your parents, even though they piss you off once in a while. People tend to think you are reliable and trustworthy. You like animals-sometimes.")
    elif ((pointsCounter >= 43) and (pointsCounter <= 53)):
        print("\nHere's your summary:\n \nSometimes there just isn't enough time in a day for you to do everything you would like to do. If there isn't anything fun going on at the moment, then you know how to get things rolling. You tend to be the kind of person people look up to, and you usually have the ability to excel at most things you try. You usually don't care what people think about you, and you have no problem kissing your mate in public. You tend to have an energy level that is one step above the others, but you can play it cool if you want to. You prefer to play sports than to watch. People have been jealous of you, but its unlikely you noticed. Your parents are active people, and may not have given you as much time as you wanted. You have a tattoo, play in a band, have blond hair, or are on a sports team. People copy you. Sometimes you are truly miserable, but not for long.")

#Initiate the runAgain function
    runAgain = input("\nDo you wish to take the test again? (Y/N)\n")
    while ((runAgain != "Y") and (runAgain != "y") and (runAgain != "N") and (runAgain !="n")):
#Check for invalid data
        print('\nPlease enter in Y,y,N, or n.')
        runAgain = input("\nDo you wish to take the test again? (Y/N)\n")

#End program       
print("\nThanks for taking the test. Have a great day!")
    




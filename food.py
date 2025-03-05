#Create a list
#Prompt the user to enter five foods, and store the responses in the list
#Display the list on one line, each item seperated by commas
#Calculate how many characters were entered and display this to the user
#Hint: Using the len() function will be useful here
#You must use a list for this assignment. Not using a list will result in an automatic 0.
#Below is a sample of what your output might look like. You do not have to follow the text exactly.
#
#Enter a food: pizza
#Enter a food: beef jerkey
#Enter a food: rice triangles
#Enter a food: steamed chinese bun
#Enter a food: fried chicken
#
#Your entered foods are:
#[pizza, beef jerkey, rice triangles, steamed chinese bun, fried chicken] 
#You entered a total of 62 characters

foodsList = []

for i in range(5):
    foodsList.append(str(input("Enter a food: ")))

charsList = []

for value in foodsList:
    charsList.append(int(len(value)))

sum = sum(charsList)

print(f"Your entered foods are: \n [{foodsList[0]}, {foodsList[1]}, {foodsList[2]}, {foodsList[3]}, {foodsList[4]}] \n You entered a total of {sum} characters.")

#I'm not sure if this was necessarily the intention, but the function listed below was my first instinct and it ended up giving a count of 82 compared to the 62 that you had gotten
#because len() counts brackets and commas when it interacts with a string directly. I also listed indices directly in the print string to have the same formatting as your example as
#well.

#foodsCharacters = len(str(foodsList))
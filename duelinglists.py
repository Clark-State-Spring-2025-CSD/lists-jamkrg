#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random
random.seed()

p1List = []
p2List = []

for i in range(10):
    p1List.append(random.randint(1,50))

for i in range(10):
    p2List.append(random.randint(1,50))

#Test purposes
#p1List = [5,7,2,9,1,1,3,8,6,9]
#p2List = [3,8,5,5,8,1,4,7,4,7]

p1Wins = 0
p2Wins = 0
#testing
#ties = 0

for i in range(10):
    if p1List[i] > p2List[i]:
        p1Wins += 1
    elif p1List[i] < p2List[i]:
        p2Wins += 1

p1Max = p1List.index(max(p1List))
p1Min = p1List.index(min(p1List))
p2Max = p2List.index(max(p2List))
p2Min = p2List.index(min(p2List))


print(f"Player One = {p1List} \nPlayer Two = {p2List}")
print(f"Player One won {p1Wins} times. \nPlayer Two won {p2Wins} times.")
#print(f"They tied {ties} times.")
print(f"Player One's highest number is {max(p1List)} at index {p1Max}.\nPlayer Two's highest number is {max(p2List)} at index {p2Max}.")
print(f"Player One's lowest number is {min(p1List)} at index {p1Min}.\nPlayer Two's lowest number is {min(p2List)} at index {p2Min}.")
import random
list1 = [-1,1,0]
computer = random.choice(list1)
youstr = input("Enter your choice : ")
youDict = {"snake" : 1,"water" : -1,"gun" : 0}
reverseDict = { 1 : "snake", -1 : "water" ,0 : "gun"}
you = youDict[youstr]
print(f"Your choice is {reverseDict[you]} , computer choice is {reverseDict[computer]}")
if(computer == you):
    print("It is a draw")
else:
     if(computer == 0 and you == 1):
         print("You Lose")
     elif(computer == 1 and you == -1):
         print("You Lose")
     elif(computer == -1 and you == 0):
         print("You Lose")
     elif(you == 0 and computer == 1):
         print("You are Winner")
     elif(you == 1 and computer == -1):
         print("You are Winner")
     elif(you == -1 and computer == 0):
         print("You are Winner")
     else:
         print("Something is wrong")
'''
We are going to write a program that generates a random number and asks the user to
guess it.

If the player's guess is higher than the actual number, the program displays "Lower
number please". Similarly, if the user's guess is too low, the program prints "higher
number please" When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.
'''
from random import randint
a = randint(1,100)
total = 0
n = None
while(a!=n):
    n = int(input("Enter a number between 1 to 100 : "))
    total+=1
    if (a==n):
        print("The guess is correct")
        print(f"the total guesses you have taken is {total}")
    elif(a>n):
        print(" uppar ka number soch na saale")
    else:
        print("neeche ka number sooch ka saale")
with open(r"C:\Users\joshi\OneDrive\Desktop\Python Project\highscore.txt","r") as f:
    a = f.read()
    if(total<int(a)):
        print(f"your new highscore is {total}")
        with open(r"C:\Users\joshi\OneDrive\Desktop\Python Project\highscore.txt","w") as f:
            f.write(str(total))
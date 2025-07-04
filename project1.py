'''
stone - 1
paper - 0
scissor - -1
'''
import random
yourdict = {"s":1,"p":0,"sc":-1}
yourinput = input("enter your choice")
computerdict = random.choice(["s","p","sc"])
computer = yourdict[computerdict]
if yourinput not in yourdict:
    print("invalid choice enter 's','p','sc'")
else:
  yourvalue = yourdict[yourinput]
  print(f"computer's choice :{computerdict}")
if ((computer == 1 and yourvalue == 0) or 
        (computer == 0 and yourvalue == -1) or 
        (computer == -1 and yourvalue == 1)):
    print("you win !")
elif computer == yourvalue:
    print("It's a tie")
else:
    print("you loose")
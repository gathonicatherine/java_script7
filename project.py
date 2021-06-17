print ("WELCOME TO THE GUESSING GAME")
start =0
while True: 
  guess= input("select(Easy,Normal,Difficult)")
  if guess =="Easy":
      end=10
      break
  elif guess =="Normal":
      end =30
      break 
  elif guess =="Difficult":
      end =40
      break
  else:
      print("That word doesn't exists")

import random        
number =random.randint(start,end)
while True:
    print("select a number from", start ,"to", end)
    guessing = int(input("Guess a number"))
    if guessing == number:
        print("Congratulations you did it")
        break
    elif guessing<start and guessing>end:   
        print("Oooops incorrect number")
    else:
        print("Try again")
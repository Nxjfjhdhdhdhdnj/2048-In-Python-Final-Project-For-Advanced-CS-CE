import random
import copy

gameDataArray = [[0,0,0,0],[0,0,0,0],[0,0,2048,0],[0,0,0,0]]
start = 0
yes="Y"
no="N"
winNum=2048

def clearConsole():
    print("\033c", end="")  # ANSI escape sequence to clear the console

def resetBoard():
  gameDataArray = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  randNumGen(gameDataArray, temp=0)
  return gameDataArray
  
def checkWinLoss(gameDataArray):
  count=0
  for x in range(len(gameDataArray)):
    for y in range(len(gameDataArray[x])):
      if(gameDataArray[x][y]==winNum):
        return "W"
      elif(gameDataArray[x][y]!=0):
        count+=1;
  if(count==16):
    count=0
    for x in range(len(gameDataArray)-1):
      for y in range(len(gameDataArray[x])-1):
        if(gameDataArray[x][y]==gameDataArray[x][y+1]):
          count+=1
        if(gameDataArray[x][y]==gameDataArray[x+1][y]):
          count+=1
  if(count!=0):
    return "noLoss"
          
def randNumGen(gameDataArray,temp):
  while(temp!=2):
    x = random.randint(0,3)
    y = random.randint(0,3)
    z = random.randint(1,10)
    if(gameDataArray[x][y]==0):
      if(z==10):
        gameDataArray[x][y]=4
      if(z in range(1,9)):
        gameDataArray[x][y]=2
      temp+=1
  return gameDataArray 

def display(gameDataArray):
  clearConsole()
  print("\n")
  for x in range(len(gameDataArray)):
    for y in range(len(gameDataArray[x])):
      print(gameDataArray[x][y], end='  ')
    print("\n")  

def inputProcessing(gameDataArray):
  q=0
  up="W"
  down="S"
  left="A"
  right="D"
  reset="R"
  test = copy.deepcopy(gameDataArray)  # Create a deep copy of the gameDataArray
  x = input("Enter a direction (W, A, S, D or R to reset): ")
  display(gameDataArray)
  while(q!=4):
    q+=1
    if(x == up.lower() or x == up):
      for y in range(len(gameDataArray)-1):
        for z in range(len(gameDataArray[y])):
          if(gameDataArray[y+1][z]==gameDataArray[y][z] and q>=4):
            gameDataArray[y][z]=gameDataArray[y][z]+gameDataArray[y+1][z]
            gameDataArray[y+1][z]=0          
          if(gameDataArray[y+1][z]!=0 and gameDataArray[y][z]==0):
            gameDataArray[y][z]=gameDataArray[y+1][z] 
            gameDataArray[y+1][z]=0
    if(x == down.lower() or x == down):
      gameDataArray.reverse()
      for y in range(len(gameDataArray)-1):
        for z in range(len(gameDataArray[y])):
          if(gameDataArray[y+1][z]==gameDataArray[y][z] and q>=4):
            gameDataArray[y][z]=gameDataArray[y][z]+gameDataArray[y+1][z]
            gameDataArray[y+1][z]=0        
          if(gameDataArray[y+1][z]!=0 and gameDataArray[y][z]==0):
            gameDataArray[y][z]=gameDataArray[y+1][z]
            gameDataArray[y+1][z]=0
      gameDataArray.reverse()
    if(x == left.lower() or x == left):
      for y in range(len(gameDataArray)):
        for z in range(len(gameDataArray[y])-1):
          if(gameDataArray[y][z+1]==gameDataArray[y][z] and q>=4):
            gameDataArray[y][z]=gameDataArray[y][z]+gameDataArray[y][z+1]
            gameDataArray[y][z+1]=0
          if(gameDataArray[y][z+1]!=0 and gameDataArray[y][z]==0):
            gameDataArray[y][z]=gameDataArray[y][z+1]
            gameDataArray[y][z+1]=0
    if(x == right.lower() or x == right):
      for y in range(len(gameDataArray)):
        gameDataArray[y].reverse()
        for z in range(len(gameDataArray[y])-1):
          if(gameDataArray[y][z+1]==gameDataArray[y][z] and q>=4):
            gameDataArray[y][z]=gameDataArray[y][z]+gameDataArray[y][z+1]
            gameDataArray[y][z+1]=0
          if(gameDataArray[y][z+1]!=0 and gameDataArray[y][z]==0):
            gameDataArray[y][z]=gameDataArray[y][z+1]
            gameDataArray[y][z+1]=0
        gameDataArray[y].reverse()
  if(x == reset.lower() or x == reset):
    gameDataArray=resetBoard()
    return gameDataArray
  if(q==4 and test!=gameDataArray):
    randNumGen(gameDataArray, temp=1)
    return gameDataArray
  else:
    display(gameDataArray)
    return gameDataArray

randNumGen(gameDataArray, temp=0)
while (start!=1):
  if(checkWinLoss(gameDataArray)=="W"):
    display(gameDataArray)
    print("You won by getting to " + str(winNum) + "! Thanks for playing!")
    proceed=str(input("Enter \"S\" to stop. \"R\" to reset. Anything else to continue. "))
    if(proceed=="r" or proceed=="R"):
      gameDataArray=resetBoard()
    elif(proceed=="s" or proceed=="S"):
      clearConsole()
      start=1
    elif(proceed!="s" or proceed!="S" or proceed!="r" or proceed!="R"): 
      winNum=int(input("Enter your next goal (multiple of 2). "))
  elif(checkWinLoss(gameDataArray)=="noLoss"):
    display(gameDataArray)
    gameDataArray = inputProcessing(gameDataArray)
    
    





#KNOWN BUGS TO FIX

#Random number generator overlaps two numbers on a tile or only generates one tile at the beginning of each game-STATUS: Fixed
#Bug where the numbers will add to each repeatedly in input process (0 2 2 4) 2+2=4+4=8 (0 0 0 8) in one input where its supposed to be (0 2 2 4) 2+2=4 so that it looks like (0 0 4 4)-STATUS: Maybe fixed with Q>=3 in the if statements in inputProcessing. Extremely fixed as far as I can tell.
#Bug where the array will repeatedly generate random numbers despite there being no movement-STATUS: Fixed
#Game stops processing inputs when there are no 0's in the array-STATUS: Maybe fixed but still does it when the numbers are randomly generated... hasn't show up in a while so I must've done something.

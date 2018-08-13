import sys
from random import randint

#Hanging platform
p1 = "    _______"
p2 = "   |/      |"
p3 = "   |      " 
p4 = "   |      "
p5 = "   |       " 
p6 = "   |      " 
p7 = "   |      "
p8 = "___|___"

#Body parts
head = "(_)"
torso = "|"
lArm = "/"
rArm = "\\"
core = "|"
lLeg = "/"
rLeg = "\\"


#List of words
l = ["popcorn", "dog", "winery", "interstellar", "mouse", "jazz", "lineage",
    "hockey", "ghost", "meatball", "cannon", "gumball", "abstract", "integral"]

#Draws the platform and adds on the body after every wrong guess
#Takes in the number of wrong answers
def draw(num):

    global p1, p2, p3, p4, p5, p6, p7, p8

    if num == 1:
        p3 += head

    if num == 2:
        p4 += lArm
        
    if num == 3:
        p4 += torso

    if num == 4:
        p4 += rArm

    if num == 5:
        p5 += core

    if num == 6:
        p6 += lLeg

    if num == 7:
        p6 += " " + rLeg
        
    print(p1 + "\n" +
          p2 + "\n" +
          p3 + "\n" +
          p4 + "\n" +
          p5 + "\n" +
          p6 + "\n" +
          p7 + "\n" +
          p8)

def clearAll():
    
    global p1, p2, p3, p4, p5, p6, p7, p8
    p1 = "    _______"
    p2 = "   |/      |"
    p3 = "   |      " 
    p4 = "   |      "
    p5 = "   |       " 
    p6 = "   |      " 
    p7 = "   |      "
    p8 = "___|___"
    

#Outputs end game text
#Takes in boolean var
def end(wl, arr):
    if wl == True:
        word = ''.join(arr)
        print("The word is: " + word)
        print("Congrats")
        print("Game over")

    else:
        print("You are a murderer")

    usrIn = input("To play again, type 'Yes', otherwise, the game will end ")
    usrIn = str (usrIn)
    
    if 'Yes' in usrIn:
        clearAll()
        play()
    else:
        sys.exit
            
    

def play():

    global l

    r = randint(0, len(l)-1)
    arr = list(l[r])
    #blank array for adding already guessed words
    arr1 = [" "] * len(arr)
    guessed = []
    numTries = 0
    winLoss = False
        
    #Game loop
    while numTries < 7:
    
        letter = input("Guess a letter: ")
        letter = str(letter)

        if letter in guessed:
            print("Already guessed!")

        elif letter in arr:
        
            for x in range(0, len(arr)):

                if arr[x] ==  letter:
                    arr1[x] = letter
            
        else:
            numTries += 1
            draw(numTries)

        if arr1 == arr:
            winLoss = True
            end(winLoss, arr)
            sys.exit()

        #prints word with characters that are already guessed
        print(arr1)
        guessed.append(letter)

    end(winLoss, arr)
    


print("""
        ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
        ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
        ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
        ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
        ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                        """)

play()



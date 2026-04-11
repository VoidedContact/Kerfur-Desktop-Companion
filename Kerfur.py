import os
from os import system
import time
import random
import winsound

#####

Idle = """
                                                                                                    
                                       @@@@              @@@@                                       
                                     @@@@@@@            @@@@@@@                                     
                                                                                                    
                                                                                                    
                         @@@@@@@                                    @@@@@@@                         
                     @@@@@@@@@@@@@@@                            @@@@@@@@@@@@@@@                     
                   @@@@@@@@   @@@@@@@@                        @@@@@@@@   @@@@@@@@                   
                 @@@@@@           @@@@@                      @@@@@           @@@@@@                 
                @@@@@               @@@@@                   @@@@               @@@@@                
                @@@@                 @@@@                  @@@@                 @@@@                
               @@@@                  @@@@@                 @@@@                  @@@@               
               @@@@                   @@@@                @@@@                   @@@@               
               @@@@                   @@@@                 @@@@                  @@@@               
                @@@@                 @@@@                  @@@@                 @@@@                
                @@@@@               @@@@@       @@@@        @@@@               @@@@@                
                 @@@@@@           @@@@@@         @@          @@@@@           @@@@@@                 
       @@@@@@      @@@@@@@@   @@@@@@@@     @@   @@@@   @@     @@@@@@@@   @@@@@@@@      @@@@@@       
                     @@@@@@@@@@@@@@@         @@@@@@@@@@         @@@@@@@@@@@@@@@                     
       @@@@@@            @@@@@@@                                    @@@@@@@            @@@@@@       
                                                                                                    
"""
                                                                                                    
Blink = """
                                                                                                    
                                                                                                    
                                       @@@@              @@@@                                       
                                     @@@@@@@            @@@@@@@                                     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                @@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@@@@@@@@@                
               @@@@@@@@@@@@@@@@@@@@@@@@@@@                 @@@@@@@@@@@@@@@@@@@@@@@@@@               
                                                                                                    
                                                                                                    
                                                                                                    
                                                @@@@                                                
       @@@@@@                                    @@                                    @@@@@@       
                                           @@   @@@@   @@                                           
       @@@@@@                                @@@@@@@@@@                                @@@@@@       
                                                                                                    
"""
                                                                                                    
Meow = """
                                                                                                    
                                       @@@@              @@@@                                       
                                     @@@@@@@            @@@@@@@                                     
                                                                                                    
                                                                                                    
                         @@@@@@@                                    @@@@@@@                         
                     @@@@@@@@@@@@@@@                            @@@@@@@@@@@@@@@                     
                   @@@@@@@@   @@@@@@@@                        @@@@@@@@   @@@@@@@@                   
                 @@@@@@           @@@@@                      @@@@@           @@@@@@                 
                @@@@@               @@@@@                   @@@@               @@@@@                
                @@@@                 @@@@                  @@@@                 @@@@                
               @@@@                  @@@@@                 @@@@                  @@@@               
               @@@@                   @@@@                @@@@                   @@@@               
               @@@@                   @@@@                 @@@@                  @@@@               
                @@@@                 @@@@                  @@@@                 @@@@                
                @@@@@               @@@@@       @@@@        @@@@               @@@@@                
                 @@@@@@           @@@@@@         @@          @@@@@           @@@@@@                 
       @@@@@@      @@@@@@@@   @@@@@@@@     @@   @@@@   @@     @@@@@@@@   @@@@@@@@      @@@@@@       
                     @@@@@@@@@@@@@@@         @@@    @@@         @@@@@@@@@@@@@@@                     
       @@@@@@            @@@@@@@               @@@@@@               @@@@@@@            @@@@@@       
                                                                                                    
"""

#####

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def iFace():
    pColored(Idle)

def bFace():
    pColored(Blink)

def mFace():
    pColored(Meow)

class TextColor:
    RESET = "\033[0m"
    RED = "\x1b[38;5;196m"
    CYAN = "\033[36m"
    PINK = "\033[38;5;213m"

def change_color(color):
    global current_color
    if color == "red":
        current_color = TextColor.RED
    elif color == "cyan":
        current_color = TextColor.CYAN
    elif color == "pink":
        current_color = TextColor.PINK

def pColored(text):
    print(current_color + text + TextColor.RESET)

def pCentColored(text):
    width = 100
    cls()
    pColored(text.center(width))

def Boot_Screen():
    cls()
    print("KERFUR-OMEGA(C) 1990-1994 ASO")
    print("BIOS VERSION 1.0.0")
    print("Main Processor: Omega-AI")
    print("Memory Test: ", end="")
    for i in range(0, 1025, 128):
        print(f"\rMemory Test: {i}KB OK", end="")
        time.sleep(0.1)
    print("\n")
    print("Detecting Audio Hardware... ", end="")
    winsound.Beep(440, 200)
    print("DONE")
    time.sleep(0.5)
    Color_Selection()
        
def Color_Selection():
    while True:
        cls()
        print("KERFUR-OMEGA(C) 1990-1994 ASO")
        print("BIOS VERSION 1.0.0")
        print("Main Processor: Omega-AI")
        print("Memory Test: 1024KB OK")
        time.sleep(1)
        print("\n")
        print("="*30)
        print("Please choose your KERFER-OMEGA color!")
        print("1. Red")
        print("2. Blue")
        print("3. Pink")
        print("="*30)
        print("\n")
        colorChoice = input("1-3> ")
        
        try:
            choice = int(colorChoice)
            if choice == 1:
                change_color("red")
                return
            elif choice == 2:
                change_color("cyan")
                return
            elif choice == 3:
                change_color("pink")
                return
            else:
                print("Invalid number! Pick 1, 2, or 3.")
                time.sleep(1)
        except ValueError: ## I'm so fucking tired, i dont think anyones going to try this... but humans are relentless fuckheads. getting every single one to follow the rules is impossible. delete this comment before publishing.
            print(f"'{colorChoice}' is not a number. Please try again.")
            time.sleep(1)
            Color_Selection()


#####

current_color = TextColor.RESET
minT1 = 2
maxT1 = 10

#####

os.system('mode con: cols=100 lines=22')
Boot_Screen()
system("title Kerfur")
while True:
    cls()
    iFace()
    time.sleep(random.uniform(minT1, maxT1))
    cls()
    bFace()
    time.sleep(0.15)
    cls()
    iFace()
    MeowChance = random.randint(1, 100)
    if MeowChance >= 80:
        MeowChoice = random.randint(1, 30)
        if MeowChoice >= 1 and MeowChoice <= 10:
            cls()
            mFace()
            winsound.PlaySound("audio/meow-01.wav", winsound.SND_FILENAME | winsound.SND_NODEFAULT)
            time.sleep(0.5)
        elif MeowChoice > 10 and MeowChoice <= 20: 
            cls()
            mFace()
            winsound.PlaySound("audio/meow-02.wav", winsound.SND_FILENAME | winsound.SND_NODEFAULT)
            time.sleep(0.5)
        elif MeowChoice > 20 and MeowChoice <= 30:
            cls()
            mFace()
            winsound.PlaySound("audio/meow-03.wav", winsound.SND_FILENAME | winsound.SND_NODEFAULT)
            time.sleep(0.5)
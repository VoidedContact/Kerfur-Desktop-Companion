import pygame
from sys import exit
import random
import os
import win32gui
import win32con

width, height = 512, 512
FPS = 60

next_blink_time = 0
blinking = False
blink_duration = 100
blink_start = 0

meowing = False
meow_duration = 300
meow_start = 0
next_meow_time = 0

next_wAlert_time = 0
wAlert = False
wAlert_duration = 500
wAlert_start = 0

config_path = "config.txt"
last_config_time = 0
config = {}

topmost_dirty = False
Always_Top = False

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kerfur Omega")
icon = pygame.image.load("assets/faces/Idle.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 10)

meow1_SFX = pygame.mixer.Sound("assets/audio/meow-01.wav")
meow2_SFX = pygame.mixer.Sound("assets/audio/meow-02.wav")
meow3_SFX = pygame.mixer.Sound("assets/audio/meow-03.wav")
wAlert_SFX = pygame.mixer.Sound("assets/audio/kerfurEXE.wav")

hwnd = pygame.display.get_wm_info()['window']
print("HWND:", hwnd)

def load_config():
    try:
        with open("config.txt", "r") as f:
            lines = f.readlines()
        
        config = {}
        
        for line in lines:
            line = line.strip()
            
            if not line:
                continue
            if line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
                
    except Exception as e:
        print("Config error: ", e)
    return config

def apply_tint():
    global iFace, bFace, mFace
    iFace = tint_image(iFace_raw, color)
    bFace = tint_image(bFace_raw, color)
    mFace = tint_image(mFace_raw, color)
    

def reload_config():
    global config, color, Water_Alert, Silence, Debug, Name, Meow_Chance, Always_Top, topmost_dirty
    
    config = load_config()
    
    color = tuple(map(int, config.get("color", "255,255,255").split(",")))
    Water_Alert = config.get("Water_Alert", "False").lower() == "true"
    Silence = config.get("Silence", "False").lower() == "true"
    Debug = config.get("Debug", "False").lower() == "true"
    Always_Top = config.get("Always_Top", "False").lower() == "true"
    topmost_dirty = True
    apply_tint()
    Name = config.get("Name")
    pygame.display.set_caption(f"{Name} | Desktop Kerfur")
    Meow_Chance = float(config.get("Meow_Chance", "0.001"))
    
    Meow_Chance = max(0.0, min(Meow_Chance, 1.0))
    
    print("Config reloaded!")
    

config = load_config()
color = tuple(map(int, config.get("color", "255,255,255").split(",")))
Water_Alert = config.get("Water_Alert", "False").lower() == "true"
Silence = config.get("Silence", "False").lower() == "true"
Debug = config.get("Debug", "False").lower() == "true"


def tint_image(image, color):
    tinted = image.copy()
    tinted.fill(color, special_flags=pygame.BLEND_RGB_MULT)
    return tinted

iFace_raw = pygame.image.load("assets/faces/Idle.png").convert_alpha()
bFace_raw = pygame.image.load("assets/faces/Blink.png").convert_alpha()
mFace_raw = pygame.image.load("assets/faces/Meow.png").convert_alpha()

iFace = tint_image(iFace_raw, color)
bFace = tint_image(bFace_raw, color)
mFace = tint_image(mFace_raw, color)

def set_always_on_top(enabled):
    global hwnd
    if not hwnd:
        return
    if enabled:
        win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_TOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    else:
        win32gui.SetWindowPos(pygame.display.get_wm_info()['window'], win32con.HWND_NOTOPMOST, 0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        

def main():
    global blinking, next_blink_time, blink_start
    global meowing, meow_start, Silence, next_meow_time, Meow_Chance
    global next_wAlert_time, wAlert_start, wAlert
    global last_config_time, Debug, color, Always_Top, topmost_dirty
    
    run = True
    print("Started")
    
    
    current_time = pygame.time.get_ticks()
    while run:
        current_mtime = os.path.getmtime(config_path)
        current_time = pygame.time.get_ticks()
        
        if topmost_dirty:
            set_always_on_top(Always_Top)
            topmost_dirty = False
        
        if Debug:
            print("Current Tick: ", current_time, " | Next Blink: ", next_blink_time, " | Next Water Alert: ", next_wAlert_time)
            print("RGB Value: ", color, " | Silent Mode: ", Silence, " | Water Alert: ", Water_Alert)
            print("Next Meow: ", next_meow_time)
        
        if current_mtime != last_config_time:
            last_config_time = current_mtime
            reload_config()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if not meowing:
                        meowing = True
                        meow_start = current_time
                        MeowChoice = random.randint(1, 3)
                        if MeowChoice == 1:
                            meow1_SFX.play()
                        elif MeowChoice == 2: 
                            meow2_SFX.play()
                        else:
                            meow3_SFX.play()
        
        if next_blink_time == 0:
            next_blink_time = current_time + random.randint(2000, 4000)
        
        if next_wAlert_time == 0:
            next_wAlert_time = current_time + (1800000)
        
        if not blinking and current_time >= next_blink_time:
            blinking = True
            blink_start = current_time
        
        if blinking and current_time - blink_start >= blink_duration:
            blinking = False
            next_blink_time = current_time + random.randint(2000, 4000)
        
        if Water_Alert and not wAlert and current_time >= next_wAlert_time:
            wAlert = True
            wAlert_start = current_time
            wAlert_SFX.play()
            
        if wAlert and current_time - wAlert_start >= wAlert_duration:
            wAlert = False
            next_wAlert_time = current_time + (1800000)
            
        
        if not Silence and not blinking and not wAlert and not meowing:
            if current_time >= next_meow_time:
                if random.random() < Meow_Chance:
                    meowing = True
                    meow_start = current_time

                    MeowChoice = random.randint(1, 3)
                    if MeowChoice == 1:
                        meow1_SFX.play()
                    elif MeowChoice == 2: 
                        meow2_SFX.play()
                    else:
                        meow3_SFX.play()
                next_meow_time = current_time + random.randint(1000, 3000)
            
            
        if meowing and current_time - meow_start >= meow_duration:
            meowing = False
                    
        if blinking:
            screen.blit(bFace, (0, 0))
        elif meowing:
            screen.blit(mFace, (0, 0))
        elif wAlert:
            screen.blit(mFace, (0, 0))
        else:
            screen.blit(iFace, (0, 0))
        
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

pygame.time.delay(200)
set_always_on_top(Always_Top)

if __name__ == "__main__":
    main()
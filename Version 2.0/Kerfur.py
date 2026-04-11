import pygame
from sys import exit
import random

width, height = 512, 512
FPS = 60

next_blink_time = 0
blinking = False
blink_duration = 100
blink_start = 0

meowing = False
meow_duration = 300
meow_start = 0

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kerfur Omega")
icon = pygame.image.load("assets/faces/Idle.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 10)

meow1 = pygame.mixer.Sound("assets/audio/meow-01.wav")
meow2 = pygame.mixer.Sound("assets/audio/meow-02.wav")
meow3 = pygame.mixer.Sound("assets/audio/meow-03.wav")

def load_config():
    try:
        with open("config.txt", "r") as f:
            lines = f.readlines()
        
        config = {}
        
        for line in lines:
            if "=" in line:
                key, value = line.strip().split("=")
                config[key] = value
                
        if "color" in config:
            r, g, b = map(int, config["color"].split(","))
            return (r, g, b)
    except Exception as e:
        print("Config error: ", e)
    return (255, 255, 255)

def tint_image(image, color):
    tinted = image.copy()
    tinted.fill(color, special_flags=pygame.BLEND_RGB_MULT)
    return tinted

color = load_config()

iFace = pygame.image.load("assets/faces/Idle.png").convert_alpha()
bFace = pygame.image.load("assets/faces/Blink.png").convert_alpha()
mFace = pygame.image.load("assets/faces/Meow.png").convert_alpha()

iFace = tint_image(iFace, color)
bFace = tint_image(bFace, color)
mFace = tint_image(mFace, color)

def main():
    global blinking, next_blink_time, blink_start
    global meowing, meow_start
    run = True
    print("Started")
    
    while run:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if next_blink_time == 0:
            next_blink_time = current_time + random.randint(2000, 4000)
        
        if not blinking and current_time >= next_blink_time:
            blinking = True
            blink_start = current_time
        
        if blinking and current_time - blink_start >= blink_duration:
            blinking = False
            next_blink_time = current_time + random.randint(2000, 4000)
            
        if not blinking and not meowing and random.random() < 0.001:
            meowing = True
            meow_start = current_time
            
            MeowChoice = random.randint(1, 3)
            if MeowChoice == 1:
                meow1.play()
            elif MeowChoice == 2: 
                meow2.play()
            else:
                meow3.play()
            
            
        if meowing and current_time - meow_start >= meow_duration:
            meowing = False
        
        screen.fill("black")
        
        if blinking:
            screen.blit(bFace, (0, 0))
        elif meowing:
            screen.blit(mFace, (0, 0))
        else:
            screen.blit(iFace, (0, 0))
        
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
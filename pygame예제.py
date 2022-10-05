import pygame, sys

if __name__ =="__main__":
    pISPLAYYOURSELF =pygame.display.set_mode((640,480))
    pygame.init()

    color=[(0,0,0),(255,255,255)]
    running=True
    while running:
        for event in pygame.event.get():
            blue = (0, 0, 255)
            RED=(255,0,0)
            screen = pygame.display.set_mode((640,480))
            screen.fill(blue)
            pygame.draw.circle(screen,RED,(320,240),50)
            pygame.display.update()


            if event.type==pygame.QUIT:
                running=False

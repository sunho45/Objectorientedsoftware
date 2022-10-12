import pygame, sys

if __name__ =="__main__":
    gamepad =pygame.display.set_mode((640,480))
    pygame.init()

    color=[(0,0,0),(255,255,255)]
    running=True
    while running:
        for event in pygame.event.get():
            blue = (0, 0, 255)
            RED=(255,0,0)
            gamepad = pygame.display.set_mode((640,480))
            gamepad.fill(blue)
            player=pygame.image.load( "C:\\Users\\skyee\\PycharmProjects\\pythonProject1\\pngwing.com.png")
            gamepad.blit(player,(0,0))
            pygame.display.update()


            if event.type==pygame.QUIT:
                running=False

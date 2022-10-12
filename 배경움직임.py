import pygame, sys
clock=pygame.time.Clock()
if __name__ =="__main__":
    gamepad =pygame.display.set_mode((1024,512))
    pygame.init()
    RED = (255, 255, 255)
    xpos = 0
    ypos = 300
    xposbg=0
    xposbgl=1024
    running=True
    while running:
        for event in pygame.event.get():
            bg=pygame.image.load( "C:\\Users\\skyee\\Downloads\\background.png")
            bg=pygame.transform.scale(bg,(1024,512))
            player = pygame.image.load("C:\\Users\\skyee\\Downloads\\player.jpg")
            player = pygame.transform.scale(player, (100, 100))

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                 ypos-=2

                elif event.key==pygame.K_DOWN:
                 ypos+=2
                elif event.key==pygame.K_LEFT:
                    xpos-=2
                elif event.key==pygame.K_RIGHT:
                    xpos+=2
            
            gamepad.blit(player, (xpos, ypos))
            pygame.display.update()

            gamepad.blit(bg, (xposbg, 0))
            gamepad.blit(bg, (xposbgl, 0))
            xposbg -= 2
            xposbgl -= 2
            if xposbg == -1024:
                xposbg = 1024
            if xposbgl == -1024:
                xposbgl = 1024
            if event.type==pygame.QUIT:
                running=False

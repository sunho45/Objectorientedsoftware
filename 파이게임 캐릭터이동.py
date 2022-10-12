import pygame, sys
clock=pygame.time.Clock()
if __name__ =="__main__":
    gamepad =pygame.display.set_mode((1024,512))
    pygame.init()
    RED = (255, 255, 255)
    xpos = 0
    ypos = 300
    running=True
    while running:
        for event in pygame.event.get():


            
            bg=pygame.image.load( "C:\\Users\\skyee\\Downloads\\background.png")
            bg=pygame.transform.scale(bg,(1024,512))
            player = pygame.image.load("C:\\Users\\skyee\\Downloads\\player.jpg")
            player = pygame.transform.scale(player, (100, 100))
            clock.tick(60)
            gamepad.blit(bg, (0, 0))
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                 ypos-=20

                elif event.key==pygame.K_DOWN:
                 ypos+=20
                elif event.key==pygame.K_LEFT:
                    xpos-=20
                elif event.key==pygame.K_RIGHT:
                    xpos+=20

            gamepad.blit(player, (xpos, ypos))
            pygame.display.update()


            if event.type==pygame.QUIT:
                running=False

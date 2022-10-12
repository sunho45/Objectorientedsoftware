import pygame, sys

if __name__ =="__main__":
    gamepad =pygame.display.set_mode((1024,512))
    pygame.init()
    RED = (255, 255, 255)

    running=True
    while running:
        for event in pygame.event.get():




            bg=pygame.image.load( "C:\\Users\\skyee\\Downloads\\background.png")
            bg=pygame.transform.scale(bg,(1024,512))
            player = pygame.image.load("C:\\Users\\skyee\\Downloads\\player.jpg")
            player = pygame.transform.scale(player, (100, 100))
            gamepad.fill(RED)
            gamepad.blit(bg, (0, 0))
            gamepad.blit(player, (0, 300))
            pygame.display.update()


            if event.type==pygame.QUIT:
                running=False

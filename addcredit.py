import pygame
import time

from paddle import Paddle
from ball import Ball
from brick import Brick

# Define colors
WHITE = (255, 255, 255)
DARKSLATE_GRAY = (47, 79, 79)
CYAN = (0, 255, 255)
CRIMSON = (220, 20, 60)
CORAL = (255, 127, 80)
KHAKI = (255, 255, 0)

number=0
def set_initial_bricks(bricks, size_brick):
    # Display initial brick
    for i in range(7):
        brick = Brick(CRIMSON, size_brick)
        brick.set_pose(60 + i * 100, 60)
        sprite_paddle_ball.add(brick)
        bricks.add(brick)
    for i in range(7):
        brick = Brick(CORAL, size_brick)
        brick.set_pose(60 + i * 100, 100)
        sprite_paddle_ball.add(brick)
        bricks.add(brick)
    for i in range(7):
        brick = Brick(KHAKI, size_brick)
        brick.set_pose(60 + i * 100, 140)
        sprite_paddle_ball.add(brick)
        bricks.add(brick)

    return bricks


if __name__ == "__main__":
    pygame.init()  # Initiate pygame engine

    score, lives = 0, 3

    # Set size
    size_screen = (800, 600)
    size_paddle = (100, 10)
    size_ball = (10, 10)
    size_brick = (80, 30)

    # Set velocity range (ball)
    vel_range = (-5.0, 5.0)
    vel_move = 5.0

    # Create a new window
    screen = pygame.display.set_mode(size_screen)
    pygame.display.set_caption("Breakout Game")

    # Create the Paddle
    paddle = Paddle(CYAN, size_paddle, size_screen)
    paddle.set_pose(320, 560)

    # Create the ball sprite
    ball = Ball(WHITE, size_ball, vel_range)
    ball.set_pose(350, 180)

    # Sprite-list for paddle & ball
    sprite_paddle_ball = pygame.sprite.Group()
    sprite_paddle_ball.add(paddle)
    sprite_paddle_ball.add(ball)

    # Sprite-list for brick
    sprite_brick = pygame.sprite.Group()
    sprite_brick = set_initial_bricks(sprite_brick, size_brick)

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # RUN LOOP --------------------------------------------------------------------------------------------------------#
    # Run program until the user exit the game (e.g. clicks the close button)
    run_loop = True
    game_state = 0  # 1: game-over, 2: complete-game
    start_time = time.time()  # Start to record time
    time_hour, time_minute, time_second = 0, 0, 0
    while run_loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If user clicked close
                run_loop = False  # Flag that we exit the program

        if game_state == 0:
            # Moving the paddle with the arrow keys
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move_left(vel_move)
            if keys[pygame.K_RIGHT]:
                paddle.move_right(vel_move)
            sprite_paddle_ball.update()

            # Check whether the ball is bouncing against any of the 4 walls
            # Write code here!
            if ball.rect.x<=0:
                ball.update_reverse()
                ball.update_vel_bounce()
            elif ball.rect.x>=790:
                ball.update_reverse()
                ball.update_vel_bounce()
            if ball.rect.y <=0:
                ball.update_reverse()
                ball.update_vel_bounce()
            elif ball.rect.y>=590:
                ball.set_pose(350, 180)
                lives-=1




            # Detect collisions between the ball and the paddles
            if pygame.sprite.collide_mask(ball, paddle):
                ball.update_reverse()
                ball.update_vel_bounce()


            # Check collision
            brick_collision_list = pygame.sprite.spritecollide(ball, sprite_brick, False)
            for brick in brick_collision_list:
                ball.update_vel_bounce()
                brick.kill()
                score += 10
                if len(sprite_brick) == 18:

                    game_state =1



        # SCREEN ------------------------------------------------------------------------------------------------------#
        # Clear the screen
        screen.fill(DARKSLATE_GRAY)
        pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
        pygame.draw.line(screen, WHITE, [0, 42], [800, 42], 2)

        # Display lives & scores & time
        # Write code here!
        font = pygame.font.Font(None, 34)

        scores = font.render("score :"+ str(score), 1, WHITE)
        live= font.render("live :"+ str(lives), 1, WHITE)
        e = 0
        if game_state==1:
            fonts = pygame.font.Font(None, 50)
            SUCCESS = fonts.render("SUCCESS" , 1, (0, 0, 255))
            again = fonts.render("nextlevel? or pause  (Y/N)", 1, (0, 0, 255))


            screen.blit(SUCCESS, (200, 300))
            screen.blit(again, (200, 400))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_y]:
                brick.kill()
                sprite_brick = pygame.sprite.Group()
                sprite_brick = set_initial_bricks(sprite_brick, size_brick)
                print(0)
                game_state=0
                lives=3
                score=0
                minute=0
                hour=0
                elapsedsecond-=elapsedsecond
            if keys[pygame.K_n]:
                e+=1


        if lives <= 0:
            fonts = pygame.font.Font(None, 100)
            fontl = pygame.font.Font(None, 50)
            game_state = 2
            GAMEOVER = fonts.render("GAMEOVER", 1, (255,0,0))

            keys = pygame.key.get_pressed()
            screen.blit(GAMEOVER, (200, 300))
            again = fontl.render("again? or pause  (Y/N)", 1, (0, 0, 255))
            screen.blit(again, (200, 400))
            if keys[pygame.K_y]:

                print(0)
                game_state=0
                lives=3
                score=0
                minute=0
                hour=0
                elapsedsecond-=elapsedsecond
            if keys[pygame.K_n]:
                e+=1
        if e == 1:
            run_loop = False
        elapsedsecond = (pygame.time.get_ticks()) / 1000

        minute=int(int(int(elapsedsecond/60)))
        hour=int(elapsedsecond/3600)
        second=int(elapsedsecond)
        second-=60*minute
        minute-=60*hour
        elapsedminute = (pygame.time.get_ticks()) / 60000
        screen.blit(scores, (40, 10))
        screen.blit(live, (200, 10))

        time = font.render("TIME :"+str(int(hour))+":"+str(int(minute))+":"+str(second), 1, WHITE)
        screen.blit(time, (500, 10))

        font = pygame.font.Font(None, 74)


        # Draw sprites
        sprite_paddle_ball.draw(screen)

        # Update display
        pygame.display.flip()

        # Limit the clock-speed
        clock.tick(60)

    # Quit pygame
pygame.quit()

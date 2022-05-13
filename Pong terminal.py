#original idea: https://www.youtube.com/watch?v=Qf3-aDXG8q4
# added a main menu, a pause option, and a scoreboard

import pygame
import random

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    #movement
    ping.x += ball_speed_x
    ping.y += ball_speed_y

    #bounce and speed up function
    if ping.top <= 0:
        ball_speed_y = (ball_speed_y * -1) + 0.1
    if ping.bottom >= screen_height:
        ball_speed_y = (ball_speed_y * -1) - 0.1

    if ping.left <= 0:
        ball_restart()
        player_score = player_score + 1
    if ping.right >= screen_width:
        ball_restart()
        opponent_score = opponent_score + 1

    #collision detection seperate this to make the game harder lol
    if ping.colliderect(player) or ping.colliderect(opponent):
        ball_speed_x *= -1
def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= 960:
        player.bottom = 960
def opponent_animation():

    #stops movement outside of bounds
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= 960:
        opponent.bottom = 960
    #allows movement following the ball at a set speed
    if opponent.centery < ping.y:
        opponent.centery += opponent_speed
    if opponent.centery > ping.y:
        opponent.centery -= opponent_speed

def ball_restart():
    global ball_speed_x, ball_speed_y
    #when someone scores this allows the ball to reset in the middle in a random direction
    ping.center = (screen_width/2, screen_height/2)
    ball_speed_x = 4.0
    ball_speed_y = 4.0
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))



pygame.init()
clock = pygame.time.Clock()

#window set up
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("Pong")

# Rectangles
ping = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30 ,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

#speeds
ball_speed_x = 4.0
ball_speed_y = 4.0
player_speed = 0
opponent_speed = 4.0

# ScoreBoard variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

#start menu
hold = False
#checks to see if paused
Paused = False


#main menu code
while hold == False:
#this code when clicking starts the game
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()

        if ev.type == pygame.MOUSEBUTTONDOWN:
            hold = True


    # Main Menu visuals
    screen.fill(pygame.Color("springgreen4"))
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), opponent)
    pygame.draw.ellipse(screen, (255, 255, 255), ping)
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height))

    #Start Text
    game_text = game_font.render(f"Click To Begin, ESC To Pause", False, (255, 255, 255))
    screen.blit(game_text, (10,10))

    #update window
    pygame.display.flip()
    clock.tick(60)

#actual game code loop
while hold:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
            if event.key == pygame.K_ESCAPE:
                if Paused == False:
                    Paused = True
                else:
                    Paused = False
                    ball_speed_x = 4.0
                    ball_speed_y = 4.0


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    #makes the ball move
    ball_animation()
    player.y += player_speed
    #stops you from moving outside
    player_animation()
    #Opponent movement
    opponent_animation()




    # visuals
    screen.fill(pygame.Color("springgreen4"))
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), opponent)
    pygame.draw.ellipse(screen, (255, 255, 255), ping)
    pygame.draw.aaline(screen, (255, 255, 255), (screen_width / 2, 0), (screen_width / 2, screen_height))

    #more scoreboard
    game_text = game_font.render(f"{opponent_score}                                                                                                                                     {player_score}", False, (255, 255, 255))
    screen.blit(game_text, (10,10))

    #update window
    pygame.display.flip()
    clock.tick(60)

    if Paused == True:
        #pauses ball speed
        ball_speed_x = 0
        ball_speed_y = 0
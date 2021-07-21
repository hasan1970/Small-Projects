import pygame
import time
import random

pygame.init()

blue=(0,0,255)
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
temp=(10,200,200)

dis_width=400
dis_height=300
display=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake Game")
 

clock=pygame.time.Clock()

snake_speed=30
snake_block=10


font_style=pygame.font.SysFont(None,25)

def message(msg,colour):
    mesg=font_style.render(msg,True,colour)
    display.blit(mesg, [dis_width/6, dis_height/3])

def our_snake(snake_block, snake_list):
    for a in snake_list:
        pygame.draw.rect(display, black, [a[0],a[1], snake_block, snake_block])




#message("You lost", red)
#pygame.display.update()
#time.sleep(2)


def gameloop():
    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_c = 0
    y1_c = 0

    snake_list=[]
    length_snake = 1

    foodx=round(random.randrange(0, dis_width - snake_block)/10.0)*10.0
    foody=round(random.randrange(0, dis_height - snake_block)/10.0)*10.0

    while not game_over:

        while game_close == True:
            display.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                   x1_c=-snake_block
                   y1_c=0
                elif event.key == pygame.K_RIGHT:
                   x1_c=snake_block
                   y1_c=0
                elif event.key == pygame.K_UP:
                   x1_c=0
                   y1_c=-snake_block
                elif event.key == pygame.K_DOWN:
                   x1_c=0
                   y1_c=snake_block

        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
              game_close=True

        x1+=x1_c
        y1+=y1_c
        display.fill(temp)
        
        pygame.draw.rect(display,blue,[foodx,foody,snake_block,snake_block])    
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list)>length_snake:
            del snake_list[0]

        for a in snake_list[:-1]:
            if a == snake_head:
                game_close=True
        our_snake(snake_block, snake_list)
        pygame.display.update()
        

        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0, dis_width - snake_block)/10.0)*10.0
            foody=round(random.randrange(0, dis_height - snake_block)/10.0)*10.0
            length_snake+=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

        


gameloop()

   
        
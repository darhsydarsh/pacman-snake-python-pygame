
#initial variables for both games
import pygame
import random
import time

#initial main game running variables
running = True
reincarnation = True
pacman_played = False
score = 0

#initialising pygame
pygame.init()

screen_width = 800
screen_height = 800


# Set the window size
screen = pygame.display.set_mode((screen_width, screen_height))

#snake menu format
# Set the font and text for the menu options
font = pygame.font.SysFont('Comic Sans MS', 30)
font_2 = pygame.font.SysFont('Comic Sans MS', 60)


#instructions words
font_instructions = pygame.font.SysFont('Comic Sans MS', 20)
instructions_text_1 = font_instructions.render('Use arrow keys or small case WASD to move the snake around the screen.', True, (0,0,0))
instructions_text_2 = font_instructions.render('Eat the food to grow the snake and earn points.', True, (0,0,0))
instructions_text_3 = font_instructions.render('Avoid hitting the walls or the snake itself.', True, (0,0,0))
instructions_text_4 = font_instructions.render('Press P button to pause the game.', True, (0,0,0))
snak_instructions_text = font_instructions.render('return to menu.', True, (0,0,0))


#rendering instructions words
instructions_text_rect_1 = instructions_text_1.get_rect(center=(400, 100))
instructions_text_rect_2 = instructions_text_2.get_rect(center=(400, 150))
instructions_text_rect_3 = instructions_text_3.get_rect(center=(400, 200))
instructions_text_rect_4 = instructions_text_4.get_rect(center=(400, 250))
snake_return_menu_rect = instructions_text_4.get_rect(center=(400, 500))



#initilises game words
snake_play_text = font.render('Play Game', True, (0,0,0))
snake_quit_text = font.render('Quit Game', True, (0, 0,0))
snake_instructions_text = font.render('instructions screen', True, (0,0,0))
snake_title_text = font_2.render('Snake Game', True, (0,0,0))

# Set the position of the menu options
snake_play_rect = snake_play_text.get_rect(center=(400, 200))
snake_quit_rect = snake_quit_text.get_rect(center=(400, 500))
snake_instructions_rect = snake_instructions_text.get_rect(center=(400, 350))
snake_title_rect = snake_title_text.get_rect(center=(400, 100))



# initial variables and menu options for pacman


font = pygame.font.SysFont('Comic Sans MS', 25)

font_instructions = pygame.font.SysFont('Comic Sans MS', 20)
pac_instructions_text_1 = font_instructions.render('Use the arrow keys or wasd to move Pacman around the maze.', True, (255, 255, 255))
pac_instructions_text_2 = font_instructions.render('Eat all the pellets to be able to come back to snake.', True, (255, 255, 255))
pac_instructions_text_3 = font_instructions.render('Avoid the ghosts. If they touch you, you die forever', True, (255, 255, 255))
pac_instructions_text_4 = font_instructions.render('Press P button to pause the game.', True, (255, 255, 255))
pac_instructions_text_5 = font_instructions.render('Eat a power pellet to temporarily become faster', True, (255, 255, 255))
pac_instructions_text = font_instructions.render('return to menu.', True, (255, 255, 255))


#rendering instructions words
pac_instructions_text_rect_1 = pac_instructions_text_1.get_rect(center=(400, 100))
pac_instructions_text_rect_2 = pac_instructions_text_2.get_rect(center=(400, 150))
pac_instructions_text_rect_3 = pac_instructions_text_3.get_rect(center=(400, 200))
pac_instructions_text_rect_4 = pac_instructions_text_4.get_rect(center=(400, 250))
pac_instructions_text_rect_5 = pac_instructions_text_5.get_rect(center=(400, 300))
pac_return_menu_rect = pac_instructions_text.get_rect(center=(400, 500))



# Set the window title
pacman_title = font.render('Pacman', False, (255, 255, 255))
pacman_play_game = font.render('Play Game', False, (255, 255, 255))
pacman_quit_game = font.render('Quit Game', False, (255, 255, 255))
pacman_instructions_game = font.render('Instructions', False, (255, 255, 255))

#set position of the menu options
pacman_title_rect = pacman_title.get_rect(center=(400,100))
pacman_play_game_rect = pacman_play_game.get_rect(center=(400,300))
pacman_quit_game_rect = pacman_quit_game.get_rect(center=(400,500))
pacman_instructions_game_rect = pacman_instructions_game.get_rect(center=(400,400))

class point:
    def __init__(self, x, y, eaten):
        self.x = x
        self.y = y
        self.eaten = eaten
        if eaten == False:
            pygame.draw.circle(screen, (100, 255, 0),(x, y),5)      
    

class boundary:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(x, y, width, height))





while running:
    snake_menu_running = True
    if reincarnation == True:
        while snake_menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Check if the mouse was clicked on the play or quit options
                    if snake_play_rect.collidepoint(event.pos): 
                        # Start the game
                        snake_running = True
                        #these are the initial variables for when we start the game
                        snake_speed = 30
                        snake_position = [100, 50]
                        snake_body = [[100, 50], [90, 50], [80, 50]]
                        if pacman_played == True:
                            for i in range(score):
                                positioning = 70 - (i * 10)
                                snake_body.append([positioning, 50])

                        direction = 'RIGHT'
                        
                        screen.fill((255, 255, 255))
                        returned_pause_value = True
                        fps = pygame.time.Clock()
                        pygame.display.update()

#                
                        def initial_score(score):
                            score_font = pygame.font.SysFont('Comic Sans MS', 30)
                            score_surface = score_font.render('Score : ' + str(score), True, (0,0,0))
                            score_rect = score_surface.get_rect()
                            screen.blit(score_surface, score_rect)
                            
                        def game_over():
                            game_over_font = pygame.font.SysFont('Comic Sans MS', 24)
                            if pacman_played == False:
                                game_over_surface = game_over_font.render('first life for snake...over with a score of ' + str(score), True, (125,0,0))
                            else:
                                game_over_surface = game_over_font.render('last life for snake... over with a score of ' + str(score), True, (125,0,0))
                            game_over_rect = game_over_surface.get_rect(center=(400, 200))
                            screen.blit(game_over_surface, game_over_rect)
                            pygame.display.flip()
                            time.sleep(5)

                        
                        #this is for the pause of the game
                        def pause():
                            pause_font = pygame.font.SysFont('Comic Sans MS', 24)
                            pause_surface = pause_font.render('Game paused', True, (0,0,0))
                            pause_rect = pause_surface.get_rect(center=(400, 100))
                            screen.blit(pause_surface, pause_rect)
                            screen.blit(snake_quit_text, snake_quit_rect)
                            screen.blit(snake_play_text, snake_play_rect)
                            pygame.display.flip()
                            paused = True
                            while paused:
                                
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return False
                                    elif event.type == pygame.MOUSEBUTTONDOWN: 
                                        if snake_play_rect.collidepoint(event.pos):
                                            return True
                                            
                                        elif snake_quit_rect.collidepoint(event.pos):
                                            # Quit the game
                                            return False     

#        
                        def food():
                            fruit_position = [random.randrange(1, (screen_width//10)) * 10,
                                        random.randrange(1, (screen_height//10)) * 10]
                            
                            return fruit_position


                        #main loop
                        fruit_position = food()
                        while snake_running == True:
                            
                            if returned_pause_value == False:
                                running = False
                                snake_running = False
                                snake_menu_running = False
#
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    snake_running = False
                                    running = False
                                    snake_menu_running = False

                                if event.type == pygame.KEYDOWN:
                                    
                                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                                        direction = 'UP'
                                        
                                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                        direction = 'DOWN'
                                        
                                    if event.key == pygame.K_a  or event.key == pygame.K_LEFT:
                                        direction = 'LEFT'
                                        
                                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                        direction = 'RIGHT'
                                        
                                    if event.key == pygame.K_p:
                                        
                                        returned_pause_value = pause()
                                        if returned_pause_value == False:
                                            snake_running = False
                                            running = False
                                            snake_menu_running = False
                                        else:
                                            screen.fill((255, 255, 255))
                                            pygame.display.update()
#
                                
                                # Moving the snake
                            if direction == 'UP':
                                snake_position[1] -= 10
                            if direction == 'DOWN':
                                snake_position[1] += 10
                            if direction == 'LEFT':
                                snake_position[0] -= 10
                            if direction == 'RIGHT':
                                snake_position[0] += 10

                                # Snake body growing mechanism
                            snake_body.insert(0, list(snake_position))
                            
                            if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
                                score += 1
                                fruit_position = food()
                            else:
                                snake_body.pop(-1)            
#
                            #snake death
                            if snake_position[0] < 0 or snake_position[0] > screen_width-10:
                                game_over()
                                snake_running = False
                                snake_menu_running = False
                                
                            if snake_position[1] < 0 or snake_position[1] > screen_height-10:
                                game_over()
                                snake_running = False
                                snake_menu_running = False
                                
                            
                            if snake_body[0] in snake_body[1:]:
                                game_over()
                                snake_running = False
                                snake_menu_running = False
                                


                            #snake rendering
                            screen.fill((255, 255, 255))
                            for i in snake_body:
                                pygame.draw.rect(screen, (0, 0, 0), 
                                            pygame.Rect(i[0], i[1], 10, 10))

                            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

#
                            initial_score(score)
                            pygame.display.update()
                            fps.tick(snake_speed)
                                    

                    elif snake_instructions_rect.collidepoint(event.pos):

                        instruction_screen_runnning = True
                        screen.fill((255, 255, 255))
                        screen.blit(instructions_text_1, instructions_text_rect_1)
                        screen.blit(instructions_text_2, instructions_text_rect_2)
                        screen.blit(instructions_text_3, instructions_text_rect_3)
                        screen.blit(instructions_text_4, instructions_text_rect_4)
                        screen.blit(snak_instructions_text, snake_return_menu_rect)
                        pygame.display.update()
                        while instruction_screen_runnning:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    instruction_screen_runnning = False
                                    running = False
                                elif event.type == pygame.MOUSEBUTTONDOWN: 
                                    if snake_return_menu_rect.collidepoint(event.pos):
                                        instruction_screen_runnning = False
            
                        
                    elif snake_quit_rect.collidepoint(event.pos):
                        # Quit the game
                        snake_running = False
                        snake_menu_running = False

 # Fill the background color
            screen.fill((0, 128, 0))

            # Draw the menu options
            screen.blit(snake_play_text, snake_play_rect)
            screen.blit(snake_instructions_text, snake_instructions_rect)
            screen.blit(snake_quit_text, snake_quit_rect)
            screen.blit(snake_title_text, snake_title_rect)

            # Update the display
            pygame.display.update()        
            # play game of snake

# playgame of pacman





    # rincationtion = True or False
    if pacman_played == True:
        running = False






    pacman_menu_running = True
    if running == True and pacman_played == False:
        while pacman_menu_running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pacman_menu_running = False
                    running = False
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                
#main game
                    if pacman_play_game_rect.collidepoint(mouse_pos):


                        pacman_running = True
                        screen.fill((0,0,0))
                        pygame.display.update()
                        direction = 'RIGHT'

                        point2 = point(540, 550, False)
                        point3 = point(260, 260, False)
                        point4 = point(315, 540, False)
                        point5 = point(485, 260, False)

                        point6 = point(770, 770, False)
                        point7 = point(770, 30, False)
                        point8 = point(30, 770, False)
                        point9 = point(30, 30, False)

                        point10 = point(210, 150, False)
                        point11 = point(590, 650, False)
                        point12 = point(650,210, False)
                        point13 = point(150,590 , False)
#
                        point14 = point(400,70 , False)
                        point15 = point(400,730 , False)
                        point16 = point(730,400 , False)
                        point17 = point(70,400 , False) 


                        point_eaten_list = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
                                        
                        pacman_position = [400,400]
                        red_ghost_position = [30,30]
                        red_ghosot_direction = 'RIGHT'

                        loop_number = 0

                        fps = pygame.time.Clock()


#
                        def pause():
                            pause_font = pygame.font.SysFont('Comic Sans MS', 24)
                            pause_surface = pause_font.render('Game paused', True, (0,0,0))
                            pause_rect = pause_surface.get_rect(center=(400, 100))
                            screen.blit(pause_surface, pause_rect)
                            screen.blit(pacman_quit_game, pacman_quit_game_rect)
                            screen.blit(pacman_play_game, pacman_play_game_rect)
                            pygame.display.flip()
                            paused = True
                            while paused:
                                
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        return False
                                    elif event.type == pygame.MOUSEBUTTONDOWN: 
                                        if pacman_play_game_rect.collidepoint(event.pos):
                                            return True
                                            
                                        elif pacman_quit_game_rect.collidepoint(event.pos):
                                            # Quit the game
                                            return False  


                        


                        
                        while pacman_running:
                            screen.fill((0,0,0))
#   


                            old_pacman_position = pacman_position
                            pointlist = [point2, point3, point4, point5,
                                        point6, point7, point8, point9,
                                        point10, point11, point12, point13,
                                        point14, point15, point16, point17
                                        ]

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pacman_running = False
                                    running = False
                                    
                                if event.type == pygame.KEYDOWN:
                                        
                                    
                                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                                        direction = 'UP'
                                        
                                        
                                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                                        direction = 'DOWN'
                                        
                                    if event.key == pygame.K_a  or event.key == pygame.K_LEFT:
                                        direction = 'LEFT'
                                        
                                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                                        direction = 'RIGHT'
                                        
                                    if event.key == pygame.K_p:
                                        
                                        returned_pause_value = pause()
                                        if returned_pause_value == False:
                                            pacman_running = False
                                            running = False
                                        else:
                                            screen.fill((0,0,0))
                                            pygame.display.update()
#


                                
                            if direction == 'UP':
                                pacman_position[1] -= 10
                            if direction == 'DOWN':
                                pacman_position[1] += 10
                            if direction == 'LEFT':
                                pacman_position[0] -= 10
                            if direction == 'RIGHT':
                                pacman_position[0] += 10
                            
                            #points
                            point2 = point(540, 550, point_eaten_list[0])
                            point3 = point(260, 260, point_eaten_list[1])
                            point4 = point(315, 540, point_eaten_list[2])
                            point5 = point(485, 260, point_eaten_list[3])

                            point6 = point(770, 770, point_eaten_list[4])
                            point7 = point(770, 30, point_eaten_list[5])
                            point8 = point(30, 770, point_eaten_list[6])
                            point9 = point(30, 30, point_eaten_list[7])

                            point10 = point(210, 150, point_eaten_list[8])
                            point11 = point(590, 650, point_eaten_list[9])
                            point12 = point(650,210, point_eaten_list[10])
                            point13 = point(150,590 , point_eaten_list[11])

                            point14 = point(400,70 , point_eaten_list[12])
                            point15 = point(400,730 , point_eaten_list[13])
                            point16 = point(730,400 , point_eaten_list[14])
                            point17 = point(70,400 , point_eaten_list[15])

                    

                            for i in pointlist:
                                if pacman_position[0] >= i.x-19 and pacman_position[0] <= i.x+19 and \
                                    pacman_position[1] >= i.y-19 and pacman_position[1] <= i.y+19:
                                    i.eaten = True
                                    point_eaten_list[pointlist.index(i)] = True
                                                      

                            if False not in point_eaten_list:
                                pacman_running = False
                                pacman_menu_running = False
                                pacman_played = True
                                    
                            
#outer boundaries
                            boundary1 = boundary(0, 0, 800, 10)
                            boundary2 = boundary(0, 0, 10, 800)
                            boundary3 = boundary(0, 790, 800, 10)
                            boundary4 = boundary(790, 0, 10, 800)

                            #inner boundaries coner squares
                            boundary5 = boundary(670, 670, 80, 80)
                            boundary6 = boundary(50, 50, 80, 80)
                            boundary7 = boundary(50, 670, 80, 80)
                            boundary8 = boundary(670, 50, 80, 80)

                            #inner boundaries horizontal lines

                            boundary9 = boundary(200, 200, 180 , 40)
                            boundary10 = boundary (420, 200, 180 , 40)
                            boundary11 = boundary(200, 560, 180 , 40)
                            boundary12 = boundary (420, 560, 180 , 40)

                            #inner boundaries vertical lines

                            boundary13 = boundary(200, 200, 40 , 240)
                            boundary14 = boundary (200, 480, 40 , 120)
                            boundary15 = boundary(560, 200, 40 , 120)
                            boundary16 = boundary (560, 360, 40 , 240)

                            #internal cubes
                            boundary17 = boundary(240,280,280,40)
                            boundary18 = boundary(280,480,280,40)

                            #internal internal cubes
                            boundary19 = boundary(420,240,40,200)
                            boundary20 = boundary(340,360,40,200)

                            #exterior lines
                            boundary21 = boundary(90,170,40,460)
                            boundary22 = boundary(670,170,40,460)
                            boundary23 = boundary(170,90,460,40)
                            boundary24 = boundary(170,670,460,40)                    


#

                            boundarylist = [boundary1, boundary2, boundary3, boundary4,
                                            boundary5, boundary6, boundary7, boundary8,
                                            boundary9, boundary10, boundary11, boundary12,
                                            boundary13, boundary14, boundary15, boundary16,
                                            boundary17, boundary18, boundary20, boundary19,
                                            boundary21, boundary22, boundary23, boundary24,
                                            ]


                            #pacman boundary detection

                            for i in boundarylist:
                                if pacman_position[0] >= i.x-19 and pacman_position[0] <= i.x+i.width+19 and \
                                    pacman_position[1] >= i.y-19 and pacman_position[1] <= i.y+i.height+19:
                                    if direction == 'UP':
                                        pacman_position[1] += 10
                                    if direction == 'DOWN':
                                        pacman_position[1] -= 10
                                    if direction == 'LEFT':
                                        pacman_position[0] += 10
                                    if direction == 'RIGHT':
                                        pacman_position[0] -= 10   



                            for i in boundarylist:
                                if red_ghost_position[0]+20 >= i.x and red_ghost_position[0] <= i.x+i.width and \
                                    red_ghost_position[1]+20 >= i.y and red_ghost_position[1] <= i.y+i.height:
                                    
                                    if red_ghosot_direction == 'UP':
                                        red_ghost_position[1] += 10

                                    if red_ghosot_direction == 'DOWN':
                                        red_ghost_position[1] -= 10

                                    if red_ghosot_direction == 'LEFT':
                                        red_ghost_position[0] += 1

                                    if red_ghosot_direction == 'RIGHT':
                                        red_ghost_position[0] -= 19                        


                            loop_number += 1

#           
                            if loop_number %15 == 0:
                                number = random.randint(1,4)
                                if number == 1:
                                    red_ghosot_direction = 'DOWN'
                                if number == 2:
                                    red_ghosot_direction = 'UP'
                                if number == 3:
                                    red_ghosot_direction = 'RIGHT'
                                if number == 4:
                                    red_ghosot_direction == 'LEFT'

                            
                            



                            if red_ghosot_direction == 'UP':
                                red_ghost_position[1] -= 10
                            if red_ghosot_direction == 'DOWN':
                                red_ghost_position[1] += 10
                            if red_ghosot_direction == 'LEFT':
                                red_ghost_position[0] -= 10
                            if red_ghosot_direction == 'RIGHT':
                                red_ghost_position[0] += 10



#pacman death        
                            if red_ghost_position[0] >= pacman_position[0]-19 and red_ghost_position[0] <= pacman_position[0]+19 and \
                                red_ghost_position[1] >= pacman_position[1]-19 and red_ghost_position[1] <= pacman_position[1]+19:
                                pacman_running = False
                                reincarnation = False
                                pacman_menu_running = False
                                running = False


                            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(red_ghost_position[0], red_ghost_position[1],20, 20))

                            




                            #drawing pacman in
                            pygame.draw.circle(screen, (255, 255, 0),(pacman_position[0], pacman_position[1]),20)
                            pacman_speed = 30
                            fps.tick(pacman_speed)
                            old_pacman_position = pacman_position
                            pygame.display.update()


#game quit
                    if pacman_quit_game_rect.collidepoint(mouse_pos):
                        running = False

                    if pacman_instructions_game_rect.collidepoint(mouse_pos):
                        instruction_screen_runnning = True
                        screen.fill((0,0,0))
                        screen.blit(pac_instructions_text_1, pac_instructions_text_rect_1)
                        screen.blit(pac_instructions_text_2, pac_instructions_text_rect_2)
                        screen.blit(pac_instructions_text_3, pac_instructions_text_rect_3)
                        screen.blit(pac_instructions_text_4, pac_instructions_text_rect_4)
                        screen.blit(pac_instructions_text, pac_return_menu_rect)
                        pygame.display.update()
                        while instruction_screen_runnning:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    instruction_screen_runnning = False
                                    running = False
                                elif event.type == pygame.MOUSEBUTTONDOWN: 
                                    if pac_return_menu_rect.collidepoint(event.pos):
                                        instruction_screen_runnning = False
                    

                    

            screen.fill((0,0,0))
            screen.blit(pacman_title, pacman_title_rect)
            screen.blit(pacman_play_game, pacman_play_game_rect)
            screen.blit(pacman_quit_game, pacman_quit_game_rect)
            screen.blit(pacman_instructions_game, pacman_instructions_game_rect)
            pygame.display.update()


#score
f = open("highscore.txt", "r")
highscore = f.read()
f.close()

if str(score) > highscore:
    f = open("highscore.txt", "w+")
    f.write(str(score))
    f.close()
    display_score = font.render("Congratulations, you have reached a new highscore of " + str(score), True, (255, 255, 255))
else:
    display_score = font.render("Your score is Score: " + str(score), True, (255, 255, 255))

display_score_rect = display_score.get_rect()
display_score_rect.center = (400, 50)

display_highscore = font.render("The highscore : " + str(highscore), True, (255, 255, 255))
display_highscore_rect = display_highscore.get_rect()
display_highscore_rect.center = (400, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    screen.fill((0, 0, 0))
    screen.blit(display_score, display_score_rect)
    screen.blit(display_highscore, display_highscore_rect)
    pygame.display.flip()

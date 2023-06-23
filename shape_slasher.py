import pygame, sys
import os
import random


player_lives = 3                                                
score = 0                                                       
shapes = ['square', 'octagon', 'hexagon', 'triangle', 'circle', 'bomb'] 
shapes_dict = {'square': 4, 'octagon':8, 'hexagon': 6, 'triangle': 3, 'circle': 1, 'bomb': 0}
elapsed_time = 0

# initialize pygame and create window
WIDTH = 1200
HEIGHT = 900
FPS = 5                                                 
pygame.init()
pygame.display.set_caption('Shape-Slasher Game')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))   
clock = pygame.time.Clock()

# Define colors
BLACK = (0,0,0)
RED = (255, 89, 94)
GREEN = (38, 166, 91)
BLUE = (25, 130, 196)
YELLOW = (255, 202, 58)
PURPLE = (106, 76, 147)

background = pygame.image.load('images/back.jpg')                                  
font = pygame.font.Font(os.path.join(os.getcwd(), 'comic.ttf'), 42)
target = random.randint(20, 50)

remaining = target
score_text = font.render(f'Score: {score}', True, BLUE)    
target_text = font.render(f'Target: {target}', True, GREEN)    
remaining_text = font.render(f'Remaining: {remaining}', True, YELLOW) 

lives_icon = pygame.image.load('images/white_lives.png')                    

# Generalized structure of the shape Dictionary
def generate_random_shapes(shape):
    shape_path = "images/" + shape + ".png"
    data[shape] = {
        'img': pygame.image.load(shape_path),
        'x' : random.randint(100,500),          
        'y' : 800,
        'speed_x': random.randint(-10,10),      
        'speed_y': random.randint(-80, -60),    
        'throw': False,                         
        't': 0,                                 
        'hit': False,
    }

    if random.random() >= 0.75:     
        data[shape]['throw'] = True
    else:
        data[shape]['throw'] = False

# Dictionary to hold the data the random shape generation
data = {}
for shape in shapes:
    generate_random_shapes(shape)

def hide_cross_lives(x, y):
    gameDisplay.blit(pygame.image.load("images/red_lives.png"), (x, y))

# Generic method to draw fonts on the screen
font_name = pygame.font.match_font('comic.ttf')
def draw_text(display, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    padding = 20
    text_rect.inflate_ip(padding * 2, padding * 2)

    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)

# draw players lives
def draw_lives(display, x, y, lives, image) :
    padding_var = 1
    for i in range(lives) :
        img = pygame.image.load(image)
        img_rect = img.get_rect()       
        padding = 20
        img_rect.inflate_ip(padding * 10, padding * 10)
        img_rect.x = int(x + 35 * i) + 200 + (padding_var * 30)   
        img_rect.y = y + 20               
        display.blit(img, img_rect)
        padding_var += 1

# show game over display & front display                                                                                                
def show_gameover_screen(elapsed_time, status=None):
    gameDisplay.blit(background, (0,0))
    # Load the image
    shapes_image_path = "images/shapes.png"
    win_image_path = "images/win.png"
    lose_image_path = "images/lose.png"
    shapes_group = pygame.image.load(shapes_image_path)
    win_image = pygame.image.load(win_image_path)
    lose_image = pygame.image.load(lose_image_path)

    # Display the image on the screen
    gameDisplay.blit(shapes_group, ((WIDTH / 2) - 50, (HEIGHT / 3)-100))
    draw_text(gameDisplay, "SHAPE SLASHER", 90, WIDTH / 2, HEIGHT / 3, BLUE)


    if not game_over :
    
        if status == 'won':
            gameDisplay.blit(win_image, ((WIDTH / 2) - 50, (HEIGHT / 3)+70))
            draw_text(gameDisplay,"You won!", 50, WIDTH / 2, (HEIGHT /2) + 20 , GREEN)
            draw_text(gameDisplay,"Score - " + str(score), 50, WIDTH / 2, HEIGHT/2 + 70, GREEN)
            draw_text(gameDisplay,"Target - " + str(target), 50, WIDTH / 2, HEIGHT/2 + 120, GREEN)
        else:
            gameDisplay.blit(lose_image, ((WIDTH / 2) - 50, (HEIGHT / 3)+70))
            draw_text(gameDisplay,"You lost!" , 50, WIDTH / 2, (HEIGHT /2)+20, RED)
            draw_text(gameDisplay,"Score - " + str(score), 50, WIDTH / 2, HEIGHT/2 + 70, RED)
            draw_text(gameDisplay,"Target - " + str(target), 50, WIDTH / 2, HEIGHT/2 + 120, RED)
        
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        draw_text(gameDisplay, f"Time: {minutes:02d}:{seconds:02d}", 50, WIDTH / 2, HEIGHT/2 + 180, BLUE)

    if first_round:
        draw_text(gameDisplay, "Slash shapes to reach the target number!", 60, WIDTH / 2, (HEIGHT /2)-50 , BLACK)
        draw_text(gameDisplay, "Circle: 1 point", 50, WIDTH / 2, (HEIGHT /2) + 20 , RED)
        draw_text(gameDisplay, "Triangle: 3 points", 50, WIDTH / 2, HEIGHT/2 + 70, GREEN)
        draw_text(gameDisplay, "Square: 4 points", 50, WIDTH / 2, HEIGHT/2 + 120, BLUE)
        draw_text(gameDisplay, "Hexagon: 6 points", 50, WIDTH / 2, HEIGHT/2 + 170, PURPLE)
        draw_text(gameDisplay, "Octagon: 8 points", 50, WIDTH / 2, HEIGHT/2 + 220, YELLOW)

    draw_text(gameDisplay, "Press a key to begin!", 92, WIDTH / 2, HEIGHT/2 + 280, BLACK)

    elapsed_time = 0
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

# Blade
class Blade:
    def __init__(self, x, y, image_path, scale):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.scale = scale

    def draw(self, surface):
        gameDisplay.blit(self.image, self.rect)

# Function to display the blade cutting effect
def display_blade_cutting(gameDisplay, x, y):
    image_path = "images/line.png"
    scale = (100, 30)
    blade = Blade(x, y, image_path, scale)

    # Draw the blade
    blade.draw(gameDisplay)

    # Update the display
    pygame.display.flip()


# Timer settings
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()


# Game Loop
first_round = True
game_over = True        
game_running = True     
while game_running :

    # Calculate the elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    if game_over :
        if first_round :
            show_gameover_screen(elapsed_time)
            first_round = False
        game_over = False
        player_lives = 3
        draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')
        score = 0
        remaining = target
        score_text = font.render(f'Score: {score}', True, BLUE)    
        target_text = font.render(f'Target: {target}', True, GREEN)    
        remaining_text = font.render(f'Remaining: {remaining}', True, YELLOW)  
        elapsed_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    gameDisplay.blit(background, (0, 0))
    gameDisplay.blit(score_text, (30, 10))
    gameDisplay.blit(target_text, (250, 10))
    gameDisplay.blit(remaining_text, (505, 10))
    

    draw_lives(gameDisplay, 690, 5, player_lives, 'images/red_lives.png')

    for key, value in data.items():
        if value['throw']:
            value['x'] += value['speed_x']          
            value['y'] += value['speed_y']          
            value['speed_y'] += (1 * value['t'])    
            value['t'] += 1                         

            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'], value['y']))
            else:
                generate_random_shapes(key)

            current_position = pygame.mouse.get_pos()

            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 \
                    and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                if key == 'bomb':
                    player_lives -= 1
                    if player_lives == 0:
                        
                        show_gameover_screen(elapsed_time)
                        game_over = True
                        
                    elif player_lives == 1 :
                        hide_cross_lives(725, 15)
                    elif player_lives == 2 :
                        hide_cross_lives(760, 15)

                    broken_shape_path = "images/explosion.png"
                else:
                    display_blade_cutting(gameDisplay, value['x']+30, value['y']+30)

                    broken_shape_path = "images/" + key + "_broken" + ".png"

                value['img'] = pygame.image.load(broken_shape_path)
                value['speed_x'] += 10
                if key != 'bomb':
                    score += shapes_dict[key]
                    remaining = target - score
                    
                    if score > target:
                        
                        show_gameover_screen(elapsed_time, 'lost')
                        game_over = True
                    elif score == target:
                        show_gameover_screen(elapsed_time, 'won')
                        game_over = True
                        
                score_text = font.render(f'Score: {score}', True, BLUE)    
                target_text = font.render(f'Target: {target}', True, GREEN)    
                remaining_text = font.render(f'Remaining: {remaining}', True, YELLOW)  
                value['hit'] = True
        else:
            generate_random_shapes(key)

    pygame.display.update()
    clock.tick(FPS)      

pygame.quit()
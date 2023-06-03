import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Set up the colors
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# Set up the game variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]
food_spawned = True
direction = 'RIGHT'
change_to = direction
score = 0

# Set up the game clock
clock = pygame.time.Clock()
snake_speed = 15

# Function to display the score
def show_score(choice=1):
    font = pygame.font.SysFont('monospace', 24)
    score_text = font.render(f"Score: {score}", True, black)
    window.blit(score_text, (5, 5))

# Game over function
def game_over():
    font = pygame.font.SysFont('monospace', 72)
    game_over_text = font.render("Game Over", True, red)
    window.blit(game_over_text, (window_width // 6, window_height // 3))
    show_score(0)
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    quit()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # Handling arrow key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'

    # Making sure the snake cannot move in the opposite direction instantly
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    # Update snake position
    if direction == 'RIGHT':
        snake_position[0] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 10
        food_spawned = False
    else:
        snake_body.pop()

    # Food spawning
    if not food_spawned:
        food_position = [random.randrange(1, (window_width // 10)) * 10, random.randrange(1, (window_height // 10)) * 10]
        food_spawned = True

    # Background
    window.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Draw food
    pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Game over conditions
    if snake_position[0] < 0 or snake_position[0] > window_width - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_height - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Display score
    show_score()

    # Refresh game screen
    pygame.display.update()

    # Refresh rate
    clock.tick(snake_speed)

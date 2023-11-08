import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Define the paddles and ball
paddle_width, paddle_height = 10, 100
ball_width, ball_height = 10, 10

player1 = pygame.Rect(50, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
player2 = pygame.Rect(WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_height // 2, ball_width, ball_height)

# Initial ball speed
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

# Scores
score1 = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control player 1 with 'W' and 'S' keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.y -= 10
    if keys[pygame.K_s]:
        player1.y += 10

    # Control player 2 with the arrow keys
    if keys[pygame.K_UP]:
        player2.y -= 10
    if keys[pygame.K_DOWN]:
        player2.y += 10

    # Update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with top and bottom walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y = -ball_speed_y

    # Ball collisions with paddles
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x = -ball_speed_x

    # Ball out of bounds
    if ball.left <= 0:
        # Player 2 scores a point
        score2 += 1
        ball = pygame.Rect(WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_height // 2, ball_width, ball_height)
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))

    if ball.right >= WIDTH:
        # Player 1 scores a point
        score1 += 1
        ball = pygame.Rect(WIDTH // 2 - ball_width // 2, HEIGHT // 2 - ball_height // 2, ball_width, ball_height)
        ball_speed_x = 7 * random.choice((1, -1))
        ball_speed_y = 7 * random.choice((1, -1))

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the paddles and ball
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, RED, ball)

    # Draw the scores
    score_display = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - score_display.get_width() // 2, 20))

    # Update the display
    pygame.display.flip()

    # Control frame rate
    clock.tick(10)  # Limit the frame rate to 60 frames per second

# Quit Pygame
pygame.quit()

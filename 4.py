import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Classes")

# Colors
BACKGROUND = (20, 30, 50)
SNAKE_HEAD_COLOR = (0, 200, 100)
SNAKE_BODY_COLOR = (0, 150, 80)
FOOD_COLOR = (255, 50, 50)
TEXT_COLOR = (255, 255, 255)
UI_BG = (40, 50, 70, 180)
GRID_COLOR = (30, 40, 60)

# Game variables
clock = pygame.time.Clock()
FPS = 10
score = 0
game_over = False
high_score = 0

# Font
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.body = [(x, y)]
        self.direction = "RIGHT"
        self.grow_pending = 0
        self.speed = 20  # Movement speed in pixels
        
    def move(self):
        # Save current head position
        head_x, head_y = self.body[0]
        
        # Calculate new head position based on direction
        if self.direction == "UP":
            new_head = (head_x, head_y - self.speed)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + self.speed)
        elif self.direction == "LEFT":
            new_head = (head_x - self.speed, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + self.speed, head_y)
            
        # Add new head to body
        self.body.insert(0, new_head)
        
        # Remove tail if not growing
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
            
    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        if (new_direction == "UP" and self.direction != "DOWN") or \
           (new_direction == "DOWN" and self.direction != "UP") or \
           (new_direction == "LEFT" and self.direction != "RIGHT") or \
           (new_direction == "RIGHT" and self.direction != "LEFT"):
            self.direction = new_direction
            
    def grow(self):
        self.grow_pending += 1
        
    def draw(self, screen):
        # Draw snake body
        for i, (x, y) in enumerate(self.body):
            # Head is a different color
            if i == 0:
                color = SNAKE_HEAD_COLOR
            else:
                color = SNAKE_BODY_COLOR
                
            pygame.draw.rect(screen, color, (x - self.size//2, y - self.size//2, self.size, self.size))
            pygame.draw.rect(screen, (255, 255, 255), (x - self.size//2, y - self.size//2, self.size, self.size), 1)
            
            # Draw eyes on head
            if i == 0:
                # Eye positions based on direction
                eye_size = 4
                if self.direction == "RIGHT":
                    pygame.draw.circle(screen, (0, 0, 0), (x + self.size//4, y - self.size//6), eye_size)
                    pygame.draw.circle(screen, (0, 0, 0), (x + self.size//4, y + self.size//6), eye_size)
                elif self.direction == "LEFT":
                    pygame.draw.circle(screen, (0, 0, 0), (x - self.size//4, y - self.size//6), eye_size)
                    pygame.draw.circle(screen, (0, 0, 0), (x - self.size//4, y + self.size//6), eye_size)
                elif self.direction == "UP":
                    pygame.draw.circle(screen, (0, 0, 0), (x - self.size//6, y - self.size//4), eye_size)
                    pygame.draw.circle(screen, (0, 0, 0), (x + self.size//6, y - self.size//4), eye_size)
                elif self.direction == "DOWN":
                    pygame.draw.circle(screen, (0, 0, 0), (x - self.size//6, y + self.size//4), eye_size)
                    pygame.draw.circle(screen, (0, 0, 0), (x + self.size//6, y + self.size//4), eye_size)
                    
    def get_head(self):
        return self.body[0]
        
    def check_collision(self):
        head = self.get_head()
        
        # Check wall collision
        if (head[0] < 0 or head[0] >= WIDTH or 
            head[1] < 0 or head[1] >= HEIGHT):
            return True
            
        # Check self collision (skip head)
        for segment in self.body[1:]:
            if head == segment:
                return True
                
        return False

class Food:
    def __init__(self):
        self.size = 20
        self.position = (0, 0)
        self.randomize_position()
        
    def randomize_position(self):
        # Generate random position within screen bounds
        self.position = (
            random.randint(0, (WIDTH - self.size) // self.size) * self.size,
            random.randint(0, (HEIGHT - self.size) // self.size) * self.size
        )
        
    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, (self.position[0] - self.size//2, 
                                             self.position[1] - self.size//2, 
                                             self.size, self.size))
        pygame.draw.rect(screen, (255, 200, 200), (self.position[0] - self.size//2, 
                                                 self.position[1] - self.size//2, 
                                                 self.size, self.size), 2)
        
        # Draw a shine effect
        pygame.draw.circle(screen, (255, 200, 200), 
                          (self.position[0] - self.size//4, self.position[1] - self.size//4), 
                          self.size//6)

def draw_grid(screen):
    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, 20):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WIDTH, y), 1)

def draw_score(screen, score, high_score):
    pygame.draw.rect(screen, UI_BG, (10, 10, 250, 80), border_radius=10)
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 20))
    
    high_score_text = font.render(f"High Score: {high_score}", True, TEXT_COLOR)
    screen.blit(high_score_text, (20, 55))

def draw_game_over(screen, score):
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    game_over_text = font.render("GAME OVER", True, (255, 50, 50))
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    restart_text = small_font.render("Press SPACE to restart", True, TEXT_COLOR)
    
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 60))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 60))

def draw_instructions(screen):
    instructions = [
        "Use Arrow Keys to Control Snake",
        "Eat Food to Grow",
        "Avoid Walls and Self-Collision"
    ]
    
    for i, text in enumerate(instructions):
        text_surface = small_font.render(text, True, (180, 200, 255))
        screen.blit(text_surface, (WIDTH//2 - text_surface.get_width()//2, 10 + i * 40))

# Create game objects
snake = Snake(WIDTH // 2, HEIGHT // 2)
food = Food()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")
            else:
                if event.key == pygame.K_SPACE:
                    # Reset game
                    snake = Snake(WIDTH // 2, HEIGHT // 2)
                    food.randomize_position()
                    score = 0
                    game_over = False
    
    if not game_over:
        # Move snake
        snake.move()
        
        # Check if snake ate food
        if snake.get_head() == food.position:
            snake.grow()
            food.randomize_position()
            score += 10
            
            # Make sure food doesn't appear on snake
            for segment in snake.body:
                if segment == food.position:
                    food.randomize_position()
        
        # Check for collisions
        if snake.check_collision():
            game_over = True
            if score > high_score:
                high_score = score
    
    # Drawing
    screen.fill(BACKGROUND)
    
    # Draw grid
    draw_grid(screen)
    
    # Draw food
    food.draw(screen)
    
    # Draw snake
    snake.draw(screen)
    
    # Draw UI
    draw_score(screen, score, high_score)
    
    # Draw instructions
    draw_instructions(screen)
    
    # Draw game over screen if needed
    if game_over:
        draw_game_over(screen, score)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()

'''
Key Concepts Taught in This Snake Game
1. Class Design
Snake class with methods for movement, direction changes, and drawing
Food class for generating and drawing food items
Proper encapsulation of snake properties and behaviors
2. Object Attributes
Snake has attributes: x, y, size, body, direction, grow_pending, speed
Food has attributes: size, position
3. Object Methods
move(): Updates snake position based on direction
change_direction(): Handles direction changes with collision prevention
grow(): Increases snake size when eating food
draw(): Renders the snake and food on screen
check_collision(): Detects wall and self-collision
get_head(): Returns current head position
4. Game Mechanics
Snake movement with arrow keys
Food generation and collision detection
Score tracking and high score system
Game over conditions (wall and self-collision)
Restart functionality
5. Visual Design
Snake with distinct head and body segments
Detailed snake with eyes that change based on direction
Food with shine effect
Grid background for better orientation
Clean UI with score display
How to Run the Game
Make sure you have Python and Pygame installed
Copy the code into a Python file (e.g., snake_game.py)
Run the file with python snake_game.py
Learning Objectives
This Snake game teaches beginners:

How to create and use classes with proper initialization
How to implement game logic using object methods
How to handle user input and game state changes
How to manage game objects (snake and food) with their own behaviors
How to implement collision detection and game over conditions
How to create visual feedback through drawing methods
How to manage game state (score, high score, game over)
The Snake game is a classic that demonstrates many OOP concepts in a fun, interactive way that's perfect for learning!
'''
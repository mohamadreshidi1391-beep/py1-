import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Class and Object Game")

# Colors
BACKGROUND = (20, 30, 50)
PLAYER_COLOR = (0, 200, 255)
ENEMY_COLOR = (255, 50, 50)
BULLET_COLOR = (255, 255, 100)
TEXT_COLOR = (255, 255, 255)
UI_BG = (40, 50, 70, 180)
HEALTH_BAR_COLOR = (0, 200, 0)
HEALTH_BAR_BG = (100, 0, 0)

# Game variables
score = 0
game_over = False
player_health = 100
enemies = []
bullets = []
particles = []

# Font
font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.speed = 5
        self.health = 100
        self.color = PLAYER_COLOR
        
    def draw(self, screen):
        # Draw player as a triangle pointing up
        points = [
            (self.x, self.y),
            (self.x - self.width//2, self.y + self.height),
            (self.x + self.width//2, self.y + self.height)
        ]
        pygame.draw.polygon(screen, self.color, points)
        pygame.draw.polygon(screen, (255, 255, 255), points, 2)
        
        # Draw health bar
        bar_width = 60
        bar_height = 8
        bar_x = self.x - bar_width//2
        bar_y = self.y - 20
        
        pygame.draw.rect(screen, HEALTH_BAR_BG, (bar_x, bar_y, bar_width, bar_height))
        pygame.draw.rect(screen, HEALTH_BAR_COLOR, (bar_x, bar_y, bar_width * (self.health/100), bar_height))
        
    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH:
            self.x += self.speed
        if direction == "up" and self.y > 0:
            self.y -= self.speed
        if direction == "down" and self.y < HEIGHT:
            self.y += self.speed
            
    def shoot(self):
        # Create a bullet at the player's position
        bullet = Bullet(self.x, self.y - 20)
        bullets.append(bullet)
        
    def get_rect(self):
        return pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = random.randint(1, 3)
        self.color = ENEMY_COLOR
        self.health = 30
        
    def draw(self, screen):
        # Draw enemy as a square with a cross
        pygame.draw.rect(screen, self.color, (self.x - self.width//2, self.y - self.height//2, self.width, self.height))
        pygame.draw.line(screen, (255, 255, 255), (self.x - 10, self.y - 10), (self.x + 10, self.y + 10), 3)
        pygame.draw.line(screen, (255, 255, 255), (self.x + 10, self.y - 10), (self.x - 10, self.y + 10), 3)
        
    def update(self):
        self.y += self.speed
        # Reset enemy if it goes off screen
        if self.y > HEIGHT + 20:
            self.y = -20
            self.x = random.randint(20, WIDTH - 20)
            
    def get_rect(self):
        return pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 15
        self.speed = 7
        self.color = BULLET_COLOR
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x - self.width//2, self.y - self.height//2, self.width, self.height))
        pygame.draw.rect(screen, (255, 255, 255), (self.x - self.width//2, self.y - self.height//2, self.width, self.height), 1)
        
    def update(self):
        self.y -= self.speed
        # Remove bullet if it goes off screen
        if self.y < -10:
            return True
        return False
        
    def get_rect(self):
        return pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = color
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)
        self.lifetime = 30  # frames
        
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)
        
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.lifetime -= 1
        return self.lifetime <= 0

# Create player
player = Player(WIDTH // 2, HEIGHT - 60)

# Create initial enemies
for i in range(5):
    enemy = Enemy(random.randint(20, WIDTH - 20), random.randint(-200, -20))
    enemies.append(enemy)

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.shoot()
            if event.key == pygame.K_r and game_over:
                # Reset game
                game_over = False
                score = 0
                player_health = 100
                player.x = WIDTH // 2
                player.y = HEIGHT - 60
                enemies = []
                bullets = []
                particles = []
                for i in range(5):
                    enemy = Enemy(random.randint(20, WIDTH - 20), random.randint(-200, -20))
                    enemies.append(enemy)
    
    if not game_over:
        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move("left")
        if keys[pygame.K_RIGHT]:
            player.move("right")
        if keys[pygame.K_UP]:
            player.move("up")
        if keys[pygame.K_DOWN]:
            player.move("down")
            
        # Update enemies
        for enemy in enemies:
            enemy.update()
            
        # Update bullets
        for bullet in bullets[:]:
            if bullet.update():
                bullets.remove(bullet)
                
        # Check collisions
        # Bullet-enemy collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.get_rect().colliderect(enemy.get_rect()):
                    # Create explosion particles
                    for _ in range(10):
                        particles.append(Particle(enemy.x, enemy.y, (255, 100, 50)))
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score += 10
                    # Add new enemy
                    new_enemy = Enemy(random.randint(20, WIDTH - 20), random.randint(-200, -20))
                    enemies.append(new_enemy)
                    break
                    
        # Player-enemy collisions
        for enemy in enemies[:]:
            if player.get_rect().colliderect(enemy.get_rect()):
                # Create explosion particles
                for _ in range(15):
                    particles.append(Particle(enemy.x, enemy.y, (255, 50, 50)))
                enemies.remove(enemy)
                player_health -= 10
                # Add new enemy
                new_enemy = Enemy(random.randint(20, WIDTH - 20), random.randint(-200, -20))
                enemies.append(new_enemy)
                
                if player_health <= 0:
                    game_over = True
                    
        # Update particles
        for particle in particles[:]:
            if particle.update():
                particles.remove(particle)
    
    # Drawing
    screen.fill(BACKGROUND)
    
    # Draw stars in background
    for i in range(100):
        x = (i * 17) % WIDTH
        y = (i * 13) % HEIGHT
        size = (i % 3) + 1
        brightness = 150 + (i % 100)
        pygame.draw.circle(screen, (brightness, brightness, brightness), (x, y), size)
    
    # Draw player
    player.draw(screen)
    
    # Draw enemies
    for enemy in enemies:
        enemy.draw(screen)
        
    # Draw bullets
    for bullet in bullets:
        bullet.draw(screen)
        
    # Draw particles
    for particle in particles:
        particle.draw(screen)
        
    # Draw UI
    pygame.draw.rect(screen, UI_BG, (10, 10, 200, 80), border_radius=10)
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 20))
    
    health_text = font.render(f"Health: {player_health}", True, TEXT_COLOR)
    screen.blit(health_text, (20, 55))
    
    if game_over:
        game_over_text = font.render("GAME OVER", True, (255, 50, 50))
        restart_text = small_font.render("Press R to restart", True, TEXT_COLOR)
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 30))
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 20))
    
    # Draw instructions
    if not game_over:
        instructions = [
            "Use arrow keys to move",
            "Press SPACE to shoot",
            "Avoid enemies or shoot them!"
        ]
        for i, text in enumerate(instructions):
            text_surface = small_font.render(text, True, (180, 200, 255))
            screen.blit(text_surface, (WIDTH - text_surface.get_width() - 10, 10 + i * 30))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

'''
Key Concepts Taught in This Example
1. Classes and Objects
The Player, Enemy, Bullet, and Particle classes define different game entities
Each class has its own properties (attributes) and methods (functions)
Objects are created from these classes (e.g., player = Player(WIDTH // 2, HEIGHT - 60))
2. Class Attributes
Player has attributes like x, y, width, height, speed, health, and color
Enemy has x, y, width, height, speed, and color
Bullet has x, y, width, height, speed, and color
3. Class Methods
draw(): Renders the object on screen
move(): Updates player position
update(): Updates enemy position or bullet movement
get_rect(): Returns a rectangle for collision detection
4. Object-Oriented Programming Concepts
Encapsulation: Each class encapsulates its own data and behavior
Reusability: Objects can be created multiple times with different properties
Interaction: Objects interact with each other through methods and events
5. Game Mechanics
Player movement with arrow keys
Shooting with spacebar
Enemy spawning and movement
Collision detection
Score tracking
Health system
Particle effects for explosions
How to Run the Game
Make sure you have Python and Pygame installed
Copy the code into a Python file (e.g., class_game.py)
Run the file with python class_game.py
Learning Objectives
This example teaches beginners:

How to define classes with __init__ methods
How to create and use objects from classes
How to define methods within classes
How to use attributes to store object state
How to implement basic game mechanics using classes
How to handle collisions between objects
How to manage multiple objects in a game loop
The game provides visual feedback and interactive elements that make learning classes and objects more engaging for beginners.
'''
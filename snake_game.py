import pygame
import random
import sys
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Colors (minimal palette)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
PINK = (255, 192, 203)
PURPLE = (128, 0, 128)
GRAY = (128, 128, 128)

class FruitType(Enum):
    APPLE = "apple"
    ORANGE = "orange"
    GRAPEFRUIT = "grapefruit"
    BERRY = "berry"

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Fruit:
    def __init__(self, fruit_type, x, y):
        self.type = fruit_type
        self.x = x
        self.y = y
        self.color = self._get_color()
        self.symbol = self._get_symbol()
    
    def _get_color(self):
        colors = {
            FruitType.APPLE: RED,
            FruitType.ORANGE: ORANGE,
            FruitType.GRAPEFRUIT: PINK,
            FruitType.BERRY: PURPLE
        }
        return colors[self.type]
    
    def _get_symbol(self):
        symbols = {
            FruitType.APPLE: "🍎",
            FruitType.ORANGE: "🍊",
            FruitType.GRAPEFRUIT: "🍇",
            FruitType.BERRY: "🫐"
        }
        return symbols[self.type]

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = Direction.RIGHT
        self.grow_pending = 0
    
    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value
        new_head = (head_x + dx, head_y + dy)
        
        self.body.insert(0, new_head)
        
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
    
    def grow(self):
        self.grow_pending += 1
    
    def check_collision(self):
        head_x, head_y = self.body[0]
        
        # Wall collision
        if head_x < 0 or head_x >= GRID_WIDTH or head_y < 0 or head_y >= GRID_HEIGHT:
            return True
        
        # Self collision
        if (head_x, head_y) in self.body[1:]:
            return True
        
        return False
    
    def change_direction(self, new_direction):
        # Prevent reversing into itself
        opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Retro Snake Game - Avoid the Apples!")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        self.reset_game()
    
    def reset_game(self):
        self.snake = Snake()
        self.fruits = []
        self.level = 0
        self.score = 0
        self.game_over = False
        self.game_won = False
        self.speed = 8  # Starting speed
        self.fruits_eaten_this_level = 0
        self.fruits_needed_per_level = 5
        
        self.spawn_fruits()
    
    def spawn_fruits(self):
        self.fruits.clear()
        
        # Level-based fruit spawning
        apple_count = min(2 + self.level, 6)  # More apples as level increases
        good_fruit_count = 3 + self.level  # More good fruits too
        
        # Spawn apples (dangerous)
        for _ in range(apple_count):
            self.spawn_fruit(FruitType.APPLE)
        
        # Spawn good fruits
        good_fruits = [FruitType.ORANGE, FruitType.GRAPEFRUIT, FruitType.BERRY]
        for _ in range(good_fruit_count):
            fruit_type = random.choice(good_fruits)
            self.spawn_fruit(fruit_type)
    
    def spawn_fruit(self, fruit_type):
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            
            # Don't spawn on snake
            if (x, y) not in self.snake.body:
                # Don't spawn on existing fruits
                if not any(f.x == x and f.y == y for f in self.fruits):
                    self.fruits.append(Fruit(fruit_type, x, y))
                    break
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                
                if self.game_over or self.game_won:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                else:
                    # Direction controls
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(Direction.RIGHT)
        
        return True
    
    def update(self):
        if self.game_over or self.game_won:
            return
        
        self.snake.move()
        
        # Check wall/self collision
        if self.snake.check_collision():
            self.game_over = True
            return
        
        # Check fruit collision
        head_x, head_y = self.snake.body[0]
        for fruit in self.fruits[:]:  # Copy list to avoid modification during iteration
            if fruit.x == head_x and fruit.y == head_y:
                if fruit.type == FruitType.APPLE:
                    # Game over - ate an apple!
                    self.game_over = True
                    return
                else:
                    # Good fruit eaten
                    self.fruits.remove(fruit)
                    self.snake.grow()
                    self.score += 10
                    self.fruits_eaten_this_level += 1
                    
                    # Spawn new good fruit
                    good_fruits = [FruitType.ORANGE, FruitType.GRAPEFRUIT, FruitType.BERRY]
                    self.spawn_fruit(random.choice(good_fruits))
                    
                    # Check level completion
                    if self.fruits_eaten_this_level >= self.fruits_needed_per_level:
                        self.level += 1
                        self.fruits_eaten_this_level = 0
                        
                        if self.level > 5:
                            self.game_won = True
                            return
                        
                        # Increase speed slightly
                        self.speed = min(self.speed + 1, 15)
                        self.spawn_fruits()
    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw snake
        for segment in self.snake.body:
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, GREEN, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 1)
        
        # Draw fruits
        for fruit in self.fruits:
            x = fruit.x * GRID_SIZE
            y = fruit.y * GRID_SIZE
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(self.screen, fruit.color, rect)
            pygame.draw.rect(self.screen, WHITE, rect, 1)
        
        # Draw UI
        self.draw_ui()
        
        # Draw game over/win screen
        if self.game_over:
            self.draw_game_over()
        elif self.game_won:
            self.draw_game_won()
        
        pygame.display.flip()
    
    def draw_ui(self):
        # Score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # Level
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        self.screen.blit(level_text, (10, 50))
        
        # Progress
        progress_text = self.font.render(f"Progress: {self.fruits_eaten_this_level}/{self.fruits_needed_per_level}", True, WHITE)
        self.screen.blit(progress_text, (10, 90))
        
        # Instructions
        if self.level == 0 and self.fruits_eaten_this_level == 0:
            instruction_text = self.font.render("Eat good fruits, AVOID APPLES!", True, WHITE)
            text_rect = instruction_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
            self.screen.blit(instruction_text, text_rect)
    
    def draw_game_over(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.big_font.render("GAME OVER!", True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(game_over_text, text_rect)
        
        reason_text = self.font.render("You ate an apple!", True, WHITE)
        text_rect = reason_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(reason_text, text_rect)
        
        final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        text_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        self.screen.blit(final_score_text, text_rect)
        
        restart_text = self.font.render("Press SPACE to restart or ESC to quit", True, WHITE)
        text_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
        self.screen.blit(restart_text, text_rect)
    
    def draw_game_won(self):
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Victory text
        victory_text = self.big_font.render("YOU WIN!", True, GREEN)
        text_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        self.screen.blit(victory_text, text_rect)
        
        congrats_text = self.font.render("Congratulations! You completed all levels!", True, WHITE)
        text_rect = congrats_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(congrats_text, text_rect)
        
        final_score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        text_rect = final_score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        self.screen.blit(final_score_text, text_rect)
        
        restart_text = self.font.render("Press SPACE to play again or ESC to quit", True, WHITE)
        text_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 70))
        self.screen.blit(restart_text, text_rect)
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.speed)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()

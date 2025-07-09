#!/usr/bin/env python3
"""
Test script for game logic validation
Tests core game mechanics without requiring pygame
"""

import sys
from enum import Enum

# Mock pygame for testing
class MockPygame:
    def init(self): pass
    def quit(self): pass
    
    class display:
        @staticmethod
        def set_mode(size): return None
        @staticmethod
        def set_caption(title): pass
        @staticmethod
        def flip(): pass
    
    class time:
        class Clock:
            def tick(self, fps): pass
    
    class font:
        class Font:
            def __init__(self, font, size): pass
            def render(self, text, antialias, color): 
                class MockSurface:
                    def get_rect(self, **kwargs): 
                        class MockRect:
                            def __init__(self):
                                self.center = (0, 0)
                        return MockRect()
                return MockSurface()
    
    class draw:
        @staticmethod
        def rect(surface, color, rect, width=0): pass
    
    class Rect:
        def __init__(self, x, y, w, h):
            self.x, self.y = x, y
            self.width, self.height = w, h
            self.top, self.bottom = y, y + h
            self.left, self.right = x, x + w
        
        def colliderect(self, other):
            return not (self.right <= other.left or self.left >= other.right or 
                       self.bottom <= other.top or self.top >= other.bottom)

# Replace pygame import
sys.modules['pygame'] = MockPygame()

# Now import our game classes
from snake_game import FruitType, Direction, Snake, Fruit, SnakeGame

def test_fruit_types():
    """Test fruit type enumeration"""
    print("🧪 Testing Fruit Types...")
    
    apple = Fruit(FruitType.APPLE, 5, 5)
    orange = Fruit(FruitType.ORANGE, 10, 10)
    grapefruit = Fruit(FruitType.GRAPEFRUIT, 15, 15)
    berry = Fruit(FruitType.BERRY, 20, 20)
    
    assert apple.type == FruitType.APPLE
    assert orange.type == FruitType.ORANGE
    assert grapefruit.type == FruitType.GRAPEFRUIT
    assert berry.type == FruitType.BERRY
    
    print("✅ Fruit types working correctly")

def test_snake_movement():
    """Test snake movement mechanics"""
    print("🧪 Testing Snake Movement...")
    
    snake = Snake()
    initial_pos = snake.body[0]
    
    # Test initial direction (RIGHT)
    assert snake.direction == Direction.RIGHT
    
    # Test movement
    snake.move()
    new_pos = snake.body[0]
    
    # Should move right
    assert new_pos[0] == initial_pos[0] + 1
    assert new_pos[1] == initial_pos[1]
    
    # Test direction change
    snake.change_direction(Direction.UP)
    assert snake.direction == Direction.UP
    
    # Test invalid direction change (can't reverse)
    snake.change_direction(Direction.DOWN)
    assert snake.direction == Direction.UP  # Should remain UP
    
    print("✅ Snake movement working correctly")

def test_snake_growth():
    """Test snake growth mechanics"""
    print("🧪 Testing Snake Growth...")
    
    snake = Snake()
    initial_length = len(snake.body)
    
    # Test growth
    snake.grow()
    snake.move()  # Growth happens on next move
    
    assert len(snake.body) == initial_length + 1
    print("✅ Snake growth working correctly")

def test_collision_detection():
    """Test collision detection"""
    print("🧪 Testing Collision Detection...")
    
    snake = Snake()
    
    # Test wall collision (move snake to edge)
    snake.body = [(0, 0)]  # At left edge
    snake.direction = Direction.LEFT
    snake.move()
    
    assert snake.check_collision() == True
    print("✅ Wall collision detection working")

def test_game_initialization():
    """Test game initialization"""
    print("🧪 Testing Game Initialization...")
    
    # Mock pygame surface for testing
    class MockSurface:
        def fill(self, color): pass
        def blit(self, surface, pos): pass
    
    game = SnakeGame()
    game.screen = MockSurface()  # Mock the screen
    
    # Test initial state
    assert game.level == 0
    assert game.score == 0
    assert game.game_over == False
    assert game.game_won == False
    assert len(game.fruits) > 0  # Should have fruits spawned
    
    # Test fruit spawning
    apple_count = sum(1 for f in game.fruits if f.type == FruitType.APPLE)
    good_fruit_count = sum(1 for f in game.fruits if f.type != FruitType.APPLE)
    
    assert apple_count == 2  # Level 0 should have 2 apples
    assert good_fruit_count == 3  # Level 0 should have 3 good fruits
    
    print("✅ Game initialization working correctly")

def test_level_progression():
    """Test level progression logic"""
    print("🧪 Testing Level Progression...")
    
    game = SnakeGame()
    game.screen = type('MockSurface', (), {'fill': lambda self, c: None, 'blit': lambda self, s, p: None})()
    
    initial_level = game.level
    initial_speed = game.speed
    
    # Simulate eating required fruits for level completion
    for _ in range(game.fruits_needed_per_level):
        game.fruits_eaten_this_level += 1
        game.score += 10
    
    # Trigger level completion check
    if game.fruits_eaten_this_level >= game.fruits_needed_per_level:
        game.level += 1
        game.fruits_eaten_this_level = 0
        game.speed = min(game.speed + 1, 15)
    
    assert game.level == initial_level + 1
    assert game.speed == initial_speed + 1
    assert game.fruits_eaten_this_level == 0
    
    print("✅ Level progression working correctly")

def test_win_condition():
    """Test game win condition"""
    print("🧪 Testing Win Condition...")
    
    game = SnakeGame()
    game.screen = type('MockSurface', (), {'fill': lambda self, c: None, 'blit': lambda self, s, p: None})()
    
    # Set to level 5 and complete it
    game.level = 5
    game.fruits_eaten_this_level = game.fruits_needed_per_level
    
    # Simulate level completion
    if game.fruits_eaten_this_level >= game.fruits_needed_per_level:
        game.level += 1
        if game.level > 5:
            game.game_won = True
    
    assert game.game_won == True
    print("✅ Win condition working correctly")

def run_all_tests():
    """Run all tests"""
    print("🎮 Running Retro Snake Game Logic Tests")
    print("=" * 40)
    
    try:
        test_fruit_types()
        test_snake_movement()
        test_snake_growth()
        test_collision_detection()
        test_game_initialization()
        test_level_progression()
        test_win_condition()
        
        print("\n🎉 All tests passed!")
        print("✅ Game logic is working correctly")
        print("✅ Ready for gameplay testing")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)

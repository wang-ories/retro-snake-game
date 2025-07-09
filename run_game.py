#!/usr/bin/env python3
"""
Retro Snake Game Launcher
Simple launcher script with dependency checking
"""

import sys
import subprocess

def check_pygame():
    """Check if pygame is installed"""
    try:
        import pygame
        return True
    except ImportError:
        return False

def install_pygame():
    """Install pygame using pip"""
    print("Installing pygame...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame==2.5.2"])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🐍 Retro Snake Game Launcher")
    print("=" * 30)
    
    # Check pygame
    if not check_pygame():
        print("❌ pygame not found!")
        response = input("Would you like to install it? (y/n): ").lower().strip()
        
        if response == 'y':
            if install_pygame():
                print("✅ pygame installed successfully!")
            else:
                print("❌ Failed to install pygame. Please install manually:")
                print("   pip install pygame==2.5.2")
                return
        else:
            print("❌ pygame is required to run the game.")
            return
    else:
        print("✅ pygame found!")
    
    print("\n🎮 Starting Retro Snake Game...")
    print("Remember: Eat good fruits, AVOID the apples! 🍎")
    
    # Import and run the game
    try:
        from snake_game import SnakeGame
        game = SnakeGame()
        game.run()
    except Exception as e:
        print(f"❌ Error starting game: {e}")

if __name__ == "__main__":
    main()

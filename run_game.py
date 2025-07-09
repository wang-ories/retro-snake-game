#!/usr/bin/env python3
"""
Retro Snake Game Launcher
Simple launcher script with dependency checking and macOS support
"""

import sys
import subprocess
import platform

def check_pygame():
    """Check if pygame is installed"""
    try:
        import pygame
        return True, pygame.version.ver
    except ImportError:
        return False, None

def install_pygame_macos():
    """Install pygame on macOS using homebrew if available"""
    print("🍎 Detected macOS - checking for Homebrew...")
    
    # Check if brew is available
    try:
        subprocess.check_call(["which", "brew"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("✅ Homebrew found!")
        
        print("Installing SDL2 dependencies...")
        subprocess.check_call(["brew", "install", "sdl2", "sdl2_image", "sdl2_mixer", "sdl2_ttf"])
        
        print("Installing pygame...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "pygame"])
        return True
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Homebrew not found or installation failed")
        return False

def install_pygame_generic():
    """Install pygame using pip"""
    print("Installing pygame...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "pygame"])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    print("🐍 Retro Snake Game Launcher")
    print("=" * 30)
    
    # Check pygame
    pygame_available, version = check_pygame()
    
    if not pygame_available:
        print("❌ pygame not found!")
        response = input("Would you like to install it? (y/n): ").lower().strip()
        
        if response == 'y':
            success = False
            
            # Try macOS-specific installation first
            if platform.system() == "Darwin":
                success = install_pygame_macos()
            
            # Fall back to generic installation
            if not success:
                success = install_pygame_generic()
            
            if success:
                pygame_available, version = check_pygame()
                if pygame_available:
                    print(f"✅ pygame {version} installed successfully!")
                else:
                    print("❌ Installation completed but pygame still not available")
                    print("You may need to restart your terminal or check your Python path")
                    return
            else:
                print("❌ Failed to install pygame automatically.")
                print("\n🔧 Manual installation options:")
                print("1. macOS with Homebrew:")
                print("   brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf")
                print("   pip3 install --user pygame")
                print("\n2. Using virtual environment:")
                print("   python3 -m venv game_env")
                print("   source game_env/bin/activate")
                print("   pip install pygame")
                print("\n3. System-wide (not recommended):")
                print("   pip3 install --break-system-packages pygame")
                return
        else:
            print("❌ pygame is required to run the game.")
            return
    else:
        print(f"✅ pygame {version} found!")
    
    print("\n🎮 Starting Retro Snake Game...")
    print("🍎 Remember: Eat good fruits, AVOID the apples!")
    print("🎯 Goal: Complete all 6 levels (0-5) to win!")
    print("\n" + "="*50)
    
    # Import and run the game
    try:
        from snake_game import SnakeGame
        game = SnakeGame()
        game.run()
    except ImportError as e:
        print(f"❌ Error importing game: {e}")
        print("Make sure snake_game.py is in the same directory")
    except Exception as e:
        print(f"❌ Error starting game: {e}")
        print("Check that all dependencies are properly installed")

if __name__ == "__main__":
    main()

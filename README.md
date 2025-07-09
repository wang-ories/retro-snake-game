# 🐍 Retro Snake Game - Avoid the Apples!

A unique twist on the classic Snake game where you must **avoid eating apples** while collecting other delicious fruits! Navigate through 6 challenging levels in this retro-styled arcade experience.

## 🎮 Game Overview

Unlike traditional Snake games, this version flips the script - **apples are dangerous!** Your goal is to eat good fruits while carefully avoiding the deadly red apples scattered throughout each level.

### 🍎 The Twist
- **🍎 Apples = GAME OVER** - Touch an apple and it's instant death!
- **🍊 Good Fruits = Points & Growth** - Eat oranges, grapefruits, and berries to score and grow
- **📈 Progressive Difficulty** - More apples and faster speeds as you advance

## 🎯 Game Features

- **6 Challenging Levels** (0-5) with increasing difficulty
- **Unique Reverse Mechanics** - Avoid apples, eat everything else
- **Retro Pixel Art Style** with minimal color palette
- **Progressive Difficulty** - More obstacles and speed per level
- **Score System** - 10 points per good fruit eaten
- **Victory Condition** - Complete all 6 levels to win!

## 🍓 Fruit Types

| Fruit | Effect | Color | Points |
|-------|--------|-------|--------|
| 🍎 **Apple** | ❌ **GAME OVER** | Red | -∞ |
| 🍊 **Orange** | ✅ Grow + Score | Orange | +10 |
| 🍇 **Pamplemousse** | ✅ Grow + Score | Pink | +10 |
| 🫐 **Berry** | ✅ Grow + Score | Purple | +10 |

## 🎮 Controls

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| **SPACE** | Restart (when game over) |
| **ESC** | Quit Game |

## 📊 Level Progression

| Level | Apples | Good Fruits | Speed | Fruits Needed |
|-------|--------|-------------|-------|---------------|
| 0 | 2 | 3 | Slow | 5 |
| 1 | 3 | 4 | ↑ | 5 |
| 2 | 4 | 5 | ↑ | 5 |
| 3 | 5 | 6 | ↑ | 5 |
| 4 | 6 | 7 | ↑ | 5 |
| 5 | 6 | 8 | Fast | 5 |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pygame library

### Installation & Running

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd retro-snake-game
   ```

2. **Easy Launch (Recommended):**
   ```bash
   python run_game.py
   ```
   *This will automatically install pygame if needed*

3. **Manual Installation:**
   ```bash
   pip install -r requirements.txt
   python snake_game.py
   ```

## 🎯 How to Play

### Objective
Complete all 6 levels by eating the required number of good fruits while avoiding apples.

### Strategy Tips
1. **Plan Your Route** - Look ahead to avoid apple clusters
2. **Use Your Length** - Longer snakes can navigate around apples easier
3. **Corner Carefully** - Don't trap yourself near apples
4. **Speed Management** - Game gets faster each level, stay controlled

### Winning Conditions
- **Level Completion**: Eat 5 good fruits per level
- **Game Victory**: Complete all levels (0-5)
- **Final Score**: Based on total fruits eaten × 10 points

### Losing Conditions
- Eating an apple 🍎
- Hitting walls
- Colliding with your own body

## 🎨 Visual Design

### Color Palette (Minimal Retro Style)
- **Background**: Black `#000000`
- **Snake**: Green `#00FF00`
- **Apple (Danger)**: Red `#FF0000`
- **Orange**: Orange `#FFA500`
- **Pamplemousse**: Pink `#FFC0CB`
- **Berry**: Purple `#800080`
- **UI Text**: White `#FFFFFF`

### Screen Layout
```
┌─────────────────────────────────────┐
│ Score: 150    Level: 2    Progress: 3/5 │
├─────────────────────────────────────┤
│                                     │
│    🍎     🍊                        │
│                                     │
│         🐍🐍🐍                      │
│                                     │
│    🫐           🍇     🍎           │
│                                     │
└─────────────────────────────────────┘
```

## 🏗️ Project Structure

```
retro-snake-game/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── snake_game.py         # Main game implementation
├── run_game.py          # Game launcher with auto-setup
├── assets/              # Game assets (future)
├── screenshots/         # Game screenshots
└── docs/               # Additional documentation
```

## 🔧 Technical Details

### Game Architecture
- **Main Game Loop**: 60 FPS with pygame
- **Grid System**: 20x20 pixel grid cells
- **Collision Detection**: Grid-based positioning
- **State Management**: Level progression and game states

### Key Classes
- `SnakeGame`: Main game controller
- `Snake`: Player snake with movement and collision
- `Fruit`: Individual fruit objects with types
- `FruitType`: Enum for different fruit varieties
- `Direction`: Movement direction management

## 🎮 Game States

1. **Playing**: Normal gameplay
2. **Game Over**: Player ate apple or crashed
3. **Victory**: All levels completed
4. **Paused**: (Future feature)

## 🚧 Development Roadmap

### ✅ Completed Features
- [x] Basic snake movement and collision
- [x] Reverse apple mechanics (apples = death)
- [x] Multiple fruit types (orange, pamplemousse, berry)
- [x] 6-level progression system
- [x] Score tracking and UI
- [x] Game over and victory screens
- [x] Progressive difficulty scaling

### 🔄 Future Enhancements
- [ ] Sound effects and background music
- [ ] High score persistence
- [ ] Power-ups and special items
- [ ] Different game modes (time attack, survival)
- [ ] Animated sprites and better graphics
- [ ] Mobile-friendly touch controls
- [ ] Leaderboard system
- [ ] Achievement system

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
git clone <your-fork>
cd retro-snake-game
pip install -r requirements.txt
python snake_game.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built with Python and pygame
- Special thanks to the retro gaming community

## 📞 Support

Having issues? Here are some common solutions:

### Common Problems
1. **pygame not found**: Run `python run_game.py` for auto-installation
2. **Game too fast/slow**: Adjust the `speed` variable in `snake_game.py`
3. **Controls not responsive**: Ensure the game window has focus

### System Requirements
- **OS**: Windows, macOS, or Linux
- **Python**: 3.8+
- **RAM**: 50MB minimum
- **Display**: 800x600 minimum resolution

---

**🎮 Ready to play? Run `python run_game.py` and start avoiding those apples!** 

*Remember: In this snake game, apples are your enemy! 🍎💀*

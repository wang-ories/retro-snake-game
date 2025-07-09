# Game Mechanics Documentation

## Core Gameplay Loop

### 1. Snake Movement
- Snake moves continuously in the current direction
- Player can change direction using arrow keys
- Snake cannot reverse directly into itself
- Movement is grid-based (20x20 pixel cells)

### 2. Fruit System

#### Fruit Types and Effects
| Fruit Type | Visual | Color | Effect | Points |
|------------|--------|-------|--------|--------|
| Apple | 🍎 | Red | **INSTANT DEATH** | Game Over |
| Orange | 🍊 | Orange | Grow + Score | +10 |
| Pamplemousse | 🍇 | Pink | Grow + Score | +10 |
| Berry | 🫐 | Purple | Grow + Score | +10 |

#### Fruit Spawning Logic
- **Level 0**: 2 apples, 3 good fruits
- **Level 1**: 3 apples, 4 good fruits
- **Level 2**: 4 apples, 5 good fruits
- **Level 3**: 5 apples, 6 good fruits
- **Level 4**: 6 apples, 7 good fruits
- **Level 5**: 6 apples, 8 good fruits

### 3. Level Progression

#### Level Requirements
- **Fruits per level**: 5 good fruits must be eaten
- **Total levels**: 6 levels (0-5)
- **Victory condition**: Complete level 5

#### Difficulty Scaling
- **Speed**: Increases by 1 each level (8 → 15 max)
- **Apple density**: More apples per level
- **Good fruit availability**: More good fruits to balance difficulty

### 4. Collision Detection

#### Fatal Collisions
1. **Apple consumption**: Immediate game over
2. **Wall collision**: Snake hits screen boundaries
3. **Self collision**: Snake hits its own body

#### Beneficial Collisions
1. **Good fruit consumption**: 
   - Snake grows by 1 segment
   - Score increases by 10 points
   - New good fruit spawns randomly

### 5. Scoring System

#### Point Values
- **Good fruits**: 10 points each
- **Level completion bonus**: None (focus on progression)
- **Final score**: Total points from all fruits eaten

#### Score Display
- Real-time score display in top-left corner
- Final score shown on game over/victory screens

### 6. Game States

#### Playing State
- Normal gameplay with snake movement
- Fruit collision detection active
- UI displays current stats

#### Game Over State
- Triggered by apple consumption or collision
- Shows final score and restart option
- Semi-transparent overlay with red "GAME OVER" text

#### Victory State
- Triggered by completing level 5
- Shows congratulations and final score
- Green "YOU WIN!" text with celebration message

### 7. User Interface

#### HUD Elements
- **Score**: Current point total
- **Level**: Current level (0-5)
- **Progress**: Fruits eaten in current level / 5
- **Instructions**: Shown on first level only

#### Visual Feedback
- **Snake**: Green squares with white borders
- **Fruits**: Colored squares matching fruit types
- **Grid**: Implicit 20x20 pixel grid system
- **Background**: Solid black for retro feel

### 8. Input Handling

#### Movement Controls
- **Arrow Up**: Change direction to up (if not moving down)
- **Arrow Down**: Change direction to down (if not moving up)
- **Arrow Left**: Change direction to left (if not moving right)
- **Arrow Right**: Change direction to right (if not moving left)

#### System Controls
- **ESC**: Quit game immediately
- **SPACE**: Restart game (only when game over/won)

### 9. Technical Specifications

#### Performance
- **Frame Rate**: 60 FPS
- **Game Speed**: 8-15 ticks per second (level dependent)
- **Grid Resolution**: 40x30 cells (800x600 pixels)

#### Memory Usage
- Minimal memory footprint
- No persistent data storage
- All game state in memory only

### 10. Balance Considerations

#### Difficulty Curve
- **Early levels**: Few apples, easy navigation
- **Mid levels**: Balanced risk/reward
- **Late levels**: High apple density, requires skill

#### Player Strategy
- **Route planning**: Essential for avoiding apple clusters
- **Length management**: Longer snake = more navigation options
- **Speed adaptation**: Players must adapt to increasing speed

## Future Enhancements

### Potential Mechanics
- **Power-ups**: Temporary invincibility, slow motion
- **Special fruits**: Double points, extra life
- **Obstacles**: Static barriers in addition to apples
- **Time pressure**: Level time limits
- **Multiplayer**: Competitive or cooperative modes

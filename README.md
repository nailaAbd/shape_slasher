# Shape Slasher Game Documentation

## Introduction
Shape Slasher is a Python game built using the Pygame module. It is a variation of the popular Fruit Ninja game but with shapes instead of fruits. The objective of the game is to slice the shapes by touching them with the mouse cursor while avoiding bombs. This documentation provides an overview of the game mechanics, features, and technologies used.

## Running the game
To run the game, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the directory where the game files are located.

3. Run the following command to install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Once the dependencies are installed, run the game using the following command:
   ```
   python shape_slasher.py
   ```

Make sure you have Python installed on your system before running the game.

Note: The `shape_slasher.py` file is the main script that runs the Shape Slasher game. The `requirements.txt` file contains a list of dependencies that need to be installed for the game to run successfully.

## Game Mechanics
1. Target Number:
   - At the start of each game, a target number is generated.
   - The player's goal is to achieve a score equal to the target number in order to win.

2. Shapes and Scoring:
   - Different shapes appear on the screen, each corresponding to a specific point value:
     - Circle shape: 1 point
     - Triangle shape: 3 points
     - Square shape: 4 points
     - Hexagon shape: 6 points
     - Octagon shape: 8 points
   - When a shape is sliced by the player's cursor, the corresponding points are added to the player's score.

3. Bombs:
   - Bombs are also present among the shapes on the screen.
   - If the player's cursor touches a bomb, it will result in a penalty.
   - If the player touches more than three bombs, the game ends and one life is deducted.
   - The player starts with three lives, which are represented by red leaves in the top right corner.

4. Winning and Losing:
   - The player wins the game if their score matches the target number.
   - The player loses the game if any of the following conditions are met:
     - The player's score exceeds the target number.
     - The player's cursor touches more than three bombs.

## Game Features
1. Visual Feedback:
   - When the player slices a shape, it is outlined to provide visual feedback.
   - This makes it clear which shapes have been successfully sliced.

2. User Interface:
   - The game displays important information at the top of the screen:
     - Current target number.
     - Remaining amount (target number minus current score).
     - Current score.
     - Remaining lives (represented by red leaves).

3. End Game Summary:
   - When the game ends, the player is presented with a summary of the game outcome.
   - The summary includes the following information:
     - Win or loss status.
     - Time taken to complete the game.
     - Target score.
     - Final score.

## Technologies Used
1. Python:
   - The game is developed using the Python programming language.
   - Python provides a powerful and flexible foundation for game development.

2. Pygame - (https://www.pygame.org/):
   - The Pygame module is utilized for building the game.
   - Pygame provides a set of libraries and tools for game development in Python.
   - It simplifies tasks such as handling graphics, sounds, and user input.

3. Visual Studio Code (VSCode):
   - The game project is created and developed using the Visual Studio Code editor.
   - VSCode offers a rich set of features for Python development, including code editing, debugging, and version control integration.

## Assets and Inspirations
1. Icons:
   - Icons used in the game are sourced from the following websites:
     - [Icons8](https://icons8.com/)
     - [IconsDB](https://www.iconsdb.com/)
   - These icons add visual representation to the shapes and bombs in the game.

2. Font:
   - The game utilizes the Comic font for text rendering.
   - This font adds a playful and engaging visual style to the game.

3. Background Picture:
   - The background picture used in the game is obtained from [WallpaperAccess](https://wallpaperaccess.com/full/358800.jpg).
   - It provides an appealing and immersive visual backdrop for the game environment.

4. Inspirations:
   - The game project takes inspiration from the implementation of the Fruit Ninja game in Python available at [Fruit Ninja Game in Python](https://github.com/GetProjects-org/Fruit-Ninja-Game-in-Python).
   - This implementation serves as a reference and guide for building the Shape Slasher game.

## Conclusion
The Shape Slasher game is an entertaining and challenging experience for players. By slicing shapes and avoiding bombs, players aim to achieve a target score within the given lives. The game's mechanics, features, and visual elements come together to provide an engaging gameplay experience. With the Python programming language and the Pygame module, you have the power to create exciting games like Shape Slasher.

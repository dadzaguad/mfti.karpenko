# Pygame Ball Clicker Game

This repository contains a simple Pygame application that features a basic clicking game where players can click on randomly generated colored balls to score points. The game is designed to provide an entertaining experience while demonstrating fundamental concepts of game development with Pygame.

## Features

- Randomly generated colorful balls that appear on the screen.
- Score tracking based on successful clicks on the balls.
- Basic game loop with event handling for quitting the game and mouse clicks.
  
## Requirements

To run this game, you need to have Python and Pygame installed on your system. You can install Pygame using pip if it's not already installed:

```bash
pip install pygame
```

## Getting Started

### Installation

1. Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/pygame-ball-clicker.git
   cd pygame-ball-clicker
   ```

2. Ensure you have Python and Pygame installed as described above.

### Running the Game

After installing Pygame, you can run the game by executing the following command:

```bash
python your_game_file.py
```

Replace `your_game_file.py` with the name of the file that contains the code.

### Gameplay Instructions

- The game initializes a window where colored balls will appear at random positions and sizes.
- Click on the balls to increase your score.
- The game runs continuously, generating new balls and allowing you to click on them until you close the window.

### Code Explanation

- The game starts by initializing Pygame and setting up the display screen dimensions (1200x900 pixels).
- A list of color tuples is defined for the balls.
- The `click` function determines if a mouse click occurs within the radius of a ball based on its coordinates.
- The main loop processes user events like clicking and quitting the game, updates the score, and creates new balls at random positions and sizes.
- The screen updates to show the balls and the score during each iteration of the loop.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any improvements, additional features, or bug fixes are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 

## Acknowledgments

Special thanks to the Pygame community and documentation for providing the necessary resources and support in game development. This game serves as a fun way to learn about event handling and graphics rendering in Python. Enjoy playing!

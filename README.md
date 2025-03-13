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

Special thanks to the Pygame community and documentation for providing the necessary resources and support in game development. This game serves as a fun way to learn about
event handling and graphics rendering in Python. Enjoy playing!

Usage
This project demonstrates various testing scenarios using different Python libraries. The main tests include:

Turtle path verification

Numpy calculation

Drawing shapes with Turtle

Plotting with Matplotlib

Drawing with Pygame

Tests
To run the tests, you can use pytest:

bash
pytest
Test 1: Turtle Path Verification
This test checks the sequence of turtle movements.

python
def test_turtle_path():
    t = turtle.Turtle()
    t.shape('turtle')
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    pos = t.position()
    expected = (50.0, 100.0)
    assert abs(pos[0] - expected[0]) < 1e-5 and abs(pos[1] - expected[1]) < 1e-5
    turtle.bye()
Test 2: Numpy Calculation
This test computes an expression using numpy.

python
def test_numpy_calculation():
    x = np.array([1, 10, 1000])
    result = (np.log((1 / np.exp(np.sin(x) + 1)) / ((5 / 4) + 1 / x  15))) / np.log(1 + x  2)
    assert result.shape == (3,)
    assert np.all(np.isfinite(result))
Test 3: Drawing a Square with Turtle
This test draws a square using turtle.

python
def test_turtle_square():
    t = turtle.Turtle()
    t.shape('turtle')
    t.forward(120)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(120)
    t.left(90)
    t.forward(120)
    pos = t.position()
    expected = (0.0, 0.0)
    assert abs(pos[0] - expected[0]) < 1e-5 and abs(pos[1] - expected[1]) < 1e-5
    turtle.bye()
Test 4: Matplotlib Plotting
This test checks the creation of a plot using matplotlib.

python
def test_matplotlib_plot():
    fig, ax = plt.subplots()
    x = np.linspace(-20, 20, 100)
    y = x * x - x - 6
    ax.plot(x, y)
    ax.set_title('y(x) = x*x - x - 6')
    assert ax.get_title() == 'y(x) = x*x - x - 6'
    lines = ax.get_lines()
    assert len(lines) == 1
    np.testing.assert_allclose(lines[0].get_ydata()[0], (-20)*(-20) - (-20) - 6)
    np.testing.assert_allclose(lines[0].get_ydata()[-1], (20)*(20) - (20) - 6)
    plt.close(fig)
Test 5: Drawing Nested Squares
This test draws nested squares using a custom draw_square function.

python
def test_draw_square_function():
    def draw_square(tur, x, y, size):
        tur.penup()
        tur.goto(x, y)
        tur.pendown()
        for n in range(4):
            tur.forward(size)
            tur.left(90)
    t = turtle.Turtle()
    t.speed(2)
    t.shape('turtle')
    size = 100
    step = 20
    start_x = -size // 2
    start_y = -size // 2
    for n in range(10):
        draw_square(t, start_x, start_y, size)
        size += step
        start_x = -size // 2
        start_y = -size // 2
    turtle.bye()
Test 6: Drawing Varying Sized Squares
This test draws multiple squares of varying sizes using turtle.

python
def test_turtle_nested_squares():
    a = 10
    t = turtle.Turtle()
    t.shape('turtle')
    x = 1
    for j in range(a):
        t.pendown()
        for i in range(4):
            t.forward(x * 10)
            t.right(90)
        t.penup()
        t.left(90)
        t.forward(10)
        t.right(90)
        t.backward(10)
        x += 2
    turtle.bye()
Test 7: Drawing Polygons
This test draws polygons with varying parameters using turtle.

python
def test_turtle_polygons():
    t = turtle.Turtle()
    t.shape('turtle')
    t.speed(3)
    polygon_angle = 3
    figure_length = 50
    x, y = 0, 0
    for n in range(10):
        for angle in range(polygon_angle):
            t.forward(figure_length)
            t.right(360 / polygon_angle)
        t.penup()
        x -= 2
        y += 10
        t.goto(x, y)
        t.pendown()
        polygon_angle += 1
        figure_length += 5
    turtle.bye()
Test 8: Drawing an Angry Smiley with Pygame
This test draws an angry smiley face using pygame.

python
def test_angry_smile_pygame():
    pygame.init()
    FPS = 30
    screen = pygame.display.set_mode((500, 500))
    rect(screen, (217, 217, 217), (0, 0, 500, 500))
    def angrysmile():
        circle(screen, (255, 255, 0), (250, 250), 100)
        circle(screen, (0, 0, 0), (250, 250), 100, 1)
        circle(screen, (255, 0, 0), (200, 235), 25)
        circle(screen, (0, 0, 0), (200, 235), 25, 1)
        circle(screen, (0, 0, 0), (200, 235), 10)
        polygon(screen, (0, 0, 0), [(230, 230), (235, 223), (152, 180), (147, 187)])
        aalines(screen, (0, 0, 0), True, [(230, 230), (235, 223), (152, 180), (147, 187)], 1000)
        circle(screen, (255, 0, 0), (300, 235), 15)
        circle(screen, (0, 0, 0), (300, 235), 15, 1)
        circle(screen, (0, 0, 0), (300, 235), 8)
        polygon(screen, (0, 0, 0), [(280, 230), (275, 223), (347, 190), (350, 197)])
        aalines(screen, (0, 0, 0), True, [(280, 230), (275, 223), (347, 190), (350, 197)], 1000)
        polygon(screen, (0, 0, 0), [(200, 310), (200, 290), (300, 290), (300, 310)])
    angrysmile()
    pygame.display.update()
    pygame.time.delay(100)
    pygame.quit()
Test 9: Drawing a Smiley with Turtle
This test draws a smiley face using turtle.

python
def test_turtle_smiley():
    t = turtle.Turtle()
    t.speed(5)
    t.up()
    t.goto(0, -100)
    t.down()
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(100)
    t.end_fill()
    t.color("red")
    t.up()
    t.goto(-67, -40)
    t.setheading(-60)
    t.width(5)
    t.down()
    t.circle(80, 120)
    t.color("black")
    t.up()
    t.goto(0, -20)
    t.setheading(-60)
    t.width(5)
    t.down()
    t.left(150)
    t.forward(30)
    t.fillcolor("blue")
    t.width(1)
    for i in range(-35, 105, 70):
        t.up()
        t.goto(i, 35)
        t.setheading(0)
        t.down()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
    turtle.bye()

from tkinter import *
import random

# Constants for game settings
GAME_WIDTH = 900
GAME_HEIGHT = 600
SPEED = 200  # Time in milliseconds between movements
SPACE_SIZE = 50  # Size of each snake segment and food
BODY_PARTS = 3  # Initial number of snake segments
SNAKE_COLOR = '#00FF00'
FOOD_COLOR = '#FF0000'
BACKGROUND_COLOR = '#000000'

# the Snake class below handles the creation and management of the snake
class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS  # Initial size of the snake
        self.coordinates = []  # List to store the coordinates of snake segments
        self.squares = []  # List to store the square objects for each segment

        # Initialize the snake's body
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])  # Starting coordinates (0,0)

        # Draw the snake on the canvas
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

# Food class handles the creation and management of the food
class Food:
    def __init__(self):
        # Randomly place the food within the game area
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        # Draw the food on the canvas
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

# Function to update the game state in each turn
def next_turn(snake, food):
    global direction

    # Get the current head position of the snake
    x, y = snake.coordinates[0]

    # Update the head position based on the current direction
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    # Insert new head coordinates at the beginning of the snake's body
    snake.coordinates.insert(0, [x, y])

    # Create a new rectangle for the new head position
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Check if the snake has eaten the food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1

        # Update the score display
        label.config(text="Score:{}".format(score))

        # Remove the old food and create new food
        canvas.delete("food")
        food = Food()
    else:
        # Remove the last segment of the snake's body
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Check for collisions with the walls or itself
    if check_collisions(snake):
        game_over()  # End the game if a collision is detected
    else:
        # Schedule the next turn
        window.after(SPEED, next_turn, snake, food)

# Function to change the direction of the snake
def change_direction(new_direction):
    global direction

    # Prevent the snake from reversing
    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

# Function to check for collisions
def check_collisions(snake):
    x, y = snake.coordinates[0]

    # Check if the snake collides with the walls
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    # Check if the snake collides with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

# Function to handle game over
def game_over():
    # Clear the canvas and display the game over message
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                       font=('consolas', 70), text="GAME OVER!", fill="red", tag="game over")

# Function to initialize the game
def initialize_game():
    global snake, food

    # Center the game window on the screen
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Bind arrow keys to change the snake's direction
    window.bind('<Left>', lambda event: change_direction('left'))
    window.bind('<Right>', lambda event: change_direction('right'))
    window.bind('<Up>', lambda event: change_direction('up'))
    window.bind('<Down>', lambda event: change_direction('down'))

    # Initialize the snake and food
    snake = Snake()
    food = Food()

    # Start the first turn
    next_turn(snake, food)

# Main setup for the Tkinter window
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

# Initialize score and direction
score = 0
direction = 'down'

# Create and pack the score label
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

# Create and pack the game canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Update the window to get its dimensions
window.update()

# Delay the initialization to ensure the window is fully created
window.after(100, initialize_game)

# Start the Tkinter main loop
window.mainloop()

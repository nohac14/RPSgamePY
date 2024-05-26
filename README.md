# Rock, Paper, Scissors Game

This project is a simple Rock, Paper, Scissors game implemented in Python. It consists of two separate scripts: `RPSgame.py` for a console-based version of the game and `RPSapp.py` for a graphical user interface (GUI) version using Tkinter.

## Project Structure

- **RPSgame.py**: This script allows you to play the Rock, Paper, Scissors game in the console.
- **RPSapp.py**: This script provides a graphical user interface (GUI) for playing the Rock, Paper, Scissors game.

## Console Version (RPSgame.py)

The console version is responsible for:

- Generating random choices for the CPU.
- Prompting the player for their choice.
- Determining the winner of each round.
- Updating and displaying game statistics.

### Key Functions

- **clear**: Clears the console.
- **choiceCPU**: Generates and displays a random choice for the CPU.
- **choicePlayer**: Prompts the player for their choice and displays it.
- **fight**: Determines the winner of the current round and updates statistics.
- **updateStats**: Updates the game statistics using the choices and outcome of the current round.

### How to Run

To play the console version of the game, run the following command in your terminal:
```bash
python RPSgame.py
```

## GUI Version (RPSapp.py)

The GUI version provides a graphical user interface for playing the Rock, Paper, Scissors game. It includes buttons for selecting Rock, Paper, or Scissors, and displays the result of each round.

### Key Components

- **createButton**: Creates a button with specified text and command.
- **choiceCPU**: Generates a random choice for the CPU.
- **fight**: Determines the winner of the current round.
- **play**: Handles the player's choice and updates the game statistics.
- **update_stats_text**: Updates the game statistics displayed in the window.
- **on_closing**: Handles the window closing event.

### How to Run

To play the GUI version of the game, run the following command in your terminal:
```bash
python RPSapp.py
```

## Example Usage

### Console Version

- Run the `RPSgame.py` script.
- Choose Rock (1), Paper (2), or Scissors (3) when prompted.
- The CPU's choice and the result of the round will be displayed.
- Choose whether to play again or not.
- The final game statistics will be displayed when you exit the game.

### GUI Version

- Run the `RPSapp.py` script.
- Click on the Rock, Paper, or Scissors button to make your choice.
- The CPU's choice and the result of the round will be displayed in the GUI.
- The game statistics will be updated and displayed in the text widget.

## Acknowledgements

- Tkinter for providing the GUI framework.

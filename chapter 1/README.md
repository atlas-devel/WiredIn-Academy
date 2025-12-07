# Rock — Paper — Scissors (CLI)

A simple command-line Rock–Paper–Scissors game implemented in Python.  
Part of the Python learning program from WiredIn Academy in collaboration with TechGym (Japan).

## Overview
- Play up to 3 scored rounds against the computer.
- Valid choices: 0 = rock ✊, 1 = paper 🖐, 2 = scissor ✌️.
- Draws do not count toward the 3-round attempt limit (the round is replayed).
- Final winner determined by the higher score after attempts finish.

## Requirements
- Python 3.6+

## Usage
1. Save the game code to a file, e.g. `rps.py`.
2. Run:
    ```
    python rps.py
    ```
3. Follow the on-screen prompts to enter 0, 1, or 2.

## Example session
```
start ‘rock-paper-scissors’

input your hand choice
0.rock ✊ 1.paper 🖐 2.scissor ✌️
> 0
My hand is rock
Computer's hand is scissor
you win

... (repeats up to 3 scored rounds)

game over
the winner is player scored 2
```

## Code structure
- `results` — mapping of result keywords to messages.
- `play_choice` — mapping of numeric choices to names.
- `score` — tracks `player` and `computer`.
- `play()` — main function that:
  - prompts user input,
  - generates computer choice,
  - compares hands,
  - updates scores,
  - prints round and final results.

## Learning goals
- Practice with: input handling, control flow, functions and nested functions, basic game logic, simple state management (scores).
- Understand simple CLI program structure.



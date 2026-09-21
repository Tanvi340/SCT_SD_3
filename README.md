# Sudoku Game & Solver

An interactive Sudoku game and automatic puzzle solver developed using Python and Tkinter.

This project allows users to play both Mini Sudoku and Classic Sudoku through a graphical user interface. It also includes an automatic solving feature based on the backtracking algorithm.

---

## Task Information

**Internship:** SkillCraft Technology Internship  
**Task:** Task 3 – Sudoku Solver  
**Language:** Python  
**GUI Framework:** Tkinter  
**Algorithm:** Backtracking  

---

## Project Overview

The objective of this task is to create a program that can automatically solve Sudoku puzzles.

The application takes an unsolved Sudoku puzzle, validates the possible numbers, and uses a backtracking algorithm to fill the empty cells with a valid solution.

In addition to the automatic solver, this project provides an interactive graphical interface where users can manually play Sudoku, check their answers, request hints, reset the puzzle, or solve it automatically.

---

## Features

- Interactive graphical Sudoku interface
- 3 × 3 Mini Sudoku mode
- 9 × 9 Classic Sudoku mode
- Easy, Medium, and Hard difficulty levels for 9 × 9 Sudoku
- Automatically generated Sudoku puzzles
- Automatic puzzle solving
- Backtracking algorithm
- Check solution functionality
- Hint functionality
- Reset puzzle functionality
- New Game option
- Number pad for entering values
- Direct keyboard input
- Selected-cell highlighting
- Visual distinction between fixed and user-entered numbers
- Sudoku 3 × 3 block highlighting
- User-friendly status messages

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Graphical User Interface |
| Random | Puzzle generation and randomization |
| Backtracking | Sudoku solving algorithm |

No external Python packages are required.

---

## How the Application Works

The application starts with a main menu where the user can select between:

1. Mini Sudoku
2. Classic Sudoku

### Mini Sudoku

The 3 × 3 mode uses numbers from 1 to 3.

Each number must appear only once in every row and column.

### Classic Sudoku

The 9 × 9 mode follows standard Sudoku rules.

The numbers 1 to 9 must appear exactly once in:

- Each row
- Each column
- Each 3 × 3 sub-grid

---

## Sudoku Solving Algorithm

The application uses the **Backtracking Algorithm** to solve Sudoku puzzles.

Backtracking is a recursive trial-and-error algorithm.

The basic process is:

1. Find an empty cell.
2. Try a possible number.
3. Check whether the number is valid.
4. If the number is valid, place it in the cell.
5. Move to the next empty cell.
6. If no valid number can be placed, go back to the previous cell.
7. Try another number.
8. Continue until the puzzle is solved.

### Algorithm Flow

```text
Start
  ↓
Find an empty cell
  ↓
Try a number
  ↓
Is the number valid?
  ↓
 ┌───────────────┐
 │               │
Yes              No
 │               │
 ↓               ↓
Place number    Try next number
 │
 ↓
Solve remaining puzzle
 │
 ├── Solved → Finish
 │
 └── Not solved
        ↓
   Backtrack
        ↓
   Try another number

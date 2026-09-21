import tkinter as tk
from tkinter import messagebox
import random


class SudokuGame:
    def __init__(self, root):
        self.root = root

        self.root.title("Sudoku Master")
        self.root.geometry("900x800")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.size = 9
        self.difficulty = "Easy"

        self.board = []
        self.solution = []
        self.original_board = []

        self.cells = []
        self.selected_cell = None

        self.status_label = None
        self.grid_frame = None
        self.number_pad = None

        self.show_home_screen()

    
    # GENERAL UI
    

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.cells = []
        self.selected_cell = None

    def create_title(self, parent, text, size=30):
        label = tk.Label(
            parent,
            text=text,
            font=("Segoe UI", size, "bold"),
            bg="#1e1e2e",
            fg="#ffffff"
        )
        label.pack(pady=(20, 5))

        return label

    # ============================================================
    # HOME SCREEN
    # ============================================================

    def show_home_screen(self):
        self.clear_window()

        container = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )
        container.pack(expand=True)

        self.create_title(
            container,
            "SUDOKU MASTER",
            34
        )

        subtitle = tk.Label(
            container,
            text="Choose your Sudoku mode",
            font=("Segoe UI", 14),
            bg="#1e1e2e",
            fg="#a6adc8"
        )
        subtitle.pack(pady=(0, 35))

        mini_button = tk.Button(
            container,
            text="3 × 3  MINI SUDOKU",
            command=lambda: self.start_game(3),
            font=("Segoe UI", 15, "bold"),
            bg="#89b4fa",
            fg="#11111b",
            activebackground="#74c7ec",
            activeforeground="#11111b",
            width=24,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        mini_button.pack(pady=10)

        classic_button = tk.Button(
            container,
            text="9 × 9  CLASSIC SUDOKU",
            command=self.show_difficulty_screen,
            font=("Segoe UI", 15, "bold"),
            bg="#a6e3a1",
            fg="#11111b",
            activebackground="#94e2d5",
            activeforeground="#11111b",
            width=24,
            height=2,
            relief="flat",
            cursor="hand2"
        )
        classic_button.pack(pady=10)

        info = tk.Label(
            container,
            text="Solve puzzles using logic, hints or the automatic solver.",
            font=("Segoe UI", 10),
            bg="#1e1e2e",
            fg="#7f849c"
        )
        info.pack(pady=35)

    
    # DIFFICULTY SCREEN
    

    def show_difficulty_screen(self):
        self.clear_window()

        container = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )
        container.pack(expand=True)

        self.create_title(
            container,
            "9 × 9 CLASSIC SUDOKU",
            30
        )

        subtitle = tk.Label(
            container,
            text="Select difficulty",
            font=("Segoe UI", 14),
            bg="#1e1e2e",
            fg="#a6adc8"
        )
        subtitle.pack(pady=(0, 25))

        difficulties = [
            ("EASY", "Easy", "#a6e3a1"),
            ("MEDIUM", "Medium", "#f9e2af"),
            ("HARD", "Hard", "#f38ba8")
        ]

        for text, difficulty, color in difficulties:
            button = tk.Button(
                container,
                text=text,
                command=lambda d=difficulty: self.start_game(9, d),
                font=("Segoe UI", 14, "bold"),
                bg=color,
                fg="#11111b",
                activebackground=color,
                width=22,
                height=2,
                relief="flat",
                cursor="hand2"
            )
            button.pack(pady=8)

        back_button = tk.Button(
            container,
            text="BACK",
            command=self.show_home_screen,
            font=("Segoe UI", 11, "bold"),
            bg="#313244",
            fg="#cdd6f4",
            activebackground="#45475a",
            activeforeground="#ffffff",
            width=12,
            relief="flat",
            cursor="hand2"
        )
        back_button.pack(pady=25)

    
    # START GAME
    
    def start_game(self, size, difficulty="Easy"):
        self.size = size
        self.difficulty = difficulty

        self.generate_puzzle()

        self.show_game_screen()

    # ============================================================
    # SUDOKU GENERATION
    # ============================================================

    def generate_puzzle(self):

        # Create empty board
        self.solution = [
            [0 for _ in range(self.size)]
            for _ in range(self.size)
        ]

        # Generate a valid completed Sudoku
        self.fill_board(self.solution)

        # Copy solution
        self.board = [
            row[:] for row in self.solution
        ]

        # Remove numbers
        if self.size == 3:
            cells_to_remove = 4

        else:
            if self.difficulty == "Easy":
                cells_to_remove = 38

            elif self.difficulty == "Medium":
                cells_to_remove = 48

            else:
                cells_to_remove = 55

        positions = [
            (r, c)
            for r in range(self.size)
            for c in range(self.size)
        ]

        random.shuffle(positions)

        for r, c in positions[:cells_to_remove]:
            self.board[r][c] = 0

        self.original_board = [
            row[:] for row in self.board
        ]

    def fill_board(self, board):

        empty = self.find_empty(board)

        if empty is None:
            return True

        row, col = empty

        numbers = list(range(1, self.size + 1))
        random.shuffle(numbers)

        for number in numbers:

            if self.is_valid(
                board,
                row,
                col,
                number
            ):
                board[row][col] = number

                if self.fill_board(board):
                    return True

                board[row][col] = 0

        return False

    # ============================================================
    # SUDOKU SOLVER
    # ============================================================

    def solve_board(self, board):

        empty = self.find_empty(board)

        if empty is None:
            return True

        row, col = empty

        for number in range(1, self.size + 1):

            if self.is_valid(
                board,
                row,
                col,
                number
            ):

                board[row][col] = number

                if self.solve_board(board):
                    return True

                board[row][col] = 0

        return False

    def find_empty(self, board):

        for row in range(self.size):

            for col in range(self.size):

                if board[row][col] == 0:
                    return row, col

        return None

    def is_valid(
        self,
        board,
        row,
        col,
        number
    ):

        # Check row
        for c in range(self.size):

            if board[row][c] == number:
                return False

        # Check column
        for r in range(self.size):

            if board[r][col] == number:
                return False

        # 9 × 9 Sudoku has 3 × 3 blocks
        if self.size == 9:

            start_row = (row // 3) * 3
            start_col = (col // 3) * 3

            for r in range(start_row, start_row + 3):

                for c in range(start_col, start_col + 3):

                    if board[r][c] == number:
                        return False

        return True

    # ============================================================
    # GAME SCREEN
    # ============================================================

    def show_game_screen(self):

        self.clear_window()

        # ---------------- HEADER ----------------

        header = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )
        header.pack(fill="x", pady=(10, 5))

        title = tk.Label(
            header,
            text=(
                "MINI SUDOKU"
                if self.size == 3
                else f"CLASSIC SUDOKU  •  {self.difficulty.upper()}"
            ),
            font=("Segoe UI", 24, "bold"),
            bg="#1e1e2e",
            fg="#ffffff"
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text="Fill the empty cells with the correct numbers",
            font=("Segoe UI", 10),
            bg="#1e1e2e",
            fg="#a6adc8"
        )
        subtitle.pack()

        # ---------------- GRID ----------------

        self.grid_frame = tk.Frame(
            self.root,
            bg="#11111b",
            padx=4,
            pady=4
        )
        self.grid_frame.pack(pady=15)

        self.create_grid()

        # ---------------- STATUS ----------------

        self.status_label = tk.Label(
            self.root,
            text="Select a cell and enter a number.",
            font=("Segoe UI", 11, "bold"),
            bg="#1e1e2e",
            fg="#89b4fa"
        )
        self.status_label.pack(pady=5)

        # ---------------- NUMBER PAD ----------------

        self.create_number_pad()

        # ---------------- CONTROL BUTTONS ----------------

        controls = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )
        controls.pack(pady=12)

        self.create_control_button(
            controls,
            "CHECK",
            self.check_puzzle,
            "#89b4fa"
        )

        self.create_control_button(
            controls,
            "HINT",
            self.give_hint,
            "#f9e2af"
        )

        self.create_control_button(
            controls,
            "SOLVE",
            self.solve_game,
            "#a6e3a1"
        )

        self.create_control_button(
            controls,
            "RESET",
            self.reset_game,
            "#f38ba8"
        )

        self.create_control_button(
            controls,
            "NEW GAME",
            self.new_game,
            "#cba6f7"
        )

        self.create_control_button(
            controls,
            "MENU",
            self.show_home_screen,
            "#313244"
        )

    
    # GRID CREATION
    

    def create_grid(self):

        for row in range(self.size):

            row_cells = []

            for col in range(self.size):

                value = self.board[row][col]

                cell = tk.Entry(
                    self.grid_frame,
                    width=2,
                    font=(
                        "Segoe UI",
                        18 if self.size == 9 else 24,
                        "bold"
                    ),
                    justify="center",
                    bg="#313244",
                    fg="#ffffff",
                    insertbackground="#ffffff",
                    relief="flat"
                )

                # Insert existing number
                if value != 0:
                    cell.insert(0, str(value))

                    cell.config(
                        state="readonly",
                        readonlybackground="#45475a",
                        fg="#89b4fa"
                    )

                else:
                    cell.config(
                        bg="#ffffff",
                        fg="#11111b"
                    )

                # Create borders
                border_color = "#11111b"

                if self.size == 9:

                    top = 3 if row % 3 == 0 else 1
                    left = 3 if col % 3 == 0 else 1
                    bottom = 3 if row == 8 or row % 3 == 2 else 1
                    right = 3 if col == 8 or col % 3 == 2 else 1

                else:

                    top = 2
                    left = 2
                    bottom = 2
                    right = 2

                cell.config(
                    highlightthickness=0,
                    bd=0
                )

                cell.grid(
                    row=row,
                    column=col,
                    padx=(left, right),
                    pady=(top, bottom),
                    ipadx=7,
                    ipady=7
                )

                # Select cell
                cell.bind(
                    "<FocusIn>",
                    lambda event, r=row, c=col:
                    self.select_cell(r, c)
                )

                cell.bind(
                    "<Button-1>",
                    lambda event, r=row, c=col:
                    self.select_cell(r, c)
                )

                # Keyboard input
                cell.bind(
                    "<KeyRelease>",
                    lambda event, r=row, c=col:
                    self.update_cell(r, c)
                )

                row_cells.append(cell)

            self.cells.append(row_cells)

    
    # CELL SELECTION
    

    def select_cell(self, row, col):

        self.selected_cell = (row, col)

        # Highlight selected cell
        for r in range(self.size):

            for c in range(self.size):

                cell = self.cells[r][c]

                if self.original_board[r][c] != 0:

                    cell.config(
                        readonlybackground="#45475a"
                    )

                else:

                    cell.config(
                        bg="#ffffff"
                    )

        selected = self.cells[row][col]

        if self.original_board[row][col] == 0:

            selected.config(
                bg="#cdd6f4"
            )

        self.status_label.config(
            text=f"Selected cell: Row {row + 1}, Column {col + 1}",
            fg="#89b4fa"
        )

    
    # CELL INPUT
    

    def update_cell(self, row, col):

        cell = self.cells[row][col]

        value = cell.get().strip()

        if value == "":
            self.board[row][col] = 0
            return

        try:

            number = int(value)

            if 1 <= number <= self.size:

                self.board[row][col] = number

            else:

                cell.delete(0, tk.END)
                self.board[row][col] = 0

        except ValueError:

            cell.delete(0, tk.END)
            self.board[row][col] = 0

    
    # NUMBER PAD
    

    def create_number_pad(self):

        self.number_pad = tk.Frame(
            self.root,
            bg="#1e1e2e"
        )
        self.number_pad.pack(pady=5)

        for number in range(1, self.size + 1):

            button = tk.Button(
                self.number_pad,
                text=str(number),
                command=lambda n=number:
                self.enter_number(n),
                font=("Segoe UI", 11, "bold"),
                width=3,
                height=1,
                bg="#313244",
                fg="#cdd6f4",
                activebackground="#45475a",
                activeforeground="#ffffff",
                relief="flat",
                cursor="hand2"
            )

            button.grid(
                row=0,
                column=number - 1,
                padx=2
            )

        clear_button = tk.Button(
            self.number_pad,
            text="Clear",
            command=self.clear_selected_cell,
            font=("Segoe UI", 10, "bold"),
            bg="#585b70",
            fg="#ffffff",
            activebackground="#6c7086",
            relief="flat",
            cursor="hand2"
        )

        clear_button.grid(
            row=0,
            column=self.size,
            padx=(8, 2)
        )

    def enter_number(self, number):

        if self.selected_cell is None:
            return

        row, col = self.selected_cell

        if self.original_board[row][col] != 0:
            return

        cell = self.cells[row][col]

        cell.delete(0, tk.END)
        cell.insert(0, str(number))

        self.board[row][col] = number

    def clear_selected_cell(self):

        if self.selected_cell is None:
            return

        row, col = self.selected_cell

        if self.original_board[row][col] != 0:
            return

        cell = self.cells[row][col]

        cell.delete(0, tk.END)

        self.board[row][col] = 0

   
    # CHECK PUZZLE
    
    def check_puzzle(self):

        self.update_board_from_gui()

        # Check empty cells
        for row in range(self.size):

            for col in range(self.size):

                if self.board[row][col] == 0:

                    self.status_label.config(
                        text="Puzzle is incomplete. Fill all cells.",
                        fg="#f9e2af"
                    )

                    return

        # Check solution
        if self.board == self.solution:

            self.status_label.config(
                text="Congratulations! Puzzle solved correctly.",
                fg="#a6e3a1"
            )

            messagebox.showinfo(
                "Sudoku Complete",
                "Congratulations!\nYou solved the Sudoku correctly!"
            )

        else:

            self.status_label.config(
                text="Some numbers are incorrect. Keep trying.",
                fg="#f38ba8"
            )

    
    # UPDATE BOARD
    
    def update_board_from_gui(self):

        for row in range(self.size):

            for col in range(self.size):

                cell = self.cells[row][col]

                value = cell.get().strip()

                if value == "":
                    self.board[row][col] = 0

                else:

                    try:
                        self.board[row][col] = int(value)

                    except ValueError:
                        self.board[row][col] = 0

    
    # HINT
    

    def give_hint(self):

        empty_cells = []

        for row in range(self.size):

            for col in range(self.size):

                if (
                    self.original_board[row][col] == 0
                    and self.board[row][col] != self.solution[row][col]
                ):
                    empty_cells.append((row, col))

        if not empty_cells:

            self.status_label.config(
                text="No hints needed. The puzzle is complete!",
                fg="#a6e3a1"
            )

            return

        row, col = random.choice(empty_cells)

        self.board[row][col] = self.solution[row][col]

        cell = self.cells[row][col]

        cell.delete(0, tk.END)
        cell.insert(0, str(self.solution[row][col]))

        cell.config(
            fg="#40a02b"
        )

        self.status_label.config(
            text=f"Hint added at Row {row + 1}, Column {col + 1}.",
            fg="#a6e3a1"
        )

    
    # SOLVE GAME
    
    def solve_game(self):

        self.board = [
            row[:] for row in self.solution
        ]

        for row in range(self.size):

            for col in range(self.size):

                cell = self.cells[row][col]

                cell.config(
                    state="normal"
                )

                cell.delete(0, tk.END)

                cell.insert(
                    0,
                    str(self.solution[row][col])
                )

                if self.original_board[row][col] != 0:

                    cell.config(
                        state="readonly",
                        readonlybackground="#45475a",
                        fg="#89b4fa"
                    )

                else:

                    cell.config(
                        fg="#a6e3a1"
                    )

        self.status_label.config(
            text="Puzzle solved automatically using backtracking.",
            fg="#a6e3a1"
        )

   
    # RESET GAME
    
    def reset_game(self):

        self.board = [
            row[:] for row in self.original_board
        ]

        for row in range(self.size):

            for col in range(self.size):

                cell = self.cells[row][col]

                # Original cells
                if self.original_board[row][col] != 0:

                    cell.config(
                        state="readonly",
                        readonlybackground="#45475a",
                        fg="#89b4fa"
                    )

                    cell.delete(0, tk.END)

                    cell.insert(
                        0,
                        str(self.original_board[row][col])
                    )

                # Empty cells
                else:

                    cell.config(
                        state="normal",
                        bg="#ffffff",
                        fg="#11111b"
                    )

                    cell.delete(0, tk.END)

        self.status_label.config(
            text="Puzzle reset to its original state.",
            fg="#89b4fa"
        )

    
    # NEW GAME
    

    def new_game(self):

        self.generate_puzzle()
        self.show_game_screen()

    # CONTROL BUTTON
    
    def create_control_button(
        self,
        parent,
        text,
        command,
        color
    ):

        button = tk.Button(
            parent,
            text=text,
            command=command,
            font=("Segoe UI", 10, "bold"),
            bg=color,
            fg="#11111b",
            activebackground=color,
            activeforeground="#11111b",
            width=10,
            height=1,
            relief="flat",
            cursor="hand2"
        )

        button.pack(
            side="left",
            padx=4
        )



# MAIN PROGRAM


if __name__ == "__main__":

    root = tk.Tk()

    app = SudokuGame(root)

    root.mainloop()
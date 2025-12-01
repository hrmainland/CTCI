from random import randrange
from enum import Enum


class GameState(Enum):
    DISPLAY = 1
    INPUT = 2
    WIN = 3
    LOSE = 4


class BoardState(Enum):
    PLAY = 1
    WIN = 2
    LOSE = 3


class Game:
    def __init__(self, width, n_bombs):
        self.board = Board(width, n_bombs)
        self.state = GameState.DISPLAY

    def play(self):
        while True:
            if self.state == GameState.INPUT:
                row, col = input("Enter row,col: ").split(",")
                is_flag = False
                if row[0] == "f":
                    is_flag = True
                    row = row[1:]
                row, col = int(row), int(col)
                if is_flag:
                    self.board.toggle_flag(row, col)
                else:
                    self.board.uncover(row, col)
                if self.board.state == BoardState.WIN:
                    self.state = GameState.WIN
                elif self.board.state == BoardState.LOSE:
                    self.state = GameState.LOSE
                else:
                    self.state = GameState.DISPLAY
            else:
                self.board.print_board()
                if self.state == GameState.WIN:
                    print("Congratulations you win :)")
                    break
                if self.state == GameState.LOSE:
                    print("You lost :(")
                    break
                self.state = GameState.INPUT


class Board:

    all_vectors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    vectors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def print_board(self):
        print("   ", *[" " + str(i) + " " for i in range(self.width)])
        print("   " + "-" * 4 * self.width)
        i = 0
        for row in self.grid:
            print(
                ("" if i > 9 else " ") + str(i),
                *[" " + str(elem) for elem in row],
                "",
                sep=" |",
            )
            print("   " + "-" * (4 * self.width + 1))
            i += 1

    def count_adj_bombs(self, srow, scol):
        count = 0
        for drow, dcol in self.all_vectors:
            nrow, ncol = srow + drow, scol + dcol
            if (
                0 <= nrow < self.width
                and 0 <= ncol < self.width
                and isinstance(self.grid[nrow][ncol], Bomb)
            ):
                count += 1
        return count

    def __init__(self, width, n_bombs):
        self.width = width
        self.n_bombs = n_bombs
        self.grid = [[None] * self.width for _ in range(self.width)]
        self.state = BoardState.PLAY
        self.uncovered_set = set()
        bomb_coords = set()
        while len(bomb_coords) < n_bombs:
            bomb_coords.add(
                (randrange(0, self.width - 1), randrange(0, self.width - 1))
            )
        for row, col in bomb_coords:
            self.grid[row][col] = Bomb(row, col)
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if not isinstance(self.grid[row][col], Bomb):
                    n_adjs = self.count_adj_bombs(row, col)
                    if n_adjs > 0:
                        self.grid[row][col] = Digit(row, col, n_adjs)
                    else:
                        self.grid[row][col] = Blank(row, col)

    def blank_dfs(self, row, col, visited, from_digit=False):
        visited.add((row, col))
        this_result = [(row, col)]
        if from_digit:
            return this_result
        for drow, dcol in self.vectors:
            nrow, ncol = row + drow, col + dcol
            if (
                0 <= nrow < self.width
                and 0 <= ncol < self.width
                and not isinstance(self.grid[nrow][ncol], Bomb)
                and (nrow, ncol) not in visited
            ):
                from_digit = isinstance(self.grid[row][col], Digit)
                this_result.extend(self.blank_dfs(nrow, ncol, visited, from_digit))
        return this_result

    def uncover(self, row, col):
        if self.grid[row][col].is_flagged:
            print("Flagged!")
            return
        if not isinstance(self.grid[row][col], Blank):
            self.grid[row][col].uncover()
            if isinstance(self.grid[row][col], Bomb):
                self.state = BoardState.LOSE
                return
            self.uncovered_set.add((row, col))
        else:
            visited = set()
            blanks = self.blank_dfs(row, col, visited)
            for row, col in blanks:
                self.grid[row][col].uncover()
            self.uncovered_set = self.uncovered_set.union(set(blanks))
        if len(self.uncovered_set) == self.width**2 - self.n_bombs:
            self.state = BoardState.WIN

    def toggle_flag(self, row, col):
        if self.grid[row][col].is_covered:
            self.grid[row][col].is_flagged = not self.grid[row][col].is_flagged


class Cell:
    def __init__(self, row, col, is_covered=True, is_flagged=False):
        self.row = row
        self.col = col
        self.is_covered = is_covered
        self.is_flagged = is_flagged

    def __str__(self):
        # return None
        if self.is_covered:
            if self.is_flagged:
                return "⚐"
            return "-"

    def uncover(self):
        self.is_covered = False
        self.is_flagged = False


class Bomb(Cell):
    def __str__(self):
        parent_str = super().__str__()
        if parent_str:
            return parent_str
        return "☢️"

    def explode(self):
        print("boom")


class Digit(Cell):

    def __init__(self, row, col, number, is_covered=True, is_flagged=False):
        super().__init__(row, col, is_covered, is_flagged)
        self.number = number

    def __str__(self):
        parent_str = super().__str__()
        if parent_str:
            return parent_str
        return str(self.number)

    def show():
        print("number")


class Blank(Cell):

    def __str__(self):
        parent_str = super().__str__()
        if parent_str:
            return parent_str
        return " "


game = Game(4, 2)
game.play()

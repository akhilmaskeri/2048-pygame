from random import randint, choices

class Board():
    def __init__(self, row_size:int, col_size:int):

        self.row_size = row_size
        self.col_size = col_size
        self._max_text_length = 1

        self.board = [[0 for _ in range(col_size)] for _ in range(row_size)]

    def possible_move_condition(self):
        return any([
            self.left(dry_run=True),
            self.right(dry_run=True),
            self.up(dry_run=True),
            self.down(dry_run=True)
        ])
    
    def _update_max_text_length(self, number):
        self._max_text_length = max(
            self._max_text_length, 
            len(str(number))
        )


    def generate(self):

        rand_number = (1+randint(0, 1))*2
        options = []

        for i in range(self.row_size):
            for j in range(self.col_size):
                if self.board[i][j] == 0:
                    options.append((i,j))

        if not options:
            return False

        rand_row, rand_col = choices(options, k=1)[0]
        self.board[rand_row][rand_col] = rand_number

        return True


    def move_sideways(self, row, col, ptr, operation, dry_run=False):

        if self.board[row][col] == 0:
            return ptr, False

        if self.board[row][ptr] == 0:
            if not dry_run:
                self.board[row][ptr] = self.board[row][col]
                self.board[row][col] = 0
            return ptr, True

        if self.board[row][ptr] == self.board[row][col]:
            if not dry_run:
                self.board[row][ptr] *= 2
                self.board[row][col] = 0
                self._update_max_text_length(self.board[row][ptr])

            return ptr+1*operation, True
        
        if ptr+1*operation != col and 0 <= ptr+1*operation < self.col_size:
            if not dry_run:
                self.board[row][ptr+1*operation] = self.board[row][col]
                self.board[row][col] = 0
            return ptr+1*operation, True
        
        return ptr+1*operation, False


    def move_topbottom(self, row, col, ptr, operation, dry_run=False):
        
        if self.board[row][col] == 0:
            return ptr, False

        if self.board[ptr][col] == 0:
            if not dry_run:
                self.board[ptr][col] = self.board[row][col]
                self.board[row][col] = 0
            return ptr, True
        
        if self.board[ptr][col] == self.board[row][col]:
            if not dry_run:
                self.board[ptr][col] *= 2
                self.board[row][col] = 0
                self._update_max_text_length(self.board[row][ptr])

            return ptr+1*operation, True

        if ptr+1*operation != row and 0 <= ptr+1*operation < self.row_size:
            if not dry_run:
                self.board[ptr+1*operation][col] = self.board[row][col]
                self.board[row][col] = 0
            return ptr+1*operation, True
        
        return ptr+1*operation, False

    
    def left(self, dry_run=False):
        board_moved = False
        for row in range(self.row_size):
            ptr = 0
            for col in range(1, self.col_size):
                ptr, moved = self.move_sideways(row, col, ptr, operation=1, dry_run=dry_run)
                board_moved = board_moved or moved
        return board_moved

    def right(self, dry_run=False):
        board_moved = False
        for row in range(self.row_size):
            ptr = self.col_size-1
            for col in range(ptr-1, -1, -1):
                ptr, moved = self.move_sideways(row, col, ptr, operation=-1, dry_run=dry_run)
                board_moved = board_moved or moved
        return board_moved

    def up(self, dry_run=False):
        board_moved = False
        for col in range(self.col_size):
            ptr = 0
            for row in range(1, self.row_size):
                ptr, moved = self.move_topbottom(row, col, ptr, operation=1, dry_run=dry_run)
                board_moved = board_moved or moved
        return board_moved

    def down(self, dry_run=False):
        board_moved = False
        for col in range(self.col_size):
            ptr = self.row_size-1
            for row in range(ptr-1, -1, -1):
                ptr, moved = self.move_topbottom(row, col, ptr, operation=-1, dry_run=dry_run)
                board_moved = board_moved or moved
        return board_moved

    
    def __repr__(self) -> str: 

        result = []
        
        for i in range(self.row_size):
            row = []
            
            for j in range(self.col_size):
                x = self.board[i][j]
                row.append(f"{ x if x > 0 else '_'*self._max_text_length : ^{self._max_text_length}}")
            
            result.append(" ".join(row))
        return "\n".join(result)

    @staticmethod
    def parse(board_str:str):

        rows = board_str.split("\n")
        R = []
        for row in rows:

            C = []
            cols = row.split(" ")

            for c in cols:
                C.append(int(c) if c != "_" else 0)

            R.append(C)
        
        b = Board(len(R), len(R[0]))
        b.board = R
        return b

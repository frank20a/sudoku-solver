class Sudoku:
    def __init__(self, loadfile=None):
        self.board = [[list(range(1, 10)) for j in range(9)] for i in range(9)]
        self.solved = False

        if loadfile:
            self.pending_extention = []
            with open(loadfile, 'r', encoding='utf-8') as file:
                for i, row in enumerate(file.readlines()):
                    for j, cell in enumerate(row.split()):
                        if cell != '0':
                            self.board[i][j] = [int(cell)]
                            self.pending_extention.append((i, j))

    def extend_rules(self, x, y):
        if len(self.board[x][y]) == 1: num = self.board[x][y][0]
        else: return False

        # Extend to row
        for i in range(9):
            if i != y:
                try:
                    self.board[x][i].remove(num)
                    if len(self.board[x][i]) == 1: self.pending_extention.append((x, i))
                except ValueError:
                    pass

        # Extend to column
        for i in range(9):
            if i != x:
                try:
                    self.board[i][y].remove(num)
                    if len(self.board[i][y]) == 1: self.pending_extention.append((i, y))
                except ValueError:
                    pass

        # Extend to block
        blockx = x//3; blocky = y//3
        for i in range(3):
            for j in range(3):
                if not (3*blockx + i == x and 3*blocky + j == y):
                    try:
                        self.board[3*blockx + i][3*blocky + j].remove(num)
                        if len(self.board[3*blockx + i][3*blocky + j]) == 1: self.pending_extention.append((3*blockx + i, 3*blocky + j))
                    except ValueError:
                        pass

    def step(self):
        if len(self.pending_extention) > 0:
            x, y = self.pending_extention.pop(0)
            self.extend_rules(x, y)
            return 'Propagating Rules from ' + str(x+1) + ',' + str(y+1)



    def solve(self):
        while not self.solved:
            if self.step() is None: break

    def get_row(self, x=0, y=None):
        return self.board[x]

    def get_column(self, x=None, y=0):
        return [self.board[i][y] for i in range(9)]

    def print_lens(self):
        for row in self.board:
            for cell in row:
                print(len(cell), end='  ')
            print()

    def __str__(self):
        res = ''
        for row in self.board:
            for cell in row:
                try:
                    if len(cell) > 1: res += '0  '
                    else: res += str(cell[0]) + '  '
                except IndexError:
                    print(cell)
            res += '\n'
        return res

if __name__ == "__main__":
    S = Sudoku('hard1.txt')
    while True:
        print(S)
        input()
        S.step()


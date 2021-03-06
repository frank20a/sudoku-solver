from copy import deepcopy as copy


def count(f, l):
    res = 0
    for sub in l:
        if f in sub: res += 1
    return res


def get_least_branching(l):
    temp = {}
    for i, row in enumerate(l):
        for j, cell in enumerate(row):
            if len(cell) > 1: temp[(i, j)] = cell

    return sorted(temp, key=lambda n: len(temp[n]))


class Sudoku:
    def __init__(self, loadfile=None, depth=float('inf')):
        self.board = [[list(range(1, 10)) for j in range(9)] for i in range(9)]
        self.pending_extention = []
        self.depth = depth

        if loadfile:
            with open(loadfile, 'r', encoding='utf-8') as file:
                for i, row in enumerate(file.readlines()):
                    for j, cell in enumerate(row.split()):
                        if cell != '0':
                            self.board[i][j] = [int(cell)]
                            self.pending_extention.append((i, j))

    def extend_rules(self, x, y):
        if len(self.board[x][y]) == 1:
            num = self.board[x][y][0]
        else:
            return False

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
        blockx = x // 3;
        blocky = y // 3
        for i in range(3):
            for j in range(3):
                if not (3 * blockx + i == x and 3 * blocky + j == y):
                    try:
                        self.board[3 * blockx + i][3 * blocky + j].remove(num)
                        if len(self.board[3 * blockx + i][3 * blocky + j]) == 1: self.pending_extention.append(
                            (3 * blockx + i, 3 * blocky + j))
                    except ValueError:
                        pass

    def check_singles(self, x, y):
        if len(self.board[x][y]) == 1: return False

        for num in self.board[x][y]:
            if count(num, self.get_row(x, y)) == 1 or count(num, self.get_col(x, y)) == 1 or count(num,
                                                                                                   self.get_block(x,
                                                                                                                  y)) == 1:
                self.board[x][y] = [num]
                self.pending_extention.append((x, y))
                return True
        return False

    def check_arc(self, x, y):
        for num in self.board[x][y]:
            deep = Sudoku(depth=self.depth - 1)
            deep.board = copy(self.board)

            deep.board[x][y] = [num]
            if not deep.solve():
                return num
        return False

    def step(self):
        # Rule Propagation
        if len(self.pending_extention) > 0:
            x, y = self.pending_extention.pop(0)
            self.extend_rules(x, y)
            return 'Propagating Rules from ' + str(x + 1) + ',' + str(y + 1)

        # Confirming Single Values of Lines/Columns/Blocks
        for i in range(9):
            for j in range(9):
                if self.check_singles(i, j): return 'Confirmed single on ' + str(i + 1) + ',' + str(j + 1)

        # Arc Consequence
        coords = get_least_branching(self.board)
        for x, y in coords:
            res = self.check_arc(x, y)
            if res:
                self.board[x][y].remove(res)
                if len(self.board[x][y]) == 1: self.pending_extention.append((x, y))
                return 'Arc Consequence on ' + str(x+1) + ',' + str(y+1)

        return 'Stuck...'

    def solve(self):
        if self.depth <= 0: return True

        while not self.solved():
            if self.step() == 'Stuck...': break
            if self.broken():
                return False
        return True

    def solved(self):
        c = 0
        for row in self.board:
            for cell in row:
                c += len(cell)
        if c > 9 ** 2: return False
        return True

    def broken(self):
        for row in self.board:
            for cell in row:
                if len(cell) == 0:
                    return True
        return False

    def get_row(self, x=0, y=None):
        if 9 < x < 0: return False
        return copy(self.board[x])

    def get_col(self, x=None, y=0):
        if 9 < y < 0: return False
        return copy([self.board[i][y] for i in range(9)])

    def get_block(self, x=0, y=0):
        if 9 < x < 0 or 9 < y < 0: return False

        res = []
        blockx = x // 3
        blocky = y // 3
        for i in range(3):
            for j in range(3):
                res.append(self.board[3 * blockx + i][3 * blocky + j])
        return copy(res)

    def print_lens(self):
        for row in self.board:
            for cell in row:
                print(len(cell), end='  ')
            print()

    def __str__(self):
        res = 'depth: ' + str(self.depth) + '\n'
        for x, row in enumerate(self.board):
            for y, cell in enumerate(row):
                try:
                    if (x + 1) % 3 == 0 and x != 8: res += '\033[4m'
                    if (y + 1) % 3 == 0 and y != 8:
                        if len(cell) > 1:
                            res += '0 |'
                        else:
                            res += str(cell[0]) + ' |'
                    else:
                        if len(cell) > 1:
                            res += '0'
                            if y != 8: res += '  '
                        else:
                            res += str(cell[0])
                            if y != 8: res += '  '
                    if (x+1) % 3 == 0: res += '\033[0m'
                except IndexError:
                    print(cell)
            res += '\n'
        return res


if __name__ == "__main__":
    S = Sudoku('games/expert1.txt', depth=3)
    print(S)
    input()
    S.solve()
    print(S)

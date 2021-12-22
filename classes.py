class Board:
    def __init__(self):
        self.X = 'X'
        self.circle = '●'
        self.board = []
        self.side_length = 19
        self.playable_pos = {
            0: (0, 0),
            1: (0, self.side_length // 2),
            2: (0, self.side_length - 1),
            3: (3, 3),
            4: (3, self.side_length // 2),
            5: (3, self.side_length - 4),
            6: (6, 6),
            7: (6, self.side_length // 2),
            8: (6, self.side_length - 7),
            9: (self.side_length // 2, 0),
            10: (self.side_length // 2, 3),
            11: (self.side_length // 2, 6),
            12: (self.side_length // 2, self.side_length - 7),
            13: (self.side_length // 2, self.side_length - 4),
            14: (self.side_length // 2, self.side_length - 1),
            15: (self.side_length - 7, 6),
            16: (self.side_length - 7, self.side_length // 2),
            17: (self.side_length - 7, self.side_length - 7),
            18: (self.side_length - 4, 3),
            19: (self.side_length - 4, self.side_length // 2),
            20: (self.side_length - 4, self.side_length - 4),
            21: (self.side_length - 1, 0),
            22: (self.side_length - 1, self.side_length // 2),
            23: (self.side_length - 1, self.side_length - 1)
        }
        self.initialize()

    def initialize(self):
        for _ in range(self.side_length):
            row = []
            for _ in range(self.side_length):
                row.append(' ')
            self.board.append(row)

        for row in range(0, self.side_length, 3):
            for j in range(self.side_length):
                self.board[row][j] = '―'

        for j in range(0, self.side_length, 3):
            for i in range(1, self.side_length - 1):
                if (i == 3 or i == self.side_length - 4) and (j == 6 or j == self.side_length - 7):
                    continue
                self.board[i][j] = '│'

        for i in [1, 2, self.side_length - 3, self.side_length - 2]:
            for j in range(1, self.side_length - 1):
                if j != self.side_length // 2:
                    self.board[i][j] = ' '
                    self.board[j][i] = ' '

        for i in [4, 5, self.side_length - 5, self.side_length - 6]:
            for j in range(5, self.side_length - 5):
                if j != self.side_length // 2:
                    self.board[i][j] = ' '
                    self.board[j][i] = ' '

        for i in range(7, self.side_length - 7):
            for j in range(7, self.side_length - 7):
                self.board[i][j] = ' '

        for key, (x, y) in self.playable_pos.items():
            self.board[x][y] = '∙'

    def show(self):
        for i in range(self.side_length):
            for j in range(self.side_length):
                print(self.board[i][j], end=' ')
            print()

    def make_the_move(self, key, is_circle=True):
        x, y = self.playable_pos[key]
        if is_circle:
            self.board[x][y] = self.circle
        else:
            self.board[x][y] = self.X

    def play(self):
        while True:
            key = int(input("Circle's Turn: "))
            while not 0 <= key <= 23:
                key = input('Enter a val in the range [0, 23]: ')

            self.make_the_move(key)
            self.show()

            key = int(input("X's Turn: "))
            while not 0 <= key <= 23:
                key = input('Enter a val in the range [0, 23]: ')

            self.make_the_move(key, False)
            self.show()

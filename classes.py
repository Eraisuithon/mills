class Board:
    def __init__(self):
        self.state = None
        self.available_X = 9
        self.available_0 = 9
        self.second = 'X'
        self.first = '●'
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
        self.state = '0' * 24
        self.available_X = 9
        self.available_0 = 9
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

    def make_the_move(self, key, is_first=True):
        x, y = self.playable_pos[key]
        if is_first:
            self.board[x][y] = self.first
            self.available_0 -= 1
            val_for_state = 1
        else:
            self.board[x][y] = self.second
            self.available_X -= 1
            val_for_state = 2

        self.state = f"{self.state[:key]}{val_for_state}{self.state[key + 1:]}"

    def player_move(self, played, is_first=True):
        string = "first's turn: " if is_first else "Second's turn: "
        key = input(string)
        while not key.isnumeric() or not 0 <= int(key) <= 23 or key in played:
            key = input('Enter a valid number in the range [0, 23]: ')
        key = int(key)
        self.make_the_move(key, is_first)

        played.append(key)
        return played

    def computer_move(self, played, is_first=True):
        key = 0
        for k, val in enumerate(self.state):
            if val == '0':
                key = k
                break

        self.make_the_move(key, is_first)
        played.append(key)
        return played

    def pvp(self):
        played = []
        while not self.available_X == self.available_0 == 0:
            played = self.player_move(played)
            self.show()

            played = self.player_move(played, is_first=False)
            self.show()

    def pvc(self, is_computer_first=False):
        played = []
        is_player_first = True
        if is_computer_first:
            is_player_first = False
            self.computer_move(played)
            self.show()

        while not self.available_X == self.available_0 == 0:
            played = self.player_move(played, is_player_first)
            self.show()

            if self.available_X == self.available_0 == 9:
                break
            print("Computer's turn: ")

            played = self.computer_move(played, not is_player_first)
            self.show()

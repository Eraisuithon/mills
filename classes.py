class Board:
    def __init__(self):
        self.playable_pos = None
        self.neighbors = None
        self.state = None
        self.Xs_on_board = 0
        self.Os_on_board = 0
        self.clear = '∙'
        self.second = 'X'
        self.first = '●'
        self.board = []
        self.side_length = 19
        self.initialize()

    def initialize(self):
        self.state = '0' * 24
        self.Xs_on_board = 0
        self.Os_on_board = 0
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

        for key, (x, y) in self.playable_pos.items():
            self.board[x][y] = self.clear

        self.neighbors = {
            0: (1, 9),
            1: (0, 2, 4),
            2: (1, 14),
            3: (4, 10),
            4: (3, 5, 1, 7),
            5: (6, 13),
            6: (7, 11),
            7: (6, 8, 4),
            8: (7, 12),
            9: (0, 10, 21),
            10: (3, 9, 11, 18),
            11: (10, 6, 15),
            12: (8, 13, 17),
            13: (12, 5, 14, 20),
            14: (13, 2, 23),
            15: (11, 16),
            16: (15, 17, 19),
            17: (16, 12),
            18: (10, 19),
            19: (18, 20, 16, 22),
            20: (19, 13),
            21: (9, 22),
            22: (21, 23, 19),
            23: (22, 14)
        }

    def show(self):
        for i in range(self.side_length):
            for j in range(self.side_length):
                print(self.board[i][j], end=' ')
            print()

    def make_the_move(self, key, is_first=True):
        x, y = self.playable_pos[key]
        if is_first:
            self.board[x][y] = self.first
            self.Os_on_board += 1
            val_for_state = 1
        else:
            self.board[x][y] = self.second
            self.Xs_on_board += 1
            val_for_state = 2

        self.state = f"{self.state[:key]}{val_for_state}{self.state[key + 1:]}"

    def drag_piece(self, key1, key2, is_first=True):
        x1, y1 = self.playable_pos[key1]
        x2, y2 = self.playable_pos[key2]
        self.board[x1][y1] = self.clear
        if is_first:
            self.board[x2][y2] = self.first
            val_for_state = 1
        else:
            self.board[x2][y2] = self.second
            val_for_state = 2

        small = min(key1, key2)
        small_val = 0 if small == key1 else val_for_state
        big = max(key1, key2)
        big_val = val_for_state - small_val
        self.state = f"{self.state[:small]}{small_val}{self.state[small + 1:big]}{big_val}{self.state[big + 1:]}"

    def is_next(self, key1, key2):
        return key2 in self.neighbors[key1]

    def draggable(self, key1, key2, is_first=True):
        x1, y1 = self.playable_pos[key1]
        x2, y2 = self.playable_pos[key2]
        if not self.is_next(key1, key2):
            return False
        if is_first:
            if self.board[x1][y1] != self.first:
                return False
        elif self.board[x1][y1] != self.second:
            return False
        if self.board[x2][y2] != self.clear:
            return False
        return True

    def enter_move(self, played, is_first=True, is_drag=False):
        string = "first's turn: " if is_first else "Second's turn: "
        key = input(string)
        if not is_drag:
            while not key.isnumeric() or not 0 <= int(key) <= 23 or int(key) in played:
                key = input('Enter a valid number in the range [0, 23]: ')
        else:
            while not key.isnumeric() or not 0 <= int(key) <= 23:
                key = input('Enter a valid number in the range [0, 23]: ')
        return int(key)

    def enter_drag(self, played, is_first=True):
        while True:
            print('Drag Piece From')
            key1 = self.enter_move(played, is_first=is_first, is_drag=True)
            print('Drag Piece To')
            key2 = self.enter_move(played, is_first=is_first, is_drag=True)
            if self.draggable(key1, key2, is_first=is_first):
                break
            print('Please enter valid input')

        self.drag_piece(key1, key2, is_first=is_first)
        played.remove(key1)
        played.add(key2)
        return played

    def player_move(self, played, is_first=True):
        key = self.enter_move(played, is_first)
        self.make_the_move(key, is_first)

        played.add(key)
        return played

    def computer_move(self, played, is_first=True):
        key = 0
        for k, val in enumerate(self.state):
            if val == '0':
                key = k
                break

        self.make_the_move(key, is_first)
        played.add(key)
        return played

    def is_first_symbol(self, is_first):
        if is_first:
            return self.first
        return self.second

    def com_drag(self, played, is_first=True):
        for key, val in self.neighbors.items():
            x, y = self.playable_pos[key]
            if self.board[x][y] != self.is_first_symbol(is_first):
                continue
            if key in played:
                for k in val:
                    if k not in played:
                        play_to = k
                        break
                else:
                    continue
                self.drag_piece(key, play_to, is_first=is_first)
                played.remove(key)
                played.add(play_to)
                return played
        return None

    def pvp(self):
        played = set()
        while not self.Xs_on_board == self.Os_on_board == 9:
            played = self.player_move(played)
            self.show()

            played = self.player_move(played, is_first=False)
            self.show()
        while True:
            played = self.enter_drag(played)
            self.show()

            played = self.enter_drag(played, is_first=False)
            self.show()

    def pvc(self, is_computer_first=False):
        played = set()
        is_player_first = True
        if is_computer_first:
            is_player_first = False
            self.computer_move(played)
            self.show()

        while not self.Xs_on_board == self.Os_on_board == 9:
            played = self.player_move(played, is_player_first)
            self.show()

            if self.Xs_on_board == self.Os_on_board == 9:
                break
            print("Computer's turn: ")

            played = self.computer_move(played, not is_player_first)
            self.show()

        if is_computer_first:
            self.com_drag(played, is_first=True)
            self.show()

        while True:
            played = self.enter_drag(played, is_first=not is_computer_first)
            self.show()

            played = self.com_drag(played, is_first=is_computer_first)
            if played is None:
                return 'Player won'
            self.show()

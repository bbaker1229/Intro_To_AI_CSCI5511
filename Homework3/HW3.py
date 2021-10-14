'''
othellogame module

sets up an Othello game closely following the book's framework for games

OthelloState is a class that will handle our state representation, then we've 
got stand-alone functions for player, actions, result and terminal_test

Differing from the book's framework, is that utility is *not* a stand-alone 
function, as each player might have their own separate way of calculating utility


'''
import copy
import random as ran

WHITE = 1
BLACK = -1
EMPTY = 0
SIZE = 8
SKIP = "SKIP"

class OthelloPlayerTemplate:
    '''Template class for an Othello Player

    An othello player *must* implement the following methods:

    get_color(self) - correctly returns the agent's color

    make_move(self, state) - given the state, returns an action that is the agent's move
    '''
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        '''Given the state, returns a legal action for the agent to take in the state
        '''
        return None

class HumanPlayer:
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        curr_move = None
        legals = actions(state)
        while curr_move == None:
            display(state)
            if self.color == 1:
                print("White ", end='')
            else:
                print("Black ", end='')
            print(" to play.")
            print("Legal moves are " + str(legals))
            move = input("Enter your move as a r,c pair:")
            if move == "":
                return legals[0]

            if move == SKIP and SKIP in legals:
                return move

            try:
                movetup = int(move.split(',')[0]), int(move.split(',')[1])
            except:
                movetup = None
            if movetup in legals:
                curr_move = movetup
            else:
                print("That doesn't look like a legal action to me")
        return curr_move

class RandomPlayer:
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        curr_move = None
        legals = actions(state)
        while curr_move == None:
            ind = ran.randint(0, len(legals) - 1)
            move = legals[ind]
            if move == "":
                return legals[0]

            if move == SKIP and SKIP in legals:
                return move

            try:
                movetup = move
            except:
                movetup = None
            if movetup in legals:
                curr_move = movetup
            else:
                print("That doesn't look like a legal action to me")
        return curr_move

class MinimaxPlayer:
    def __init__(self, mycolor, plydepth):
        self.color = mycolor
        self.depth = plydepth

    def get_color(self):
        return self.color

    def get_depth(self):
        return self.depth

    def make_move(self, state):
        depth = self.get_depth()
        color = self.get_color()
        curr_move = None
        legals = actions(state)
        while curr_move == None:
            # ind = ran.randint(0, len(legals) - 1)
            # move = legals[ind]
            move = minimax_search(state, color, depth)
            if move == "":
                return legals[0]

            if move == SKIP and SKIP in legals:
                return move

            try:
                movetup = move
            except:
                movetup = None
            if movetup in legals:
                curr_move = movetup
            else:
                print("That doesn't look like a legal action to me")
        return curr_move

class AlphabetaPlayer:
    def __init__(self, mycolor, plydepth):
        self.color = mycolor
        self.depth = plydepth

    def get_color(self):
        return self.color

    def get_depth(self):
        return self.depth

    def make_move(self, state):
        depth = self.get_depth()
        color = self.get_color()
        curr_move = None
        legals = actions(state)
        while curr_move == None:
            # ind = ran.randint(0, len(legals) - 1)
            # move = legals[ind]
            move = alpha_beta_search(state, color, depth)
            if move == "":
                return legals[0]

            if move == SKIP and SKIP in legals:
                return move

            try:
                movetup = move
            except:
                movetup = None
            if movetup in legals:
                curr_move = movetup
            else:
                print("That doesn't look like a legal action to me")
        return curr_move

def utility(state, color):
    """
    Count the difference in the number of spaces owned by a color and their opponent.
    """
    player_cnt = 0
    opponent_cnt = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[j][i] == color:
                player_cnt += 1
            else:
                opponent_cnt += 1
    return player_cnt - opponent_cnt

def utility_eval(state, color):
    """
    Count the number of available moves from this state.
    """
    return len(actions(state))

def minimax_search(state, color, depth):
    _, move = max_value(state, color, depth - 1)
    return move

def max_value(state, color, depth):
    if terminal_test(state):
        return utility(state, color), None
    if depth == 0:
        return utility_eval(state, color), None
    v = -100
    move = None
    for a in actions(state):
        v2, a2 = min_value(result(state, a), color, depth - 1)
        if v2 > v:
            v = v2
            move = a
    return v, move

def min_value(state, color, depth):
    if terminal_test(state):
        return utility(state, color), None
    if depth == 0:
        return utility_eval(state, color), None
    v = 100
    move = None
    for a in actions(state):
        v2, a2 = max_value(result(state, a), color, depth - 1)
        if v2 < v:
            v = v2
            move = a
    return v, move

def alpha_beta_search(state, color, depth):
    _, move = ab_max_value(state, color, -100, 100, depth - 1)
    return move

def ab_max_value(state, color, alpha, beta, depth):
    if terminal_test(state):
        return utility(state, color), None
    if depth == 0:
        return utility_eval(state, color), None
    v = -100
    move = None
    for a in actions(state):
        v2, a2 = ab_min_value(result(state, a), color, alpha, beta, depth - 1)
        if v2 > v:
            v = v2
            move = a
            alpha = max(alpha, v)
        if v >= beta:
            return v, move
    return v, move

def ab_min_value(state, color, alpha, beta, depth):
    if terminal_test(state):
        return utility(state, color), None
    if depth == 0:
        return utility_eval(state, color), None
    v = 100
    move = None
    for a in actions(state):
        v2, a2 = ab_max_value(result(state, a), color, alpha, beta, depth - 1)
        if v2 < v:
            v = v2
            move = a
            beta = min(beta, v)
        if v <= alpha:
            return v, move
    return v, move

class OthelloState:
    '''A class to represent an othello game state'''

    def __init__(self, currentplayer, otherplayer, board_array = None, num_skips = 0):
        if board_array != None:
            self.board_array = board_array
        else:
            self.board_array = [[EMPTY] * SIZE for i in range(SIZE)]
            self.board_array[3][3] = WHITE
            self.board_array[4][4] = WHITE
            self.board_array[3][4] = BLACK
            self.board_array[4][3] = BLACK
        self.num_skips = num_skips
        self.current = currentplayer
        self.other = otherplayer


def player(state):
    return state.current

def actions(state):
    '''Return a list of possible actions given the current state
    '''
    legal_actions = []
    for i in range(SIZE):
        for j in range(SIZE):
            if result(state, (i,j)) != None:
                legal_actions.append((i,j))
    if len(legal_actions) == 0:
        legal_actions.append(SKIP)
    return legal_actions

def result(state, action):
    '''Returns the resulting state after taking the given action

    (This is the workhorse function for checking legal moves as well as making moves)

    If the given action is not legal, returns None

    '''
    # first, special case! an action of SKIP is allowed if the current agent has no legal moves
    # in this case, we just skip to the other player's turn but keep the same board
    if action == SKIP:
        newstate = OthelloState(state.other, state.current, copy.deepcopy(state.board_array), state.num_skips + 1)
        return newstate

    if state.board_array[action[0]][action[1]] != EMPTY:
        return None

    color = state.current.get_color()
    # create new state with players swapped and a copy of the current board
    newstate = OthelloState(state.other, state.current, copy.deepcopy(state.board_array))

    newstate.board_array[action[0]][action[1]] = color
    
    flipped = False
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for d in directions:
        i = 1
        count = 0
        while i <= SIZE:
            x = action[0] + i * d[0]
            y = action[1] + i * d[1]
            if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
                count = 0
                break
            elif newstate.board_array[x][y] == -1 * color:
                count += 1
            elif newstate.board_array[x][y] == color:
                break
            else:
                count = 0
                break
            i += 1

        if count > 0:
            flipped = True

        for i in range(count):
            x = action[0] + (i+1) * d[0]
            y = action[1] + (i+1) * d[1]
            newstate.board_array[x][y] = color

    if flipped:
        return newstate
    else:  
        # if no pieces are flipped, it's not a legal move
        return None

def terminal_test(state):
    '''Simple terminal test
    '''
    # if both players have skipped
    if state.num_skips == 2:
        return True

    # if there are no empty spaces
    empty_count = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == EMPTY:
                empty_count += 1
    if empty_count == 0:
        return True
    return False

def display(state):
    '''Displays the current state in the terminal window
    '''
    print('  ', end='')
    for i in range(SIZE):
        print(i,end='')
    print()
    for i in range(SIZE):
        print(i, '', end='')
        for j in range(SIZE):
            if state.board_array[j][i] == WHITE:
                print('W', end='')
            elif state.board_array[j][i] == BLACK:
                print('B', end='')
            else:
                print('-', end='')
        print()

def display_final(state):
    '''Displays the score and declares a winner (or tie)
    '''
    wcount = 0
    bcount = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[i][j] == WHITE:
                wcount += 1
            elif state.board_array[i][j] == BLACK:
                bcount += 1

    print("Black: " + str(bcount))
    print("White: " + str(wcount))
    if wcount > bcount:
        print("White wins")
    elif wcount < bcount:
        print("Black wins")
    else:
        print("Tie")

def play_game(p1 = None, p2 = None):
    '''Plays a game with two players. By default, uses two humans
    '''
    if p1 == None:
        p1 = HumanPlayer(BLACK)
    if p2 == None:
        p2 = HumanPlayer(WHITE)

    s = OthelloState(p1, p2)
    while True:
        action = p1.make_move(s)
        if action not in actions(s):
            print("Illegal move made by Black")
            print("White wins!")
            return
        s = result(s, action)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            print(f"Black utility = {utility(s, BLACK)}")
            print(f"White utility = {utility(s, WHITE)}")
            return
        action = p2.make_move(s)
        if action not in actions(s):
            print("Illegal move made by White")
            print("Black wins!")
            return
        s = result(s, action)
        if terminal_test(s):
            print("Game Over")
            display(s)
            display_final(s)
            print(f"Black utility = {utility(s, BLACK)}")
            print(f"White utility = {utility(s, WHITE)}")
            return

def main():
    player1 = RandomPlayer(BLACK)
    player2 = RandomPlayer(WHITE)
    play_game(player1, player2)

    player2 = MinimaxPlayer(WHITE, 4)
    play_game(player1, player2)

    player2 = AlphabetaPlayer(WHITE, 4)
    play_game(player1, player2)

if __name__ == '__main__':
    main()

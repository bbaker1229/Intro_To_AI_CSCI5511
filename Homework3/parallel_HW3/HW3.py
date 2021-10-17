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
import time

import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor

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

###############################################################################################
# Begin code created for Homework 3
###############################################################################################
class RandomPlayer:
    """
    This class creates an automated player that plays a random legal move for each turn.
    """
    def __init__(self, mycolor):
        self.color = mycolor

    def get_color(self):
        return self.color

    def make_move(self, state):
        curr_move = None
        legals = actions(state)
        ind = ran.randint(0, len(legals) - 1)  # Choose a random index from the list of legal moves
        curr_move = legals[ind]
        return curr_move

class MinimaxPlayer:
    """
    This class creates an automated player that plays a move based on a depth limited minimax function for each turn.
    """
    def __init__(self, mycolor, plydepth):
        self.color = mycolor
        self.depth = plydepth  # Store the ply depth

    def get_color(self):
        return self.color

    def get_depth(self):
        return self.depth  # This is a method for the class to return the depth.  Required for make_move.

    def make_move(self, state):
        depth = self.get_depth()
        color = self.get_color()
        curr_move = None
        curr_move = minimax_search(state, color, depth)  # Call the minimax search function.
        return curr_move

class AlphabetaPlayer:
    """
    This class creates an automated player that plays a move based on a depth limited alpha-beta minimax function for each turn.
    """
    def __init__(self, mycolor, plydepth):
        self.color = mycolor
        self.depth = plydepth  # Store the ply depth

    def get_color(self):
        return self.color

    def get_depth(self):
        return self.depth  # This is a method for the class to return the depth.  Required for make_move.

    def make_move(self, state):
        depth = self.get_depth()
        color = self.get_color()
        curr_move = None
        curr_move = alpha_beta_search(state, color, depth)  # Call the alpha-beta minimax search function.
        return curr_move

def utility(state, color):
    """
    This is a utility function to use for minimax.
    Count the difference in the number of spaces owned by a color and their opponent.
    If this is a terminal state then a win is returned as a high number +100 and a loss is a low number -100.
    """
    player_cnt = 0
    opponent_cnt = 0
    for i in range(SIZE):
        for j in range(SIZE):
            if state.board_array[j][i] == color:
                player_cnt += 1
            else:
                opponent_cnt += 1
    if terminal_test(state):
        if player_cnt > opponent_cnt:
            return 100
        if opponent_cnt > player_cnt:
            return -100
    return player_cnt - opponent_cnt

def utility_eval(state, color):
    """
    This is experimental for a non terminal state.  It was very slow and didn't win very often.
    Count the number of available moves from this state.
    """
    return len(actions(state))

def minimax_search(state, color, depth):
    _, move = parallel_max_value(state, color, depth, True)  # The depth is decreased for each ply.
    return move

def parallel_max_value(state, color, depth, parallel):
    print(parallel)
    if parallel:
        # mp.set_start_method('spawn')
        moves = actions(state)
        results = []
        for i in moves:
            results.append(result(state, i))
        color_lst = [color for i in range(len(moves))]
        depth_lst = [depth - 1 for i in range(len(moves))]
        # num_cores = mp.cpu_count()
        rets = []
        # pool = mp.Pool(num_cores)
        # pool = ProcessPoolExecutor(num_cores)
        # value = pool.starmap_async(min_value, zip(moves, results, color_lst, depth_lst), callback=rets.append)
        args = zip(moves, results, color_lst, depth_lst)
        # with ProcessPoolExecutor(num_cores) as pool:
        pool = ProcessPoolExecutor()
        value = list(pool.map(min_value, args))
        print(value)
        # rets = value.get()
        # print(rets)
        # pool.close()
        # pool.join()
        # with mp.Pool(num_cores) as p:
        #     p.starmap_async(min_value, zip(moves, results, color_lst, depth_lst), callback=rets.append)
        #     # rets.append(values.get())
        #     p.close()
        #     p.join()
        v = -100
        move = None
        for item in value:
            if item[0] > v:
                v = item[0]
                move = item[1]
    else:
        v, move = max_value(state, color, depth)
    print(v, move)
    return v, move

# def max_value(state, color, depth):
def max_value(args):
    state = args[0]
    color = args[1]
    depth = args[2]
    if terminal_test(state) or depth == 0:  # Since the depth is decreased for each ply we can find the utility once the depth is zero.
        return utility(state, color), None
    v = -100  # Initialize the utility to a low number.
    move = None  # Initialize to return no move 
    for a in actions(state):
        next_args = (a, result(state, a), color, depth - 1)
        v2, a2 = min_value(next_args)
        # v2, a2 = min_value(a, result(state, a), color, depth - 1)  # Call the min_value function for the opponent.  Decrease the depth.
        if v2 > v:  # Check if the utility of this move is better than the current best utility.
            v = v2
            move = a
    return v, move

# def min_value(action, state, color, depth):
def min_value(args):
    action = args[0]
    state = args[1]
    color = args[2]
    depth = args[3]
    if terminal_test(state) or depth == 0:  # Since the depth is decreased for each ply we can find the utility once the depth is zero.
        return utility(state, color), None
    v = 100  # Initialize the utility to a high number.
    move = None  # Initialize to return no move 
    for a in actions(state):
        next_args = (result(state, a), color, depth - 1)
        v2, a2 = max_value(next_args)
        # v2, a2 = max_value(result(state, a), color, depth - 1)  # Call the max_value function to try to the players next move.  Decrease the depth.
        # print(a, color, depth, v2)
        if v2 < v:  # check if the utility of this move is worse than the current worse utility.  The opponent will probably choose this one.
            v = v2
            move = a
    return v, move

def alpha_beta_search(state, color, depth):
    _, move = ab_max_value(state, color, -100, 100, depth - 1)  # The depth is decreased for each ply.  Initialize alpha low and beta high.
    return move

def ab_max_value(state, color, alpha, beta, depth):
    if terminal_test(state) or depth == 0:  # Since the depth is decreased for each ply we can find the utility once the depth is zero.
        return utility(state, color), None
    v = -100  # Initialize the utility to a low number.
    move = None  # Initialize to return no move
    for a in actions(state):
        # Call the min_value alpha-beta function for the opponent.  Decrease the depth.
        v2, a2 = ab_min_value(result(state, a), color, alpha, beta, depth - 1)
        if v2 > v:  # Check if the utility of this move is better than the current best utility.
            v = v2
            move = a
            alpha = max(alpha, v)  # Possibly update alpha to check for future cutoffs in ab_min_value.
        if v >= beta:  # If our best utility is greater than beta return the move because the opponent will not take this route.
            return v, move
    return v, move

def ab_min_value(state, color, alpha, beta, depth):
    if terminal_test(state) or depth == 0:  # Since the depth is decreased for each ply we can find the utility once the depth is zero.
        return utility(state, color), None
    v = 100  # Initialize the utility to a high number.
    move = None  # Initialize to return no move
    for a in actions(state):
        # Call the max_value alpha-beta function for the player.  Decrease the depth.
        v2, a2 = ab_max_value(result(state, a), color, alpha, beta, depth - 1)
        if v2 < v:  # Check if the utility of this move is worse than the current worst utility.
            v = v2
            move = a
            beta = min(beta, v)  # Possibly update beta to check for future cutoffs in ab_max_value.
        if v <= alpha:  # If our best utility is worse than alpha return the move because the player will not find a better move in this route.
            return v, move
    return v, move

###############################################################################################
# End code created for Homework 3
###############################################################################################

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

    # print("Black: " + str(bcount))
    # print("White: " + str(wcount))
    if wcount > bcount:
        # print("White wins")
        winner = "WHITE"
    elif wcount < bcount:
        # print("Black wins")
        winner = "BLACK"
    else:
        # print("Tie")
        winner = "TIE"
    return winner

def play_game(p1 = None, p2 = None):
    '''Plays a game with two players. By default, uses two humans
    '''
    if p1 == None:
        p1 = HumanPlayer(BLACK)
    if p2 == None:
        p2 = HumanPlayer(WHITE)

    s = OthelloState(p1, p2)
    p1_times = []
    p2_times = []
    while True:
        t_start = time.perf_counter()
        action = p1.make_move(s)
        t_end = time.perf_counter() - t_start
        p1_times.append(t_end)
        if action not in actions(s):
            # print("Illegal move made by Black")
            # print("White wins!")
            return p1_times, p2_times, "WHITE"
        s = result(s, action)
        if terminal_test(s):
            # print("Game Over")
            # display(s)
            winner = display_final(s)
            # print(f"Player1 move statistics: min_time = {min(p1_times)}; avg_time = {sum(p1_times) / len(p1_times)}; max_time = {max(p1_times)}; N = {len(p1_times)}")
            # print(f"Player2 move statistics: min_time = {min(p2_times)}; avg_time = {sum(p2_times) / len(p2_times)}; max_time = {max(p2_times)}; N = {len(p2_times)}")
            return p1_times, p2_times, winner
        t_start = time.perf_counter()
        action = p2.make_move(s)
        t_end = time.perf_counter() - t_start
        p2_times.append(t_end)
        if action not in actions(s):
            # print("Illegal move made by White")
            # print("Black wins!")
            return p1_times, p2_times, "BLACK"
        s = result(s, action)
        if terminal_test(s):
            # print("Game Over")
            # display(s)
            winner = display_final(s)
            # print(f"Player1 move statistics: min_time = {min(p1_times)}; avg_time = {sum(p1_times) / len(p1_times)}; max_time = {max(p1_times)}; N = {len(p1_times)}")
            # print(f"Player2 move statistics: min_time = {min(p2_times)}; avg_time = {sum(p2_times) / len(p2_times)}; max_time = {max(p2_times)}; N = {len(p2_times)}")
            return p1_times, p2_times, winner

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

import HW3 as student
import numpy as np
import multiprocessing as mp

def summarize(list_a):
    white_wins = 0
    black_wins = 0
    ties = 0
    for value in list_a:
        if value == "WHITE":
            white_wins += 1
        if value == "BLACK":
            black_wins += 1
        if value == "TIE":
            ties += 1
    print(f"Black wins = {black_wins}")
    print(f"White wins = {white_wins}")
    print(f"Ties = {ties}")

def main():
    print("Play single games:")
    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / RandomPlayer")
    player1 = student.RandomPlayer(student.BLACK)
    player2 = student.RandomPlayer(student.WHITE)
    p1_time, p2_time, winner = student.play_game(player1, player2)
    p1_time = np.array(p1_time)
    p2_time = np.array(p2_time)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    print(f"Winner = {winner}")
    print("")
    
    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / MinimaxPlayer / depth = 4")
    player1 = student.RandomPlayer(student.BLACK)
    player2 = student.MinimaxPlayer(student.WHITE, 4)
    p1_time, p2_time, winner = student.play_game(player1, player2)
    p1_time = np.array(p1_time)
    p2_time = np.array(p2_time)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    print(f"Winner = {winner}")
    print("")
    """   
    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 4")
    player1 = student.RandomPlayer(student.BLACK)
    player2 = student.AlphabetaPlayer(student.WHITE, 4)
    p1_time, p2_time, winner = student.play_game(player1, player2)
    p1_time = np.array(p1_time)
    p2_time = np.array(p2_time)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    print(f"Winner = {winner}")
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 5")
    player1 = student.RandomPlayer(student.BLACK)
    player2 = student.AlphabetaPlayer(student.WHITE, 5)
    p1_time, p2_time, winner = student.play_game(player1, player2)
    p1_time = np.array(p1_time)
    p2_time = np.array(p2_time)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    print(f"Winner = {winner}")
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 6")
    player1 = student.RandomPlayer(student.BLACK)
    player2 = student.AlphabetaPlayer(student.WHITE, 6)
    p1_time, p2_time, winner = student.play_game(player1, player2)
    p1_time = np.array(p1_time)
    p2_time = np.array(p2_time)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    print(f"Winner = {winner}")
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 7")
    player1 = student.RandomPlayer(student.BLACK)
    player2 = student.AlphabetaPlayer(student.WHITE, 7)
    p1_time, p2_time, winner = student.play_game(player1, player2)
    p1_time = np.array(p1_time)
    p2_time = np.array(p2_time)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    print(f"Winner = {winner}")
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 8")  # 8 looks like the max else too long.
    player1 = student.RandomPlayer(student.BLACK)
    player2 = student.AlphabetaPlayer(student.WHITE, 8)
    p1_time, p2_time, winner = student.play_game(player1, player2)
    p1_time = np.array(p1_time)
    p2_time = np.array(p2_time)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    print(f"Winner = {winner}")
    print("")

    print("Play 20 games:")
    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / RandomPlayer")
    p1_time = np.array([])
    p2_time = np.array([])
    winners = []
    for i in range(20):
        player1 = student.RandomPlayer(student.BLACK)
        player2 = student.RandomPlayer(student.WHITE)
        p1_temp, p2_temp, temp_winner = student.play_game(player1, player2)
        p1_time = np.concatenate((p1_time, np.array(p1_temp)), axis=None)
        p2_time = np.concatenate((p2_time, np.array(p2_temp)), axis=None)
        winners.append(temp_winner)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    summarize(winners)
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / MinimaxPlayer / depth = 4")
    p1_time = np.array([])
    p2_time = np.array([])
    winners = []
    for i in range(20):
        player1 = student.RandomPlayer(student.BLACK)
        player2 = student.MinimaxPlayer(student.WHITE, 4)
        p1_temp, p2_temp, temp_winner = student.play_game(player1, player2)
        p1_time = np.concatenate((p1_time, np.array(p1_temp)), axis=None)
        p2_time = np.concatenate((p2_time, np.array(p2_temp)), axis=None)
        winners.append(temp_winner)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    summarize(winners)
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 4")
    p1_time = np.array([])
    p2_time = np.array([])
    winners = []
    for i in range(20):
        player1 = student.RandomPlayer(student.BLACK)
        player2 = student.AlphabetaPlayer(student.WHITE, 4)
        p1_temp, p2_temp, temp_winner = student.play_game(player1, player2)
        p1_time = np.concatenate((p1_time, np.array(p1_temp)), axis=None)
        p2_time = np.concatenate((p2_time, np.array(p2_temp)), axis=None)
        winners.append(temp_winner)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    summarize(winners)
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 5")
    p1_time = np.array([])
    p2_time = np.array([])
    winners = []
    for i in range(20):
        player1 = student.RandomPlayer(student.BLACK)
        player2 = student.AlphabetaPlayer(student.WHITE, 5)
        p1_temp, p2_temp, temp_winner = student.play_game(player1, player2)
        p1_time = np.concatenate((p1_time, np.array(p1_temp)), axis=None)
        p2_time = np.concatenate((p2_time, np.array(p2_temp)), axis=None)
        winners.append(temp_winner)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    summarize(winners)
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 6")
    p1_time = np.array([])
    p2_time = np.array([])
    winners = []
    for i in range(20):
        player1 = student.RandomPlayer(student.BLACK)
        player2 = student.AlphabetaPlayer(student.WHITE, 6)
        p1_temp, p2_temp, temp_winner = student.play_game(player1, player2)
        p1_time = np.concatenate((p1_time, np.array(p1_temp)), axis=None)
        p2_time = np.concatenate((p2_time, np.array(p2_temp)), axis=None)
        winners.append(temp_winner)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    summarize(winners)
    print("")

    print("Player1 = BLACK / RandomPlayer; Player2 = WHITE / AlphabetaPlayer / depth = 7")
    p1_time = np.array([])
    p2_time = np.array([])
    winners = []
    for i in range(20):
        player1 = student.RandomPlayer(student.BLACK)
        player2 = student.AlphabetaPlayer(student.WHITE, 7)
        p1_temp, p2_temp, temp_winner = student.play_game(player1, player2)
        p1_time = np.concatenate((p1_time, np.array(p1_temp)), axis=None)
        p2_time = np.concatenate((p2_time, np.array(p2_temp)), axis=None)
        winners.append(temp_winner)
    print(f"Player1 move statistics: min_time = {p1_time.min():0.6f}; avg_time = {(p1_time.sum() / p1_time.size):0.6f}; max_time = {p1_time.max():0.6f}; N = {p1_time.size}")
    print(f"Player2 move statistics: min_time = {p2_time.min():0.6f}; avg_time = {(p2_time.sum() / p2_time.size):0.6f}; max_time = {p2_time.max():0.6f}; N = {p2_time.size}")
    summarize(winners)
    print("")
    """
    


if __name__ == '__main__':
    main()

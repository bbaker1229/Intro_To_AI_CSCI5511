import tournament_exle0002
import tournament_achan009
import tournament_alai0003
import tournament_apost035
import tournament_bake1358
import tournament_govin088
import tournament_guo00208
import tournament_helle219
import tournament_khanx370
import tournament_kluzw001
import tournament_nels9876
import tournament_nolet004
import tournament_pete9621
import tournament_rane0017
import tournament_sunda132


import threading
import os
import pickle

RESULTFILE = 'tourney_results.dat'


def load_results(result_file):
    results = {}
    if os.path.exists(result_file):
        with open(result_file, 'rb') as f:
            results = pickle.load(f)
    print("loaded: " + str(results))
    return results

def score(s):
    oth = tournament_exle0002
    wcount = 0
    bcount = 0
    for i in range(oth.SIZE):
        for j in range(oth.SIZE):
            if s.board_array[i][j] == oth.WHITE:
                wcount += 1
            elif s.board_array[i][j] == oth.BLACK:
                bcount += 1
    if bcount > wcount:
        return (1, 'Black wins {}-{}'.format(bcount, wcount))
    elif wcount > bcount:
        return (0, 'White wins {}-{}'.format(bcount, wcount))
    else:
        return (0.5, 'Draw {}-{}'.format(bcount, count))

def timed_move(player, currstate, action_list):
    try:
        action_list[0] = player.make_move(currstate)
    except Exception as inst:
        print(inst)
        action_list[0] = "Exception"
    return

def safe_move(player, currstate):
    actionlist = [None]
    try:
        t = threading.Thread(target = timed_move, args=(player, currstate, actionlist))
        t.start()
        t.join(60.0)
    except:
        actionlist[0] = "Exception"
    return actionlist[0]

def play_game(p1class, p2class):
    oth = tournament_exle0002
    p1 = p1class(oth.BLACK)
    p2 = p2class(oth.WHITE)
    s = oth.OthelloState(p1, p2)
    while True:
        action = safe_move(p1, s)
        if action == None:
            return (0, "Black timed out")
        elif action == "Exception":
            return (0, "Black agent had some error")
        elif action not in oth.actions(s):
            return (0, "Black made illegal move")
        s = oth.result(s, action)
        if oth.terminal_test(s):
            return score(s)
        oth.display(s)

        action = safe_move(p2, s)
        if action == None:
            return (1, "White timed out")
        elif action == "Exception":
            return (1, "White agent had some error")
        elif action not in oth.actions(s):
            return (1, "White made illegal move")
        s = oth.result(s, action)
        if oth.terminal_test(s):
            return score(s)

def run_games(player_list, results):
    for p1 in player_list:
        for p2 in player_list:
            if p1 != p2:
                p1name = p1.__module__ + "." + p1.__name__
                p2name = p2.__module__ + "." + p2.__name__
                if (p1name,p2name) not in results:
                    print(p1name + " vs. " + p2name)
                    score1 = play_game(p1, p2)
                    print(score1)
                    score2 = play_game(p2, p1)
                    print(score2)
                    results[(p1name,p2name)] = [score1, (1-score2[0], score2[1])]
                    results[(p2name,p1name)] = [(1-score1[0], score1[1]), score2]
                    write_results(results, RESULTFILE)

def write_results(results, result_file):
    with open(result_file, 'wb') as f:
        pickle.dump(results, f)

def main():
    players = [
                tournament_exle0002.TourneyPlayer, 
                #tournament_achan009.TourneyPlayer, # signals
                tournament_alai0003.TourneyPlayer,
                #tournament_apost035.TourneyPlayer  # missing global DEPTH
                tournament_bake1358.TourneyPlayer,
                tournament_govin088.TourneyPlayer,
                tournament_guo00208.TourneyPlayer,
                tournament_helle219.TourneyPlayer,
                #tournament_khanx370.TourneyPlayer  # missing functions
                #tournament_kluzw001.TourneyPlayer  # threading
                #tournament_nels9876.TourneyPlayer  # missing functions
                tournament_nolet004.TourneyPlayer
                #tournament_pete9621.TourneyPlayer  # missing functions
                #tournament_rane0017.TourneyPlayer  # no default values set
                #tournament_sunda132.TourneyPlayer  # missing functions
                

                ]
    results = load_results(RESULTFILE)
    run_games(players, results)

if __name__ == '__main__':
    main()

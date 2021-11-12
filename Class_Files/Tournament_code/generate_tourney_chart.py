import pickle
import sys
import os

def load_results(fname):
    assert os.path.exists(fname), 'Cannot find file ' + str(fname)
    
    with open(fname, 'rb') as fp:
        results = pickle.load(fp)
        return results

def create_chart(results):
    assert isinstance(results, dict), 'results is not a dictionary'

    agentscore = {}
    agentpairs = list(results.keys())
    for pair in results:
        if pair[0] not in agentscore:
            agentscore[pair[0]] = 0
        agentscore[pair[0]] += results[pair][0][0] + results[pair][1][0]
    scoresort = []
    for a in agentscore:
        scoresort.append((agentscore[a], a))
    scoresort.sort()
    scoresort.reverse()
    print(scoresort)
    
    print("<table>")
    print("<th>", end = '')
    for a in scoresort:
        agent = a[1].replace(".TourneyPlayer", "").replace("tournament_", "")
        print("<td>{}</td> ".format(agent), end='')
    print("</th>")


    for a in scoresort:
        print("<tr>", end ='')
        agent = a[1].replace(".TourneyPlayer", "").replace("tournament_", "")
        print("<td>{} ({})</td>".format(agent, a[0]))
        for a2 in scoresort:
            if a[1] == a2[1]:
                print("<td>X</td>", end = '')
            else:
                scoreline = results[(a[1],a2[1])]
                wins = scoreline[0][0] + scoreline[1][0]
                print("<td>{}-{}</td>".format(wins, 2-wins), end='')
        print("</tr>")
    print("</table>")

def main():
    if len(sys.argv) > 1:
        fname = sys.argv[1]
    else:
        fname = "tourney_results.dat"
    results = load_results(fname)
    create_chart(results)

if __name__ == '__main__':
    main()

from GraphWorld import *
from RandomGraph import RandomGraph
import numpy as np


def test_phase_transition(n):
    # create n Vertices
    n = int(n)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    con_list = []
    # for k in np.linspace(0, 1, 200):
    limit = (1-math.e) * math.log(n, math.e) / n
    print limit
    for k in np.linspace(0, 1, 500):
        this_time_connect_list = []
        for x in range(3):
            g = RandomGraph(vs)
            try:
                g.add_random_edges(k)
            except:
                continue
            con = g.is_connected()
            this_time_connect_list.append(1 if con else -1)
        this_con = sum(this_time_connect_list)
        con_list.append((round(k, 4), this_con))
    for x in xrange(len(con_list) - 1):
        if con_list[x][1] * con_list[x + 1][1] < 0:
            print con_list[x], '>>>>', con_list[x+1]

if __name__ == '__main__':
    import sys
    test_phase_transition(sys.argv[1])
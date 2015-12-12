from GraphWorld import *
from RandomGraph import RandomGraph
from tools.tools import destroy_graph


def test_regular_generator(n, k):
    # create n Vertices
    n = int(n)
    k = int(k)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = Graph(vs)
    # g.add_all_edges()
    g.add_regular_edges(k)
    layout = CircleLayout(g)

    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()

def test_random_generator(n, p):
    # create n Vertices
    n = int(n)
    p = float(p)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]

    # create a graph and a layout
    g = RandomGraph(vs)
    # g.add_all_edges()
    g.add_random_edges(p)
    layout = CircleLayout(g)
    # draw the graph
    gw = GraphWorld()
    gw.show_graph(g, layout)
    destroy_graph(gw, 2)
    gw.mainloop()

if __name__ == '__main__':
    import sys
    # test_regular_generator(sys.argv[1], sys.argv[2])
    test_random_generator(sys.argv[1], sys.argv[2])
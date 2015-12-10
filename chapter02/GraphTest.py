from GraphWorld import *


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

if __name__ == '__main__':
    import sys
    test_regular_generator(sys.argv[1], sys.argv[2])
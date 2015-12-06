from Graph import *


def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    print w
    e = Edge(v, w)
    print e
    g = Graph([v,w], [e])
    print g


if __name__ == '__main__':
    import sys
    main(*sys.argv)
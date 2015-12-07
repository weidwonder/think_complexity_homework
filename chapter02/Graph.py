""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.
"""

class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            raise ValueError, 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.

    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=None, es=None, directed=False):
        """Creates a new graph.
        vs: list of vertices;
        es: list of edges.
        """
        super(Graph, self).__init__()
        vs = vs or []
        es = es or []
        self.directed = directed
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        if v in self.iterkeys():
            return
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        for _ in e:
            self.add_vertex(_)
        self[v][w] = e
        if not self.directed:
            self[w][v] = e

    def get_edge(self, v, w):
        """ Get the edge between vertex v and w.
        """
        edge = self.get(v, {}).get(w, None)
        return edge

    def remove_edge(self, v, w):
        """ Remove the edge between vertex v and w.
        if the edge between v and w is exist, then delete it and return True.
        else it returns False.
        """
        try:
            del self[v][w]
            if not self.directed:
                del self[w][v]
            return True
        except:
            return False

    def vertices(self):
        """ Get all vertices in this Graph as a list.
        """
        vs = self.keys()
        if not self.directed:
            return vs
        vs = set(vs) | set([_.keys() for _ in vs])
        return list(vs)

    def edges(self):
        """ Get all edges in this Graph as a list.
        """
        edges = set()
        for ws in self.itervalues():
            for e in ws.itervalues():
                edges.add(e)
        return list(edges)

    def out_vertices(self, v):
        """ Get all vertices connect to v directly.
        """
        vertices = self.get(v, {}).keys()
        return vertices

    def out_edges(self, v):
        """ Get all edges connected to v.
        """
        edges = self.get(v, {}).values()
        return edges

    def add_all_edges(self):
        """ add edges to Graph to make graph complete graph.
        """
        all_vertices = set(self.vertices())
        for v in all_vertices:
            v_out_vertices = self.get(v)
            if not v_out_vertices:
                self[v] = v_out_vertices = {}
            for w in all_vertices - set(v_out_vertices.keys() + [v]):
                self.add_edge(Edge(v, w))



def main(script, *args):
    v = Vertex('v')
    print v
    w = Vertex('w')
    print w
    e = Edge(v, w)
    print e
    g = Graph([v,w], [e])
    print g

    va = Vertex('va')
    e1 = Edge(va, w)
    g.add_edge(e1)
    print g.out_edges(w)
    print g.out_vertices(w)
    g.add_all_edges()
    print g.out_edges(v)
    print g.edges()

if __name__ == '__main__':
    import sys
    main(*sys.argv)
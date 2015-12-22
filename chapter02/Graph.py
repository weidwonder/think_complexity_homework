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
        self.vs = []
        self.es = []
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
        self.vs.append(v)

    def add_edge(self, e_or_v, w=None):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        if w:
            e_or_v = Edge(e_or_v, w)
        v, w = e_or_v
        for _ in e_or_v:
            self.add_vertex(_)
        if self[v].get(w):
            return
        self[v][w] = e_or_v
        if not self.directed:
            self[w][v] = e_or_v
        self.es.append(e_or_v)

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
            e = self[v][w]
            self.es.remove(e)
            del self[v][w]
            if not self.directed:
                e = self[w][v]
                del self[w][v]
            return True
        except:
            return False

    def vertices(self):
        """ Get all vertices in this Graph as a list.
        """
        return self.vs

    def edges(self):
        """ Get all edges in this Graph as a list.
        """
        return self.es

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

    def add_regular_edges(self, k):
        """ Add edges to Graph to make graph regular graph.
        """
        # TODO to make method support graphs has already had edges.
        if self.es:
            raise ValueError('This graph already has edges.')
        num_v = len(self.vs)
        if not isinstance(k, int) or k < 0 or k > num_v - 1 or num_v * k % 2:
            raise ValueError('Probability is wrong. must int and in range of 0 ~ n-1 and nk is even.')
        is_k_odd = k % 2
        is_n_odd = num_v % 2
        if is_n_odd:
            multiple_2 = k / 2
            middle_left = num_v / 2
            for src_i in xrange(num_v):
                v = self.vs[src_i]
                for tar_i in xrange(1, 1 + multiple_2):
                    va = self.vs[(src_i + middle_left - tar_i + 1) % num_v]
                    vb = self.vs[(src_i + middle_left + tar_i) % num_v]
                    self.add_edge(v, va)
                    self.add_edge(v, vb)
        else:
            multiple_2 = k / 2
            middle = num_v / 2
            for src_i in xrange(num_v):
                v = self.vs[src_i]
                for tar_i in xrange(1, 1 + multiple_2):
                    va = self.vs[(src_i + middle - tar_i) % num_v]
                    vb = self.vs[(src_i + middle + tar_i) % num_v]
                    self.add_edge(v, va)
                    self.add_edge(v, vb)
                if is_k_odd:
                    self.add_edge(v, self.vs[(src_i + middle) % num_v])

    def is_connected(self):
        if len(self.vs) <= 1: return True
        start_node = self.vs[0]
        to_visit = set(self[start_node].keys())
        visited = set()
        while to_visit:
            start_node = to_visit.pop()
            visited.add(start_node)
            to_visit = to_visit | set(self[start_node].keys()) - visited
        return visited == set(self.vs)


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

def test_is_connected(*args):
    g = Graph()
    v_list = []
    for x in range(10):
        v = Vertex(str(x))
        g.add_vertex(v)
        v_list.append(v)
    g.add_edge(v_list[1], v_list[2])
    g.add_edge(v_list[3], v_list[4])
    g.add_edge(v_list[6], v_list[5])
    g.add_edge(v_list[9], v_list[0])
    g.add_edge(v_list[2], v_list[3])
    g.add_edge(v_list[4], v_list[5])
    g.add_edge(v_list[8], v_list[9])
    g.add_edge(v_list[1], v_list[0])
    print g.is_connected()

    g.add_all_edges()
    print g.is_connected()


if __name__ == '__main__':
    import sys
    # main(*sys.argv)
    test_is_connected()
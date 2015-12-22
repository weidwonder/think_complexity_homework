from random import random
from Graph import Graph


class RandomGraph(Graph):

    def add_random_edges(self, p):
        """ Add edges to Graph to make graph random graph.
        """
        # TODO to make method support graphs has already had edges.
        if self.es:
            raise ValueError('This graph already has edges.')
        num_v = len(self.vs)
        if not isinstance(p, float) or p < 0 or p > 1:
            raise ValueError('`p` must be a float in range from 0 to 1.')
        if_connect = lambda : random() < p
        for i in xrange(num_v - 1):
            for j in xrange(i + 1, num_v):
                if if_connect():
                    self.add_edge(self.vs[i], self.vs[j])

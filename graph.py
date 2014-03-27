# -*- encoding: utf-8 -*-

# A very simple implementation of graphs in python, including graphs
# embedded in the plane.

class Graph():
    def size(self):
        return len(self.vertices())

class AdjacencyGraph(Graph):
    '''A graph represented as a dictionary which maps vertices to sets of neighbors.'''
    def __init__(self, adjacency):
        self.adjacency = {u : set(vs) for (u,vs) in adjacency.items()}

    def __repr__(self):
        return 'AdjacencyGraph({0})'.format(self.adjacency)

    def vertices(self):
        '''The set vertices of the graph as an iterator.'''
        return self.adjacency.keys()

    def edges(self):
        '''The edges of the graph as an iterator.'''
        for (u, vs) in self.adjacency.items():
            for v in vs:
                yield (u,v)

    def source(self, e):
        '''The source of the given edge.'''
        return e[0]

    def target(self, e):
        '''The target of the given edge.'''
        return e[1]

    def neighbors(self, v):
        '''The neighbors of the given vertex.'''
        return self.adjacency[v]

class SimpleGraph(Graph):
    '''A graph without loops, undirected edges and at most one edge between two vertices.'''

    def __init__(self, vertices, edges):
        '''A list of vertices and a list of (unordered) pairs of vertices.'''
        self.vertex_set = set(vertices)
        self.edge_set = set(edges)

    def __repr__(self):
        return 'SymmtericGraph({0},{1})'.format(self.vertex_set, self.edge_set)

    def vertices(self):
        '''The set of vertices as an iterator.'''
        return self.vertex_set

    def edges(self):
        '''The set of edges as an iterator.'''
        return self.edge_set

def complete_graph(n):
    '''Complete graph on n vertices.'''
    return SimpleGraph(range(n),
                       [(i,j) for j in range(n) for i in range(j)])

def perm_compose(p,q):
    return tuple([p[i] for i in q])

def cayley_graph(generators, composition=perm_compose):
    gs = set(generators)
    adj = {}

    def generate(x):
        if x not in adj:            
            adj[x] = {composition(x,y) for y in gs}
            for z in adj[x]: generate(z)

    for x in gs: generate(x)
    return AdjacencyGraph(adj)

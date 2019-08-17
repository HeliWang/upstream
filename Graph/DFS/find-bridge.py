import graph
import unittest


class VertexColor:
    """
    When doing a DFS, any node is in one of three states:
      1. before being visited
      2. during recursively visiting its descendants
      3. after all its descendants have been visited and the recursion has backtracked from the vertex
    """
    WHITE = 1  # State 1
    GREY = 2  # State 2
    BLACK = 3  # State 3


class FindBridges:
    def __init__(self, g):
        self.g = g
        self.in_cycle = [False] * g.V
        self.path_to = {}  # visited vertex v -> vertex w, w found v in dfs tree
        self.state = [VertexColor.WHITE] * g.V

    def mark_cycle(self, w, v):
        """
        :param w: a vertex of the cycle
        :param v: a vertex of the cycle, a descendent of w in dfs tree
        """
        cycle = []
        while v != w:
            cycle.append(v)
            v = self.path_to[v]
        cycle.append(w)
        for c in cycle:
            self.in_cycle[c] = True

    def explore_cycle_dfs(self, u, v):
        self.state[v] = VertexColor.GREY
        for w in self.g.adj(v):
            if w == u: continue
            if self.state[w] == VertexColor.GREY:  # found back edge v-w
                self.mark_cycle(w, v)
            elif self.state[w] == VertexColor.WHITE:
                self.path_to[w] = v
                self.explore_cycle_dfs(v, w)
            # else for self.state[w] == VertexColor.BLACK, say 5 -> 8 the children
        self.state[v] = VertexColor.BLACK

    def find_bridges(self):
        self.path_to[0] = 0
        self.explore_cycle_dfs(0, 0)
        res = []
        visited = set()
        for v in range(self.g.V):
            visited.add(v)
            for w in self.g.adj(v):
                if w in visited:
                    continue
                if self.in_cycle[w] and self.in_cycle[v]:
                    continue
                res.append((v, w))
        return res


g = graph.Graph.import_graph("input/1.txt")
f = FindBridges(g)
assert f.find_bridges() == [(2, 3), (3, 6), (6, 7)]

g = graph.Graph.import_graph("input/2.txt")
f = FindBridges(g)
assert f.find_bridges() == [(2, 3), (3, 6), (6, 7)]

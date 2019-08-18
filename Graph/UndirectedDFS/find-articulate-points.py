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


class ArticulatePoints:
    def __init__(self, g):
        """
        :param g: Graph Object
        """
        self.g = g
        self.d = [0] * g.V
        # self.d[v] is the time when a vertex is discovered by a dfs (before visiting its descendants)
        self.vertexColor = [VertexColor.WHITE] * g.V
        self.low = [0] * g.V
        # self.low[v] = min{d[v], d[w] : (u,w) is a back edge for some descendents u of v}
        # So, low(v) is the discovery time of the vertex closest to the
        #   root and reachable from v by following zero or more edges
        #   downward, and then at most one back edge in a DFS tree
        self.cnt = 0  # a increasing counter, increase by 1 when dfs visiting a node never visited before
        self.is_articulate = [False] * g.V
        self.dfs(-1, 0)

    def __dfs(self, u, v):
        """A sample dfs with d and color traced.
        :param u: the parent of v, None if v is the starting point of the dfs
        :param v: a vertex

        Note: we can also use  parent[v] to keeps the record of parent of each vertex
        """
        self.cnt += 1
        self.vertexColor[v] = VertexColor.GREY
        self.d[v] = self.cnt
        for w in self.g.adj(v):
            if self.vertexColor[w] == VertexColor.WHITE:
                self.__dfs(v, w)
            elif w != u:  # is a back-edge but not incident with the parent of v
                # self.vertexColor[w] can be VertexColor.GREY or VertexColor.Black
                pass
        self.vertexColor[v] = VertexColor.BLACK

    def dfs(self, u, v):
        """Check if vertex v is articulate and update self.is_articulate[v]
        :param u: the parent of v, None if v is the starting point of the dfs
        :param v: a vertex
        """
        self.cnt += 1
        self.vertexColor[v] = VertexColor.GREY
        self.d[v] = self.cnt
        self.low[v] = self.cnt
        childCount = 0
        for w in self.g.adj(v):
            if w == u:
                continue
            if self.vertexColor[w] == VertexColor.WHITE:
                childCount += 1
                self.dfs(v, w)
                if self.d[v] <= self.low[w] and u != -1:  # v not the root
                    self.is_articulate[v] = True
        for w in self.g.adj(v):
            if w == u:
                continue
            self.low[v] = min(self.low[w], self.low[v])
        self.vertexColor[v] = VertexColor.BLACK
        if u == -1 and childCount > 1:
            self.is_articulate[v] = True
            # root of DFS is an articulation point if it has more than 1 child

    def is_articulate(self, v):
        """
        :param v: vertex
        :return: return true if the vertex v is articulate
        """
        return self.is_articulate[v]

    def get_articulate_vertices(self):
        """Suppose v is a non-root vertex of the DFS tree T,
        Then v is an articulation point of G if and only if there is a child w of v
           in DFS Tree T (Not in original Tree) with low(w) >= d[v]

        Note: A point in a graph is called an Articulation Point or Cut-Vertex if upon removing that point let's say P,
        there is at least one child(C) of it(P) , that is disconnected from the whole graph.
        In other words at least one of P's child C cannot find a "back edge".

        :return: a list of articulation vertices
        """
        res = []
        # if len(self.g.adj(0)) == 1:
        #    self.is_articulate[0] = False
        for i, v in enumerate(self.is_articulate):
            if self.is_articulate[i]:
                res.append(i)
        return res


class TestSolution(unittest.TestCase):
    def test_1(self):
        g = graph.Graph.import_graph("input/1.txt")
        s = ArticulatePoints(g)
        assert list(s.get_articulate_vertices()) == [2, 3, 6]

    def test_2(self):
        g = graph.Graph.import_graph("input/2.txt")
        s = ArticulatePoints(g)
        assert sorted(s.get_articulate_vertices()) == [2, 3, 5, 6]

    def test_3(self):
        g = graph.Graph.import_graph("input/3.txt")
        s = ArticulatePoints(g)
        assert sorted(s.get_articulate_vertices()) == [0, 2, 4, 5]


unittest.main()

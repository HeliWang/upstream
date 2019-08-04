import graph

g = graph.Graph.import_graph("input/1.txt")


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
        self.d = [0] * g.V()
        # self.d[v] is the time when a vertex is discovered by a dfs (before visiting its descendants)
        self.vertexColor = [VertexColor.WHITE] * g.V()
        self.low = [0] * g.V()
        # self.low[v] = min{d[v], d[w] : (u,w) is a back edge for some descendents u of v}
        # So, low(v) is the discovery time of the vertex closest to the
        #   root and reachable from v by following zero or more edges
        #   downward, and then at most one back edge
        self.cnt = 0  # a increasing counter, increase by 1 when dfs visiting a node never visited before

    def __dfs(self, u, v):
        """A sample dfs with d and color traced.
        :param u: the parent of v, None if v is the starting point of the dfs
        :param v: a vertex
        """
        self.cnt += 1
        self.vertexColor[v] = VertexColor.GREY
        self.d[v] = self.cnt
        for w in self.g.adj(v):
            if self.vertexColor[w] == VertexColor.GREY:
                self.__dfs(w)
            elif w != u:  # is a back-edge but not incident with the parent of v
                # self.vertexColor[w] can be VertexColor.GREY or VertexColor.Black
                pass
        self.vertexColor[v] = VertexColor.BLACK

    def is_articulate(self, v):
        """
        :param v: vertex
        :return: return true if the vertex v is articulate
        """
        pass

    def get_articulate_vertices(self):
        """Suppose v is a non-root vertex of the DFS tree T,
        Then v is an articulation point of G if and only if there is a child w of v
        in T with low(w) >= d[v]
        :return: a list of articulation vertices
        """
        pass

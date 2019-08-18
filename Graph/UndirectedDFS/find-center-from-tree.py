"""
Given a connected graph with no cycle (tree)
(1) A path that does not repeat vertices is called a simple path. Design an algorithm to find the longest simple path in the graph.
(2) Design an algorithm to find a vertex such that its maximum distance from any other vertex is minimized.

A Graph Class is given for your convenience:
g = Graph()

# of vertices: g.V
Vertices will have id 0, 1, ..., V - 1
e.g. The left graph will have g.V = 10

g.adj(vertexID) will return a list of the vertices adjacent to vertex v with the vertexID
e.g g.adj(1) = [0, 2, 6]
"""
import graph
import unittest
import sys


class FindCenter:
    def __init__(self, g):
        """Initialize to find the center of Graph g
        Args:
            g: Graph with no cycle
        """
        self.g = g

    def __init_path_array(self, s):
        self.edge_to = [-1] * self.g.V  # edge_to[v] = last edge on path to v from a starting point s
        self.dist_to = [sys.maxsize] * self.g.V  # dist_to[v] = length of shortest s->v path
        self.edge_to[s] = s
        self.dist_to[s] = 0

    def __longest_path(self, s, parent=None):
        """Find longest path starting from vertex s in a graph g

        Args:
            s: vertex id
        """
        for w in self.g.adj(s):
            if parent != w:
                # important!! although dfs to the tree will not result in visiting duplicate vertices, it
                #  can still visit parent.
                self.edge_to[w] = s
                self.dist_to[w] = self.dist_to[s] + 1
                self.__longest_path(w, s)

    def path_to(self, v):
        """ Returns a shortest path from {@code s} (or sources) to {@code v}, or
        Args:
            v: the vertex
        Returns:
            the sequence of vertices on a shortest path, as a list
        """
        stack = []
        cur = v
        while self.dist_to[cur] != 0:
            stack.append(cur)
            cur = self.edge_to[cur]
        stack.append(cur)
        return stack[::-1]

    def find_longest_path(self):
        """Find longest path in the graph g

        Returns:
            a list of vertices representing the path
        """
        # Pick any vertex s, say vertex 0
        self.__init_path_array(0)

        # Compute the path from s to every other vertex.
        self.__longest_path(0)

        # Let w be the vertex with the largest path distance.
        w = self.dist_to.index(max(self.dist_to))

        # Compute the path from w to every other vertex.
        self.__init_path_array(w)
        self.__longest_path(w)

        # Let x be the vertex with the largest path distance.
        x = self.dist_to.index(max(self.dist_to))

        # The path from w to x gives the longest path.
        return self.path_to(x)

    def find_center(self):
        longest_path = self.find_longest_path()
        # Note:
        #    Find mid when array is in odd length or higher mid when in even length
        #      longest_path[len(longest_path) // 2]
        #    Find mid when array is in odd length or lower mid when in even length
        #      longest_path[(len(longest_path) - 1) // 2]
        return longest_path[len(longest_path) // 2]


class TestFindCenter(unittest.TestCase):
    def test_1(self):
        g = graph.Graph.import_graph("input/3.txt")
        s = FindCenter(g)
        assert s.find_longest_path() == [1, 5, 4, 0, 2, 3]
        assert s.find_center() == 0

    def test_2(self):
        g = graph.Graph.import_graph("input/4.txt")
        s = FindCenter(g)
        assert s.find_longest_path() == [5, 4, 2, 1, 6, 7]
        assert s.find_center() == 1

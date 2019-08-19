"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0
  you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
  is it possible for you to finish all courses?

Solve by by finding a cycle in the directed graph
"""
from collections import defaultdict


class VertexColor:
    """
    When doing a DFS, any node is in one of three states:
      1. before being visited
      2. in stack frame, during recursively visiting its descendants
      3. after all its descendants have been visited and the recursion has backtracked from the vertex
    """
    WHITE = 1  # State 1
    GREY = 2  # State 2
    BLACK = 3  # State 3


class Solution(object):
    def build_graph(self, prerequisites, edge):
        for i, j in prerequisites:
            edge[i].append(j)

    def dfs(self, v, edge, color):
        color[v] = VertexColor.GREY
        for w in edge[v]:
            if color[w] == VertexColor.WHITE:
                if self.dfs(w, edge, color): return True  # max recursion depth exceeded
            ## if w == u: continue NOT RIGHT in DIRECTED GRAPH
            if color[w] == VertexColor.GREY:
                return True
        color[v] = VertexColor.BLACK
        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :param numCourses
        :param prerequisites:  Some courses may have prerequisites,
         for example to take course 0 you have to first take course 1,
         which is expressed as a pair: [0,1]
        :return: True if possible to finish all courses - if there is no SCC with size larger than 1
        """
        n = numCourses
        edge = defaultdict(list)  # i -> [j, k, l] adjacency list
        self.build_graph(prerequisites, edge)
        color = [VertexColor.WHITE] * n
        for i in range(n):
            if color[i] == VertexColor.WHITE:
                if self.dfs(i, edge, color):
                    return False
        return True

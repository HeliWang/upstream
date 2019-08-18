"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0
  you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
  is it possible for you to finish all courses?

Solve by by finding SCC with size larger than 1
"""
from collections import defaultdict


class Solution(object):
    def build_graph(self, prerequisites, edge, r_edge):
        for i, j in prerequisites:
            # i -> j in original graph
            edge[i].append(j)
            r_edge[j].append(i)

    def dfs(self, v, edge, res, visited):
        for w in edge[v]:
            if w not in visited:
                visited.add(w)
                self.dfs(w, edge, res, visited)
        res.append(v)

    def topological_sort(self, n, edge):
        """
        :return: a list of node in topo sort of given graph
        """
        visited = set()
        res = []
        for i in range(n):
            if i not in visited:
                visited.add(i)
                self.dfs(i, edge, res, visited)
        return res[::-1]

    def find_scc(self, v, edge, scc, scc_id):
        visited = set()
        res = []
        visited.add(v)
        self.dfs(v, edge, res, visited)
        for w in res:
            scc[w] = scc_id

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
        r_edge = defaultdict(list)  # reversed edge in adjacency list
        self.build_graph(prerequisites, edge, r_edge)
        reversed_graph_topo = self.topological_sort(n, r_edge)
        # find SCC
        scc = [None] * n
        numSCC = 0
        for i in reversed_graph_topo:
            if scc[i] != None: continue
            self.find_scc(i, edge, scc, numSCC)
            numSCC += 1
        if numSCC == n: return True
        return False

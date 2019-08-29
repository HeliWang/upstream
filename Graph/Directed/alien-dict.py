"""
# Solution1: Word Pairwise Comparison + Post order Traversal + Topo Order Check
"""
import collections


class Solution:
    def topo_dfs(self, cur_char, visited, edge_map, topo_result):
        for neighbour in edge_map[cur_char]:
            if neighbour in visited: continue
            # x -> y, x -> z -> y
            visited.add(neighbour)
            self.topo_dfs(neighbour, visited, edge_map, topo_result)
        topo_result.append(cur_char)

    def alienOrder(self, words):
        n = len(words)  # 6
        edge_map = collections.defaultdict(set)  # x -> set[chars less than x]
        char_set = set()
        for i in range(n - 1):
            word1 = words[i]  # wrt       wxtzz
            word2 = words[i + 1]  # wrtzx     wxz
            char_set = char_set | set(word1)
            i = 0
            while i < len(word1) and i < len(word2):
                if word1[i] == word2[i]:
                    i += 1
                    continue
                edge_map[word1[i]].add(word2[i])
                break
        char_set = char_set | set(words[-1])
        visited = set()
        topo = []
        for c in char_set:
            if c not in visited:
                visited.add(c)
                self.topof(c, visited, edge_map, topo)
        topo = topo[::-1]
        pairs = zip(topo, list(range(len(topo))))
        char_index_dict = dict(pairs)
        for edge in edge_map.items():
            a, bs = edge
            for b in bs:
                if char_index_dict[a] > char_index_dict[b]:
                    return ""
        return "".join(topo)


"""
# Solution2: BFS Pairwise Comparison + In-degree Topo Order Traversal
"""
import collections
from collections import deque


class Solution:
    def alienOrder(self, words):  # ["wrt","wrf","er","ett","rftt"]
        n = len(words)
        in_edge, out_edge = collections.defaultdict(set), collections.defaultdict(set)
        char_set = set(''.join(words))
        q = deque([words])
        while q:
            # BFS should be layer by layer;
            # Otherwise the end of this layer and the start of next layer will be connected;
            # however, the layer is not the traditional one
            # need to separate different group within one layer,
            #    otherwise the elements in different group will be connected
            group = q.popleft()
            for i in range(len(group) - 1):
                word1 = group[i]
                word2 = group[i + 1]
                if word1[0] != word2[0]:
                    out_edge[word1[0]].add(word2[0])
                    in_edge[word2[0]].add(word1[0])
                else:
                    new_group = []
                    if len(word1) > 1: new_group.append(word1[1:])
                    if len(word2) > 1: new_group.append(word2[1:])
                    q.append(new_group)

        topo_q = deque([c for c in char_set if len(in_edge[c]) == 0])
        res = []
        while topo_q:
            c = topo_q.popleft()
            res.append(c)
            for out in out_edge[c]:
                in_edge[out].remove(c)
                if len(in_edge[out]) == 0: topo_q.append(out)
        return "".join(res) if len(res) == len(char_set) else ""

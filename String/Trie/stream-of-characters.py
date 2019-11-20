import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class StreamChecker:
    """
    Basically, put all the words in a trie.
    Then, as queries come in, maintain a list of partial
      queries that still have a chance of forming a word as more queries flow in.
      This is just a list of pointers to nodes in the trie. On each round,
      check through the partial queries.
      If the partial query does not have the new letter in its children, it is discarded;
      otherwise, it is advanced so it points to the child, and is retained for the next round.
    If a word is made by extending any partial, we have a match and will return true;
    otherwise, return false .
    """

    def __init__(self, words):
        self.trie = TrieNode()
        for word in words:
            self.insert(word)

        self.partials = [self.trie]

    def query(self, l):
        new_partials, match = [self.trie], False
        for p in self.partials:
            if l in p.children:
                new_partials.append(p.children[l])
                if p.children[l].is_word:
                    match = True
        self.partials = new_partials
        return match

    def insert(self, word):
        curr = self.trie
        for c in word:
            curr = curr.children[c]
        curr.is_word = True

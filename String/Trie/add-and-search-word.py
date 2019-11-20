import collections


class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary():
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word):
        node = self.trie
        for c in word:
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the data structure.
         A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """

        def dfs(node=self.trie, i=0):
            if i == len(word):
                if node.isWord:
                    self.result = True
                return
            if word[i] == ".":
                for child in node.children.values():
                    dfs(child, i + 1)
            else:
                if word[i] in node.children:
                    dfs(node.children[word[i]], i + 1)

        self.result = False
        dfs()
        return self.result

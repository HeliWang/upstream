# """
# https://leetcode.com/problems/guess-the-word/
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """
import random


class Solution:
    def diff(self, secret, word):
        c = 0
        for i in range(len(secret)):
            if secret[i] == word[i]:
                c += 1
        return c

    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        while len(wordlist) != 1:
            i = random.randrange(0, len(wordlist) - 1)
            word = wordlist[i]
            word_target_diff = master.guess(word)
            wordlist = list(filter(lambda w: self.diff(w, word) == word_target_diff, wordlist))
        master.guess(wordlist[0])

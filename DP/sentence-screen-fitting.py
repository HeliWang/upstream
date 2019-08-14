"""
Given a rows x cols screen and a sentence represented by a list of non-empty words,
find how many times the given sentence can be fitted on the screen.

width = 10 (chars)
height = 15

[hello, world]
hello-
world-
hello-
world-

[hello, help]
hello-help
hello-help
hello-help

[hi, hi]
hi-hi-hi
hi-hi-hi
hi-hi

[hello, world] w=10, h=3
hello-
world
"""


def count_sentence(w, h, word_list):
    """
    :param w: width
    :param h: height
    :param word_list: the list of words in a sentence
    :return: count of filled sentence
    """
    i = 0  # current world of current sentence to put
    sentence_count = 0
    for r in range(h):
        left_w = w
        while True:
            word_len = len(word_list[i])
            # the word is not the first word in the row, add a space before adding the word
            if left_w != w:
                word_len += 1
            if word_len <= left_w:
                left_w -= word_len
                i = (i + 1) % len(word_list)
                if i == 0:
                    sentence_count += 1
            else:
                break
    return sentence_count


"""
Test for count_sentence(10, 4, ["hello", "world"])

i = 0
sentence_count = 0

when r = 0 
 left_w = 10
 word_len = 5
 left_w = 5
 i = 1

 left_w = 5
 word_len = 6

when r = 1
 left_w = 10
 word_len = 5
 left_w = 5
 i = 2 % 2 = 0
 sentence_count = 1
 
when r = 2
when r = 3
sentence_count = 2

Finish Clarification: 9 mins
Finish Coding: 17 mins
Finish Test: 21 mins
"""


class Solution(object):

    def wordsTyping(self, sentence, rows, cols):
        jump_map = {}
        # idx of first word of a  row ->
        #  (index of first word of the next row,
        #    the # of end word bypass in the row)

        # ["I", "had", "apple", "pie"]
        # 4, 5
        # I
        n = len(sentence)
        for i, word in enumerate(sentence):
            j = i + 1
            c = cols - len(word)
            if c < 0:
                jump_map[i] = (i, 0)
                continue
            while c >= 1 + len(sentence[j % n]):
                c -= (1 + len(sentence[j % n]))
                j += 1
            jump_map[i] = (j % n, j // n)
        # count sentences
        i = 0  # i is the current index of word
        res = 0
        for j in range(rows):
            next_i, completed = jump_map[i]
            res += completed
            i = next_i
        return res

def findAndReplacePattern(self, words, p):
    def get_pattern(w):  # Normalise Word
        m = {}
        return [m.setdefault(c, len(m)) for c in w]
        # compare to m.get(key, [default]), setdefault will also set the default value as value to the key

    p_pattern = get_pattern(p)
    return [w for w in words if get_pattern(w) == p_pattern]

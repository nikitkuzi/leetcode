class Trie:
    def __init__(self, words, index, level):
        self.index = index
        self.level = level
        self.children = {}
        self.smallest_descendent = None
        self.build(words)
    def build(self, words):
        # print(words, list(map(lambda x: self.index[x], words)))
        if len(words) == 1:
            self.smallest_descendent = min(words, key=lambda x: self.index[x])
            return

        d = defaultdict(list)
        for w in words:
            if len(w) > self.level:
                d[w[self.level]].append(w)
        self.smallest_descendent = min(words, key=lambda x: self.index[x])
        # print(words, self.smallest_descendent, self.index[self.smallest_descendent])
        assert self.smallest_descendent is not None, words

        for k, v in d.items():
            self.children[k] = Trie(v, self.index, self.level + 1)

    def query(self, w):
        if self.level >= len(w) or w[self.level] not in self.children:
            return self.index[self.smallest_descendent][1]
        return self.children[w[self.level]].query(w)


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        words = [w[::-1] for w in wordsContainer]
        queries = [w[::-1] for w in wordsQuery]

        index = {}
        for i, w in enumerate(words):
            if w not in index:  # to account for duplicate words
                index[w] = (len(w), i)

        t = Trie(words, index, 0)
        res = [t.query(w) for w in queries]
        return res
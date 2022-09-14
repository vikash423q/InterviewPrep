#   https://leetcode.com/problems/design-add-and-search-words-data-structure/


class Node:
    def __init__(self):
        self.end = False
        self.char_map = {}


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        def add(wd: str, node: Node):
            if not wd:
                node.end = True
                return
            if wd[0] not in node.char_map:
                node.char_map[wd[0]] = Node()
            return add(wd[1:], node.char_map[wd[0]])

        add(word, self.root)

    def search(self, word: str) -> bool:
        def wordsearch(wd: str, node: Node):
            if not wd:
                return node.end

            if wd[0] == '.':
                for ch in node.char_map:
                    if wordsearch(wd[1:], node.char_map[ch]):
                        return True
                return False

            elif wd[0] not in node.char_map:
                return False

            return wordsearch(wd[1:], node.char_map[wd[0]])

        return wordsearch(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

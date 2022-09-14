#   https://leetcode.com/problems/implement-trie-prefix-tree/


class Node:
    def __init__(self):
        self.end = False
        self.char_map: dict = {}


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        def insert_node(wd: str, node: Node):
            if not wd:
                node.end = True
                return
            if wd[0] not in node.char_map:
                node.char_map[wd[0]] = Node()
            insert_node(wd[1:], node.char_map[wd[0]])

        insert_node(word, self.root)

    def search(self, word: str) -> bool:
        def search_word(wd: str, node: Node):
            if not wd:
                return node.end
            if wd[0] not in node.char_map:
                return False
            return search_word(wd[1:], node.char_map[wd[0]])

        return search_word(word, self.root)

    def startsWith(self, prefix: str) -> bool:
        def starts(wd: str, node: Node):
            if not wd:
                return True
            if wd[0] not in node.char_map:
                return False
            return starts(wd[1:], node.char_map[wd[0]])

        return starts(prefix, self.root)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

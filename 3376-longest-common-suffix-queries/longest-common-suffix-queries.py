class Node:
    def __init__(self):
        self.children = {}
        self.index = None
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, index, word, wordsContainer) -> None:
        curr  = self.root
        if curr.index is None:
            curr.index = index
        else:
            if len(wordsContainer[index]) < len(wordsContainer[curr.index]):
                curr.index = index
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]

            if curr.index is None:
                curr.index = index
            else:
                old_len = len(wordsContainer[curr.index])
                new_len = len(wordsContainer[index])
                if new_len < old_len:
                    curr.index = index           

    def suffix(self, word) -> int:
        curr = self.root
        for ch in word:
            if ch in curr.children:
                curr = curr.children[ch]
            else:
                return curr.index
        return curr.index


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        prefix_tree = Trie()

        for index, word in enumerate(wordsContainer):
            prefix_tree.insert(index, word[::-1], wordsContainer)
        
        output = [0] * len(wordsQuery)

        for index, word in enumerate(wordsQuery):
            prefix_index = prefix_tree.suffix(word[::-1])

            output[index] = prefix_index
        return output


        
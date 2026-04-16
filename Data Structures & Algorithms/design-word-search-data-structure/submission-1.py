class TreeNode:
    def __init__(self):
        self.children = {}
        self.word = False
    
    def dfs(self, word: str) -> bool:
        if not word:
            return self.word
        if not self.children:
            return False
        left = word[0]
        right = word[1:]

        if left in self.children:
            return self.children[left].dfs(right)
        elif left == ".":
            out = False
            for c in self.children:
                out = out | self.children[c].dfs(right)
            return out
        else:
            return False
class WordDictionary:
    def __init__(self):
        self.root = TreeNode()
    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TreeNode()
            cur = cur.children[i]
        cur.word = True
    def search(self, word: str) -> bool:
        return self.root.dfs(word)
        


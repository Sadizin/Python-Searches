#Arvore trie com palvras

class Trienode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word= False  #autocomplete 'app' true e ap false
        
class Trie: 
    def __init__(self):
        self.root = Trienode()
        
    def insert(self, word):
        current_node = self.root 
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Trienode() 
            current_node = current_node.children[char]
        current_node.is_end_of_word = True
    
    def search(self, word): #verificar se a palavra existe na trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word
    
    def starts_with(self, prefix): #verificar se a palavra existe na trie, começa com um pre-fixo
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
    
trie = Trie()
trie.insert('apple')
trie.insert('app')
trie.insert('Sadi')
trie.insert('Sadan Hussein')

print(trie.search('Sadi'))
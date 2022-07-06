class Node:
    def __init__(self):
        self.dict = {}
        self.comp = False
    
class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.dict:
                cur.dict[c] = Node()
            cur = cur.dict[c]
        cur.comp = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.dict:
                return False
            cur = cur.dict[c]
        
        return cur.comp
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.dict:
                return False
            cur = cur.dict[c]
        
        return True
      
'''
FAILED
class Node:
    def __init__(self, wrd=""): # 1. word init failed
        self.child = []
        self.word = wrd
        self.comp = True # 4-2. passing word divided in middle
    
class Trie:
    def __init__(self):
        self.root = Node("")
        self.root.comp = False

    def insert(self, word: str) -> None:
        idx = 0
        cur = self.root
        comp = word[idx:]
        cont = True
        
        while cont:
            comp = word[idx:]
            cont = False
            
            #print("i", idx, comp[:10])
            for n in cur.child:
                #print(n.word[:10], comp[:10])
                if n.word == comp:
                    n.comp = True
                    return
                elif n.word[0] == comp[0]: # 4. MLE: divided in middle
                    i = 1
                    while i < len(n.word) and i < len(comp):
                        if n.word[i] != comp[i]:
                            break
                        i += 1
                    count = 2
                    if i < len(n.word):
                        node = Node(n.word[i:])
                        n.child.append(node)
                        count -= 1
                    if i < len(comp):
                        node = Node(comp[i:])
                        n.child.append(node)
                        count -= 1
                    if count == 0:
                        n.comp = False
                    n.word = n.word[:i]
                    return
                    #print(comp[:10], n.word[:10])
                elif comp.startswith(n.word):
                    idx += len(n.word)
                    cur = n
                    cont = True
                    break
                else: # 3. add new word
                    node = Node(comp)
                    cur.child.append(node)
                    return
                
        if not cur.child:
            node = Node(comp) # 2. inserted not sliced word
            cur.child.append(node)
            #print(node.word[:10])
                    
                    

    def search(self, word: str) -> bool:
        idx = 0
        cur = self.root
        cont = True
        
        while cont:
            comp = word[idx:]
            cont = False
            
            #print("s", word[:10])
            for n in cur.child:
                #print(n.word[:10])
                if n.word == comp:
                    return n.comp
                if len(n.word) < len(comp) and comp.startswith(n.word):
                    idx += len(n.word)
                    cur = n
                    cont = True
                    break
                    
        return False
            
        
    def startsWith(self, prefix: str) -> bool:
        idx = 0
        cur = self.root
        cont = True
        
        while cont:
            comp = prefix[idx:]
            cont = False
            
            #print("sw", prefix[:10])
            for n in cur.child:
                #print(n.word)
                if n.word == comp:
                    return True
                if len(n.word) > len(comp) and n.word.startswith(comp):
                    return True
                if len(n.word) < len(comp) and comp.startswith(n.word):
                    idx += len(n.word)
                    cur = n
                    cont = True
                    break
                        
        return False
'''

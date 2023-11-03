import heapq
class Node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.right = right
        self.left = left
        self.huff = ''
    
    def __lt__(self, nxt):
        return self.freq < nxt.freq

    
def printNodes(root, val = ''):
    newVal = val + str(root.huff)
    
    if root.left:
        printNodes(root.left, newVal)
    if root.right:
        printNodes(root.right, newVal)
    
    if not root.left and not root.right:
        print(f"{root.symbol} -> {newVal}")

chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

nodes = []

for x in range(len(chars)):
    heapq.heappush(nodes, Node(freq[x], chars[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    
    left.huff = 0
    right.huff = 1
    
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    
    heapq.heappush(nodes, newNode)

printNodes(nodes[0])

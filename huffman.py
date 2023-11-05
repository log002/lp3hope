import heapq

class node:
    def __init__(self, freq, symbol, left = None, right = None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''
    
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    if not node.left and not node.right:
        print("{}->{}".format(node.symbol, newVal))

if __name__ == "__main__":
    s = input("Enter the String: ")
    res = {}
    
    for i in s:
        if(i == ' '):
            continue
        res[i] = res.get(i, 0) + 1
    print(res)
    chars = []
    freq = []
    
    for i in res:
        chars.append(i)
        freq.append(res[i])
    nodes = []
    
    for i in range(len(chars)):
        heapq.heappush(nodes, node(freq[i], chars[i]))
    
    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)
        
        left.huff = 0
        right.huff = 1
        
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)
    
    printNodes(nodes[0])

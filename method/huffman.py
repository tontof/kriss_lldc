# https://github.com/python/cpython/blob/3.10/Lib/heapq.py
from heapq import heappush, heappop, heapify
from collections import Counter

def tree_binary(tree):
    if isinstance(tree, list):
        return '1'+tree_binary(tree[0])+tree_binary(tree[1])
    else:
        return '0'+"{0:08b}".format(ord(tree))

def binary_tree(binary):
    current = 0
    expected = 1
    code = ""
    dico = {}
    i = 0
    while current != expected:
        c = binary[i]
        i += 1
        if c == '0':
            current += 1
            dico[code] = chr(int(binary[i:i+8],2))
            if code[len(code)-1] == '0':
                code = code[:-1]
                code += "1"
            else:
                code = code[:-2]
                code += "1"
            i += 8
        else:
            expected += 1
            code += "0"
    return [dico, binary[i:]]

def dico_tree(dico):
    tree = []
    parent = tree
    for item in dico.items():
        current = tree
        for idx in item[1]:
            try:
                parent = current
                current = current[int(idx)]
            except IndexError as e:
                current.append([[],[]])
                try:
                    current = current[int(idx)]
                except IndexError as e:
                    current.append([[],[]])
                    current = current[int(idx)]                    
        if idx == '0':
            parent[0] = item[0]
        else:
            parent[1] = item[0]
    return tree
    
# http://www.rosettacode.org/wiki/Huffman_coding#Python
def compress(uncompressed):
    """Huffman encode the given dict mapping symbols to weights"""
    symb2freq = Counter(uncompressed)
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    dico = {_[0]:_[1] for _ in heappop(heap)[1:]}
    tree = dico_tree(dico)
    readable = ':'.join([c+':'+dico[c] for c in uncompressed])
    binary = tree_binary(tree)+''.join([dico[c] for c in uncompressed])
    return [binary, readable]

def decompress(binary):
    uncompressed = ""
    dico, binary = binary_tree(binary)
    current = ""
    readable = []
    for c in binary:
        current += c
        try:
            uncompressed += dico[current]
            readable.append(dico[current]+':'+current)
            current = ""
        except KeyError as e:
            pass
    readable = ':'.join(readable)
    return [uncompressed, readable]

symbol = "!"

def write_orle(count, current, output):
    binary = ""
    if count > 3 or (count <= 3 and current == symbol):
        output.append([symbol, count, current])
        binary += "{0:08b}".format(ord(symbol))
        binary += "{0:08b}".format(count)
        binary += "{0:08b}".format(ord(current))
    else:
        while count != 0:
            output.append([current])
            binary += "{0:08b}".format(ord(current))
            count-=1
    return binary

def compress(uncompressed):
    i = 1             
    count = 1         
    current = uncompressed[0]
    binary = ""
    readable = []
    while i<len(uncompressed):
        if current != uncompressed[i] or count>256:
            binary += write_orle(count, current, readable)
            count = 1
            current = uncompressed[i] 
        elif current == uncompressed[i]:
            count = count + 1
        i += 1
    binary += write_orle(count, current, readable)
    
    return [binary, readable]

def decompress(binary):
    uncompressed = ""
    readable = []
    i = 0
    while i < len(binary):
        c = chr(int(binary[i:i+8], 2))
        i += 8
        if c == symbol:
            count = int(binary[i:i+8], 2)
            i += 8
            current = chr(int(binary[i:i+8], 2))
            i += 8
            uncompressed = uncompressed + current*count
            readable.append([symbol, count, current])
        else:
            uncompressed = uncompressed + c
            readable.append([c])
    return [uncompressed, readable]

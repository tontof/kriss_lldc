def write_rle(count, current, output):
    binary = ""
    binary += "{0:08b}".format(count)
    binary += "{0:08b}".format(ord(current))
    output.append([count, current])

    return binary

def compress(uncompressed):
    i = 1             
    count = 1         
    current = uncompressed[0]
    binary = ""
    readable = []
    while i<len(uncompressed):
        if current != uncompressed[i] or count>256:
            binary += write_rle(count, current, readable)
            count = 1
            current = uncompressed[i] 
        elif current == uncompressed[i]:
            count = count + 1
        i += 1
    binary += write_rle(count, current, readable)
    
    return [binary, readable]

def decompress(binary):
    uncompressed = ""
    readable = []
    i = 0
    while i < len(binary):
        count = int(binary[i:i+8], 2)
        i += 8
        current = chr(int(binary[i:i+8], 2))
        i += 8
        uncompressed = uncompressed + current*count
        readable.append([count, current])
    return [uncompressed, readable]

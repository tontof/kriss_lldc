# Inspired by https://rosettacode.org/wiki/LZW_compression#Python
def compress(uncompressed):
    dico = {chr(_):_ for _ in range(256)}
    def format_binary(dico, index):
        return ("{0:0%sb}" % (len("{:b}".format(len(dico)-1)))).format(index)
    def format_readable(index):
        return dico[buf] if dico[buf] > 255 else chr(dico[buf])
    buf = ""
    readable = []
    binary = ""
    for c in uncompressed:
        current = buf + c
        if current in dico:
            buf = current
        else:
            binary += format_binary(dico, dico[buf])
            readable.append(format_readable(dico[buf]))
            dico[current] = len(dico)
            buf = c
 
    if buf != "":
        binary += format_binary(dico, dico[buf])
        readable.append(format_readable(dico[buf]))

    return [binary, readable]
 

def decompress(binary):
    dico = {_:chr(_) for _ in range(256)}

    i = 8
    buf = dico[int(binary[0:8], 2)]
    uncompressed = buf
    readable = [buf]
    while i < len(binary):
        pad = len("{:b}".format(len(dico)))
        current = int(binary[i:i+pad], 2)
        readable.append(current if current > 255 else chr(current))
        i += pad
        if current in dico:
            entry = dico[current]
        elif current == len(dico):
            entry = buf + buf[0]
        else:
            raise ValueError('%s' % current)
        uncompressed += entry
        dico[len(dico)] = buf + entry[0]
        buf = entry

    return [uncompressed, readable]

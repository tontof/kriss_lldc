offset = 7
max_length = 3

def compress(uncompressed):
    uncompressed = ['']*offset + [c for c in uncompressed]
    pos = offset
    readable = []
    binary = ""
    while pos < len(uncompressed):
        dico = ''.join(uncompressed[pos-offset:pos])[::-1]
        pref = ''.join(uncompressed[pos:pos+max_length])[::-1]
        index = -1
        while index == -1 and len(pref) > 0:
            try:
                index = dico.index(pref)
            except ValueError as e:
                index = -1
            if index == -1:
                pref = pref[1:]
        dico = dico[::-1]
        pref = pref[::-1]
        if len(pref) == 0: #not found
            next = uncompressed[pos]
            pos += 1
            index = 0
        else: #pref found
            index += len(pref)
            pos += len(pref)
            if index == len(pref): #pref found at the end, search for a repeated pattern
                i = 0
                while len(pref) < max_length and pos < len(uncompressed) and uncompressed[pos]==pref[i]:
                    pref += pref[i]
                    i += 1
                    pos += 1
            next = uncompressed[pos] if pos < len(uncompressed) else ''
            pos+=1
        readable.append([index,len(pref),next])
        binary += ("{0:0%sb}" % (len("{:b}".format(offset)))).format(index)
        binary += ("{0:0%sb}" % (len("{:b}".format(max_length)))).format(len(pref))
        if (len(next)>0):
            binary += "{0:08b}".format(ord(next))
    return [binary, readable]

def decompress(binary):
    readable = []
    offset_bit = len("{:b}".format(offset)) # nb bits
    max_length_bit = len("{:b}".format(max_length)) # nb bits
    while len(binary) > 0:
        prefix = int(binary[0:offset_bit], 2)
        binary = binary[offset_bit:]
        length = int(binary[0:max_length_bit], 2)
        binary = binary[max_length_bit:]
        try:
            c = chr(int(binary[0:8], 2))
        except ValueError as e:
            c = ''
        binary = binary[8:]
        readable.append([prefix, length, c])
    uncompressed = ''
    # copy readable
    for elt in [[a,b,c] for [a,b,c] in readable]:
        while(elt[1]!=0):
            uncompressed += uncompressed[len(uncompressed)-elt[0]]
            elt[1]-=1
        uncompressed += elt[2]
    return [uncompressed, readable]

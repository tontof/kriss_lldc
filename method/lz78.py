# https://github.com/hpanago/LZ77-LZ78/
def compress(uncompressed):
        i = 0
        dictionary = {}
        position = 1
        buf = ""
        readable = []
        binary = ""
        def write_binary(index, letter):
                pad = len("{:b}".format(len(dictionary)-1))
                if len(letter) > 0:
                        return ("{0:0%sb}" % (pad)).format(index) + "{0:08b}".format(ord(letter))
                else:
                        return ("{0:0%sb}" % (pad)).format(index)

        #now the EOF happens when we meet a new paragraph
        while True:
                c = uncompressed[i]
                i += 1
                buf += c
                if buf not in dictionary:
                        dictionary[buf] = position
                        position += 1
                        if len(buf) == 1:
                                binary += write_binary(0, buf)
                                readable.append([0, buf])
                        elif len(buf) == 0:
                                pass
                        else:
                                char = buf[:-1]
                                pos = dictionary[char]
                                binary += write_binary(pos, buf[-1])
                                readable.append([pos, buf[-1]])
                        buf = ""

                if i >= len(uncompressed):
                        if len(buf) > 0:
                                pos = dictionary[buf]
                                binary += write_binary(pos, '')
                                readable.append([pos, ''])
                        break
        return [binary, readable]

def decompress(binary):
        dictionary = {0:''}
        uncompressed = ""
        readable = []
        i = 0
        while i < len(binary):
                pad = len("{:b}".format(len(dictionary)-1))
                index = int(binary[i:i+pad], 2)
                i += pad
                letter = chr(int(binary[i:i+8], 2)) if i < len(binary) else ''
                i += 8
                dictionary[len(dictionary)] = dictionary[index]+letter
                prefix = dictionary[index]
                uncompressed += dictionary[index]+letter
                readable.append([index, letter])
        return [uncompressed, readable]
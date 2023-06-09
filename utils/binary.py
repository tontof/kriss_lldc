from io import StringIO

def binary_set(bits):
    suffix = (8-(len(bits)+3)%8)%8
    return bits + suffix*'0' + "{0:03b}".format(suffix)

def binary_get(bits):
    suffix = int(bits[-3:], 2)
    return bits[:-(suffix+3)]

# https://gist.github.com/gngdb/3781ec8cba30769f881e9f9cbd54ed36
def write_bitstream(fname, bits):
    sio = StringIO(binary_set(bits))
    with open(fname, 'wb') as f:
        while 1:
            # Grab the next 8 bits
            b = sio.read(8)
            # Bail if we hit EOF
            if not b:
                break
            # If we got fewer than 8 bits, pad with zeroes on the right
            if len(b) < 8:
                b = b + '0' * (8 - len(b))
                # Convert to int
            i = int(b, 2)
            # Write
            f.write(i.to_bytes(1, byteorder='big'))

def read_bitstream(fname):
    bits = ""
    size = 0
    with open(fname, 'rb') as file:
        while 1:
            byte_s = file.read(1)
            if not byte_s:
                break
            bits += "{0:08b}".format(byte_s[0])
    return binary_get(bits)

import argparse, os.path
from utils.binary import write_bitstream, read_bitstream

import method.huffman as huffman
import method.ahuffman as ahuffman
import method.arithmetic as arithmetic
import method.rle as rle
import method.orle as orle
import method.lz77 as lz77
import method.lz78 as lz78
import method.lzw as lzw

METHODS = [
    'ahuffman',
    'arithmetic',
    'huffman',
    'lz77',
    'lz78',
    'lzw',
    'orle',
    'rle'
]

def read_input(inputfilename):
    f = open(inputfilename,'r')
    filedata = f.read()
    return filedata

def write_output(outputfilename, content):
    f = open(outputfilename,'w', encoding='utf-8')
    f.write(content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--action', default='compress', help='action to use: compress, decompress')
    parser.add_argument('-m', '--method', required=True, help=('method to use: ' + (', '.join(METHODS))))
    parser.add_argument('-i', '--input', default=None, help='path to input file or direct input', required=True)
    parser.add_argument('-o', '--output', default=None, help='path to output file')
    parser.add_argument('--lz77_offset', default=7, type=int, help='lZ77 offset')
    parser.add_argument('--lz77_length', default=3, type=int, help='lZ77 length')
    parser.add_argument('-v', '--verbose', action='store_true', help='print progress')
    args = parser.parse_args()

    lz77.offset = args.lz77_offset
    lz77.max_length = args.lz77_length
    
    if args.verbose:
        print("Method:\t\t{}".format(args.method))
        print("Action:\t\t{}".format(args.action))
        print("Input File:\t{}".format(args.input))
        print("Output File:\t{}".format(args.output))

    if args.method not in METHODS:
        print("choose a valid compression method")
        print(METHODS)
        exit()

    if not os.path.isfile(args.input):
        input = args.input
    else:
        if args.action == 'compress':
            input = read_input(args.input)
        else:
            input = read_bitstream(args.input)
    result, readable = eval(args.method+'.'+args.action)(input)
    if args.verbose:
        print("Input:\t\t{}".format(input))
        print("Input length:\t{}".format(len(input)))
        print("{}:\t{}{}".format(args.method, '\t' if len(args.method) < 7 else '', readable))
        print("Output:\t\t{}".format(result))
        print("Output length:\t{}".format(len(result)))
    if args.output:
        if args.action == 'compress':
            write_bitstream(args.output, result)
        else:
            write_output(args.output, result)

if __name__ == "__main__":
   main()


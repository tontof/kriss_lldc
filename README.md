kriss_lldc
==========

A simple and smart (or stupid) lossless data compression repository

For educational purpose only to illustrate a data compression lecture (Huffman, Adaptative Huffman, Arithmetic coding, Run length coding, Optimized run length coding, LZ77, LZ78, LZW):
https://tontof.net/tuto/compression/ (in french)

- Huffman: http://www.rosettacode.org/wiki/Huffman_coding#Python
- Adaptative Huffman: https://github.com/sh1r0/adaptive-huffman-coding
- Arithmetic coding: https://github.com/nayuki/Reference-arithmetic-coding
- LZ78: https://github.com/hpanago/LZ77-LZ78/
- LZW: https://rosettacode.org/wiki/LZW_compression#Python

Installation
============
```bash
git clone https://github.com/tontof/kriss_lldc
cd kriss_lldc
python3 test.py
```

The output should be:
```
..........
----------------------------------------------------------------------
Ran 10 tests in 0.007s

OK
```

Usage
=====
To calculate entropy of a string
```bash
python3 entropy.py ABBCCCDDDDEEEEE

2.1492553971685
```

To calculate entropy of a file
```bash
python3 entropy.py data/message

2.1492553971685
```

To compress/decompress
```bash
python3 main.py -h

usage: main.py [-h] [-a ACTION] -m METHOD -i INPUT [-o OUTPUT]
               [--lz77_offset LZ77_OFFSET] [--lz77_length LZ77_LENGTH] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -a ACTION, --action ACTION
                        action to use: compress, decompress
  -m METHOD, --method METHOD
                        method to use: ahuffman, arithmetic, huffman, lz77,
                        lz78, lzw, orle, rle
  -i INPUT, --input INPUT
                        path to input file or direct input
  -o OUTPUT, --output OUTPUT
                        path to output file
  --lz77_offset LZ77_OFFSET
                        lZ77 offset
  --lz77_length LZ77_LENGTH
                        lZ77 length
  -v, --verbose         print progress
```

Example with Huffman:
```bash
python3 main.py -a compress -m huffman -i data/message -v

Method:		huffman
Action:		compress
Input File:	data/message
Output File:	None
Input:		ABBCCCDDDDEEEEE
Input length:	15
huffman:	A:000:B:001:B:001:C:01:C:01:C:01:D:10:D:10:D:10:D:10:E:11:E:11:E:11:E:11:E:11
Output:		1110010000010010000100010000111001000100001000101000001001010101101010101111111111
Output length:	82
```

Licence
=======
Copyleft (ɔ) - Tontof - https://tontof.net

Use KrISS lldc at your own risk.

[Free software means users have the four essential freedoms](http://www.gnu.org/philosophy/philosophy.html):
* to run the program
* to study and change the program in source code form
* to redistribute exact copies, and
* to distribute modified versions.

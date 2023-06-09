import unittest

from utils.binary import binary_get, binary_set

import method.huffman as huffman
import method.ahuffman as ahuffman
import method.arithmetic as arithmetic
import method.rle as rle
import method.orle as orle
import method.lz77 as lz77
import method.lz78 as lz78
import method.lzw as lzw

chaine = "ABBCCCDDDDEEEEE"

class BinaryTest(unittest.TestCase):
    def test_binary(var):
        bits_test = {
            "0": "00000100",
            "1": "10000100",
            "01": "01000011",
            "010": "01000010",
            "0110": "01100001",
            "01110": "01110000",
            "011110": "0111100000000111",
            "0111110": "0111110000000110",
            "01111110": "0111111000000101",
            "011111110": "0111111100000100"
        }
        for bits, value in bits_test.items():
            var.assertEqual(binary_set(bits), value)
            var.assertEqual(binary_get(binary_set(bits)), bits)

class HuffmanTest(unittest.TestCase):
    def test_huffman(var):
        binary, readable = huffman.compress(chaine)
        uncompressed, readable = huffman.decompress(binary)
        var.assertEqual(uncompressed, chaine)

class AHuffmanTest(unittest.TestCase):
    def test_ahuffman(var):
        binary, readable = ahuffman.compress(chaine)
        uncompressed, readable = ahuffman.decompress(binary)
        var.assertEqual(uncompressed, chaine)

class ArithmeticTest(unittest.TestCase):
    def test_arithmetic(var):
        binary, readable = arithmetic.compress(chaine)
        uncompressed, readable = arithmetic.decompress(binary)
        var.assertEqual(uncompressed, chaine)

class RLETest(unittest.TestCase):
    def test_rle(var):
        binary, output = rle.compress(chaine)
        uncompressed, output = rle.decompress(binary)
        var.assertEqual(uncompressed, chaine)

class ORLETest(unittest.TestCase):
    def test_orle(var):
        binary, readable = orle.compress(chaine)
        uncompressed, readable = orle.decompress(binary)
        var.assertEqual(uncompressed, chaine)

class LZ77Test(unittest.TestCase):
    def test_lz77(var):
        lz77.max_length = 3
        chaine = "ABBCCCDDDDEEEEE"
        binary, readable = lz77.compress(chaine)
        var.assertEqual(readable, [[0, 0, 'A'], [0, 0, 'B'], [1, 1, 'C'], [1, 2, 'D'], [1, 3, 'E'], [1, 3, 'E']])
        var.assertEqual(binary, "000000100000100000010000100010101000011001100100010000111010001010011101000101")
        uncompressed, readable = lz77.decompress(binary)
        var.assertEqual(readable, [[0, 0, 'A'], [0, 0, 'B'], [1, 1, 'C'], [1, 2, 'D'], [1, 3, 'E'], [1, 3, 'E']])
        var.assertEqual(uncompressed, chaine)

    def test_lz77_alt(var):
        chaine = "ABBCCCDDDDEEEEE"
        lz77.max_length = 4
        binary, compressed = lz77.compress(chaine)
        var.assertEqual(compressed, [[0, 0, 'A'], [0, 0, 'B'], [1, 1, 'C'], [1, 2, 'D'], [1, 3, 'E'], [1, 4, '']])
        uncompressed, readable = lz77.decompress(binary)
        var.assertEqual(uncompressed, chaine)

        chaine = "ABCDABCDABCD"
        lz77.max_length = 8
        binary, compressed = lz77.compress(chaine)
        var.assertEqual(compressed, [[0, 0, 'A'], [0, 0, 'B'], [0, 0, 'C'], [0, 0, 'D'], [4, 8, '']])
        uncompressed, readable = lz77.decompress(binary)
        var.assertEqual(uncompressed, chaine)

        chaine = "ABCDBCDBCD"
        lz77.max_length = 8
        binary, compressed = lz77.compress(chaine)
        var.assertEqual(compressed, [[0, 0, 'A'], [0, 0, 'B'], [0, 0, 'C'], [0, 0, 'D'], [3, 6, '']])
        uncompressed, readable = lz77.decompress(binary)
        var.assertEqual(uncompressed, chaine)

        chaine = "ABCABD"
        lz77.max_length = 3
        binary, compressed = lz77.compress(chaine)
        var.assertEqual(compressed, [[0, 0, 'A'], [0, 0, 'B'], [0, 0, 'C'], [3, 2, 'D']])
        uncompressed, readable = lz77.decompress(binary)
        var.assertEqual(uncompressed, chaine)

class LZ78Test(unittest.TestCase):
    def test_lz78(var):
        binary, readable = lz78.compress(chaine)
        uncompressed, readable = lz78.decompress(binary)
        var.assertEqual(uncompressed, chaine)
    
class LZ7WTest(unittest.TestCase):
    def test_lz7w(var):
        binary, readable = lzw.compress(chaine)
        uncompressed, readable = lzw.decompress(binary)
        var.assertEqual(uncompressed, chaine)
        
if __name__ == "__main__":
    unittest.main()


"""Minimal Huffman encoder/decoder used by the JPEG notebook.

The notebook represents each image block as a list of RLE tuples. This module
flattens those symbols, adds an end-of-block marker, builds a Huffman code, and
then reconstructs the original block structure during decoding.
"""

from collections import Counter
import heapq
from itertools import count

END_BLOCK = ("__END_BLOCK__",)


def _build_codes(symbols):
    frequencies = Counter(symbols)

    if len(frequencies) == 1:
        only_symbol = next(iter(frequencies))
        return {only_symbol: "0"}

    unique_counter = count()
    heap = []

    for symbol, frequency in frequencies.items():
        heapq.heappush(heap, (frequency, next(unique_counter), symbol))

    while len(heap) > 1:
        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)
        heapq.heappush(heap, (f1 + f2, next(unique_counter), (left, right)))

    root = heap[0][2]
    codes = {}

    def walk(node, prefix):
        if not isinstance(node, tuple) or node == END_BLOCK or (len(node) == 2 and all(isinstance(v, (int, float)) for v in node)):
            codes[node] = prefix or "0"
            return
        left, right = node
        walk(left, prefix + "0")
        walk(right, prefix + "1")

    walk(root, "")
    return codes


def encode_huffman(blocks_rle):
    """Encode RLE blocks and return ``bitstream, tree``.

    ``tree`` is a compact decoding dictionary, not a graphical tree object.
    """
    symbols = []
    for block in blocks_rle:
        symbols.extend(tuple(symbol) for symbol in block)
        symbols.append(END_BLOCK)

    codes = _build_codes(symbols)
    bitstream = "".join(codes[symbol] for symbol in symbols)
    reverse_codes = {code: symbol for symbol, code in codes.items()}

    tree = {
        "codes": codes,
        "reverse_codes": reverse_codes,
        "end_block": END_BLOCK,
    }
    return bitstream, tree


def decode_huffman(bitstream, tree):
    """Decode a Huffman bitstream back into RLE blocks."""
    reverse_codes = tree["reverse_codes"]
    blocks = []
    current_block = []
    current_code = ""

    for bit in bitstream:
        current_code += bit
        if current_code not in reverse_codes:
            continue

        symbol = reverse_codes[current_code]
        if symbol == END_BLOCK:
            blocks.append(current_block)
            current_block = []
        else:
            current_block.append(symbol)
        current_code = ""

    if current_code:
        raise ValueError("Invalid Huffman bitstream: leftover bits could not be decoded.")

    return blocks

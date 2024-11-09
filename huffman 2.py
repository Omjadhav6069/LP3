import heapq
from collections import Counter, defaultdict

# Build the Huffman Tree
def build_huffman_tree(text):
    freq = Counter(text)
    heap = [[weight, [char, ""]] for char, weight in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return dict(sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)))

# Encode text using the generated Huffman codes
def huffman_encode(text, huffman_codes):
    return ''.join(huffman_codes[char] for char in text)

# Decode the encoded text
def huffman_decode(encoded_text, huffman_codes):
    reversed_codes = {v: k for k, v in huffman_codes.items()}
    code, decoded_text = "", []
    for bit in encoded_text:
        code += bit
        if code in reversed_codes:
            decoded_text.append(reversed_codes[code])
            code = ""
    return ''.join(decoded_text)

# Main function
if __name__ == "__main__":
    text = input("Enter the text to encode: ")

    # Build Huffman Tree and encode the text
    huffman_codes = build_huffman_tree(text)
    encoded_text = huffman_encode(text, huffman_codes)

    print("Huffman Codes:", huffman_codes)
    print("Encoded Text:", encoded_text)
    print("Decoded Text:", huffman_decode(encoded_text, huffman_codes))

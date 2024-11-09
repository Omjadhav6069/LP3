import heapq
from collections import defaultdict, Counter

# Define the Node class for the Huffman Tree
class Node:
    def __init__(self, char, freq):
        self.char = char  # Character (if it's a leaf node)
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child node
        self.right = None  # Right child node

    # Comparison function for the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

# Function to build the Huffman Tree
def build_huffman_tree(text):
    # Count the frequency of each character in the text
    frequency = Counter(text)

    # Initialize the priority queue with nodes for each character
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    # Combine nodes until there is only one node in the queue (the root of the tree)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    # The last remaining node is the root of the Huffman Tree
    return heap[0]

# Function to generate Huffman codes from the tree
def generate_huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    # If the node is a leaf, it contains a character, so store the code
    if root.char is not None:
        codes[root.char] = current_code
        return codes

    # Traverse the left and right subtrees to generate codes
    if root.left:
        generate_huffman_codes(root.left, current_code + "0", codes)
    if root.right:
        generate_huffman_codes(root.right, current_code + "1", codes)

    return codes

# Function to encode the text using the generated Huffman codes
def huffman_encode(text, codes):
    encoded_text = "".join(codes[char] for char in text)
    return encoded_text

# Function to decode the encoded text using the Huffman Tree
def huffman_decode(encoded_text, root):
    decoded_text = []
    current_node = root
    for bit in encoded_text:
        # Traverse the tree based on the current bit
        current_node = current_node.left if bit == "0" else current_node.right
        # If we reach a leaf node, add the character to the result
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root

    return "".join(decoded_text)

# Main function to demonstrate Huffman Encoding
if __name__ == "__main__":
    text = input("Enter the text to encode: ")

    # Step 1: Build Huffman Tree
    root = build_huffman_tree(text)

    # Step 2: Generate Huffman Codes
    huffman_codes = generate_huffman_codes(root)

    # Step 3: Encode the text
    encoded_text = huffman_encode(text, huffman_codes)

    # Display the results
    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"'{char}': {code}")

    print("\nEncoded Text:")
    print(encoded_text)

    # Step 4: Decode the encoded text
    decoded_text = huffman_decode(encoded_text, root)
    print("\nDecoded Text (should match original):")
    print(decoded_text)

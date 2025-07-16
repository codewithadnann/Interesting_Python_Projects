import hashlib
import time

class Block:
    def __init__(self, index, data, prev_hash):
        self.timestamp = time.time()
        self.index = index
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        content = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}"
        return hashlib.sha256(content.encode()).hexdigest()

# Create the blockchain
blockchain = [Block(0, "Genesis Block", "0")]

# Add more blocks
for i in range(1, 4):
    prev = blockchain[-1]
    blockchain.append(Block(i, f"Block {i} data", prev.hash))

# Print blockchain
for block in blockchain:
    print(f"Block {block.index}: {block.hash}")

import hashlib
import time
import json
from transaction import Transaction

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions  # List of transactions
        self.nonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Generates SHA-256 hash of the block."""
        block_content = f"{self.index}{self.previous_hash}{self.timestamp}{json.dumps(self.transactions, sort_keys=True)}{self.nonce}"
        return hashlib.sha256(block_content.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        """Proof-of-Work mining function."""
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"⛏️ Block {self.index} mined: {self.hash}")

class Blockchain:
    def __init__(self, difficulty=4, mining_reward=10):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []
        self.mining_reward = mining_reward

    def create_genesis_block(self):
        """Creates the first block in the blockchain."""
        return Block(0, "0", time.time(), [])

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction, signature):
        """Validates and adds a transaction to the pool."""
        if Transaction.verify_transaction(transaction, signature):
            self.pending_transactions.append(transaction)
        else:
            print("❌ Invalid transaction!")

    def mine_pending_transactions(self, miner_address):
        """Mines transactions and rewards the miner."""
        new_block = Block(len(self.chain), self.get_latest_block().hash, time.time(), self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = [{"sender": "Network", "recipient": miner_address, "amount": self.mining_reward}]

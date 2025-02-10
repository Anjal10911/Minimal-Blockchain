## Tiny Blockchain in Python
A minimal blockchain implementation in Python, demonstrating how transactions, mining, and proof-of-work function in a decentralized network.

# Features
🔹 Simple Blockchain Structure – Blocks contain an index, timestamp, transactions, proof (nonce), and the previous block’s hash.
🔹 Proof of Work (PoW) – Implements a basic consensus mechanism to prevent spam and ensure valid block mining.
🔹 Mining Functionality – Nodes can mine new blocks and receive rewards.
🔹 Transaction Handling – Users can add transactions to the blockchain.
🔹 REST API with Flask – Provides endpoints for interacting with the blockchain (adding transactions, mining blocks, and viewing the chain).
🔹 Decentralized Design – Each node maintains a copy of the blockchain and syncs with others.

# How It Works
A user submits a transaction.
Miners validate and add the transaction to a block.
Miners solve a cryptographic puzzle (Proof of Work).
The block is added to the blockchain and distributed across the network.
# Running the Project
Clone the Repository
sh
Copy
Edit
git clone https://github.com/yourusername/tiny-blockchain.git
cd tiny-blockchain
# Install Dependencies
sh
Copy
Edit
pip install flask requests
# Run the Blockchain Node
sh
Copy
Edit
python blockchain.py
Interact via API using tools like Postman or cURL.
## API Endpoints
GET /chain – View the blockchain.
POST /transactions/new – Add a new transaction.
GET /mine – Mine a new block.
POST /nodes/register – Register new blockchain nodes.
GET /nodes/resolve – Consensus mechanism to resolve chain conflicts.
## Future Enhancements
🚀 Implement digital signatures for secure transactions.
🔗 Add peer-to-peer communication for full decentralization.
💡 Improve Proof-of-Work efficiency with a difficulty adjustment mechanism.

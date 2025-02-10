from flask import Flask, request, jsonify
from blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    """Mines a block and rewards the miner."""
    miner_address = request.args.get('address')
    if not miner_address:
        return jsonify({"error": "No miner address provided"}), 400
    
    blockchain.mine_pending_transactions(miner_address)
    return jsonify({"message": "Block mined successfully!"})

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    """Adds a new transaction to the blockchain."""
    values = request.get_json()
    required_fields = ["sender", "recipient", "amount", "signature"]
    if not all(field in values for field in required_fields):
        return jsonify({"error": "Missing transaction fields"}), 400
    
    blockchain.add_transaction(values, values["signature"])
    return jsonify({"message": "Transaction added successfully!"})

@app.route('/chain', methods=['GET'])
def get_chain():
    """Returns the full blockchain."""
    return jsonify(blockchain.chain)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

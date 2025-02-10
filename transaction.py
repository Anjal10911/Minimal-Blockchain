import json
import ecdsa

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {"sender": self.sender, "recipient": self.recipient, "amount": self.amount}

    def sign_transaction(self, private_key):
        """Signs the transaction using the sender's private key."""
        private_key_obj = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
        message = json.dumps(self.to_dict(), sort_keys=True).encode()
        signature = private_key_obj.sign(message).hex()
        return signature

    @staticmethod
    def verify_transaction(transaction, signature):
        """Verifies that the transaction was signed correctly."""
        public_key_obj = ecdsa.VerifyingKey.from_string(bytes.fromhex(transaction["sender"]), curve=ecdsa.SECP256k1)
        message = json.dumps(transaction, sort_keys=True).encode()
        try:
            return public_key_obj.verify(bytes.fromhex(signature), message)
        except ecdsa.BadSignatureError:
            return False


import ecdsa

def generate_keys():
    """Generates a new public/private key pair."""
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()

    return private_key.to_string().hex(), public_key.to_string().hex()

# Generate a new wallet
private_key, public_key = generate_keys()
print(f"🔑 Your Public Key (Address): {public_key}")
print(f"🔒 Your Private Key: {private_key}")

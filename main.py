class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(previous_hash="1", proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': get_timestamp(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, amount, signature):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'amount': amount,
            'signature': signature
        }
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    def verify_transaction(self, transaction):
        sender_public_key = transaction['sender']
        signature = transaction['signature']
        document = str(transaction)
        return verify(sender_public_key, document, signature)

    @property
    def last_block(self):
        return self.chain[-1]

class Wallet:
    def __init__(self):
        self.private_key, self.public_key = generate_keys()

    def sign_transaction(self, transaction):
        return sign(self.private_key, transaction)

    def send_transaction(self, blockchain, receiver, amount):
        transaction = {
            'sender': self.public_key,
            'receiver': receiver,
            'amount': amount
        }
        signature = self.sign_transaction(str(transaction))
        blockchain.add_transaction(self.public_key, receiver, amount, signature)
blockchain = Blockchain()
wallet = Wallet()

sender = wallet.public_key
receiver = public_key
amount = 10

wallet.send_transaction(blockchain, receiver, amount)

blockchain.create_block(proof=200, previous_hash="hash_value")

print("Blockchain:")
for i in blockchain.chain:
    print(i)
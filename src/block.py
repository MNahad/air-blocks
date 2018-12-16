import hashlib, time, json
from pprint import pprint

blockchainPath = "assets/blockchain.json"


class Block:
    def __init__(self, data, prevHash):
        self.data = data
        self.timestamp = time.time()
        self.prevHash = prevHash

        hash = hashlib.sha256()
        hash.update(str(self.timestamp).encode())
        hash.update(str(self.prevHash).encode())
        hash.update(str(self.data).encode())
        self.hash = hash.digest()


    def addToTheChain(self):
        with open(blockchainPath) as theChain:
            chain = json.load(theChain)

        newBlock = {
            "Timestamp": self.timestamp,
            "PrevHash": self.prevHash,
            "Data": self.data,
            "Hash": self.hash,
        }

        chain.update(newBlock)

        with open(blockchainPath, 'w') as theChain:
            json.dump(chain, theChain)


if __name__ == "__main__":
    myBlock = Block("2", "0")
    myBlock.addToTheChain()

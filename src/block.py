import hashlib, time, json
from pprint import pprint

blockchainPath = "assets/blockchain.json"


class Block:
    def __init__(self, data, prevHash):
        self.data = str(data)
        self.timestamp = float(time.time())
        self.prevHash = str(prevHash).encode()

        hash = hashlib.sha256()
        hash.update(str(self.timestamp).encode())
        hash.update(self.prevHash)
        hash.update(str(self.data).encode())
        self.hash = hash.digest()


    def addToTheChain(self):
        with open(blockchainPath) as theChain:
            chain = json.load(theChain)

        newBlock = {
            "Timestamp": float(self.timestamp),
            "PrevHash": str(self.prevHash),
            "Data": str(self.data),
            "Hash": str(self.hash),
        }

        chain.update(newBlock)

        with open(blockchainPath, 'w') as theChain:
            json.dump(chain, theChain)


def fullBlockchain():
    with open(blockchainPath) as theChain:
        chain = json.load(theChain)
    return chain


def loadPrevHash():
    with open(blockchainPath) as theChain:
        chain = json.load(theChain)
    return bytes(chain["Hash"])


if __name__ == "__main__":
    myBlock = Block("2", "0")
    myBlock.addToTheChain()

    pprint(fullBlockchain())

    myNxtBlk = Block("42", loadPrevHash())
    myNxtBlk.addToTheChain()

    pprint(fullBlockchain())

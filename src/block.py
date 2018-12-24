import hashlib, time, json
from pprint import pprint

blockchainPath = "assets/blockchain.json"


class Block:
    def __init__(self, data, prevHash):
        self.data = str(data)
        self.timestamp = float(time.time())
        self.prevHash = prevHash

        theHash = hashlib.sha256()
        theHash.update(str(self.timestamp).encode())
        theHash.update(self.prevHash)
        theHash.update(str(self.data).encode())
        self.hash = theHash.digest()


    def addToTheChain(self):
        with open(blockchainPath) as theChain:
            chain = json.load(theChain)

        prevStr = ""
        for theByte in self.prevHash:
            prevStr += chr(theByte)
        hashStr = ""
        for theByte in self.hash:
            hashStr += chr(theByte)

        newBlock = {
            "Timestamp": float(self.timestamp),
            "PrevHash": prevStr,
            "Data": str(self.data),
            "Hash": hashStr,
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
    num = []
    for c in chain["Hash"]:
        num.append(ord(c))
    theHash = bytes(num)
    return theHash


if __name__ == "__main__":
    genesis = hashlib.sha256()
    genesis.update(b"0")
    myBlock = Block("42", genesis.digest())
    myBlock.addToTheChain()

    pprint(fullBlockchain())

    myNxtBlk = Block("42", loadPrevHash())
    myNxtBlk.addToTheChain()

    pprint(fullBlockchain())

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
    GBOAC_gen_data = {
        "AC": "G-BOAC",
        "Sign": "MN",
    }
    genesisHash = hashlib.sha256()
    genesisHash.update(b"0")
    GBOAC_gen = Block(GBOAC_gen_data, genesisHash.digest())
    GBOAC_gen.addToTheChain()

    pprint(fullBlockchain())

    GBOAC_new_data = {
        "ChkDate": float(time.time()) - 86400,
    }
    GBOAC_new = Block(GBOAC_new_data, loadPrevHash())
    GBOAC_new.addToTheChain()

    pprint(fullBlockchain())

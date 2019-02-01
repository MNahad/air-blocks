#!/usr/bin/env python3

import hashlib, time, os, json
from pprint import pprint

blockchainPath = "assets/blockchain.json"


class Block:
    def __init__(self, data, prevHash):
        self.data = data
        self.timestamp = int(time.time())
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
            "Timestamp": int(self.timestamp),
            "PrevHash": prevStr,
            "Data": self.data,
            "Hash": hashStr,
        }

        chain.append(newBlock)

        with open(blockchainPath, 'w') as theChain:
            json.dump(chain, theChain)


def fullBlockchain():
    with open(blockchainPath) as theChain:
        chain = json.load(theChain)
    return chain


def loadPrevHash():
    with open(blockchainPath) as theChain:
        chain = json.load(theChain)
    hashNum = []
    for c in chain[len(chain)-1]["Hash"]:
        hashNum.append(ord(c))
    theHash = bytes(hashNum)
    return theHash


if __name__ == "__main__":
    os.environ['TZ']='UTC'

    GBOAC_gen_data = {
        "AC": "G-BOAC",
        "FH": 0,
        "FC": 0,
        "HRS": 0,
    }
    genesisHash = hashlib.sha256()
    genesisHash.update(b"0")
    GBOAC_gen = Block(GBOAC_gen_data, genesisHash.digest())
    GBOAC_gen.addToTheChain()

    print("New chain for " + GBOAC_gen_data["AC"])
    pprint(fullBlockchain())

    GBOAC_new_data = {
        "Chk": "PREDEP",
        "ChkDate": int(time.mktime(time.strptime(
            "2019-01-31 00:10:15",
            "%Y-%m-%d %H:%M:%S",
        ))),
        "Sign": "MN",
    }
    GBOAC_new = Block(GBOAC_new_data, loadPrevHash())
    GBOAC_new.addToTheChain()

    print("Appended block for " + GBOAC_gen_data["AC"])
    pprint(fullBlockchain())

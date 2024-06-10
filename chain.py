import hashlib
from block import Block

class Chain():
    def __init__(self , difficaulty):
        self.difficaulty = difficaulty
        self.blocks = []
        self.pool = []
        self.create_origin_block()

    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest() ,16) < 2**(256-self.difficaulty) and block.previous_hash == self.blocks[-1].hash
    

    def  add_to_chain(self, block):
        if self.proof_of_work(block):
            self.blocks.append(block)

    def add_to_pool(self ,data):
        self.pool.append(data)

    def print_block(self , block):
        print("\n**********************************************")
        print("Hash:\t" , block.hash.hexdigest())
        print("Previous Hash:\t" , block.previous_hash.hexdigest() )
        print("Nonce:\t" , block.nonce)
        print("Data:\t" , block.data)

    def mine(self):
        if len(self.pool) > 0:
            data = self.pool.pop()
            block = Block(data , self.blocks[-1].hash)
            block.mine(self.difficaulty)
            self.add_to_chain(block)
            self.print_block(block)

    def create_origin_block(self):
        h = hashlib.sha256()
        h.update(''.encode("utf-8"))
        origin = Block("origin",h)
        origin.mine(self.difficaulty)
        self.blocks.append(origin)


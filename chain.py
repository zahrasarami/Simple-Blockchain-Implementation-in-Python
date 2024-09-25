import hashlib
from block import Block

class Chain():
    def __init__(self , math_problems):
        self.math_problems = math_problems
        self.blocks = []
        self.pool = []
        self.current_index = 0 
        self.create_origin_block()

    def proof_of_work(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and hash.hexdigest().endswith(self.math_problems[-1]) and block.previous_hash == self.blocks[-1].hash
    

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
            # print(self.math_problems[self.current_index])
            block = Block(data , self.blocks[-1].hash ,self.math_problems[self.current_index])
            block.mine()
            self.add_to_chain(block)
            self.print_block(block)

    def create_origin_block(self):
        h = hashlib.sha256()
        h.update(''.encode("utf-8"))
        origin = Block("origin",h,self.math_problems[0])
        origin.mine_genesis_block()
        self.blocks.append(origin)

    def set_current_index(self , index):
        self.current_index = index
        return


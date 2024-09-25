import hashlib

class Block():
    def __init__(self , data , previous_hash , math_problem):
        self.hash = hashlib.sha256()
        self.previous_hash = previous_hash
        self.nonce = 0
        self.data = data
        self.math_problem = math_problem


    def __str__(self) :
        return "{}{}{}".format(self.previous_hash.hexdigest() ,self.data , self.nonce)
    

    def mine(self):
        self.hash.update(str(self).encode('utf-8'))
        # print(self.hash)
        # print(self.hash.hexdigest().endswith(self.math_problem))
        while not self.hash.hexdigest().endswith(self.math_problem):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))

    def mine_genesis_block(self):
        self.hash.update(str(self).encode('utf-8'))    
        self.nonce += 1
        self.hash = hashlib.sha256()
        self.hash.update(str(self).encode('utf-8'))
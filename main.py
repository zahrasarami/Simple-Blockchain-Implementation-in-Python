from chain import Chain
import json
import os  

def get_genesis_block():
    file_path = './GenesisBlock/GenesisBlock.json'
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

def get_math_problems():
    file_indices = range(2, 17)
    math_problems = [None] * (len(file_indices) + 2)
    directory = './Math_Problems/'

    for i in file_indices:
        file_name = f'Math_Problem_Number{i}.json'
        file_path = os.path.join(directory, file_name)
        
        with open(file_path, 'r') as file:
            data = json.load(file)
            block_number = data['blockNumber']
            math_problem = data['mathProblem']
            math_problems[block_number] = math_problem
    math_problems = math_problems[1:]
    math_problems[0] = '' # first ledger difficaulty
    return math_problems


def get_ledgers_data():
    file_indices = range(2, 17)
    ledger_list = [None] * (len(file_indices) + 2)
    directory = './Ledgers/'

    for i in file_indices:
        file_name = f'Ledger_Number{i}.json'
        file_path = os.path.join(directory, file_name)
        
        with open(file_path, 'r') as file:
            data = json.load(file)
            block_number = data['blockNumber']
            ledger_list[block_number] = data

    ledger_list = ledger_list[1:]
    ledger_list[0] =  get_genesis_block()
    return ledger_list


ledgers_data = get_ledgers_data()
math_problems =  get_math_problems()

chain = Chain(math_problems)

i=0

while(i<16):
    data = ledgers_data[i]
    chain.set_current_index(i)
    chain.add_to_pool(data)
    chain.mine()
    i +=1

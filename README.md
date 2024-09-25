# Simple Blockchain Implementation in Python
This project demonstrates the creation of a simple blockchain with 16 blocks using Python.

The blockchain starts with a genesis block, and each subsequent block is built by solving a cryptographic puzzle. In each round, a nonce value is determined by computing the SHA-256 hash of the block’s data to satisfy a difficulty condition.

The blockchain consists of 15 ledgers, and each block is linked to the previous one through its hash.

## Project Overview
Genesis Block: The first block (genesis block) is provided in JSON format.

`Puzzles`: 
Each ledger has a corresponding cryptographic puzzle that 
needs to be solved by finding the correct nonce value.

`Blocks`: The program generates a total of 16 blocks. For each block, the program prints the block number, block hash, previous block's hash, and the corresponding nonce value.

`Block 16`: The 16th block involves a more computationally intensive math puzzle. Due to its complexity, it is recommended to use a cloud-based environment, such as Google Colab, for the computation.

## Features
1. Implements a basic blockchain structure with SHA-256 hashing.

2. Solves cryptographic puzzles using nonce values.

3. Maintains immutability between blocks by including the hash of the previous block.
4. Designed to work efficiently for 15 blocks on a local machine, with an additional 16th block that requires external computational resources.

## Output
For each round, the program will output:

    Block number
    Block hash (SHA-256)
    Previous block’s hash
    Nonce value

you can see sample outpuut in mined_data.pdf 

Google Colab for Block 16: For solving block 16, upload the Python script to Google Colab and execute it to handle the computational complexity.
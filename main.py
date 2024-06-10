from chain import Chain

chain = Chain(0)

i=0

while(i<5):
    data = input("data:")
    chain.add_to_pool(data)
    chain.mine()
    i +=1

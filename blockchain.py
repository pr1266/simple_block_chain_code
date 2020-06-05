from block import Block
import datetime

block_chain = [Block.create_genesis_block()]

print('the genesis block has been created !')
print('Hash : %s' % block_chain[-1].hash)

num_blocks_to_add = 10

for i in range(1, num_blocks_to_add + 1):
    block_chain.append(Block(block_chain[-1].hash, f'Data : {i}', datetime.datetime.now()))

    print('Block %d has been created' % i)
    print('Hash : %s' % block_chain[i].hash)
    print('transaction time : %s' % block_chain[i].timestamp)
    print()
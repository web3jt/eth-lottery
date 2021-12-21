import os
from lib import settings
from lib import functions as fn

web3 = settings.PROVIDER

START_BLOCK = 12345678

OUTPUT_COUNT = 13
OUTPUT_COUNT_LENGTH = 2

output = []
lines = []


def touch(block_number):
    block = web3.eth.get_block(block_number)
    block_hash = block.hash.hex()
    block_hash_decimal = int(block_hash, 16)
    index = block_hash_decimal % len(rows)
    index_str = str(index).rjust(OUTPUT_COUNT_LENGTH, ' ')

    if rows[index] not in output:
        output.append(rows[index])
        line = ' #{} - {} % {} = {} :: {}'.format(block_number, block_hash, OUTPUT_COUNT, index_str, rows[index])
        lines.append(line)
        print(line)
    else:
        line = ' #{} - {} % {} = {}'.format(block_number, block_hash, OUTPUT_COUNT, index_str)
        lines.append(line)
        print(line)


if __name__ == '__main__':
    print('\nRead `input.txt`:')

    rows = fn.read_list_from_file(os.path.join(settings.DATA_DIR, 'input.txt'))
    rows = fn.remove_duplicated_from_list(rows)
    for row in rows:
        print(' ... {}'.format(row))
    length = len(rows)

    if OUTPUT_COUNT > length:
        raise Exception('`OUTPUT_COUNT = {}`, but `len(rows) = {}`'.format(OUTPUT_COUNT, length))

    line1 = '--- Pick {} from {} ---'.format(OUTPUT_COUNT, length)
    lines.append(line1)
    print('\n{}'.format(line1))

    print('\nWrite `output.txt`:')
    i = 0
    while i < OUTPUT_COUNT:
        nonce = START_BLOCK + i
        touch(nonce)
        i += 1

    fn.put_list_to_file(os.path.join(settings.DATA_DIR, 'log.txt'), lines)
    fn.put_list_to_file(os.path.join(settings.DATA_DIR, 'output.txt'), output)

import os
import sys
import getopt
from lib import settings
from lib import functions as fn

web3 = settings.PROVIDER

START_BLOCK = 0
PICK_OUT = 1
PICK_OUT_LENGTH = 1

output = []
lines = []


def exit_with_help():
    print('\nlottery.py -n <block-number> -p <pick-out>')
    sys.exit()


def log(s):
    lines.append(s)
    print(s)


def touch(block_number):
    block = web3.eth.get_block(block_number)
    block_hash = block.hash.hex()
    block_hash_decimal = int(block_hash, 16)
    index = block_hash_decimal % len(rows)
    index_str = str(index).rjust(PICK_OUT_LENGTH, ' ')

    if rows[index] not in output:
        output.append(rows[index])
        log(' #{} - {} % {} = {} :: {}'.format(block_number, block_hash, len(rows), index_str, rows[index]))
    else:
        log(' #{} - {} % {} = {}'.format(block_number, block_hash, len(rows), index_str))


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hn:p:', ['block-number=', 'pick-out='])
        for opt, arg in opts:
            if opt in ('-h', '--help'):
                exit_with_help()
            elif opt in ('-n', '--block-number'):
                try:
                    START_BLOCK = int(arg)
                except:
                    exit_with_help()
            elif opt in ('-p', '--pick-out'):
                try:
                    PICK_OUT = int(arg)
                except:
                    exit_with_help()
    except getopt.GetoptError:
        exit_with_help()

    if START_BLOCK == 0:
        exit_with_help()

    PICK_OUT_LENGTH = len(str(PICK_OUT))

    # start here
    print('\n')
    log('Read `input.txt`:')

    rows = fn.read_list_from_file(os.path.join(settings.DATA_DIR, 'input.txt'))
    rows = fn.remove_duplicated_from_list(rows)
    for row in rows:
        log(' ... {}'.format(row))
    length = len(rows)

    if PICK_OUT > length:
        raise Exception('`OUTPUT_COUNT = {}`, but `len(rows) = {}`'.format(PICK_OUT, length))

    log('\n--- Pick {} from {} ---'.format(PICK_OUT, length))
    log('\nWrite `output.txt`:')

    i = 0
    while len(output) < PICK_OUT:
        nonce = START_BLOCK + i
        touch(nonce)
        i += 1

    fn.put_list_to_file(os.path.join(settings.DATA_DIR, 'log.txt'), lines)
    fn.put_list_to_file(os.path.join(settings.DATA_DIR, 'output.txt'), output)

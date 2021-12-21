# Lottery by Ethereum Blockchain

## Set your web3 provider url in `.env`

```text
PROVIDER=https://mainnet.infura.io/v3/<YOUR-INFURA-TOKEN>
```

## Create your source file `./data/input.txt`

For example:
```txt
lorem
ipsum
dolor
sit
amet
consectetur
adipiscing
elit
curabitur
curabitur
curabitur
curabitur
ornare
commodo
eros
sed
cursus
```

## Run

```bash
$ lottery.py -n <block-number> -p <pick-out>
```

For example:
```bash
$ lottery.py -n 12345678 -p 5
#
# Read `input.txt`:
#  ... lorem
#  ... ipsum
#  ... dolor
#  ... sit
#  ... amet
#  ... consectetur
#  ... adipiscing
#  ... elit
#  ... curabitur
#  ... ornare
#  ... commodo
#  ... eros
#  ... sed
#  ... cursus
#
# --- Pick 5 from 14 ---
#
# Write `output.txt`:
#  #12345678 - 0xb2a8b39935a5eb4b7c9b0117bca06c8d2c0629e0937d20e62c44aace6f05bda3 % 5 = 9 :: ornare
#  #12345679 - 0xac7f164008dd1bdf29c6c8799cb737d41663fa7d3215b38dfee20135c87a12e4 % 5 = 4 :: amet
#  #12345680 - 0x189bad2344f34ac6332e522a2c3aceaa28b4eddee63f842109c67cb16360fc3f % 5 = 13 :: cursus
#  #12345681 - 0x7c9d621ef426c60824a7d5e9871cde3376bcb48f17d1c209d6a6f033f493a090 % 5 = 4
#  #12345682 - 0xb63493b5909cb9aebb7d7bc0078369aee6a8b4c4b6f928d15e6f101f8a8148e3 % 5 = 3 :: sit
```

## Then

You will get `./data/output.txt` and `./data/log.txt`

`./data/output.txt`:
```text
ornare
amet
cursus
sit
```

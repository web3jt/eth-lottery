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
$ lottery.py -n 12345678 -p 10
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
# --- Pick 10 from 14 ---
#
# Write `output.txt`:
#  #12345679 - 0xac7f164008dd1bdf29c6c8799cb737d41663fa7d3215b38dfee20135c87a12e4 % 10 =  4 :: amet
#  #12345680 - 0x189bad2344f34ac6332e522a2c3aceaa28b4eddee63f842109c67cb16360fc3f % 10 = 13 :: cursus
#  #12345681 - 0x7c9d621ef426c60824a7d5e9871cde3376bcb48f17d1c209d6a6f033f493a090 % 10 =  4
#  #12345682 - 0xb63493b5909cb9aebb7d7bc0078369aee6a8b4c4b6f928d15e6f101f8a8148e3 % 10 =  3 :: sit
#  #12345683 - 0xa22cc64c1bae76698b248b785f0aca52f6a4dc6731dc03c547e2092bfa359b91 % 10 = 11 :: eros
#  #12345684 - 0x5b1ba21686f1857970066a65f3f188c8b5b908c9abb786b5d69120c06f307f4f % 10 =  3
#  #12345685 - 0x8365b9c5db946eab0256bb222b1c8b9d2ff5b85cd43757dc14d45d5a52fc181c % 10 =  8 :: curabitur
#  #12345686 - 0xc013b70b96bc64f3cdcc14ce641889e48d4a24b1cb36afb5193521cf6a748e82 % 10 =  8
#  #12345687 - 0x7f5aead9d7bed1c727169eaefdf9f42f1364f3157b3a37d5b9509b3c8e9de3df % 10 =  3
#  #12345688 - 0xfd9e556381a0fb3b6334f0557bf63bd6255a8200839145686b49afc5148b45d7 % 10 =  1 :: ipsum
#  #12345689 - 0xb96530735699884090fbf9b52a12dd5db35fd26cc98c207a87b766b62ae39805 % 10 =  7 :: elit
#  #12345690 - 0x405ce038cd88d623ae37b788141b7ff598c1de2ee59884c647be467a0834c129 % 10 =  3
#  #12345691 - 0xff8792d8378fa1910fa543f467eaa6d00e6a662fcf11a061e30cb7c686967d02 % 10 =  2 :: dolor
#  #12345692 - 0x17884860627988547dc6d9d2789c4259df1cd9f12e30bb864fe525fbcde4852b % 10 =  7
#  #12345693 - 0x74778bb54485899a5aa3fad9f9f4f14290d02c9b84f137142e4c604310c4b156 % 10 =  4
#  #12345694 - 0x254ba055bd867281a872d4df639ef6af99671c0f7a430d3cdc972ae2954c8a5e % 10 =  6 :: adipiscing
#  #12345695 - 0xddc21672a1ab51fe7cb1819493ca8343fe092007ad0864532bb5aac948c5fecc % 10 =  4
#  #12345696 - 0x14e4807f58c7b9feb8e318b66647f819af2bb020cfa6790aa5e6e561551c0fc6 % 10 = 10 :: commodo
```

## Then

You will get `./data/output.txt` and `./data/log.txt`

`./data/output.txt`:
```text
amet
cursus
sit
eros
curabitur
ipsum
elit
dolor
adipiscing
commodo
```

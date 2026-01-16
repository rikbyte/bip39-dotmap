"""
生成属于你自己的Bip-39助记词顺序
Generate your own Bip-39 mnemonic word order.
"""
import random

secure_rng = random.SystemRandom()
with open('english.txt', 'r') as f:
    mnemonic = [x.strip() for x in f.readlines()]
secure_rng.shuffle(mnemonic)


def parse(s: str) -> str:
    splits = s.split('|')
    if len(splits) != 7 or splits[1] == ' Index ' or splits[1] == '-------':
        return s
    splits[2] = f' {mnemonic[int(splits[1].strip()) - 1]:9}'
    return '|'.join(splits)


def main():
    with open("README.md", 'r') as f:
        readme = f.readlines()
    with open("MyOwn.md", 'w') as f:
        for line in readme:
            f.write(parse(line))


if __name__ == '__main__':
    main()

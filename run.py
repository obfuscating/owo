import sys
exec(
    "".join([
        chr(len(char)) for char in open(sys.argv[1], encoding='utf-8').read().split("⠀")
    ])
)
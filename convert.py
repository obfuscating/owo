import sys
def convert_code(code: str):
    string = ""
    for line in code.splitlines():
        line.strip('\n')
        for character in line:
            string += str("owo " * ord(character))[:ord(character)] + "⠀"
        string += str("owo " * ord("\n"))[:ord("\n")] + "⠀"
    with open("owo.owo", 'w', encoding='utf-8') as owo:
        owo.write(string.strip()[:len(string.strip())-1])
convert_code(open(sys.argv[1], encoding='utf-8').read())
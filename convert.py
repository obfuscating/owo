import sys
def convert_code(code: str):
    CHARACTERS = "owo "
    DELIMITER = "⠀" # set this in run.py too in the .split() method
    string = ""
    for line in code.splitlines():
        line.strip('\n')
        for character in line:
            string += str(CHARACTERS * ord(character))[:ord(character)] + DELIMITER
        string += str(CHARACTERS * ord("\n"))[:ord("\n")] + DELIMITER
    with open("owo.owo", 'w', encoding='utf-8') as owo:
        owo.write(string.strip()[:len(string.strip())-1])
convert_code(open(sys.argv[1], encoding='utf-8').read())

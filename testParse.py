
def readFileContents(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            d = line[:-1].split(',')

            coderaw = d[0]
            code = coderaw
            reg = ''
            if 'N' in coderaw or 'X' in coderaw or 'Y' in coderaw:
                code = coderaw.replace
                #bool(re.match('0...', '0123'))
            # data[] = {'c': d[1], 'i': d[2]}
    return data

from pprint import pprint
d = readFileContents("opcodes.csv")

for a in d:
    print(a, d[a])
print(end='\n\n')
with open("IBM Logo.ch8", "rb") as f:
    while (byte := f.read(2)):
        opcode = byte.hex().upper()
        
        if (opcode in d):
            print(d[opcode]['i'])
        else:
            print(opcode)

from pprint import pprint
import re

def readFileContents(filename):
    data = {}
    with open(filename, 'r') as file:
        for line in file:
            d = line[:-1].split(',')

            coderaw = d[0]
            reg = coderaw
            if 'N' in coderaw or 'X' in coderaw or 'Y' in coderaw:
                reg = coderaw.replace('N', '.')
                reg = reg.replace('Y', '.')
                reg = reg.replace('X', '.')
                #bool(re.match('0...', '0123'))
            data[coderaw] = {'r': reg, 'c': d[1], 'i': d[2]}
    return data


d = readFileContents("opcodes.csv")

for a in d:
    print(a, d[a])
print(end='\n\n')
with open("IBM Logo.ch8", "rb") as f:
    while (byte := f.read(2)):
        opcode = byte.hex().upper()

        print(opcode, end=' - ')
        if opcode in d:
            print('~' + d[opcode]['i'], end='')
        else:
            for code in d:
                if (re.match(d[code]['r'], opcode)):
                    print(d[code]['i'], end='')
        #check full
        # if opcode in d:
        #     print('~' + d[opcode]['i'])
        # else:
        #     #check re
            
        #     for code in d:
        #         if (re.match(d[code]['r'], opcode)):
        #             print(d[opcode]['i'])

        print()

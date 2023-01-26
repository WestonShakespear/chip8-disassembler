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

def readBinData(filename):
    hexData = []
    with open(filename, "rb") as f:
        while (byte := f.read(1)):
            hexData.append(byte.hex().upper())

    return hexData

def parseCode(codeList, opcode):
    if opcode in codeList:
            return '~' + codeList[opcode]['i']
    else:
        for code in codeList:
            if (re.match(codeList[code]['r'], opcode)):
                return codeList[code]['i']
    return '*'


def disAssemble(codeList, binData):
    for byteC in range(0, len(binData), 2):
        opcode = binData[byteC] + binData[byteC + 1]

        info = parseCode(codeList, opcode)

        print('B:', str(byteC).zfill(3), ' OP:', opcode, '   ', info)
        



codeList = readFileContents("opcodes.csv")
binData = readBinData("IBM Logo.ch8")

#list opcodes
for a in codeList:
    print(a, codeList[a])
print(end='\n\n')

#list bindata
for i,a in enumerate(binData):
    print(i, a)


#disassemble
disAssemble(codeList, binData)


# with open(, "rb") as f:
#     while (byte := f.read(2)):
#         opcode = byte.hex().upper()

#         print(opcode, end=' - ')
#         if opcode in d:
#             print('~' + d[opcode]['i'], end='')
#         else:
#             for code in d:
#                 if (re.match(d[code]['r'], opcode)):
#                     print(d[code]['i'], end='')
#         #check full
#         # if opcode in d:
#         #     print('~' + d[opcode]['i'])
#         # else:
#         #     #check re
            
#         #     for code in d:
#         #         if (re.match(d[code]['r'], opcode)):
#         #             print(d[opcode]['i'])

#         print()

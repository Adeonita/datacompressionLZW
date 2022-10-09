from array import array
from base64 import decode
import string
import json

def generateAscTable():
    dict = {}

    for x in range(1, 256):
        character = chr(x) #ch retorna aspas simples
        dict.update({character: x })

    return dict

def addInDict(value: str, dictAsc: dict):
    lastKey = list(dictAsc.values())[-1]
    nextKey = lastKey + 1
    dictAsc.update({value : nextKey})

    return dictAsc

def writeInDict(filePath, text):
    with open(filePath, 'w') as file:
        file.write(text)

def hasSequence(dict: dict, value: str):
    hasValue = dict.get(value)
    
    return bool(hasValue)

def getCodeByKey(dict: dict, key: string):
    return dict.get(key)

def getSequenceByCode(dict: dict, sequence: string):
    return dict.get(sequence)

def readFile():
    with open('files/ed2test.txt', 'r', encoding='utf-8-sig') as file:
        return file.read()

def writeFile(path: string, data):
    with open(path, 'a') as file:
        file.write(data)

def enconding():
    dictAsc = generateAscTable()
    
    with open('files/ed2test.txt', 'r', encoding='utf-8-sig') as file:
        firstSymbol = ''
        encondingSequence = []
        
        while True:
            ch = file.read(1)
            if not ch:
                break
            seq = firstSymbol + ch

            if hasSequence(dictAsc, seq):
                firstSymbol = seq
            else:
                encondingSequence.append(getCodeByKey(dictAsc, firstSymbol))
                addInDict(seq, dictAsc)
                firstSymbol = ch

    encondingSequence.append(getCodeByKey(dictAsc, firstSymbol))

    writeFile('files/encodingSequence.txt', str(encondingSequence))
    writeFile('files/encodingSequence.txt', '\n')
    writeFile('files/encodingSequence.txt', str(dictAsc))

def sanitizeEncodingSequence(encondingSequence: string) :
    encondingSequence = encondingSequence.replace('[', '')
    encondingSequence = encondingSequence.replace(']', '')
    encondingSequence = encondingSequence.replace(' ', '')
    encondingSequence = encondingSequence.replace('\n', '')

    return encondingSequence.split(',')

def recoveryDictAndEncodingSequence():
    encondingSequence: array = None
    ascTable: str = None

    with open('files/encodingSequence.txt', 'r', encoding='utf-8-sig') as file:
        count = 0

        while True:
            line = file.readline()

            if not line:
                break

            if count == 0 :
                encondingSequence = line
                count = count + 1
            else :
                ascTable = line
                count = count + 1

    encondingSequence = sanitizeEncodingSequence(encondingSequence)
    ascTable = json.loads(ascTable) #resolver problema de caracateres que possuem escape

    return encondingSequence, ascTable


def decoding():
    encondingSequence, ascTable = recoveryDictAndEncodingSequence()
    decodingSequence = ''

    invertedTable = dict(zip(ascTable.values(), ascTable.keys())) 

    for code in encondingSequence:
        character = invertedTable.get(int(code))
        decodingSequence = decodingSequence + character
    
    writeFile('files/decodingSequence.txt', str(decodingSequence))

# enconding()
decoding()


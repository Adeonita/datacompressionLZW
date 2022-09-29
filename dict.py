import string

def generateAscDict():
    dict = {}

    for x in range(1, 256):
        character = chr(x)
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

def readFile():
    with open('files/ed2test.txt', 'r', encoding='utf-8-sig') as file:
        return file.read()

def enconding():
    dictAsc = generateAscDict()
    
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
    print(encondingSequence)


enconding()

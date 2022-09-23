import os.path

def generatedict():
    dict = {}

    for x in range(33, 127):
        character = chr(x)
        dict.update({x : character})

    for x in range(161, 246):
        character = chr(x)
        
        dict.update({x : character})
    
    return dict

def writeInDict(filePath, text):
   with open(filePath, 'w') as file:
    file.write(text)

dictasc = generatedict()

filePath = 'files/asc.txt'

if (not os.path.exists(filePath)):
    print("file not found")


with open(filePath, 'a') as file:
    for key, value in dictasc.items():
        text  = str(key )+ ':' + value
        file.write(text)
        file.write('\n')

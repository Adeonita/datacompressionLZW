from LZW import LZW

filePath = './files/file.txt'
encodedSequencePath = './files/encodedSequence.txt'
decodedSequencePath = './files/decodedSequence.txt'

LZW().encode(filePath, encodedSequencePath)
LZW().decode(decodedSequencePath, encodedSequencePath)
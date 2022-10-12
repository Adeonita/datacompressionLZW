# Compressão com LZW

Este projeto tem como objetivo realizar a compressão de um arquivo de texto utilizando o algoritmo LZW.

# Requisitos 
- [python 3.8.10.^](https://www.python.org/downloads/)


# Estrutura
- A classe LZW é responsável por conter os códigos de codificação e de decodificação 

- files
    - `file.txt`: Arquivo a ser comprimido
    - `encodedSequence.txt`: Arquivo que conterá a sequência codificada e o dicionário responsável por conter as n combinações possíveis
    - `decodedSequence.txt`: Arquivo que conterá a sequência decodificada, e seu conteúdo deverá ser identico ao file.txt


# Como rodar
Na raiz do arquivo execute o comando 
`python index.py`

# Saídas esperadas

## EncodedSequence
É esperado que neste arquivo contenha a sequência codificada gerada a partir de um dicionário de dados, e o dicionário gerado

## DecodedSequence
É esperado que neste arquivo contenha a sequência codificada descomprimida e que a mesma seja idêntica ao arquivo original, que neste exemplo é o file.txt

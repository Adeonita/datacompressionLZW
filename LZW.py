import json
import string

class LZW:

    def _get_asc_table(self):
        asc_table = {}

        for x in range(1, 256):
            character = chr(x)
            asc_table.update({ character: x })
        
        return asc_table

    def _add_in_database(self, value: str, dict_asc: dict):
        lastKey = list(dict_asc.values())[-1]
        nextKey = lastKey + 1
        dict_asc.update({value : nextKey})

        return dict_asc


    def _has_sequence(self, dict: dict, value: str):
        has_value = dict.get(value)
        
        return bool(has_value)

    def _get_code_by_key(self, dict: dict, key: string):
        return dict.get(key)


    def _write_file(self, path: string, data, is_json = True):
        with open(path, 'a') as file:
            if is_json:
                file.write(json.dumps(data))
                return
            
            file.write(data)

    def encode(self, filePath: string, encodeFilePath: string):
        dict_asc = self._get_asc_table()

        with open(filePath, 'r', encoding='utf-8-sig') as file:
            frist_symbol = ''
            encode_sequence = ''

            while True:
                ch = file.read(1)
                if not ch:
                    break
                seq = frist_symbol + ch

                if self._has_sequence(dict_asc, seq):
                    frist_symbol = seq
                else:
                    encode_sequence = encode_sequence + str(self._get_code_by_key(dict_asc, frist_symbol)) + ', '

                    self._add_in_database(seq, dict_asc)
                    frist_symbol = ch

        encode_sequence = encode_sequence + str(self._get_code_by_key(dict_asc, frist_symbol))

        file = {
            "encode_sequence" : encode_sequence,
            "dict" : dict_asc
        }

        self._write_file(encodeFilePath, file)


    def decode(self, decodeFilePath: string, encodeFilePath: string):
        file = None
        decoded_sequence = ''

        with open(encodeFilePath, 'r', encoding='utf-8-sig') as file:
            file = json.loads(file.read())

        encodedSequence = file.get('encode_sequence').split(',')

        dict_asc = file.get('dict')

        invertedTable = dict(zip(dict_asc.values(), dict_asc.keys()))

        for code in encodedSequence:
            character = invertedTable.get(int(code))
            decoded_sequence = decoded_sequence + character

        self._write_file(decodeFilePath, decoded_sequence, False)

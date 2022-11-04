import hashlib
from pathlib import Path


class Helper:
    
    def convert_to_dict(self, value):

        split_list = value.split(';')

        new = [i.strip() for i in split_list]

        js = dict()

        for string in new:

            item = []
            item2 = []

            for i in string:
                if i == ':':
                    break
                item.append(i)

            key = ''.join(item)

            for i in reversed(string):
                if i == ':':
                    break
                item2.append(i)

            value = ''.join(item2)
            value = value.strip()[::-1]

            if value == 'none':
                value = None

            js[key] = value

        return js

    def get_output_name(self, path):

        file_name = Path(path).stem

        return file_name

    def convert_hash(self, value):
        encoded = value.encode()

        result = hashlib.sha256(encoded).hexdigest()

        return result

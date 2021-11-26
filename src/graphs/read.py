import json


class Reader:
    @classmethod
    def read_JSON(cls, path):
        if ".json" in path:
            with open(path) as json_file:
                content = json.load(json_file)
                return content
        else:
            raise ValueError("Arquivo inválido")

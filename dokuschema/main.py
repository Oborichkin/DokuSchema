import json

from .dokuwiki import DokuWikiFactory


class DokuSchema:
    def __init__(self, schema):
        self.root = Element(schema)

    @staticmethod
    def from_file(filename: str) -> "DokuSchema":
        with open(filename, "r") as f:
            return DokuSchema(json.loads(f.read()))


class Element:
    def __init__(self, json_obj: dict):
        self.title = json_obj.get("title")
        self.desc = json_obj.get("description")
        self.properties = [Element(json_obj["properties"][prop]) for prop in json_obj.get("properties", [])]
        self.factory = DokuWikiFactory()

    def doku(self, heading_depth=1):
        if self.title:
            res = self.factory.heading(self.title, heading_depth)
            res += self.factory.text(self.desc)
            for prop in self.properties:
                res += prop.doku(heading_depth + 1)
            return res
        return ""

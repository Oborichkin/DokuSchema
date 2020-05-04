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
    def __init__(self, json_obj: dict, name: str = None):
        self.title = json_obj.get("title", "NO TITLE")
        self.name = self.title if name is None else name
        self.desc = json_obj.get("description")
        self.type = json_obj["type"]
        self.properties = []
        for name, prop in json_obj.get("properties", {}).items():
            if "allOf" not in prop and "$ref" not in prop:
                self.properties.append(Element(prop, name))
        self.factory = DokuWikiFactory()

    @property
    def reference(self):
        heading = ("Имя", "Тип")
        rows = [(prop.name, prop.type) for prop in self.properties]
        return [heading, *rows]

    def doku(self, heading_depth=1):
        if self.title:
            res = self.factory.heading(self.title, heading_depth)
            res += self.factory.text(self.desc)
            res += self.factory.table(heading=self.reference[0], rows=self.reference[1:])
            res += "\n"
            for prop in self.properties:
                res += prop.doku(heading_depth + 1)
            return res
        return ""

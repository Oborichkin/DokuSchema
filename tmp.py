import json

from dokuschema.main import DokuSchema

s = DokuSchema.from_file("data/json/schema.json")

with open("data/pages/schema.txt", "w+") as f:
    f.write(s.root.doku())

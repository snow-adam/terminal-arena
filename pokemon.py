import json

with open("data/pokedex.json") as dex:
    pokedex = json.load(dex)

class Pokemon():
    def __init__(self, name):
        self.name = pokedex[name]
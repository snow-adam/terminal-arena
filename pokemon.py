import json

with open("data/pokedex.json") as dex:
    pokedex = json.load(dex)

class Pokemon():
    def __init__(self, name):
        self.name = name
        self.mon = pokedex[name]

    def __repr__(self):
        return "{}: \nType: {}\nHP: {}\nMoves: {}".format(self.name, self.mon["type"], self.mon["hp"], " / ".join(self.mon["moves"]))
    
    def get_name(self):
        return self.name
    
    def get_hp(self):
        return self.mon["hp"]
    
    def get_moves(self):
        return self.mon["moves"]
    
    def get_type(self):
        return self.mon["type"]
    
    def reduce_hp(self, power, type):
        if (self.mon["type"] == type) or (self.mon["type"] == "Grass" and type == "Water") or (self.mon["type"] == "Fire" and type == "Grass") or (self.mon["type"] == "Water" and type == "Fire"):
            self.mon["hp"] -= power / 8
            return "It's not very effective.".format(self.mon)
        elif (self.mon["type"] == "Fire" and type == "Water") or (self.mon["type"] == "Water" and type == "Grass") or (self.mon["type"] == "Grass" and type == "Fire"):
            self.mon["hp"] -= power / 2
            return "It's super effective!".format(self.mon)
        else:
            self.mon["hp"] -= power / 4
            return "{} was hurt by the attack.".format(self.name)
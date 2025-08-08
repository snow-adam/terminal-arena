import pokemon

class Trainer():
    def __init__(self, name, mon=""):
        self.name = name
        self.pokemon = pokemon.Pokemon(mon)

    def set_pokemon(self, mon):
        self.pokemon = pokemon.Pokemon(mon)

    def get_pokemon(self):
        return self.pokemon
    
    def get_name(self):
        return self.name
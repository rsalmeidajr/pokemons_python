class Pokemon: # criacao da classe
    def __init__(self, id, name, type, attacks):
        self.id = id
        self.name = name
        self.type = type
        self.attacks = attacks


pikachu = Pokemon(25, "Pikachu", "Eletric", "Thunderbolt") # criacao do objeto
onix = Pokemon(98, "onix", "Rock", "Rock Slide")
vulpix = Pokemon(36, "vulpix", "Fire", "Ember")

# print(pikachu.name, pikachu.id, pikachu.type, pikachu.attacks)
# print(onix.name, onix.id, onix.type, onix.attacks)
# print(vulpix.name, vulpix.id, vulpix.type, vulpix.attacks)


meus_pokemons = [pikachu, onix, vulpix] # criacao da lista


# for p in meus_pokemons:
#     print(p.name)


posicao = 0
while (posicao < 3):
    print(meus_pokemons[posicao].name)
    posicao = posicao + 1
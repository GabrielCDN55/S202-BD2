from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
##db.resetDatabase() ##comando para criar o database no mongo Compass

def pokemon_ovo(egg: str):
    return db.collection.find({"egg": egg})

def show_pokedex_ate_id(id: int):
    return db.collection.find({"id": {"$lt": id}})

def show_pokemons_por_tipo(types: list,numero_evo: int):
    return db.collection.find({"$and": [{"type": {"$in": types}}, {"next_evolution": {"$size": numero_evo}}]})

def show_pokemons_com_x_tipos(n_tipos: int):
    return db.collection.find({"type": {"$size": n_tipos}})

def show_pokemons_Letra_C():
    return db.collection.find({"name": {"$regex": "^C", "$options": "i"}})

pokemon1 = pokemon_ovo('2 km')
writeAJson(pokemon1,"Pokedex mostrando pokemons que precisam de 2km para ter os ovos chocados")

pokemon2 = show_pokedex_ate_id(30)
writeAJson(pokemon2, "Pokedex completa até o id solicitado")

tipos = ["Grass", "Fire"]
pokemon3 = show_pokemons_por_tipo(tipos,2)
writeAJson(pokemon3, "Pokedex mostrando pokemons do tipo solicitado com até x evolucoes")

pokemon4 = show_pokemons_com_x_tipos(1)
writeAJson(pokemon4, "Pokedex mostrando pokemons com x tipos")

pokemon5 = show_pokemons_Letra_C()
writeAJson(pokemon5, "Pokedex mostrando pokemons que começam com C")

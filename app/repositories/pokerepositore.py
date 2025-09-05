from app.config.dbconfig import get_database
from app.modeles.pokemodel import Pokemon

class PokemonRepository:
    
    def __init__(self):
        self.db = get_database()
        self.collection_name = "pokedex"
        self.pokemon_collection = self.db[self.collection_name]

    def getByName(self, name: str):
        pokemon = self.pokemon_collection.find_one({"name.english": name})
        return pokemon

    def getById(self, pokemon_id: int):
        pokemon = self.pokemon_collection.find_one({"id": pokemon_id})
        return pokemon

    def getAllByType(self, pokemon_type: str, page: int = 1, page_size: int = 10):
        skip = (page - 1) * page_size
        pokemons = self.pokemon_collection.find({"type": pokemon_type}).skip(skip).limit(page_size)
        return list(pokemons)
    
    def create(self, pokemon: Pokemon):
        result = self.pokemon_collection.insert_one(pokemon.model_dump())
        return result.inserted_id

    def update(self, pokemon_id: int, updated_data: Pokemon):
        result = self.pokemon_collection.update_one({"id": pokemon_id}, {"$set": updated_data.model_dump()})
        return result.modified_count

    def delete(self, pokemon_id: int):
        result = self.pokemon_collection.delete_one({"id": pokemon_id})
        return result.deleted_count
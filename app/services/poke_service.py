from fastapi import HTTPException
from app.repositories.pokerepositore import PokemonRepository
from app.modeles.pokemodel import Pokemon
from bson.json_util import dumps
import json

class PokeService:
    def __init__(self):
        self._repository = PokemonRepository()
    
    def jsoninfo(self, data):
        data = dumps(data)
        data = json.loads(data)
        return data

    def get_pokemon_by_name(self, name: str):
        pokemon = self._repository.getByName(name)
        pokemon = self.jsoninfo(pokemon)

        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon não encontrado")
        
        return pokemon

    def get_pokemon_by_id(self, pokemon_id: int):
        pokemon = self._repository.getById(pokemon_id)
        pokemon = self.jsoninfo(pokemon)

        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon não encontrado")
        
        return pokemon

    def get_all_pokemons_by_type(self, pokemon_type: str, page: int=1, page_size: int=10):
        pokemons = self._repository.getAllByType(pokemon_type, page, page_size)
        pokemons = self.jsoninfo(pokemons)

        return pokemons

    def create_pokemon(self, pokemon: Pokemon):
        try:
            existing_pokemon = self.get_pokemon_by_id(pokemon.id)
            if existing_pokemon:
                raise HTTPException(status_code=400, detail="Pokemon com este ID já existe")
        except ValueError:
            existing_pokemon = None

        created_pokemon = str(self._repository.create(pokemon))
        if not created_pokemon:
            raise HTTPException(status_code=400, detail="Error ao criar pokemon")
        
        return created_pokemon

    def update_pokemon(self, pokemon_id, updated_data: Pokemon):
        self.get_pokemon_by_id(pokemon_id)
        
        modified_count = self._repository.update(pokemon_id, updated_data)
        if modified_count == 0:
            raise HTTPException(status_code=400, detail="Nenhuma alteração feita no Pokemon")

        return modified_count

    def delete_pokemon(self, pokemon_id):
        self.get_pokemon_by_id(pokemon_id)
        
        deleted_count = self._repository.delete(pokemon_id)
        if deleted_count == 0:
            raise HTTPException(status_code=400, detail="Falha ao deletar o Pokemon")

        return deleted_count
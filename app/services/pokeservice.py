from fastapi import HTTPException
from app.repositories.pokerepositore import PokemonRepository
from app.modeles.pokemodel import Pokemon
from bson.json_util import dumps
import json

class PokeService:
    def __init__(self):
        self.repository = PokemonRepository()

    def get_pokemon_by_name(self, name: str):
        pokemon = self.repository.getByName(name)
        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return json.loads(dumps(pokemon))

    def get_pokemon_by_id(self, pokemon_id: int):
        pokemon = self.repository.getById(pokemon_id)
        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        return json.loads(dumps(pokemon))

    def get_all_pokemons_by_type(self, pokemon_type: str, page=1, page_size=10):
        pokemons = self.repository.getAllByType(pokemon_type, page, page_size)
        return json.loads(dumps(list(pokemons)))

    def create_pokemon(self, pokemon: Pokemon):
        existing_pokemon = self.repository.getById(pokemon.id)
        if existing_pokemon:
            raise HTTPException(status_code=400, detail="Pokemon with this ID already exists")
        inserted_id = self.repository.create(pokemon)
        return {"inserted_id": inserted_id}

    def update_pokemon(self, pokemon_id: int, updated_data):
        existing_pokemon = self.repository.getById(pokemon_id)
        if not existing_pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        modified_count = self.repository.update(pokemon_id, updated_data)
        if modified_count == 0:
            raise HTTPException(status_code=400, detail="No changes made to the Pokemon")
        return {"modified_count": modified_count}

    def delete_pokemon(self, pokemon_id: int):
        existing_pokemon = self.repository.getById(pokemon_id)
        if not existing_pokemon:
            raise HTTPException(status_code=404, detail="Pokemon not found")
        deleted_count = self.repository.delete(pokemon_id)
        if deleted_count == 0:
            raise HTTPException(status_code=400, detail="Failed to delete the Pokemon")
        return {"deleted_count": deleted_count}
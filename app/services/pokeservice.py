from fastapi import HTTPException
from app.repositories.pokerepositore import PokemonRepository
from app.modeles.pokemodel import Pokemon
from bson.json_util import dumps
import json

class PokeService:
    def __init__(self):
        self.repository = PokemonRepository()
    
    def jsoninfo(self, data):
        data = dumps(data)
        data = json.loads(data)
        return data

    def get_pokemon_by_name(self, name: str):
        pokemon = self.repository.getByName(name)
        pokemon = self.jsoninfo(pokemon)

        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon não encontrado")
        
        return pokemon

    def get_pokemon_by_id(self, pokemon_id: int):
        pokemon = self.repository.getById(pokemon_id)
        pokemon = self.jsoninfo(pokemon)

        if not pokemon:
            raise HTTPException(status_code=404, detail="Pokemon não encontrado")
        
        return pokemon

    def get_all_pokemons_by_type(self, pokemon_type: str, page=1, page_size=10):
        pokemons = self.repository.getAllByType(pokemon_type, page, page_size)
        pokemons = self.jsoninfo(pokemons)

        return pokemons

    def create_pokemon(self, pokemon: Pokemon):
        existing_pokemon = self.repository.getById(pokemon.id)
        if existing_pokemon:
            raise HTTPException(status_code=400, detail="Pokemon com este ID já existe")

        created_pokemon = str(self.repository.create(pokemon))
        if created_pokemon:
            return HTTPException(status_code=201, detail=f"Pokemon criado com Sucesso!")
        if not created_pokemon:
            raise HTTPException(status_code=400, detail="Error ao criar pokemon")
        
        return created_pokemon

    def update_pokemon(self, pokemon_id, updated_data: Pokemon):
        existing_pokemon = self.repository.getById(pokemon_id)
        if not existing_pokemon:
            raise HTTPException(status_code=404, detail="Pokemon não encontrado")
        
        modified_count = self.repository.update(pokemon_id, updated_data)
        if modified_count == 0:
            raise HTTPException(status_code=400, detail="Nenhuma alteração feita no Pokemon")

        return modified_count

    def delete_pokemon(self, pokemon_id):
        existing_pokemon = self.repository.getById(pokemon_id)
        if not existing_pokemon:
            raise HTTPException(status_code=404, detail="Pokemon não encontrado")
        
        deleted_count = self.repository.delete(pokemon_id)
        if deleted_count == 0:
            raise HTTPException(status_code=400, detail="Falha ao deletar o Pokemon")

        return deleted_count
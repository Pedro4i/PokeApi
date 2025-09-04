from fastapi import APIRouter, Query
from app.modeles.pokemodel import Pokemon
from app.services.pokeservice import PokeService

router = APIRouter(
    prefix="/pokemon",
    tags=["Pokemon"]
)

pokemonService = PokeService()

@router.get("/name/{name}")
async def get_pokemon_by_name(name: str):
    return pokemonService.get_pokemon_by_name(name)

@router.get("/id/{pokemon_id}")
async def get_pokemon_by_id(pokemon_id: int):
    return pokemonService.get_pokemon_by_id(pokemon_id)

@router.get("/type/{pokemon_type}")
async def get_all_pokemons_by_type(pokemon_type: str, page: int = Query(1), page_size: int = Query(50)):
    pokemons = pokemonService.get_all_pokemons_by_type(pokemon_type, page, page_size)
    return pokemons

@router.post("/")
async def create_pokemon(pokemon: Pokemon):
    return pokemonService.create_pokemon(pokemon)

@router.put("/{pokemon_id}")
async def update_pokemon(pokemon_id: int, updated_data: Pokemon):
    return pokemonService.update_pokemon(pokemon_id, updated_data)

@router.delete("/{pokemon_id}")
async def delete_pokemon(pokemon_id: int):
    return pokemonService.delete_pokemon(pokemon_id)


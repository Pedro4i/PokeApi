from fastapi import FastAPI
from app.routes.pokeroute import router as pokemon_router

app = FastAPI()

app.include_router(pokemon_router)

@app.get("/")
async def root():
    return {"message": "Seja bem-vindo à sua Pokedéx!"}
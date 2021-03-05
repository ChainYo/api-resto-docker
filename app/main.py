from fastapi import FastAPI
from database import DB

app = FastAPI()

@app.get("/")
def index():
    return {"Hello":"World"}

@app.get("/api/resto", tags=["Informations"])
async def get_resto_id(id=None):
    return DB.find_resto_by_id(id)

@app.get("/api/inspect", tags='Informations')
async def get_nb_inspect(id=None):
    return DB.find_nb_inspect(id)

@app.get("/api/type", tags=['Informations'])
async def get_resto_cooking_type(typeResto=None):
    return DB.find_resto_by_type(typeResto)

@app.get("/api/grade", tags=['TOP 10'])
async def get_resto_grade(grade=None):
    return DB.find_top_grade(grade)

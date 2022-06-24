from fastapi import FastAPI, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi_jwt import JwtAuthorizationCredentials, JwtAccessBearer


app = FastAPI()
access_security = JwtAccessBearer(secret_key="secret_key", auto_error=True)


@app.post("/auth/{email}")
def auth(email: str):
    # nie ma walidacji więc przekazuwanie hasła jest bez sensu
    subject = {"email": email}
    return {"new_token": access_security.create_access_token(subject=subject), "status": "ok"}


@app.get("/users/me")
def read_current_user(credentials: JwtAuthorizationCredentials = Security(access_security)):
    return {"username": credentials["username"], "role": credentials["role"]}


origins = [
    "http://domainname.com",
    "https://domainname.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/listazadan")
async def listazadan():

    return [
        {"idtask": 1, "tekst": "Zadanie 1", "czyZakonczone": False, "iduser": 1},
        {"idtask": 2, "tekst": "Zadanie 2", "czyZakonczone": False, "iduser": 1},
        {"idtask": 3, "tekst": "Zadanie 3", "czyZakonczone": True, "iduser": 1},
        {"idtask": 4, "tekst": "Zadanie 4", "czyZakonczone": True, "iduser": 1},
        {"idtask": 5, "tekst": "Zadanie 5", "czyZakonczone": False, "iduser": 1},
        {"idtask": 6, "tekst": "Zadanie 6", "czyZakonczone": True, "iduser": 1},
    ]


@app.post("/checked/{id}")
async def rejestracja(id: int):
    # tutaj wstawił bym kod zmieniający wartość w bazie danych

    return {"status": "ok", "id": id}


@app.post("/rejestracja/{email}/{password}")
async def rejestracja(email: str, password: str):

    return {"status": "ok", "email": email, "password": password}


@app.post("/rejestracja/{email}/{password}")
async def login(email: str, password: str):

    return {"status": "ok", "email": email, "password": password, "data": {"token": "asdasdasd"}}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

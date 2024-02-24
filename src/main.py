from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fasthx import Jinja
from pydantic import BaseModel
import json

app = FastAPI()
jinja = Jinja(Jinja2Templates(directory="templates"))

tournaments_mock = "../data-mock/tournaments.json"
players_mock = "../data-mock/players.json"
matches_mock = "../data-mock/matches.json"

f = open(tournaments_mock)
tournaments = json.load(f)
f.close()
f = open(players_mock)
players = json.load(f)
f.close()
f = open(matches_mock)
matches = json.load(f)
f.close()

class Player(BaseModel):
    id: int
    name: str
    games_played: int
    wins: int
    losses: int
    ties: int

class Tournament(BaseModel):
    id: int
    name: str
    status: str
    participants: list

class Match(BaseModel):
    id: int
    tournament_id: int
    home_team: Player
    visitor_team: Player
    status: str
    home_score: int
    visitor_score: int
    winner: Player


@app.get("/")
@jinja.page("base.html")
async def index() -> None:
    return {
        "data": "paskaa"
    }

@app.get("/tournaments")
@jinja.hx("tournament-list.html")
async def tournament_list() -> list[Tournament]:
    return {"tournaments": tournaments}

@app.get("/players")
@jinja.hx("players-list.html")
async def tournament_list() -> list[Player]:
    return {"players": players}

@app.get("/matches")
@jinja.hx("matches-list.html")
async def tournament_list() -> list[Match]:
    return {"matches": matches}
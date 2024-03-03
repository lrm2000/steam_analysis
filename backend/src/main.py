from fastapi import FastAPI
from routes.user.main import SteamAPI

app = FastAPI()
steam_api = SteamAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/player_achievements/")
async def player_achievements(steam_id: str, app_id: str):
    """
    Endpoint to get player achievements for a specific Steam ID and App ID.
    """
    achievements = steam_api.get_player_achievements(steam_id, app_id)
    return achievements

@app.get("/user_summary/")
async def user_summary(steam_id: str):
    """
    Endpoint to get the user summary for a specific Steam ID.
    """
    summary = steam_api.get_user_summary(steam_id)
    return summary

@app.get("/owned_games/")
async def owned_games(steam_id: str):
    """
    Endpoint to get owned games for a specific Steam ID.
    """
    games = steam_api.get_owned_games(steam_id)
    return games
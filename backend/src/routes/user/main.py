import requests
from dotenv import load_dotenv
import os
from typing import Dict

class SteamAPI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("API_KEY")
        self.base_url = "http://api.steampowered.com"

    def get_player_achievements(self, steam_id: str, app_id: str) -> Dict:
        """
        Fetches player achievements for a given Steam ID and app ID.

        Args:
            steam_id (str): The Steam ID of the user.
            app_id (str): The application ID of the game.

        Returns:
            dict: A dictionary containing the response from the Steam API.
        """
        url = f"{self.base_url}/ISteamUserStats/GetPlayerAchievements/v0001/?appid={app_id}&key={self.api_key}&steamid={steam_id}"
        response = requests.get(url)
        return response.json()

    def get_user_summary(self, steam_id: str) -> Dict:
        """
        Fetches the user summary for a given Steam ID from the Steam API.

        Args:
            steam_id (str): The Steam ID of the user.
        
        Returns:
            dict: A dictionary containing the response from the Steam API.
        """
        url = f"{self.base_url}/ISteamUser/GetPlayerSummaries/v0002/?key={self.api_key}&steamids={steam_id}"
        response = requests.get(url)
        return response.json()

    def get_owned_games(self, steam_id: str) -> Dict:
        """
        Fetches the owned games for a given SteamID from the Steam API.

        Args:
            steam_id (str): The Steam ID of the user.
        
        Returns:
            dict: A dictionary containing the response from the Steam API.
        """
        url = f"{self.base_url}/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={steam_id}&format=json"
        response = requests.get(url)
        return response.json()

# Example usage: 
# steam_api = SteamAPI()
# steam_id = "76561198111287877"
# print(steam_api.get_player_achievements(steam_id, "2161700"))
# print(steam_api.get_user_summary(steam_id))
# print(steam_api.get_owned_games(steam_id))

from pydantic import BaseModel

class PlayerSummaries(BaseModel):
    """
    Arguments
    - steamids: csv of 64bit steamid (limit: 100)
    - format: Output format. json (default), xml or vdf.
    Returns
    - public data associated with steam account 
    """
    gameid: str
    format_: str

class PlayerAchievements(BaseModel):
    """
    Arguments:
    - steamid: id for the user data
    - appid: id for the game data
    - langauge: output language of data
    Returns:
    - response: list of achievements for the user by app id
    """
    steamid: str
    appid: str
    language: str


# code -r file.py
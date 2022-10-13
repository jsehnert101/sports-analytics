import os
from dotenv import load_dotenv, find_dotenv

def get_api_key(source: str = "odds") -> str:
    load_dotenv(find_dotenv())
    if source == "odds":
        return os.environ.get("ODDS_API_KEY")
    else:
        print("Oops - looks like we don't have that API key.")
        return
    
    
if __name__ == "main":
    api_key = get_api_key()
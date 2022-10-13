# %% Import necessary libraries
import numpy as np
import pandas as pd
pd.options.display.max_columns = 50

from nba_api.stats.static import players, teams

from data.utils.dict_manager import *


# %%
# Define class to wrangle + clean NBA team data
class NBATeams():

    def __init__(self):
        self.team_matadata = teams.get_teams()

    def retrieve_team_id_dict(self, save: bool = True, pth: str = "../nba/team_id_dict.pickle") -> dict:
        """Retrieves dictionary in format [team name -> team ID, team city -> team ID] to
           ease access of Team IDs for future use.

        Args:
            save (bool, optional): whether or not to save the output. Defaults to True.
            pth (str, optional): path to store resulating dictionary. Must end in ".pickle". Defaults to "../nba/team_id_dict.pickle".

        Returns:
            dict: _description_
        """
        try:
            return load_dict(pth)
        except:
            team_ids = {}
            for team in self.team_metadata:
                team_ids[team["nickname"]] = team["id"]
                team_ids[team["city"]] = team["id"]
            if save:
                save_dict(pth=pth, d=team_ids)
            return team_ids
            

# %%
# Create + store dictionary of format [team name: team_id]
nba_teams = NBATeams()
team_ids = nba_teams.retrieve_team_id_dict()
team_ids

# %%
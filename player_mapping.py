import pandas as pd
from nba_api.stats.static import players

# Step 1: Fetch NBA player data
nba_players = players.get_players()

# Step 2: Create a mapping between player IDs and player names
player_mapping = {player['id']: player['full_name'] for player in nba_players}

# Step 3: Load your dataset
nba_cleaned = pd.read_csv("player_gamelogs_2025.csv")

# Step 4: Replace player IDs with player names
nba_cleaned['Player_Name'] = nba_cleaned['PLAYER_ID'].map(player_mapping)

# Step 5: Remove the 'Player_ID' column
nba_cleaned = nba_cleaned.drop(columns=['PLAYER_ID'])

# Step 6: Save the updated dataset
nba_cleaned.to_csv("nba_cleaned_with_names.csv", index=False)

print("Player IDs replaced with names and Player_ID column removed successfully!")

import pandas as pd

df_players = pd.read_csv('nba_processed_data.csv')
df_opponents = pd.read_csv('nba_opponent_stats.csv')

team_mapping = {
    "ATL": "Atlanta Hawks",
    "BOS": "Boston Celtics",
    "BKN": "Brooklyn Nets",
    "CHA": "Charlotte Hornets",
    "CHI": "Chicago Bulls",
    "CLE": "Cleveland Cavaliers",
    "DAL": "Dallas Mavericks",
    "DEN": "Denver Nuggets",
    "DET": "Detroit Pistons",
    "GSW": "Golden State Warriors",
    "HOU": "Houston Rockets",
    "IND": "Indiana Pacers",
    "LAC": "LA Clippers",
    "LAL": "Los Angeles Lakers",
    "MEM": "Memphis Grizzlies",
    "MIA": "Miami Heat",
    "MIL": "Milwaukee Bucks",
    "MIN": "Minnesota Timberwolves",
    "NOP": "New Orleans Pelicans",
    "NYK": "New York Knicks",
    "OKC": "Oklahoma City Thunder",
    "ORL": "Orlando Magic",
    "PHI": "Philadelphia 76ers",
    "PHX": "Phoenix Suns",
    "POR": "Portland Trail Blazers",
    "SAC": "Sacramento Kings",
    "SAS": "San Antonio Spurs",
    "TOR": "Toronto Raptors",
    "UTA": "Utah Jazz",
    "WAS": "Washington Wizards"
}

df_players["OPPONENT_TEAM"] = df_players["MATCHUP"].apply(lambda x: x.split(' ')[-1])  # Extract team abbreviation from MATCHUP column
df_players["OPPONENT_TEAM"] = df_players["OPPONENT_TEAM"].map(team_mapping)  # Map abbreviation to full team name

df_merged = df_players.merge(df_defense, left_on="OPPONENT_TEAM", right_on="TEAM_NAME", how="left")

df_merged.to_csv('player_data_with_def_stats.csv', index=False)

print("Data merged and saved to 'merged_data.csv'")

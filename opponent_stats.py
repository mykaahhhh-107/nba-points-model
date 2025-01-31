from nba_api.stats.endpoints import LeagueDashTeamStats
import pandas as pd

# Fetch defensive stats for the 2023-24 season
data = LeagueDashTeamStats(season='2024-25', measure_type_detailed_defense='Opponent')

# Convert to DataFrame
df_defense = data.get_data_frames()[0]

# Save to CSV (optional)
df_defense.to_csv('nba_opponent_stats.csv', index=False)

# Display the first few rows
print(df_defense.head())

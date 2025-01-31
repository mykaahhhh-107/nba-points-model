df = pd.read_csv('nba_cleaned_with_names.csv')

# Rolling average of points scored over the last 5 games for each player
df['Rolling_PTS_5'] = df.groupby('PLAYER_NAME')['PTS'].rolling(window=5, min_periods=1).mean().reset_index(drop=True)

# Last 3 games average points scored
df['Last_3_PTS_Avg'] = df.groupby('PLAYER_NAME')['PTS'].rolling(window=3, min_periods=1).mean().reset_index(drop=True)

# True Shooting Percentage
df['TS%'] = df['PTS'] / (2 * (df['FGA'] + 0.44 * df['FTA']))

# Effective Field Goal Percentage
df['eFG%'] = (df['FGM'] + 0.5 * df['FG3M']) / df['FGA']

# Checking the engineered features
print(df[['PLAYER_NAME', 'Rolling_PTS_5', 'Last_3_PTS_Avg', 'TS%', 'eFG%', 'Is_Home_Game', 'Team_Rolling_PTS_5']].head())

df.to_csv('nba_processed_data.csv', index=False)

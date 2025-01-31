from nba_api.stats.endpoints import playergamelogs

if get_new_player_gamelogs:
    # Iterate through the seasons and save each season to a csv
    for n in range(0, number_of_seasons):
        # construct the season name for the request
        season_name = f"20{latest_season-(n+1)}-{latest_season-n}"
        # request the gamelogs for the season
        playergamefinder = playergamelogs.PlayerGameLogs(season_nullable=season_name, league_id_nullable='00')
        player_game_df = playergamefinder.get_data_frames()
        # save the returned results to csv
        player_game_df[0].to_csv(f"Data/PlayerGameLogs/player_gamelogs_20{latest_season-n}.csv")
        print(f"Player gamelogs obtained for 20{latest_season-n}")
    print("COMPLETE: Player gamelogs obtained")
else:
    print("Player gamelogs not requested (as per configuration")
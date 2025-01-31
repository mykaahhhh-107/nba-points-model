import schedule
import time
from nba_api.stats.static import players

def collect_player_data():
    # Use NBA API or any other source to collect data
    player_stats = players.get_players()  # Example call, you can customize it
    # Now send this data to the Flask/FastAPI API
    # You'll need a way to call your local API and get predictions based on this data.

# Set a job to run every day at midnight
schedule.every().day.at("00:00").do(collect_player_data)

while True:
    schedule.run_pending()
    time.sleep(1)

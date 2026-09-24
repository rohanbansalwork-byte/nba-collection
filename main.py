from nba_api.stats.endpoints import leaguedashplayerstats
import time

def main():
    print("Fetching NBA player stats for the 2025-26 season")
    time.sleep(1)
    data = leaguedashplayerstats.LeagueDashPlayerStats(season='2025-26')
    df = data.get_data_frames()[0]
    df.to_csv('nba_player_stats_2025_26.csv', index=False)
    print("Data saved to csv")
    print(df.columns)


if __name__ == "__main__":
    main();
import pandas as pd


def check_required_columns(df, required_columns):
    missing_columns = []
    for column in required_columns:
        if column not in df.columns:
            missing_columns.append(column)
    return missing_columns


# First Factor being Age
def average_age(df, team):
    team_data = df[df["TEAM_ABBREVIATION"] == team]
    return round(team_data["AGE"].mean(), 1) if not team_data.empty else None


# Second Factor being Assists
def total_assists(df, team):
    team_data = df[df["TEAM_ABBREVIATION"] == team]
    return team_data["AST"].sum() if not team_data.empty else None


# Third Factor being Rebounds
def total_rebounds(df, team):
    team_data = df[df["TEAM_ABBREVIATION"] == team]
    return team_data["REB"].sum() if not team_data.empty else None



# Fourth Factor being Field Goal Percentage
def field_goal_percentage(df, team):
    team_data = df[df["TEAM_ABBREVIATION"] == team]
    fg_made = team_data["FGM"].sum()
    fg_attempted = team_data["FGA"].sum()
    return round(100 * (fg_made / fg_attempted), 2) if fg_attempted != 0 else None

# Fifth Factor being Total Points
def total_points(df, team):
    team_data = df[df["TEAM_ABBREVIATION"] == team]
    return team_data["PTS"].sum() if not team_data.empty else None


def compare_team_stats(df, team1, team2):
    required_columns = ["AGE", "AST", "REB", "FGM", "FGA", "PTS"]

    missing_columns = check_required_columns(df, required_columns)
    if missing_columns:
        print(f"Missing required columns: {', '.join(missing_columns)}")
        return

    # Team1 Stats
    team1_avg_age = average_age(df, team1)
    team1_assists = total_assists(df, team1)
    team1_rebounds = total_rebounds(df, team1)
    team1_fg_pct = field_goal_percentage(df, team1)
    team1_points = total_points(df, team1)

    # Team2 Stats
    team2_avg_age = average_age(df, team2)
    team2_assists = total_assists(df, team2)
    team2_rebounds = total_rebounds(df, team2)
    team2_fg_pct = field_goal_percentage(df, team2)
    team2_points = total_points(df, team2)

    # Comparison Output
    print(f"Comparison between {team1} and {team2}:")
    print(
        f"{team1} - Average Age: {team1_avg_age}, Total Assists: {team1_assists}, Total Rebounds: {team1_rebounds}, FG%: {team1_fg_pct}"
        f", Points: {team1_points}")
    print(
        f"{team2} - Average Age: {team2_avg_age}, Total Assists: {team2_assists}, Total Rebounds: {team2_rebounds}, FG%: {team2_fg_pct}"
        f", Points: {team2_points}")

    return {
        team1: {"Average Age": team1_avg_age, "Total Assists": team1_assists, "Total Rebounds": team1_rebounds,
                "Field Goal %": team1_fg_pct},
        team2: {"Average Age": team2_avg_age, "Total Assists": team2_assists, "Total Rebounds": team2_rebounds,
                "Field Goal %": team2_fg_pct}
    }


# Main function to execute the comparison
def main():
    # Load the dataset
    df = pd.read_csv("nba_player_stats_2025_26.csv")

    # List of playoff teams
    playoffteams = ["OKC", "MEM", "DEN", "LAC", "LAL", "MIN", "HOU", "GSW", "CLE", "MIA", "IND", "MIL", "NYK", "DET",
                    "BOS", "ORL"]

    # Choose two teams to compare
    team1 = "DEN"
    team2 = "DET"


    compare_team_stats(df, team1, team2)



if __name__ == '__main__':
    main()

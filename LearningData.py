import pandas as pd
from matplotlib import pyplot as plt

def main():
    df = pd.read_csv('nba_player_stats_2025_26.csv')
    
    playoffteams = ["OKC","PHX", "LAL", "HOU", "DEN", "MIN", "SAS", "POR", "DET", "ORL", "CLE", "TOR", "NYK", "ATL", "BOS", "PHI"]
    for head, teamStats in df.iterrows():
        if teamStats["TEAM_ABBREVIATION"] in playoffteams:
            print(teamStats["TEAM_ABBREVIATION"], teamStats["PLAYER_NAME"], "Age:", teamStats["AGE"], "," , teamStats["PTS"], "PTS,", teamStats["AST"], "AST,", teamStats["REB"], "REB,", teamStats["FGM"], "FGM,", teamStats["FGA"], "FGA,", "FG%:", teamStats["FG_PCT"])

    print(avgAGE(df, "LAL"))
    team_fg = FGP(df, playoffteams)
    for index, values in team_fg.items():
        print(index, "FG%:", values)
    plotFGP(team_fg, "Field Goal Percentage of Playoff Teams", "%")


def avgAGE(df, team):
    team_age = df[df["TEAM_ABBREVIATION"] == team]
    return team_age["AGE"].mean() if not team_age.empty else None

def FGP(df, playoffteams):
    team_fg = {}
    team_fgp = {}
    for index, teamStats in df.iterrows():
        if teamStats["TEAM_ABBREVIATION"] in playoffteams:
            if teamStats["TEAM_ABBREVIATION"] not in team_fg:
                team_fg[teamStats["TEAM_ABBREVIATION"]] = {"FGM": 0, "FGA": 0}
            team_fg[teamStats["TEAM_ABBREVIATION"]]["FGM"] += teamStats["FGM"]
            team_fg[teamStats["TEAM_ABBREVIATION"]]["FGA"] += teamStats["FGA"]
    for team, stats in team_fg.items():
        if stats["FGA"] != 0:
            fgpct = stats["FGM"] / stats["FGA"]
            team_fgp[team] = fgpct
        else:
            print("ERROR, DIVISION BY ZERO")
    return  team_fgp


def plotFGP(team_fgp, title, label):
    sorted_teams = sorted(team_fgp.items(), key=lambda x: x[1], reverse=True)
    teams, fgpct = zip(*sorted_teams)
    plt.figure (figsize=(10, 6))
    plt.barh(teams, fgpct, color='skyblue')
    plt.xlabel(label)
    plt.title(title)
    plt.xlim(0, 1)
    plt.gca ().invert_yaxis()
    plt.show()

if __name__ == "__main__":
    main()
from nba_api.stats.static import teams
from nba_api.stats.endpoints import cumestatsteamgames, cumestatsteam
import pandas as pd
import numpy as np
import json
import difflib
import time
import requests


# Retry Wrapper with logging
def retry(func, retries=3):
    def retry_wrapper(*args, **kwargs):
        attempts = 0
        while attempts < retries:
            try:
                return func(*args, **kwargs)
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempts + 1} failed with error: {e}. Retrying...")
                time.sleep(30)
                attempts += 1

    return retry_wrapper


# Get Season Schedule Function
def getSeasonScheduleFrame(seasons, seasonType):
    # Helper functions
    def getGameDate(matchup):
        return matchup.partition(" at")[0][:10]

    def getHomeTeam(matchup):
        return matchup.partition(" at")[2]

    def getAwayTeam(matchup):
        return matchup.partition(" at")[0][10:]

    # Map team nickname to team ID
    def getTeamIDFromNickname(nickname):
        return teamLookup.loc[
            teamLookup["nickname"]
            == difflib.get_close_matches(nickname, teamLookup["nickname"], 1)[0]
        ].values[0][0]

    @retry
    def getRegularSeasonSchedule(season, teamID, seasonType):
        season_str = f"{season}-{str(season + 1)[-2:]}"
        teamGames = cumestatsteamgames.CumeStatsTeamGames(
            league_id="00",
            season=season_str,
            season_type_all_star=seasonType,
            team_id=teamID,
        ).get_normalized_json()
        teamGames = pd.DataFrame(json.loads(teamGames)["CumeStatsTeamGames"])
        teamGames["SEASON"] = season_str
        return teamGames

    # Get team lookup table
    teamLookup = pd.DataFrame(teams.get_teams())

    # Compile schedule for each team for each season
    scheduleFrame = pd.DataFrame()
    for season in seasons:
        print(f"Processing season {season}...")
        for team_id in teamLookup["id"]:
            time.sleep(1)  # Adjust as necessary to avoid rate limits
            team_schedule = getRegularSeasonSchedule(season, team_id, seasonType)
            scheduleFrame = pd.concat([scheduleFrame, team_schedule], ignore_index=True)

    # Map additional columns
    scheduleFrame["GAME_DATE"] = pd.to_datetime(
        scheduleFrame["MATCHUP"].map(getGameDate)
    )
    scheduleFrame["HOME_TEAM_NICKNAME"] = scheduleFrame["MATCHUP"].map(getHomeTeam)
    scheduleFrame["HOME_TEAM_ID"] = scheduleFrame["HOME_TEAM_NICKNAME"].map(
        getTeamIDFromNickname
    )
    scheduleFrame["AWAY_TEAM_NICKNAME"] = scheduleFrame["MATCHUP"].map(getAwayTeam)
    scheduleFrame["AWAY_TEAM_ID"] = scheduleFrame["AWAY_TEAM_NICKNAME"].map(
        getTeamIDFromNickname
    )
    scheduleFrame = scheduleFrame.drop_duplicates().reset_index(drop=True)
    return scheduleFrame


# Get Single Game Metrics
def getSingleGameMetrics(
    gameID, homeTeamID, awayTeamID, awayTeamNickname, seasonYear, gameDate
):
    @retry
    def getGameStats(teamID, gameID, seasonYear):
        gameStats = cumestatsteam.CumeStatsTeam(
            game_ids=gameID,
            league_id="00",
            season=seasonYear,
            season_type_all_star="Regular Season",
            team_id=teamID,
        ).get_normalized_json()
        return pd.DataFrame(json.loads(gameStats)["TotalTeamStats"])

    data = getGameStats(homeTeamID, gameID, seasonYear)
    data.at[1, "NICKNAME"], data.at[1, "TEAM_ID"] = awayTeamNickname, awayTeamID
    data.at[1, "OFFENSIVE_EFFICIENCY"] = (data.at[1, "FG"] + data.at[1, "AST"]) / (
        data.at[1, "FGA"]
        - data.at[1, "OFF_REB"]
        + data.at[1, "AST"]
        + data.at[1, "TOTAL_TURNOVERS"]
    )
    data.at[1, "SCORING_MARGIN"] = data.at[1, "PTS"] - data.at[0, "PTS"]
    data.at[0, "OFFENSIVE_EFFICIENCY"] = (data.at[0, "FG"] + data.at[0, "AST"]) / (
        data.at[0, "FGA"]
        - data.at[0, "OFF_REB"]
        + data.at[0, "AST"]
        + data.at[0, "TOTAL_TURNOVERS"]
    )
    data.at[0, "SCORING_MARGIN"] = data.at[0, "PTS"] - data.at[1, "PTS"]
    data["SEASON"], data["GAME_DATE"], data["GAME_ID"] = seasonYear, gameDate, gameID
    return data


# Collect all game logs for specified seasons
def getGameLogs(gameLogs, scheduleFrame):
    for i in range(len(scheduleFrame)):
        print(f"Processing game {i+1}/{len(scheduleFrame)}")
        gameMetrics = getSingleGameMetrics(
            scheduleFrame.at[i, "GAME_ID"],
            scheduleFrame.at[i, "HOME_TEAM_ID"],
            scheduleFrame.at[i, "AWAY_TEAM_ID"],
            scheduleFrame.at[i, "AWAY_TEAM_NICKNAME"],
            scheduleFrame.at[i, "SEASON"],
            scheduleFrame.at[i, "GAME_DATE"],
        )
        gameLogs = pd.concat([gameLogs, gameMetrics], ignore_index=True)
    return gameLogs


# Main script execution
if __name__ == "__main__":
    seasons = list(range(2013, 2024))
    seasonType = "Regular Season"

    # Get the schedule frame for all specified seasons
    scheduleFrame = getSeasonScheduleFrame(seasons, seasonType)

    # Initialize DataFrame to hold game logs
    gameLogs = pd.DataFrame()
    gameLogs = getGameLogs(gameLogs, scheduleFrame)

    # Calculate cumulative wins and losses for each team by season
    win_loss_summary = (
        gameLogs.groupby(["TEAM_ID", "SEASON"])
        .agg(
            total_wins=pd.NamedAgg(column="W", aggfunc="sum"),
            total_losses=pd.NamedAgg(column="L", aggfunc="sum"),
        )
        .reset_index()
    )

    # Calculate win percentage
    win_loss_summary["win_percentage"] = win_loss_summary["total_wins"] / (
        win_loss_summary["total_wins"] + win_loss_summary["total_losses"]
    )

    # Output the result to a CSV file
    win_loss_summary.to_csv("nba_win_loss_summary_2013_2024.csv", index=False)
    print("Win-loss data saved to nba_win_loss_summary_2013_2024.csv")

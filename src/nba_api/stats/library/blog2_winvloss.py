from nba_api.stats.static import teams
from nba_api.stats.endpoints import cumestatsteamgames, cumestatsteam
import pandas as pd
import numpy as np
import json
import difflib
import time
import requests


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


def getSeasonScheduleFrame(seasons, seasonType):
    def getGameDate(matchup):
        return matchup.partition(" at")[0][:10]

    def getHomeTeam(matchup):
        return matchup.partition(" at")[2]

    def getAwayTeam(matchup):
        return matchup.partition(" at")[0][10:]

    # team ID
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

    # team lookup table
    teamLookup = pd.DataFrame(teams.get_teams())

    # schedule for each team for each season
    scheduleFrame = pd.DataFrame()
    for season in seasons:
        print(f"Processing season {season}...")
        for team_id in teamLookup["id"]:
            time.sleep(1)
            team_schedule = getRegularSeasonSchedule(season, team_id, seasonType)
            scheduleFrame = pd.concat([scheduleFrame, team_schedule], ignore_index=True)

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


# game logs for specified seasons
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

        # home and away games
        gameMetrics["HOME_FLAG"] = [1, 0]  # 1 for home team, 0 for away team
        gameMetrics["AWAY_FLAG"] = [0, 1]  # 0 for home team, 1 for away team

        gameLogs = pd.concat([gameLogs, gameMetrics], ignore_index=True)

    return gameLogs


if __name__ == "__main__":
    seasons = list(range(2016, 2024))
    seasonType = "Regular Season"

    scheduleFrame = getSeasonScheduleFrame(seasons, seasonType)

    gameLogs = pd.DataFrame()
    gameLogs = getGameLogs(gameLogs, scheduleFrame)

    # home and road wins and losses for each team by season
    win_loss_summary = (
        gameLogs.groupby(["TEAM_ID", "SEASON", "HOME_FLAG"])
        .agg(
            total_wins=pd.NamedAgg(column="W", aggfunc="sum"),
            total_losses=pd.NamedAgg(column="L", aggfunc="sum"),
        )
        .reset_index()
    )

    # home and road stats
    home_summary = win_loss_summary[win_loss_summary["HOME_FLAG"] == 1].copy()
    road_summary = win_loss_summary[win_loss_summary["HOME_FLAG"] == 0].copy()

    # win percentages
    home_summary["home_win_percentage"] = home_summary["total_wins"] / (
        home_summary["total_wins"] + home_summary["total_losses"]
    )
    road_summary["road_win_percentage"] = road_summary["total_wins"] / (
        road_summary["total_wins"] + road_summary["total_losses"]
    )

    # home and road summaries
    win_loss_combined = pd.merge(
        home_summary[["TEAM_ID", "SEASON", "home_win_percentage"]],
        road_summary[["TEAM_ID", "SEASON", "road_win_percentage"]],
        on=["TEAM_ID", "SEASON"],
        how="outer",
    )

    # CSV file
    win_loss_combined.to_csv("nba_home_road_win_percentage_2016_2024.csv", index=False)
    print(
        "Home and road win percentages saved to nba_home_road_win_percentage_2016_2024.csv"
    )

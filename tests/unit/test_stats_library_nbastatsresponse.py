import json
import pytest
from nba_api.stats.library.nba_api_http import NBAStatsResponse

responses = [
    {
        "response": '{"meta":{"version":1,"request":"http://nba.cloud/games/0021700807/boxscoreusage?Format=json","time":"2023-09-14T19:35:59.3559Z"},"boxScoreUsage":{"gameId":"0021700807","awayTeamId":1610612750,"homeTeamId":1610612739,"homeTeam":{"teamId":1610612739,"teamCity":"Cleveland","teamName":"Cavaliers","teamTricode":"CLE","teamSlug":"cavaliers","players":[{"personId":2544,"firstName":"LeBron","familyName":"James","nameI":"L. James","playerSlug":"lebron-james","position":"F","comment":"","jerseyNum":"","statistics":{"minutes":"48:19","usagePercentage":0.276,"percentageFieldGoalsMade":0.333,"percentageFieldGoalsAttempted":0.278,"percentageThreePointersMade":0.25,"percentageThreePointersAttempted":0.184,"percentageFreeThrowsMade":0,"percentageFreeThrowsAttempted":0.105,"percentageReboundsOffensive":0.2,"percentageReboundsDefensive":0.29,"percentageReboundsTotal":0.278,"percentageAssists":0.484,"percentageTurnovers":0.357,"percentageSteals":0.25,"percentageBlocks":1,"percentageBlocksAllowed":0,"percentagePersonalFouls":0.176,"percentagePersonalFoulsDrawn":0.188,"percentagePoints":0.287}},{"personId":203109,"firstName":"Jae","familyName":"Crowder","nameI":"J. Crowder","playerSlug":"jae-crowder","position":"F","comment":"","jerseyNum":"","statistics":{"minutes":"23:37","usagePercentage":0.118,"percentageFieldGoalsMade":0.115,"percentageFieldGoalsAttempted":0.122,"percentageThreePointersMade":0.1,"percentageThreePointersAttempted":0.125,"percentageFreeThrowsMade":0.5,"percentageFreeThrowsAttempted":0.364,"percentageReboundsOffensive":0,"percentageReboundsDefensive":0.182,"percentageReboundsTotal":0.143,"percentageAssists":0.125,"percentageTurnovers":0,"percentageSteals":0.333,"percentageBlocks":0,"percentageBlocksAllowed":0,"percentagePersonalFouls":0.5,"percentagePersonalFoulsDrawn":0.375,"percentagePoints":0.147}}],"statistics":{"minutes":"265:00","usagePercentage":1,"percentageFieldGoalsMade":1,"percentageFieldGoalsAttempted":1,"percentageThreePointersMade":1,"percentageThreePointersAttempted":1,"percentageFreeThrowsMade":1,"percentageFreeThrowsAttempted":1,"percentageReboundsOffensive":1,"percentageReboundsDefensive":1,"percentageReboundsTotal":1,"percentageAssists":1,"percentageTurnovers":1,"percentageSteals":1,"percentageBlocks":1,"percentageBlocksAllowed":1,"percentagePersonalFouls":1,"percentagePersonalFoulsDrawn":1,"percentagePoints":1}},"awayTeam":{"teamId":1610612750,"teamCity":"Minnesota","teamName":"Timberwolves","teamTricode":"MIN","teamSlug":"timberwolves","players":[{"personId":203952,"firstName":"Andrew","familyName":"Wiggins","nameI":"A. Wiggins","playerSlug":"andrew-wiggins","position":"F","comment":"","jerseyNum":"","statistics":{"minutes":"39:51","usagePercentage":0.194,"percentageFieldGoalsMade":0.167,"percentageFieldGoalsAttempted":0.188,"percentageThreePointersMade":0.286,"percentageThreePointersAttempted":0.381,"percentageFreeThrowsMade":0.111,"percentageFreeThrowsAttempted":0.2,"percentageReboundsOffensive":0,"percentageReboundsDefensive":0.08,"percentageReboundsTotal":0.071,"percentageAssists":0.043,"percentageTurnovers":0.222,"percentageSteals":0,"percentageBlocks":0,"percentageBlocksAllowed":0,"percentagePersonalFouls":0.273,"percentagePersonalFoulsDrawn":0.111,"percentagePoints":0.178}},{"personId":201959,"firstName":"Taj","familyName":"Gibson","nameI":"T. Gibson","playerSlug":"taj-gibson","position":"F","comment":"","jerseyNum":"","statistics":{"minutes":"35:08","usagePercentage":0.11,"percentageFieldGoalsMade":0.103,"percentageFieldGoalsAttempted":0.131,"percentageThreePointersMade":0,"percentageThreePointersAttempted":0,"percentageFreeThrowsMade":0.143,"percentageFreeThrowsAttempted":0.125,"percentageReboundsOffensive":0.667,"percentageReboundsDefensive":0.15,"percentageReboundsTotal":0.217,"percentageAssists":0.087,"percentageTurnovers":0,"percentageSteals":0,"percentageBlocks":0.5,"percentageBlocksAllowed":0,"percentagePersonalFouls":0.111,"percentagePersonalFoulsDrawn":0.125,"percentagePoints":0.09}}],"statistics":{"minutes":"265:00","usagePercentage":1,"percentageFieldGoalsMade":1,"percentageFieldGoalsAttempted":1,"percentageThreePointersMade":1,"percentageThreePointersAttempted":1,"percentageFreeThrowsMade":1,"percentageFreeThrowsAttempted":1,"percentageReboundsOffensive":1,"percentageReboundsDefensive":1,"percentageReboundsTotal":1,"percentageAssists":1,"percentageTurnovers":1,"percentageSteals":1,"percentageBlocks":1,"percentageBlocksAllowed":1,"percentagePersonalFouls":1,"percentagePersonalFoulsDrawn":1,"percentagePoints":1}}}}',
        "status_code": 200,
        "url": "https://stats.nba.com/stats/boxscoreusagev3?GameID=0021700807&LeagueID=00&endPeriod=0&endRange=0&rangeType=0&startPeriod=0&startRange=0",
        "exp_parameters": None,
        "exp_status_code": 200,
        "exp_normalized_dict": {},
        "exp_normalized_json": "{}",
        "exp_headers_from_data_sets": {},
        "exp_data_sets": {
            "PlayerStats": {
                "headers": [
                    "gameId",
                    "teamId",
                    "teamCity",
                    "teamName",
                    "teamTricode",
                    "teamSlug",
                    "personId",
                    "firstName",
                    "familyName",
                    "nameI",
                    "playerSlug",
                    "position",
                    "comment",
                    "jerseyNum",
                    "minutes",
                    "usagePercentage",
                    "percentageFieldGoalsMade",
                    "percentageFieldGoalsAttempted",
                    "percentageThreePointersMade",
                    "percentageThreePointersAttempted",
                    "percentageFreeThrowsMade",
                    "percentageFreeThrowsAttempted",
                    "percentageReboundsOffensive",
                    "percentageReboundsDefensive",
                    "percentageReboundsTotal",
                    "percentageAssists",
                    "percentageTurnovers",
                    "percentageSteals",
                    "percentageBlocks",
                    "percentageBlocksAllowed",
                    "percentagePersonalFouls",
                    "percentagePersonalFoulsDrawn",
                    "percentagePoints",
                ],
                "data": [
                    [
                        "0021700807",
                        1610612750,
                        "Minnesota",
                        "Timberwolves",
                        "MIN",
                        "timberwolves",
                        203952,
                        "Andrew",
                        "Wiggins",
                        "A. Wiggins",
                        "andrew-wiggins",
                        "F",
                        "",
                        "",
                        "39:51",
                        0.194,
                        0.167,
                        0.188,
                        0.286,
                        0.381,
                        0.111,
                        0.2,
                        0,
                        0.08,
                        0.071,
                        0.043,
                        0.222,
                        0,
                        0,
                        0,
                        0.273,
                        0.111,
                        0.178,
                    ],
                    [
                        "0021700807",
                        1610612750,
                        "Minnesota",
                        "Timberwolves",
                        "MIN",
                        "timberwolves",
                        201959,
                        "Taj",
                        "Gibson",
                        "T. Gibson",
                        "taj-gibson",
                        "F",
                        "",
                        "",
                        "35:08",
                        0.11,
                        0.103,
                        0.131,
                        0,
                        0,
                        0.143,
                        0.125,
                        0.667,
                        0.15,
                        0.217,
                        0.087,
                        0,
                        0,
                        0.5,
                        0,
                        0.111,
                        0.125,
                        0.09,
                    ],
                    [
                        "0021700807",
                        1610612739,
                        "Cleveland",
                        "Cavaliers",
                        "CLE",
                        "cavaliers",
                        2544,
                        "LeBron",
                        "James",
                        "L. James",
                        "lebron-james",
                        "F",
                        "",
                        "",
                        "48:19",
                        0.276,
                        0.333,
                        0.278,
                        0.25,
                        0.184,
                        0,
                        0.105,
                        0.2,
                        0.29,
                        0.278,
                        0.484,
                        0.357,
                        0.25,
                        1,
                        0,
                        0.176,
                        0.188,
                        0.287,
                    ],
                    [
                        "0021700807",
                        1610612739,
                        "Cleveland",
                        "Cavaliers",
                        "CLE",
                        "cavaliers",
                        203109,
                        "Jae",
                        "Crowder",
                        "J. Crowder",
                        "jae-crowder",
                        "F",
                        "",
                        "",
                        "23:37",
                        0.118,
                        0.115,
                        0.122,
                        0.1,
                        0.125,
                        0.5,
                        0.364,
                        0,
                        0.182,
                        0.143,
                        0.125,
                        0,
                        0.333,
                        0,
                        0,
                        0.5,
                        0.375,
                        0.147,
                    ],
                ],
            },
            "TeamStats": {
                "headers": [
                    "gameId",
                    "teamId",
                    "teamCity",
                    "teamName",
                    "teamTricode",
                    "teamSlug",
                    "minutes",
                    "usagePercentage",
                    "percentageFieldGoalsMade",
                    "percentageFieldGoalsAttempted",
                    "percentageThreePointersMade",
                    "percentageThreePointersAttempted",
                    "percentageFreeThrowsMade",
                    "percentageFreeThrowsAttempted",
                    "percentageReboundsOffensive",
                    "percentageReboundsDefensive",
                    "percentageReboundsTotal",
                    "percentageAssists",
                    "percentageTurnovers",
                    "percentageSteals",
                    "percentageBlocks",
                    "percentageBlocksAllowed",
                    "percentagePersonalFouls",
                    "percentagePersonalFoulsDrawn",
                    "percentagePoints",
                ],
                "data": [
                    [
                        "0021700807",
                        1610612739,
                        "Cleveland",
                        "Cavaliers",
                        "CLE",
                        "cavaliers",
                        "265:00",
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                    ],
                    [
                        "0021700807",
                        1610612750,
                        "Minnesota",
                        "Timberwolves",
                        "MIN",
                        "timberwolves",
                        "265:00",
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                    ],
                ],
            },
        },
        "endpoint": "boxscoreusagev3",
    },
    {
        "response": '{"resource":"boxscore","parameters":{"GameID":"0021700807","StartPeriod":0,"EndPeriod":0,"StartRange":0,"EndRange":0,"RangeType":0},"resultSets":[{"name":"sqlPlayersUsage","headers":["GAME_ID","TEAM_ID","TEAM_ABBREVIATION","TEAM_CITY","PLAYER_ID","PLAYER_NAME","NICKNAME","START_POSITION","COMMENT","MIN","USG_PCT","PCT_FGM","PCT_FGA","PCT_FG3M","PCT_FG3A","PCT_FTM","PCT_FTA","PCT_OREB","PCT_DREB","PCT_REB","PCT_AST","PCT_TOV","PCT_STL","PCT_BLK","PCT_BLKA","PCT_PF","PCT_PFD","PCT_PTS"],"rowSet":[["0021700807",1610612750,"MIN","Minnesota",203952,"Andrew Wiggins","Andrew","F","","39.000000:51",0.194,0.167,0.188,0.286,0.381,0.111,0.2,0,0.08,0.071,0.043,0.222,0,0,0,0.273,0.111,0.178],["0021700807",1610612750,"MIN","Minnesota",201959,"Taj Gibson","Taj","F","","35.000000:08",0.11,0.103,0.131,0,0,0.143,0.125,0.667,0.15,0.217,0.087,0,0,0.5,0,0.111,0.125,0.09],["0021700807",1610612739,"CLE","Cleveland",2544,"LeBron James","LeBron","F","","48.000000:19",0.276,0.333,0.278,0.25,0.184,0,0.105,0.2,0.29,0.278,0.484,0.357,0.25,1,0,0.176,0.188,0.287],["0021700807",1610612739,"CLE","Cleveland",203109,"Jae Crowder","Jae","F","","23.000000:37",0.118,0.115,0.122,0.1,0.125,0.5,0.364,0,0.182,0.143,0.125,0,0.333,0,0,0.5,0.375,0.147]]},{"name":"sqlTeamsUsage","headers":["GAME_ID","TEAM_ID","TEAM_NAME","TEAM_ABBREVIATION","TEAM_CITY","MIN","USG_PCT","PCT_FGM","PCT_FGA","PCT_FG3M","PCT_FG3A","PCT_FTM","PCT_FTA","PCT_OREB","PCT_DREB","PCT_REB","PCT_AST","PCT_TOV","PCT_STL","PCT_BLK","PCT_BLKA","PCT_PF","PCT_PFD","PCT_PTS"],"rowSet":[["0021700807",1610612750,"Timberwolves","MIN","Minnesota","265.000000:00",1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],["0021700807",1610612739,"Cavaliers","CLE","Cleveland","265.000000:00",1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]}]}',
        "status_code": 200,
        "url": "https://stats.nba.com/stats/boxscoreusagev2?GameID=0021700807&LeagueID=00&endPeriod=0&endRange=0&rangeType=0&startPeriod=0&startRange=0",
        "exp_parameters": {
            "GameID": "0021700807",
            "StartPeriod": 0,
            "EndPeriod": 0,
            "StartRange": 0,
            "EndRange": 0,
            "RangeType": 0,
        },
        "exp_status_code": 200,
        "exp_normalized_dict": {
            "sqlPlayersUsage": [
                {
                    "GAME_ID": "0021700807",
                    "TEAM_ID": 1610612750,
                    "TEAM_ABBREVIATION": "MIN",
                    "TEAM_CITY": "Minnesota",
                    "PLAYER_ID": 203952,
                    "PLAYER_NAME": "Andrew Wiggins",
                    "NICKNAME": "Andrew",
                    "START_POSITION": "F",
                    "COMMENT": "",
                    "MIN": "39.000000:51",
                    "USG_PCT": 0.194,
                    "PCT_FGM": 0.167,
                    "PCT_FGA": 0.188,
                    "PCT_FG3M": 0.286,
                    "PCT_FG3A": 0.381,
                    "PCT_FTM": 0.111,
                    "PCT_FTA": 0.2,
                    "PCT_OREB": 0,
                    "PCT_DREB": 0.08,
                    "PCT_REB": 0.071,
                    "PCT_AST": 0.043,
                    "PCT_TOV": 0.222,
                    "PCT_STL": 0,
                    "PCT_BLK": 0,
                    "PCT_BLKA": 0,
                    "PCT_PF": 0.273,
                    "PCT_PFD": 0.111,
                    "PCT_PTS": 0.178,
                },
                {
                    "GAME_ID": "0021700807",
                    "TEAM_ID": 1610612750,
                    "TEAM_ABBREVIATION": "MIN",
                    "TEAM_CITY": "Minnesota",
                    "PLAYER_ID": 201959,
                    "PLAYER_NAME": "Taj Gibson",
                    "NICKNAME": "Taj",
                    "START_POSITION": "F",
                    "COMMENT": "",
                    "MIN": "35.000000:08",
                    "USG_PCT": 0.11,
                    "PCT_FGM": 0.103,
                    "PCT_FGA": 0.131,
                    "PCT_FG3M": 0,
                    "PCT_FG3A": 0,
                    "PCT_FTM": 0.143,
                    "PCT_FTA": 0.125,
                    "PCT_OREB": 0.667,
                    "PCT_DREB": 0.15,
                    "PCT_REB": 0.217,
                    "PCT_AST": 0.087,
                    "PCT_TOV": 0,
                    "PCT_STL": 0,
                    "PCT_BLK": 0.5,
                    "PCT_BLKA": 0,
                    "PCT_PF": 0.111,
                    "PCT_PFD": 0.125,
                    "PCT_PTS": 0.09,
                },
                {
                    "GAME_ID": "0021700807",
                    "TEAM_ID": 1610612739,
                    "TEAM_ABBREVIATION": "CLE",
                    "TEAM_CITY": "Cleveland",
                    "PLAYER_ID": 2544,
                    "PLAYER_NAME": "LeBron James",
                    "NICKNAME": "LeBron",
                    "START_POSITION": "F",
                    "COMMENT": "",
                    "MIN": "48.000000:19",
                    "USG_PCT": 0.276,
                    "PCT_FGM": 0.333,
                    "PCT_FGA": 0.278,
                    "PCT_FG3M": 0.25,
                    "PCT_FG3A": 0.184,
                    "PCT_FTM": 0,
                    "PCT_FTA": 0.105,
                    "PCT_OREB": 0.2,
                    "PCT_DREB": 0.29,
                    "PCT_REB": 0.278,
                    "PCT_AST": 0.484,
                    "PCT_TOV": 0.357,
                    "PCT_STL": 0.25,
                    "PCT_BLK": 1,
                    "PCT_BLKA": 0,
                    "PCT_PF": 0.176,
                    "PCT_PFD": 0.188,
                    "PCT_PTS": 0.287,
                },
                {
                    "GAME_ID": "0021700807",
                    "TEAM_ID": 1610612739,
                    "TEAM_ABBREVIATION": "CLE",
                    "TEAM_CITY": "Cleveland",
                    "PLAYER_ID": 203109,
                    "PLAYER_NAME": "Jae Crowder",
                    "NICKNAME": "Jae",
                    "START_POSITION": "F",
                    "COMMENT": "",
                    "MIN": "23.000000:37",
                    "USG_PCT": 0.118,
                    "PCT_FGM": 0.115,
                    "PCT_FGA": 0.122,
                    "PCT_FG3M": 0.1,
                    "PCT_FG3A": 0.125,
                    "PCT_FTM": 0.5,
                    "PCT_FTA": 0.364,
                    "PCT_OREB": 0,
                    "PCT_DREB": 0.182,
                    "PCT_REB": 0.143,
                    "PCT_AST": 0.125,
                    "PCT_TOV": 0,
                    "PCT_STL": 0.333,
                    "PCT_BLK": 0,
                    "PCT_BLKA": 0,
                    "PCT_PF": 0.5,
                    "PCT_PFD": 0.375,
                    "PCT_PTS": 0.147,
                },
            ],
            "sqlTeamsUsage": [
                {
                    "GAME_ID": "0021700807",
                    "TEAM_ID": 1610612750,
                    "TEAM_NAME": "Timberwolves",
                    "TEAM_ABBREVIATION": "MIN",
                    "TEAM_CITY": "Minnesota",
                    "MIN": "265.000000:00",
                    "USG_PCT": 1,
                    "PCT_FGM": 1,
                    "PCT_FGA": 1,
                    "PCT_FG3M": 1,
                    "PCT_FG3A": 1,
                    "PCT_FTM": 1,
                    "PCT_FTA": 1,
                    "PCT_OREB": 1,
                    "PCT_DREB": 1,
                    "PCT_REB": 1,
                    "PCT_AST": 1,
                    "PCT_TOV": 1,
                    "PCT_STL": 1,
                    "PCT_BLK": 1,
                    "PCT_BLKA": 1,
                    "PCT_PF": 1,
                    "PCT_PFD": 1,
                    "PCT_PTS": 1,
                },
                {
                    "GAME_ID": "0021700807",
                    "TEAM_ID": 1610612739,
                    "TEAM_NAME": "Cavaliers",
                    "TEAM_ABBREVIATION": "CLE",
                    "TEAM_CITY": "Cleveland",
                    "MIN": "265.000000:00",
                    "USG_PCT": 1,
                    "PCT_FGM": 1,
                    "PCT_FGA": 1,
                    "PCT_FG3M": 1,
                    "PCT_FG3A": 1,
                    "PCT_FTM": 1,
                    "PCT_FTA": 1,
                    "PCT_OREB": 1,
                    "PCT_DREB": 1,
                    "PCT_REB": 1,
                    "PCT_AST": 1,
                    "PCT_TOV": 1,
                    "PCT_STL": 1,
                    "PCT_BLK": 1,
                    "PCT_BLKA": 1,
                    "PCT_PF": 1,
                    "PCT_PFD": 1,
                    "PCT_PTS": 1,
                },
            ],
        },
        "exp_normalized_json": '{"sqlPlayersUsage": [{"GAME_ID": "0021700807", "TEAM_ID": 1610612750, "TEAM_ABBREVIATION": "MIN", "TEAM_CITY": "Minnesota", "PLAYER_ID": 203952, "PLAYER_NAME": "Andrew Wiggins", "NICKNAME": "Andrew", "START_POSITION": "F", "COMMENT": "", "MIN": "39.000000:51", "USG_PCT": 0.194, "PCT_FGM": 0.167, "PCT_FGA": 0.188, "PCT_FG3M": 0.286, "PCT_FG3A": 0.381, "PCT_FTM": 0.111, "PCT_FTA": 0.2, "PCT_OREB": 0, "PCT_DREB": 0.08, "PCT_REB": 0.071, "PCT_AST": 0.043, "PCT_TOV": 0.222, "PCT_STL": 0, "PCT_BLK": 0, "PCT_BLKA": 0, "PCT_PF": 0.273, "PCT_PFD": 0.111, "PCT_PTS": 0.178}, {"GAME_ID": "0021700807", "TEAM_ID": 1610612750, "TEAM_ABBREVIATION": "MIN", "TEAM_CITY": "Minnesota", "PLAYER_ID": 201959, "PLAYER_NAME": "Taj Gibson", "NICKNAME": "Taj", "START_POSITION": "F", "COMMENT": "", "MIN": "35.000000:08", "USG_PCT": 0.11, "PCT_FGM": 0.103, "PCT_FGA": 0.131, "PCT_FG3M": 0, "PCT_FG3A": 0, "PCT_FTM": 0.143, "PCT_FTA": 0.125, "PCT_OREB": 0.667, "PCT_DREB": 0.15, "PCT_REB": 0.217, "PCT_AST": 0.087, "PCT_TOV": 0, "PCT_STL": 0, "PCT_BLK": 0.5, "PCT_BLKA": 0, "PCT_PF": 0.111, "PCT_PFD": 0.125, "PCT_PTS": 0.09}, {"GAME_ID": "0021700807", "TEAM_ID": 1610612739, "TEAM_ABBREVIATION": "CLE", "TEAM_CITY": "Cleveland", "PLAYER_ID": 2544, "PLAYER_NAME": "LeBron James", "NICKNAME": "LeBron", "START_POSITION": "F", "COMMENT": "", "MIN": "48.000000:19", "USG_PCT": 0.276, "PCT_FGM": 0.333, "PCT_FGA": 0.278, "PCT_FG3M": 0.25, "PCT_FG3A": 0.184, "PCT_FTM": 0, "PCT_FTA": 0.105, "PCT_OREB": 0.2, "PCT_DREB": 0.29, "PCT_REB": 0.278, "PCT_AST": 0.484, "PCT_TOV": 0.357, "PCT_STL": 0.25, "PCT_BLK": 1, "PCT_BLKA": 0, "PCT_PF": 0.176, "PCT_PFD": 0.188, "PCT_PTS": 0.287}, {"GAME_ID": "0021700807", "TEAM_ID": 1610612739, "TEAM_ABBREVIATION": "CLE", "TEAM_CITY": "Cleveland", "PLAYER_ID": 203109, "PLAYER_NAME": "Jae Crowder", "NICKNAME": "Jae", "START_POSITION": "F", "COMMENT": "", "MIN": "23.000000:37", "USG_PCT": 0.118, "PCT_FGM": 0.115, "PCT_FGA": 0.122, "PCT_FG3M": 0.1, "PCT_FG3A": 0.125, "PCT_FTM": 0.5, "PCT_FTA": 0.364, "PCT_OREB": 0, "PCT_DREB": 0.182, "PCT_REB": 0.143, "PCT_AST": 0.125, "PCT_TOV": 0, "PCT_STL": 0.333, "PCT_BLK": 0, "PCT_BLKA": 0, "PCT_PF": 0.5, "PCT_PFD": 0.375, "PCT_PTS": 0.147}], "sqlTeamsUsage": [{"GAME_ID": "0021700807", "TEAM_ID": 1610612750, "TEAM_NAME": "Timberwolves", "TEAM_ABBREVIATION": "MIN", "TEAM_CITY": "Minnesota", "MIN": "265.000000:00", "USG_PCT": 1, "PCT_FGM": 1, "PCT_FGA": 1, "PCT_FG3M": 1, "PCT_FG3A": 1, "PCT_FTM": 1, "PCT_FTA": 1, "PCT_OREB": 1, "PCT_DREB": 1, "PCT_REB": 1, "PCT_AST": 1, "PCT_TOV": 1, "PCT_STL": 1, "PCT_BLK": 1, "PCT_BLKA": 1, "PCT_PF": 1, "PCT_PFD": 1, "PCT_PTS": 1}, {"GAME_ID": "0021700807", "TEAM_ID": 1610612739, "TEAM_NAME": "Cavaliers", "TEAM_ABBREVIATION": "CLE", "TEAM_CITY": "Cleveland", "MIN": "265.000000:00", "USG_PCT": 1, "PCT_FGM": 1, "PCT_FGA": 1, "PCT_FG3M": 1, "PCT_FG3A": 1, "PCT_FTM": 1, "PCT_FTA": 1, "PCT_OREB": 1, "PCT_DREB": 1, "PCT_REB": 1, "PCT_AST": 1, "PCT_TOV": 1, "PCT_STL": 1, "PCT_BLK": 1, "PCT_BLKA": 1, "PCT_PF": 1, "PCT_PFD": 1, "PCT_PTS": 1}]}',
        "exp_headers_from_data_sets": {
            "sqlPlayersUsage": [
                "GAME_ID",
                "TEAM_ID",
                "TEAM_ABBREVIATION",
                "TEAM_CITY",
                "PLAYER_ID",
                "PLAYER_NAME",
                "NICKNAME",
                "START_POSITION",
                "COMMENT",
                "MIN",
                "USG_PCT",
                "PCT_FGM",
                "PCT_FGA",
                "PCT_FG3M",
                "PCT_FG3A",
                "PCT_FTM",
                "PCT_FTA",
                "PCT_OREB",
                "PCT_DREB",
                "PCT_REB",
                "PCT_AST",
                "PCT_TOV",
                "PCT_STL",
                "PCT_BLK",
                "PCT_BLKA",
                "PCT_PF",
                "PCT_PFD",
                "PCT_PTS",
            ],
            "sqlTeamsUsage": [
                "GAME_ID",
                "TEAM_ID",
                "TEAM_NAME",
                "TEAM_ABBREVIATION",
                "TEAM_CITY",
                "MIN",
                "USG_PCT",
                "PCT_FGM",
                "PCT_FGA",
                "PCT_FG3M",
                "PCT_FG3A",
                "PCT_FTM",
                "PCT_FTA",
                "PCT_OREB",
                "PCT_DREB",
                "PCT_REB",
                "PCT_AST",
                "PCT_TOV",
                "PCT_STL",
                "PCT_BLK",
                "PCT_BLKA",
                "PCT_PF",
                "PCT_PFD",
                "PCT_PTS",
            ],
        },
        "exp_data_sets": {
            "sqlPlayersUsage": {
                "headers": [
                    "GAME_ID",
                    "TEAM_ID",
                    "TEAM_ABBREVIATION",
                    "TEAM_CITY",
                    "PLAYER_ID",
                    "PLAYER_NAME",
                    "NICKNAME",
                    "START_POSITION",
                    "COMMENT",
                    "MIN",
                    "USG_PCT",
                    "PCT_FGM",
                    "PCT_FGA",
                    "PCT_FG3M",
                    "PCT_FG3A",
                    "PCT_FTM",
                    "PCT_FTA",
                    "PCT_OREB",
                    "PCT_DREB",
                    "PCT_REB",
                    "PCT_AST",
                    "PCT_TOV",
                    "PCT_STL",
                    "PCT_BLK",
                    "PCT_BLKA",
                    "PCT_PF",
                    "PCT_PFD",
                    "PCT_PTS",
                ],
                "data": [
                    [
                        "0021700807",
                        1610612750,
                        "MIN",
                        "Minnesota",
                        203952,
                        "Andrew Wiggins",
                        "Andrew",
                        "F",
                        "",
                        "39.000000:51",
                        0.194,
                        0.167,
                        0.188,
                        0.286,
                        0.381,
                        0.111,
                        0.2,
                        0,
                        0.08,
                        0.071,
                        0.043,
                        0.222,
                        0,
                        0,
                        0,
                        0.273,
                        0.111,
                        0.178,
                    ],
                    [
                        "0021700807",
                        1610612750,
                        "MIN",
                        "Minnesota",
                        201959,
                        "Taj Gibson",
                        "Taj",
                        "F",
                        "",
                        "35.000000:08",
                        0.11,
                        0.103,
                        0.131,
                        0,
                        0,
                        0.143,
                        0.125,
                        0.667,
                        0.15,
                        0.217,
                        0.087,
                        0,
                        0,
                        0.5,
                        0,
                        0.111,
                        0.125,
                        0.09,
                    ],
                    [
                        "0021700807",
                        1610612739,
                        "CLE",
                        "Cleveland",
                        2544,
                        "LeBron James",
                        "LeBron",
                        "F",
                        "",
                        "48.000000:19",
                        0.276,
                        0.333,
                        0.278,
                        0.25,
                        0.184,
                        0,
                        0.105,
                        0.2,
                        0.29,
                        0.278,
                        0.484,
                        0.357,
                        0.25,
                        1,
                        0,
                        0.176,
                        0.188,
                        0.287,
                    ],
                    [
                        "0021700807",
                        1610612739,
                        "CLE",
                        "Cleveland",
                        203109,
                        "Jae Crowder",
                        "Jae",
                        "F",
                        "",
                        "23.000000:37",
                        0.118,
                        0.115,
                        0.122,
                        0.1,
                        0.125,
                        0.5,
                        0.364,
                        0,
                        0.182,
                        0.143,
                        0.125,
                        0,
                        0.333,
                        0,
                        0,
                        0.5,
                        0.375,
                        0.147,
                    ],
                ],
            },
            "sqlTeamsUsage": {
                "headers": [
                    "GAME_ID",
                    "TEAM_ID",
                    "TEAM_NAME",
                    "TEAM_ABBREVIATION",
                    "TEAM_CITY",
                    "MIN",
                    "USG_PCT",
                    "PCT_FGM",
                    "PCT_FGA",
                    "PCT_FG3M",
                    "PCT_FG3A",
                    "PCT_FTM",
                    "PCT_FTA",
                    "PCT_OREB",
                    "PCT_DREB",
                    "PCT_REB",
                    "PCT_AST",
                    "PCT_TOV",
                    "PCT_STL",
                    "PCT_BLK",
                    "PCT_BLKA",
                    "PCT_PF",
                    "PCT_PFD",
                    "PCT_PTS",
                ],
                "data": [
                    [
                        "0021700807",
                        1610612750,
                        "Timberwolves",
                        "MIN",
                        "Minnesota",
                        "265.000000:00",
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                    ],
                    [
                        "0021700807",
                        1610612739,
                        "Cavaliers",
                        "CLE",
                        "Cleveland",
                        "265.000000:00",
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                        1,
                    ],
                ],
            },
        },
        "endpoint": None,
    },
]


@pytest.mark.parametrize("response", responses)
class TestNBAStatsResponse:
    def nbastatsresponse(self, response):
        return NBAStatsResponse(
            response["response"], response["status_code"], response["url"]
        )

    def test_get_parameters(self, response):
        assert (
            self.nbastatsresponse(response).get_parameters()
            == response["exp_parameters"]
        )

    def test_get_normalized_dict(self, response):
        assert (
            self.nbastatsresponse(response).get_normalized_dict()
            == response["exp_normalized_dict"]
        )

    def test_get_normalized_json(self, response):
        assert (
            self.nbastatsresponse(response).get_normalized_json()
            == response["exp_normalized_json"]
        )

    def test_get_headers_from_data_sets(self, response):
        assert (
            self.nbastatsresponse(response).get_headers_from_data_sets()
            == response["exp_headers_from_data_sets"]
        )

    def test_get_data_sets(self, response):
        assert (
            self.nbastatsresponse(response).get_data_sets(endpoint=response["endpoint"])
            == response["exp_data_sets"]
        )

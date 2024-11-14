from nba_api.stats.endpoints._base import Endpoint
from nba_api.stats.library.nba_api_http import NBAStatsHTTP
from nba_api.stats.library.parameters import (
    LastNGames,
    MeasureTypeDetailedDefense,
    Month,
    PaceAdjust,
    PerModeDetailed,
    Period,
    PlusMinus,
    Rank,
    Season,
    SeasonTypeAllStar,
    GameSegmentNullable,
    LeagueIDNullable,
    LocationNullable,
    OutcomeNullable,
    SeasonSegmentNullable,
    ShotClockRangeNullable,
    ConferenceNullable,
    DivisionNullable,
)


class TeamDashboardByShootingSplits(Endpoint):
    endpoint = "teamdashboardbyshootingsplits"
    expected_data = {
        "AssistedBy": [
            "GROUP_SET",
            "PLAYER_ID",
            "PLAYER_NAME",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "AssitedShotTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "OverallTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "Shot5FTTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "Shot8FTTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "ShotAreaTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS",
        ],
        "ShotTypeTeamDashboard": [
            "GROUP_SET",
            "GROUP_VALUE",
            "FGM",
            "FGA",
            "FG_PCT",
            "FG3M",
            "FG3A",
            "FG3_PCT",
            "EFG_PCT",
            "BLKA",
            "PCT_AST_2PM",
            "PCT_UAST_2PM",
            "PCT_AST_3PM",
            "PCT_UAST_3PM",
            "PCT_AST_FGM",
            "PCT_UAST_FGM",
            "FGM_RANK",
            "FGA_RANK",
            "FG_PCT_RANK",
            "FG3M_RANK",
            "FG3A_RANK",
            "FG3_PCT_RANK",
            "EFG_PCT_RANK",
            "BLKA_RANK",
            "PCT_AST_2PM_RANK",
            "PCT_UAST_2PM_RANK",
            "PCT_AST_3PM_RANK",
            "PCT_UAST_3PM_RANK",
            "PCT_AST_FGM_RANK",
            "PCT_UAST_FGM_RANK",
            "CFID",
            "CFPARAMS",
        ],
    }

    nba_response = None
    data_sets = None
    player_stats = None
    team_stats = None
    headers = None

    def __init__(
        self,
        team_id,
        last_n_games=LastNGames.default,
        measure_type_detailed_defense=MeasureTypeDetailedDefense.default,
        month=Month.default,
        opponent_team_id=0,
        pace_adjust=PaceAdjust.default,
        per_mode_detailed=PerModeDetailed.default,
        period=Period.default,
        plus_minus=PlusMinus.default,
        rank=Rank.default,
        season=Season.default,
        season_type_all_star=SeasonTypeAllStar.default,
        date_from_nullable="",
        date_to_nullable="",
        game_segment_nullable=GameSegmentNullable.default,
        league_id_nullable=LeagueIDNullable.default,
        location_nullable=LocationNullable.default,
        outcome_nullable=OutcomeNullable.default,
        po_round_nullable="",
        season_segment_nullable=SeasonSegmentNullable.default,
        shot_clock_range_nullable=ShotClockRangeNullable.default,
        vs_conference_nullable=ConferenceNullable.default,
        vs_division_nullable=DivisionNullable.default,
        proxy=None,
        headers=None,
        timeout=30,
        get_request=True,
    ):
        self.proxy = proxy
        if headers is not None:
            self.headers = headers
        self.timeout = timeout
        self.parameters = {
            "TeamID": team_id,
            "LastNGames": last_n_games,
            "MeasureType": measure_type_detailed_defense,
            "Month": month,
            "OpponentTeamID": opponent_team_id,
            "PaceAdjust": pace_adjust,
            "PerMode": per_mode_detailed,
            "Period": period,
            "PlusMinus": plus_minus,
            "Rank": rank,
            "Season": season,
            "SeasonType": season_type_all_star,
            "DateFrom": date_from_nullable,
            "DateTo": date_to_nullable,
            "GameSegment": game_segment_nullable,
            "LeagueID": league_id_nullable,
            "Location": location_nullable,
            "Outcome": outcome_nullable,
            "PORound": po_round_nullable,
            "SeasonSegment": season_segment_nullable,
            "ShotClockRange": shot_clock_range_nullable,
            "VsConference": vs_conference_nullable,
            "VsDivision": vs_division_nullable,
        }
        if get_request:
            self.get_request()

    def get_request(self):
        self.nba_response = NBAStatsHTTP().send_api_request(
            endpoint=self.endpoint,
            parameters=self.parameters,
            proxy=self.proxy,
            headers=self.headers,
            timeout=self.timeout,
        )
        self.load_response()

    def load_response(self):
        data_sets = self.nba_response.get_data_sets()
        self.data_sets = [
            Endpoint.DataSet(data=data_set)
            for data_set_name, data_set in data_sets.items()
        ]
        self.assisted_by = Endpoint.DataSet(data=data_sets["AssistedBy"])
        self.assited_shot_team_dashboard = Endpoint.DataSet(
            data=data_sets["AssitedShotTeamDashboard"]
        )
        self.overall_team_dashboard = Endpoint.DataSet(
            data=data_sets["OverallTeamDashboard"]
        )
        self.shot5_ft_team_dashboard = Endpoint.DataSet(
            data=data_sets["Shot5FTTeamDashboard"]
        )
        self.shot8_ft_team_dashboard = Endpoint.DataSet(
            data=data_sets["Shot8FTTeamDashboard"]
        )
        self.shot_area_team_dashboard = Endpoint.DataSet(
            data=data_sets["ShotAreaTeamDashboard"]
        )
        self.shot_type_team_dashboard = Endpoint.DataSet(
            data=data_sets["ShotTypeTeamDashboard"]
        )

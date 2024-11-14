import pandas as pd

# Creating a sample DataFrame with the provided data for analysis
data = [
    ("Atlanta Hawks", 0.554, 0.384),
    ("Boston Celtics", 0.661, 0.589),
    ("Brooklyn Nets", 0.500, 0.429),
    ("Charlotte Hornets", 0.500, 0.348),
    ("Chicago Bulls", 0.39, 0.317),
    ("Cleveland Cavaliers", 0.707, 0.707),
    ("Dallas Mavericks", 0.707, 0.707),
    ("Denver Nuggets", 0.293, 0.195),
    ("Detroit Pistons", 0.585, 0.512),
    ("Golden State Warriors", 0.707, 0.707),
    ("Houston Rockets", 0.707, 0.707),
    ("Indiana Pacers", 0.78, 0.78),
    ("Los Angeles Clippers", 0.707, 0.707),
    ("Los Angeles Lakers", 0.439, 0.439),
    ("Memphis Grizzlies", 0.293, 0.195),
    ("Miami Heat", 0.585, 0.512),
    ("Milwaukee Bucks", 0.585, 0.512),
    ("Minnesota Timberwolves", 0.707, 0.439),
    ("New Orleans Pelicans", 0.585, 0.585),
    ("New York Knicks", 0.512, 0.195),
    ("Oklahoma City Thunder", 0.707, 0.512),
    ("Orlando Magic", 0.317, 0.244),
    ("Philadelphia 76ers", 0.707, 0.585),
    ("Phoenix Suns", 0.195, 0.244),
    ("Portland Trail Blazers", 0.707, 0.512),
    ("Sacramento Kings", 0.446, 0.348),
    ("San Antonio Spurs", 0.607, 0.500),
    ("Toronto Raptors", 0.661, 0.554),
    ("Utah Jazz", 0.607, 0.500),
    ("Washington Wizards", 0.500, 0.384),
]

# Creating the DataFrame
df = pd.DataFrame(
    data, columns=["Team Name", "Home Win Percentage", "Road Win Percentage"]
)

# Calculating average home and road win percentages by team
average_df = df.groupby("Team Name", as_index=False).mean()

import ace_tools as tools

tools.display_dataframe_to_user(
    name="Average Home and Road Win Percentages", dataframe=average_df
)

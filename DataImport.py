import pandas as pd

wr_dataframe = pd.read_csv(r'/Users/dansullivan/NFL_DATA/WR_TOTALS_2019_CSV.csv')

player_name = wr_dataframe.get('Player')

new_player_name = []

for name in player_name:
    if '*' in name:
        new_name = name.split('*', 1)[0]
    elif '\\' in name:
        new_name = name.split('\\',1)[0]
    # print(new_name)
    new_player_name.append(new_name)

wr_dataframe['Player'] = new_player_name

wr_dataframe.to_csv(r'/Users/dansullivan/NFL_DATA/WR_TOTALS_2019_CSV.csv')

print(new_player_name)

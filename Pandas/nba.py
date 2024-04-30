import pandas as pd
import numpy as np

df = pd.read_csv("all_seasons.csv")

result = df

result = df.head(10) # ilk 10

result = len(df.index) # toplam index sayısı

result = df["age"].mean() # Yaş ortalaması

result = df["age"].max() # En büyük yaş

result = df[df["age"]==df["age"].max()]["player_name"].iloc[0] # En yaşlı oyuncunun adı

# result = df[(df["age"]>=20)&(df["age"]<25)][["player_name","team_abbreviationteam_abbreviation"]].sort_values("age",ascending=False) # bune aq

result = df[df["player_name"] == "Glen Rice"]["team_abbreviationteam_abbreviation"].iloc[0]

result = df.groupby("team_abbreviationteam_abbreviation").mean()

# Bu videoyu bida izle aq ya

print(result)
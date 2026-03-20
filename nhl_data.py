from nhlpy import NHLClient
import pandas as pd
import pprint
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
#Simple
client = NHLClient()


stats = client.stats.skater_stats_summary(
    start_season='20242025',
    end_season='20242025',
    limit=50
)


players = []

for player in stats:
    players.append({
        'name': player['skaterFullName'],
        'points': player['points'],
        'ppg': player['pointsPerGame'],
        'games': player['gamesPlayed'],
        'avgToi': player['timeOnIcePerGame'],
        'shootingPct': player['shootingPct'],
        'shots': player["shots"],
        'ppPoints': player["ppPoints"],
        'evPoints': player['evPoints'],
        'team': player['teamAbbrevs']
}) 

qualified = [player for player in players if player['games']>=60]    

points_rank=sorted(qualified, key=lambda x:x['points'], reverse=True)
# ppg_rank=sorted(qualified, key=lambda x:x['ppg'], reverse=True)
# avgToi_rank = sorted(qualified, key=lambda x:x['avgToi'], reverse=True)
# shootingPct_rank = sorted(qualified, key=lambda x:x['shootingPct'], reverse=True)
# shots_rank = sorted(qualified, key=lambda x:x['shots'], reverse=True) 
# ppPoints_rank=sorted(qualified, key = lambda x:x['ppPoints'], reverse = True)  

# ranks = [points_rank, ppg_rank, avgToi_rank, shootingPct_rank, shots_rank, ppPoints_rank]
df = pd.DataFrame(points_rank)
# print(df)

corr = df[['points', 'avgToi', 'shootingPct', 'shots', 'ppPoints']].corr()
sort1=corr['points'].sort_values(ascending=False)

#Advanced
#For original csv file
# max_speed=[]
# burst1820= []
# burst2022= []
# burst22 = []
# maxdistancegame = []
# maxdistance60 = []
# avgshotspeed=[]
# shotAttempts70To80=[]
# shotAttempts80To90 = []
# shotAttempts90To100 = []
# shotAttemptsOver100 = []
# maxShotspeed= []
# allshotnumber=[]
# high_danger=[]
# mid_range=[]
# long_range=[]
# dzonestarts = []
# nzonestarts = []
# ozonestarts= []
# dzonepctg = []
# nzonepctg = []
# ozonepctg = []


# for player in stats:
#     speed = client.edge.skater_skating_speed_detail(
#         player_id = player['playerId'], 
#         season=20242025,
#         game_type=2
#         )
#     details = speed['skatingSpeedDetails']
  
#     max_speed.append(details['maxSkatingSpeed']['imperial'])
   
#     burst1820.append(details['bursts18To20']['value'])
  
#     burst2022.append(details['bursts20To22']['value'])
    
#     burst22.append(details['burstsOver22']['value'])
    
#     distance = client.edge.skater_skating_distance_detail(
#         player_id=player['playerId'],
#         season=20242025,
#         game_type=2
#     )
#     maxdistancegame.append(distance['skatingDistanceDetails'][0]['distanceMaxGame']['imperial'])
#     maxdistance60.append(distance['skatingDistanceDetails'][0]['distancePer60']['imperial'])

#     shotspeed = client.edge.skater_shot_speed_detail(
#         player_id=player['playerId'],
#         season=20242025,
#         game_type=2
#     )
#     shotdetails= shotspeed['shotSpeedDetails']
#     avgshotspeed.append(shotdetails['avgShotSpeed']['imperial'])
#     shotAttempts70To80.append(shotdetails['shotAttempts70To80']['value'])
#     shotAttempts80To90.append(shotdetails['shotAttempts80To90']['value'])
#     shotAttempts90To100.append(shotdetails['shotAttempts90To100']['value'])
#     shotAttemptsOver100.append(shotdetails['shotAttemptsOver100']['value'])
#     maxShotspeed.append(shotdetails['topShotSpeed']['imperial'])


#     shotlocation = client.edge.skater_shot_location_detail(
#      player_id=player['playerId'],
#     season=20242025,
#     game_type=2
#     )
#     shotlocdetails = shotlocation['shotLocationTotals']
#     # soglocs = [shotlocdetails[n]['locationCode'] for n in range (4)]
#     # sognumbers = [shotlocdetails[n]['sog'] for n in range (4)]
#     # shotloc = dict(zip(soglocs, sognumbers))
#     allshotnumber.append(shotlocdetails[0]['sog'])
#     high_danger.append(shotlocdetails[1]['sog'])
#     long_range.append(shotlocdetails[2]['sog'])
#     mid_range.append(shotlocdetails[3]['sog'])
    
#     zonetime = client.edge.skater_zone_time(
#         player_id=player['playerId'],
#         season=20242025,
#         game_type=2
#     )
#     starts = zonetime['zoneStarts']
#     dzonestarts.append(starts['defensiveZoneStartsPctg'])
#     nzonestarts.append(starts['neutralZoneStartsPctg'])
#     ozonestarts.append(starts['offensiveZoneStartsPctg'])

#     timedetails = zonetime['zoneTimeDetails'][0]
#     dzonepctg.append(timedetails['defensiveZonePctg'])
#     nzonepctg.append(timedetails['neutralZonePctg'])
#     ozonepctg.append(timedetails['offensiveZonePctg'])

# advanced_data = {
#     'name':[player['skaterFullName'] for player in stats],
#     'points':[player['points'] for player in stats],
#     'max_speed':max_speed,
#     'burst1820':burst1820,
#     'burst2022':burst2022,
#     'burst22':burst22,
#     'maxdistancegame':maxdistancegame,
#     'maxdistance60':maxdistance60,
#     'avgshotspeed':avgshotspeed,
#     'shotAttempts70To80':shotAttempts70To80,
#     'shotAttempts80To90' : shotAttempts80To90,
#     'shotAttempts90To100' : shotAttempts90To100,
#     'shotAttemptsOver100' : shotAttemptsOver100,
#     'maxShotspeed': maxShotspeed,
#     'allshotnumber':allshotnumber,
#     'high_danger':high_danger,
#     'mid_range':mid_range,
#     'long_range':long_range,
#     'dzonestarts' : dzonestarts,
#     'nzonestarts' : nzonestarts,
#     'ozonestarts': ozonestarts,
#     'dzonepctg' : dzonepctg,
#     'nzonepctg' : nzonepctg,
#     'ozonepctg' : ozonepctg
# }

# df1 = pd.DataFrame(advanced_data)
# print(df1)

# df1.to_csv('data.csv', index=False)

filepath = r'C:\Users\etxux\data.csv'
df1 = pd.read_csv(filepath)
corr1 = df1[['points','max_speed', 'burst1820', 'burst2022', 'burst22', 'maxdistancegame', 'maxdistance60', 'avgshotspeed', 'shotAttempts70To80', 'shotAttempts80To90', 'shotAttempts90To100', 'shotAttemptsOver100', 'maxShotspeed','high_danger','mid_range','long_range','dzonestarts', 'nzonestarts','ozonestarts','dzonepctg','nzonepctg','ozonepctg']].corr()
sort2 = corr1['points'].sort_values(ascending=False)

#Conclusions and graphs of conclusions

#Bar Graphs of most useful stats
combined = pd.concat([sort1, sort2])
combined = combined[~combined.index.duplicated()]
sorted_comb = combined.reindex(combined.abs().sort_values(ascending=False).index)
print(sorted_comb)
top= sorted_comb.iloc[1:11]
categories = top.index
values = top.values

plt.barh(categories, values, color = 'skyblue')

plt.title('Top NHL Performance Metrics Correlated with Point Production')
plt.ylabel('Top Ten Stats')
plt.xticks(rotation = 45)
plt.xlabel('Correlation(R)')

# Scatter Plots

y = df1['points'].values
x1 = df1['burst22'].values
x2 = df1['maxShotspeed'].values
m, b = np.polyfit(x1, y, 1)
m2, b2 = np.polyfit(x2, y, 1)

y_pred1 = m*x1+b
r21=r2_score(y, y_pred1)
print(f"R^2 correlations for bursts over 22mph: {r21}")

y_pred2 = m2*x2+b2
r22=r2_score(y, y_pred2)
print(f"R^2 correlations for max shot speed: {r22}")

figure, axes = plt.subplots(1, 2)

order1 = np.argsort(x1)
order2 = np.argsort(x2)
axes[0].scatter(x1, y, color='skyblue')
axes[0].set_xlabel('Bursts over 22 mph')
axes[0].plot(x1[order1], y_pred1[order1], color='black', label='Best Fit Line')
axes[0].set_ylabel('Points in 2024-2025 Season')
axes[0].set_title('Points vs Speed Bursts')
axes[0].legend()

axes[1].scatter(x2, y, color='red')
axes[1].plot(x2[order2], y_pred2[order2], color='black', label='Best Fit Line')
axes[1].set_xlabel('Max Shot Speed')
axes[1].set_ylabel('Points in 2024-2025 Season')
axes[1].set_title('Points vs Max Shot Speed')
axes[1].legend()


plt.tight_layout()
plt.show()






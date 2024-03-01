
def get_players_for_topic(preferences):
  players_per_topic = {}
  player = 0
  for player_topics in preferences:
    for topic in player_topics:
      if topic in players_per_topic:
        players_per_topic[topic].append(player)
      else:
        players_per_topic[topic] = [player]
    player+=1
  return players_per_topic

def find_decomposition(budget: list[float], preferences: list[set[int]]):
  players_per_topic = get_players_for_topic(preferences)
  player_budget = sum(budget) / len(preferences)
  players_money = [player_budget for _ in range(len(preferences))]
  ans = []
  for i in range(len(budget)):
    if budget[i] > len(players_per_topic[i])*player_budget:
      print('no decompostition')
      return []
    if budget[i] == len(players_per_topic[i])*player_budget:
      for player in players_per_topic[i]:
        players_money[player] -= player_budget
        ans.append(f"player {player} gave {player_budget} to item {i}")
    else:
      for player in players_per_topic[i]:
        if(players_money[player] > 0):  
          players_money[player] -= player_budget - budget[i]
          ans.append(f"player {player} gave {player_budget - budget[i]} to item {i}")
  for balance in players_money:
    if balance != 0:
      print('no decomposition')
      return []
  return ans

budget = [400, 50, 50, 0]
preferences = [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}]
#Expected  - 
# player 0 gave 100.0 to item 0
# player 1 gave 100.0 to item 0
# player 2 gave 100.0 to item 0
# player 4 gave 100.0 to item 0
# player 3 gave 50.0 to item 1
# player 3 gave 50.0 to item 2
ans = find_decomposition(budget, preferences)
for purchase in ans:
  print(purchase)
#Expected - 
# no decomposition
budget = [0, 300]
preferences = [{0}, {1}, {1}]
ans = find_decomposition(budget, preferences)
for purchase in ans:
  print(purchase)
#Expected - 
# player 0 gave 100.0 to item 0
# player 1 gave 100.0 to item 1
# player 2 gave 100.0 to item 1
budget = [100, 200]
preferences = [{0}, {1}, {1}]
ans = find_decomposition(budget, preferences)
for purchase in ans:
  print(purchase)
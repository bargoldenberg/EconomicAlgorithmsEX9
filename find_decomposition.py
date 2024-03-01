#IMPLEMENTED BY: BAR GOLDENBERG
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
  print(players_per_topic) 
  player_budget = sum(budget) / len(preferences)
  print(player_budget)
  players_money = [player_budget for _ in range(len(preferences))]
  ans = []
  for i in range(len(budget)):
    if budget[i] > len(players_per_topic[i])*player_budget:
      print('no decompostition')
      return []
    for player in players_per_topic[i]:
        if players_money[player] <= 0:
          continue
        if budget[i] == players_money[player]:
          players_money[player] = 0
          ans.append(f"player {player} gave {budget[i]} to item {i}")
          continue
        amount_to_give = player_budget if budget[i] == len(players_per_topic[i])*player_budget else (player_budget - budget[i])
        players_money[player] -= amount_to_give
        ans.append(f"player {player} gave {amount_to_give} to item {i}")
  return ans

budget = [400, 50, 50, 0]
preferences = [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}]
ans = find_decomposition(budget, preferences)
#Expected  - 
# player 0 gave 100.0 to item 0
# player 1 gave 100.0 to item 0
# player 2 gave 100.0 to item 0
# player 4 gave 100.0 to item 0
# player 3 gave 50.0 to item 1
# player 3 gave 50.0 to item 2
for purchase in ans:
  print(purchase)
budget = [0, 300]
preferences = [{0}, {1}, {1}]
ans = find_decomposition(budget, preferences)
#Expected - 
# no decomposition
for purchase in ans:
  print(purchase)
budget = [100, 200]
preferences = [{0}, {1}, {1}]
ans = find_decomposition(budget, preferences)
#Expected - 
# player 0 gave 100.0 to item 0
# player 1 gave 100.0 to item 1
# player 2 gave 100.0 to item 1
for purchase in ans:
  print(purchase)

budget = [150, 150]
preferences = [{0, 1}, {0, 1}]
ans = find_decomposition(budget, preferences)
#Expected - 
# player 0 gave 150 to item 0
# player 1 gave 150 to item 0
for purchase in ans:
  print(purchase)
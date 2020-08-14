import urllib.request, json

with urllib.request.urlopen("http://nptriton.cqproject.net/game/4845520221372416/full") as url:
    data = json.loads(url.read().decode())

# print("Weapons Level: ", data["players"]["0"])
# print(type(data))

print("Alias", "Systems", "Ships", "Carriers", "Upgrades")

upgrades = ["scanning", "propulsion", "terraforming", "research", "weapons", "banking", "manufacturing"]

for player in range(len(data["players"])):
    player = str(player)
    upgrade_array = []
    for upgrade in upgrades:
        upgrade_array.append(data["players"][player]["tech"][upgrade]["level"])
    print(data["players"][player]["alias"],
    data["players"][player]["total_stars"],
    data["players"][player]["total_strength"],
    data["players"][player]["total_fleets"],
    upgrade_array)

# num = 0
# numS = str(num)

# print(data["players"][numS]["tech"]["weapons"])
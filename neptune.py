import urllib.request, json

with urllib.request.urlopen("http://nptriton.cqproject.net/game/4845520221372416/full") as url:
    data = json.loads(url.read().decode())

# print("Weapons Level: ", data["players"]["0"])
# print(type(data))

print("Alias", "Systems", "Ships", "Carriers")

upgrades = ["scanning", "propulsion", "terraforming", "research", "weapons", "banking", "manufacturing"]

for player in range(len(data["players"])):
    player = str(player)
    print(data["players"][player]["alias"],
    data["players"][player]["total_stars"],
    data["players"][player]["total_strength"],
    data["players"][player]["total_fleets"])
    for upgrade in upgrades:
        print(upgrade, data["players"][player]["tech"][upgrade]["level"])

# num = 0
# numS = str(num)

# print(data["players"][numS]["tech"]["weapons"])
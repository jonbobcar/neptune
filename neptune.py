import urllib.request, json, csv, datetime, pathlib

path = str(pathlib.Path(__file__).parent.absolute())

print(path)

with open(path + "\game_number.txt", "r") as f:
    game_number = f.read()

# game_number = 4845520221372416
url = "http://nptriton.cqproject.net/game/" + str(game_number) + "/full"

with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

class Player():
    def __init__(self, uid):
        uid = str(uid)
        self.alias = data["players"][uid]["alias"]
        self.systems = data["players"][uid]["total_stars"]
        self.ships = data["players"][uid]["total_strength"]
        self.carriers = data["players"][uid]["total_fleets"]
        self.scanning = data["players"][uid]["tech"]["scanning"]["level"]
        self.range = data["players"][uid]["tech"]["propulsion"]["level"]
        self.terraforming = data["players"][uid]["tech"]["terraforming"]["level"]
        self.research = data["players"][uid]["tech"]["research"]["level"]
        self.weapons = data["players"][uid]["tech"]["weapons"]["level"]
        self.banking = data["players"][uid]["tech"]["banking"]["level"]
        self.manufacturing = data["players"][uid]["tech"]["manufacturing"]["level"]

fieldnames = [
    "alias",
    "total_stars",
    "total_strength",
    "total_fleets",
    "scanning",
    "propulsion",
    "terraforming",
    "research",
    "weapons",
    "banking",
    "manufacturing"
]

file_name = path + "\\neptune.csv"

with open(file_name, "w") as write_file:
    csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
    csv_writer.writeheader()

write_line = []

for player in range(len(data["players"])):
    player = str(player)
    write_line.append({
        "alias":            data["players"][player]["alias"],
        "total_stars":      data["players"][player]["total_stars"],
        "total_strength":   data["players"][player]["total_strength"],
        "total_fleets":     data["players"][player]["total_fleets"],
        "scanning":         data["players"][player]["tech"]["scanning"]["level"],
        "propulsion":       data["players"][player]["tech"]["propulsion"]["level"],
        "terraforming":     data["players"][player]["tech"]["terraforming"]["level"],
        "research":         data["players"][player]["tech"]["research"]["level"],
        "weapons":          data["players"][player]["tech"]["weapons"]["level"],
        "banking":          data["players"][player]["tech"]["banking"]["level"],
        "manufacturing":    data["players"][player]["tech"]["manufacturing"]["level"],
    })

with open(file_name, "a") as write_file:
    csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
    for row in write_line:
        csv_writer.writerow(row)

with open(file_name, "r") as file:
    table = file.read()

with open(file_name, "w") as file:
    file.write(datetime.datetime.now().strftime("%A %H:%M\n"))
    file.write(table)

players = []

for player in range(len(data["players"])):
    players.append(data["players"][str(player)])

historical = path + "\historical.txt"

with open(historical, "a") as file:
    file.write(str(players))
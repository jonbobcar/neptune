# url = "http://nptriton.cqproject.net/game/4845520221372416/full"

import urllib.request, json, csv, datetime, pathlib, os

path = str(pathlib.Path(__file__).parent.absolute()) + "/"

with open(path + "game_number.txt", "r") as f:
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
        self.total_economy = data["players"][player]["total_economy"]
        self.total_industry = data["players"][player]["total_industry"]
        self.total_science = data["players"][player]["total_science"]
        self.scanning = data["players"][uid]["tech"]["scanning"]["level"]
        self.range = data["players"][uid]["tech"]["propulsion"]["level"]
        self.terraforming = data["players"][uid]["tech"]["terraforming"]["level"]
        self.research = data["players"][uid]["tech"]["research"]["level"]
        self.weapons = data["players"][uid]["tech"]["weapons"]["level"]
        self.banking = data["players"][uid]["tech"]["banking"]["level"]
        self.manufacturing = data["players"][uid]["tech"]["manufacturing"]["level"]

class Board():
    def __init__(self):
        self.stars = data["stars"]
        self.tick = datetime.datetime.now().strftime("%Y%m%d %H")

stars_file = path + "stars.txt"
file_exists = os.path.isfile(stars_file)

now_board = Board()

if file_exists:
    with open(path + "stars.txt", "r") as file:
        past_board = json.loads(file.read())

    for star in past_board:
        if past_board[str(star)]["puid"] is not now_board.stars[str(star)]["puid"]:
            if past_board[str(star)]["puid"] == -1:
                with open(path + "trades.txt", "a") as file:
                    change = str(
                        datetime.datetime.now().strftime("%Y/%m/%d %H:") + "53" + " - " +
                        past_board[str(star)]["n"] + " - " +
                        "Unclaimed System" +
                        " -> " +
                        data["players"][str(now_board.stars[str(star)]["puid"])]["alias"] +  " (+1; " +
                        str(data["players"][str(now_board.stars[str(star)]["puid"])]["total_stars"]) + ")" +
                        "\n"
                        )
                    file.write(change)
            elif now_board.stars[str(star)]["puid"] == -1:
                with open(path + "trades.txt", "a") as file:
                    change = str(
                        datetime.datetime.now().strftime("%Y/%m/%d %H:") + "53" + " - " +
                        past_board[str(star)]["n"] + " - " +
                        data["players"][str(past_board[str(star)]["puid"])]["alias"] + " (-1; " +
                        str(data["players"][str(past_board[str(star)]["puid"])]["total_stars"]) + ")" +
                        " -> " +
                        "System Abandoned" +
                        "\n"
                        )
                    file.write(change)    
            else:
                with open(path + "trades.txt", "a") as file:
                    change = str(
                        datetime.datetime.now().strftime("%Y/%m/%d %H:") + "53" + " - " +
                        past_board[str(star)]["n"] + " - " +
                        data["players"][str(past_board[str(star)]["puid"])]["alias"] + " (-1; " +
                        str(data["players"][str(past_board[str(star)]["puid"])]["total_stars"]) + ")" +
                        " -> " +
                        data["players"][str(now_board.stars[str(star)]["puid"])]["alias"] +  " (+1; " +
                        str(data["players"][str(now_board.stars[str(star)]["puid"])]["total_stars"]) + ")" +
                        "\n"
                        )
                    file.write(change)    
            print(change)

with open(path + "stars.txt", "w") as file:
    file.write(json.dumps(now_board.stars))


fieldnames = [
    "alias",
    "total_stars",
    "total_strength",
    "total_fleets",
    "total_economy",
    "total_industry",
    "total_science",
    "scanning",
    "propulsion",
    "terraforming",
    "research",
    "weapons",
    "banking",
    "manufacturing"
]

file_name = path + "neptune.csv"

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
        "total_economy":    data["players"][player]["total_economy"],
        "total_industry":   data["players"][player]["total_industry"],
        "total_science":    data["players"][player]["total_science"],
        "scanning":         data["players"][player]["tech"]["scanning"]["level"],
        "propulsion":       data["players"][player]["tech"]["propulsion"]["level"],
        "terraforming":     data["players"][player]["tech"]["terraforming"]["level"],
        "research":         data["players"][player]["tech"]["research"]["level"],
        "weapons":          data["players"][player]["tech"]["weapons"]["level"],
        "banking":          data["players"][player]["tech"]["banking"]["level"],
        "manufacturing":    data["players"][player]["tech"]["manufacturing"]["level"],
    })

player_line = ["tick"]
stats = ["total_stars", "total_strength", "total_economy", "total_industry", "total_science"]
stat_line = {"tick": datetime.datetime.now()}

for player in range(len(data["players"])):
    for stat in stats:
        stat_line.update({data["players"][str(player)]["alias"] + ": " + stat: data["players"][str(player)][stat]})
        player_line.append(data["players"][str(player)]["alias"] + ": " + stat)

file_exists = os.path.isfile(path + "stats.csv")

if not file_exists:
    with open(path + "stats.csv", "w") as write_file:
        csv_writer = csv.DictWriter(write_file, fieldnames=player_line)
        csv_writer.writeheader()
        csv_writer.writerow(stat_line)

else:
    with open(path + "stats.csv", "a") as write_file:
        csv_writer = csv.DictWriter(write_file, fieldnames=player_line)
        csv_writer.writerow(stat_line)

with open(file_name, "a") as write_file:
    csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
    for row in write_line:
        csv_writer.writerow(row)

with open(file_name, "r") as file:
    table = file.read()

with open(file_name, "w") as file:
    file.write(datetime.datetime.now().strftime("%A %H:%M\n"))
    file.write(table)

players = {datetime.datetime.now().strftime("%Y%m%d %H"):
            data["players"]}

historical = path + "historical.txt"

file_exists = os.path.isfile(historical)

if file_exists:
    with open(historical, "r") as file:
        players_history = json.loads(file.read())
        players.update(players_history)

with open(historical, "w") as file:
    file.write(json.dumps(players, indent=2))
    
print("neptune.py")
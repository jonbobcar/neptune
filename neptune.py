# url = "http://nptriton.cqproject.net/game/4845520221372416/full"

import urllib.request 
import json 
import shutil
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
import pathlib
import csv
import datetime
from cycler import cycler
from matplotlib.ticker import MaxNLocator

def nep_monitor():
    change = False
    print(change)

    path = str(pathlib.Path(__file__).parent.absolute()) + "/"

    with open(path + "game_number.txt", "r") as f:
        game_number = f.read()

    # game_number = 4845520221372416
    url = "http://nptriton.cqproject.net/game/" + str(game_number) + "/full"

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    if os.path.isfile(path + "tick.txt"):
        with open(path + "tick.txt", "r") as f:
            tick = f.read(data["tick"])
            tick = int(tick)
            print(tick)
            print(int(data["tick"]))
        if tick != (int(data["tick"])):
            change = True
    else:
        change = True
        with open(path + "tick.txt", "w") as f:
            f.write(str(data["tick"]))

    return change

def nep_get():
    path = str(pathlib.Path(__file__).parent.absolute()) + "/"

    with open(path + "game_number.txt", "r") as f:
        game_number = f.read()

    # game_number = 4845520221372416
    url = "http://nptriton.cqproject.net/game/" + str(game_number) + "/full"

    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())

    with open(path + "tick.txt", "w") as f:
        f.write(str(data["tick"]))

## Check old board vs new board for system changes

    class Board():
        def __init__(self):
            self.stars = data["stars"]
            self.tick = datetime.datetime.now().strftime("%Y%m%d %H")

    now_board = Board()

    stars_file = path + "stars.txt"
    file_exists = os.path.isfile(stars_file)

    if file_exists:
        with open(path + "stars.txt", "r") as file:
            past_board = json.loads(file.read())

        for star in past_board:
            if past_board[str(star)]["puid"] is not now_board.stars[str(star)]["puid"]:
                if past_board[str(star)]["puid"] == -1:
                    with open(path + "trades.txt", "a") as file:
                        change = str(
                            datetime.datetime.now().strftime("%Y/%m/%d %H:%M")  + " - " +
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
                            datetime.datetime.now().strftime("%Y/%m/%d %H:%M") + " - " +
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
                            datetime.datetime.now().strftime("%Y/%m/%d %H:%M") + " - " +
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

## Record individual player stats to neptune.csv

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

    with open(path + "neptune.csv", "w") as write_file:
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
    


    with open(path + "neptune.csv", "a") as write_file:
        csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        for row in write_line:
            csv_writer.writerow(row)

    with open(path + "neptune.csv", "r") as file:
        table = file.read()

    with open(path + "neptune.csv", "w") as file:
        file.write(datetime.datetime.now().strftime("%A %H:%M\n"))
        file.write(table)

## Prepare individual galaxy stats and write to stats.csv

    player_line = ["tick"]
    stats = ["total_stars", "total_strength", "total_economy", "total_industry", "total_science"]
    stat_line = {"tick": datetime.datetime.now()}

    for player in range(len(data["players"])):
        for stat in stats:
            stat_line.update({str(player) + ": " + data["players"][str(player)]["alias"] + ": " + stat: data["players"][str(player)][stat]})
            player_line.append(str(player) + ": " + data["players"][str(player)]["alias"] + ": " + stat)

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

## Prepare individual research stats and write to research.csv

    player_line = ["tick"]
    stats = ["scanning", "propulsion", "terraforming", "research", "weapons", "banking", "manufacturing"]
    stat_line = {"tick": datetime.datetime.now()}

    for player in range(len(data["players"])):
        for stat in stats:
            stat_line.update({data["players"][str(player)]["alias"] + ": " + stat: data["players"][str(player)]["tech"][stat]["level"]})
            player_line.append(data["players"][str(player)]["alias"] + ": " + stat)

    file_exists = os.path.isfile(path + "research.csv")

    if not file_exists:
        with open(path + "research.csv", "w") as write_file:
            csv_writer = csv.DictWriter(write_file, fieldnames=player_line)
            csv_writer.writeheader()
            csv_writer.writerow(stat_line)

    else:
        with open(path + "research.csv", "a") as write_file:
            csv_writer = csv.DictWriter(write_file, fieldnames=player_line)
            csv_writer.writerow(stat_line)
        
    print("neptune.py")
    
def nep_plot():
    path = str(pathlib.Path(__file__).parent.absolute()) + "/"

    file_exists = os.path.isfile(path + "stats.csv")

    if file_exists:
        with open(path + "stats.csv", "r") as f:
            csv_reader = csv.DictReader(f)
            csv_stats = list(csv_reader)
            fieldnames = csv_reader.fieldnames

    csv_line = []
    i = 0
    number_of_players = int((len(fieldnames) - 1) / 5)

    for line in csv_stats:
        i += 1
        for field in fieldnames:
            csv_line.append(line[field])

    csv_array = np.reshape(csv_line, (i, int(len(fieldnames))))

    back_ticks = -24

    t = csv_array[back_ticks:,0]
    time = []

    for entry in t:
        time.append(datetime.datetime.strptime(entry, "%Y-%m-%d %H:%M:%S.%f").strftime("%A %H:%M:%S"))

    print(time[-1])

    csv_array = csv_array[...,1:]
    csv_array = csv_array.astype(np.int)
    stars = csv_array[back_ticks:, 0::5]
    ships = csv_array[back_ticks:, 1::5]
    economy = csv_array[back_ticks:,2::5]
    industry = csv_array[back_ticks:,3::5]
    science = csv_array[back_ticks:,4::5]

    plots = ["stars", "ships", "economy", "industry", "science"]
    colors = [
        "blue", "cyan", "lime", "gold", 
        "orange", "red", "fuchsia", "purple",
        "blue", "cyan", "lime", "gold", 
        "orange", "red", "fuchsia", "purple"
        ]
    lines = [
        (0, (3, 5)), (0, (4, 5)), (0, (5, 5)), (0, (6, 5)),
        (0, (5, 3)), (0, (5, 4)), (0, (5, 5)), (0, (5, 6)),
        (0, (3, 5)), (0, (4, 5)), (0, (5, 5)), (0, (6, 5)),
        (0, (5, 3)), (0, (5, 4)), (0, (5, 5)), (0, (5, 6))
        ]
    markers = []
    for group in range(4):
        for sub_group in range(8):
            if group == 0:
                markers.append("o")
            elif group == 1:
                markers.append("s")
            elif group == 2:
                markers.append("^")
            else:
                markers.append("h")

    t_label = fieldnames[0]

    for plot in range(len(plots)):
        plt.rc('lines', linewidth=3)
        plt.rc('axes', prop_cycle=(cycler('color', colors[0:number_of_players]) +
                            cycler('linestyle', lines[0:number_of_players]) +
                            cycler('marker', markers[0:number_of_players])))
        fig, ax = plt.subplots(figsize=(9,6))

        ax.plot(time, csv_array[back_ticks:, plot::5])

        fig.autofmt_xdate(rotation=60)
        

        ax.set(title=plots[plot])
        ax.grid()
        ax.yaxis.set_label_position("right")
        ax.yaxis.tick_right()
        plt.tight_layout()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))


        fig.savefig(plots[plot] + ".png")

    print("stats_plotter.py")

def nep_html():
    
    path = str(pathlib.Path(__file__).parent.absolute()) + "/"

    if os.path.isfile(path + "trades.txt"):
        with open(path + "trades.txt", "r") as f:
            trades = f.readlines()

    with open(path + "neptune.csv", "r") as f:
        positions = f.readlines()

    positions[1] = 'alias, stars, ships, carriers, econ, ind, sci, scan, range, terra, research, weap, bank, manuf'

    with open(path + "index.html", "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<body>\n")
        f.write("<h1>\n")
        f.write("positions")
        f.write("</h1>\n")
        for line in positions:
            f.write("<p>" + line + "</p>")
        
        f.write("<p1>\n")
        f.write("<img src=\"stars.png\" alt=\"Stars\">\n")
        f.write("<img src=\"ships.png\" alt=\"Stars\">\n")
        f.write("<img src=\"economy.png\" alt=\"Stars\">\n")
        f.write("<img src=\"industry.png\" alt=\"Stars\">\n")
        f.write("<img src=\"science.png\" alt=\"Stars\">\n")
        f.write("</p1>\n")
        
        f.write("<h1>\n")
        f.write("system trades\n")
        f.write("</h1>\n")
        
        f.write("<p1>\n")
        f.write("most recent first")
        if os.path.isfile(path + "trades.txt"):       
            for line in reversed(trades):
                f.write("<p>" + line + "</p>")
        f.write("</p1>\n")
        f.write("</body>\n")
        f.write("</html>\n")

        print("neptune_to_html.py")

def nep_copy():
    shutil.copy("/home/jonathon/neptune/index.html", "/var/www/html/jonbobcar.com/public_html/index.html")
    shutil.copy("/home/jonathon/neptune/stars.png", "/var/www/html/jonbobcar.com/public_html/stars.png")
    shutil.copy("/home/jonathon/neptune/ships.png", "/var/www/html/jonbobcar.com/public_html/ships.png")
    shutil.copy("/home/jonathon/neptune/economy.png", "/var/www/html/jonbobcar.com/public_html/economy.png")
    shutil.copy("/home/jonathon/neptune/industry.png", "/var/www/html/jonbobcar.com/public_html/industry.png")
    shutil.copy("/home/jonathon/neptune/science.png", "/var/www/html/jonbobcar.com/public_html/science.png")

    print("neptune_move.py")
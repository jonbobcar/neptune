import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
import pathlib
import csv
import datetime
from cycler import cycler
from matplotlib.ticker import MaxNLocator

path = str(pathlib.Path(__file__).parent.absolute()) + "/"
file_name = path + "stats.csv"

file_exists = os.path.isfile(file_name)

if file_exists:
    with open(file_name, "r") as f:
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
    time.append(datetime.datetime.strptime(entry, "%Y-%m-%d %H:%M:%S.%f").strftime("%A %H:%M"))

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
    "orange", "red", "fuchsia", "purple"
    ]
lines = [
    (0, (3, 5)), (0, (4, 5)), (0, (5, 5)), (0, (6, 5)),
    (0, (5, 3)), (0, (5, 4)), (0, (5, 5)), (0, (5, 6))
    ]
markers = [] 

t_label = fieldnames[0]

for plot in range(len(plots)):
    plt.rc('lines', linewidth=3)
    plt.rc('axes', prop_cycle=(cycler('color', colors[0:number_of_players]) +
                           cycler('linestyle', lines[0:number_of_players])))
    fig, ax = plt.subplots(figsize=(9,6))
    for _ in range(number_of_players):
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
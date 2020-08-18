import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import os
import pathlib
import csv
import datetime

path = str(pathlib.Path(__file__).parent.absolute()) + "/"
file_name = path + "stats.csv"

file_exists = os.path.isfile(file_name)

if file_exists:
    with open(file_name, "r") as f:
        csv_reader = csv.DictReader(f)
        csv_stats = list(csv_reader)
        fieldnames = csv_reader.fieldnames

now = datetime.datetime.now()
t = []
i = 0
s = []

number_of_players = int((len(fieldnames) - 1) / 5)
print(number_of_players)

for line in csv_stats:
    t.append(datetime.datetime.strptime(line["tick"], "%Y-%m-%d %H:%M:%S.%f"))

for field in fieldnames:
    if field != "tick":
        s.append(line[field])
print(s)
# print(t)

# Data for plotting

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()
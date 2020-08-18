import urllib.request, json, csv, datetime, pathlib, os

path = str(pathlib.Path(__file__).parent.absolute()) + "/"

with open(path + "trades.txt", "r") as f:
    trades = f.readlines()

with open(path + "neptune.csv", "r") as f:
    positions = f.readlines()

with open(path + "index.html", "w") as f:
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<body>\n")
    f.write("<h1>\n")
    f.write("Positions")
    f.write("</h1>\n")
    for line in positions:
        f.write("<p>" + line + "</p>")
    
#    f.write("<p1>\n")
#    f.write("<img src=\"stars.png\" alt=\"Stars\">\n")
#    f.write("<img src=\"ships.png\" alt=\"Stars\">\n")
#    f.write("<img src=\"economy.png\" alt=\"Stars\">\n")
#    f.write("<img src=\"industry.png\" alt=\"Stars\">\n")
#    f.write("<img src=\"science.png\" alt=\"Stars\">\n")
#    f.write("</p1>\n")
    
    f.write("<h1>\n")
    f.write("System Trades\n")
    f.write("</h1>\n")
    
    f.write("<p1>\n")
    f.write("Most Recent First")
    for line in reversed(trades):
        f.write("<p>" + line + "</p>")
    f.write("</p1>\n")
    f.write("</body>\n")
    f.write("</html>\n")

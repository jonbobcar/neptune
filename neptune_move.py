import shutil

def nep_copy():
    shutil.copy("/home/jonathon/neptune/index.html", "/var/www/html/jonbobcar.com/public_html/index.html")
    shutil.copy("/home/jonathon/neptune/stars.png", "/var/www/html/jonbobcar.com/public_html/stars.png")
    shutil.copy("/home/jonathon/neptune/ships.png", "/var/www/html/jonbobcar.com/public_html/ships.png")
    shutil.copy("/home/jonathon/neptune/economy.png", "/var/www/html/jonbobcar.com/public_html/economy.png")
    shutil.copy("/home/jonathon/neptune/industry.png", "/var/www/html/jonbobcar.com/public_html/industry.png")
    shutil.copy("/home/jonathon/neptune/science.png", "/var/www/html/jonbobcar.com/public_html/science.png")

    print("neptune_move.py")
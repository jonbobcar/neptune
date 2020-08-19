import time
import schedule
import shutil
import os

def job():
    import neptune
    import stats_plotter
    import neptune_to_html
    import neptune_move

    # shutil.copy("/home/jonathon/neptune/index.html", "/var/www/html/jonbobcar.com/public_html/index.html")
    # shutil.copy("/home/jonathon/neptune/stars.png", "/var/www/html/jonbobcar.com/public_html/stars.png")
    # shutil.copy("/home/jonathon/neptune/ships.png", "/var/www/html/jonbobcar.com/public_html/ships.png")
    # shutil.copy("/home/jonathon/neptune/economy.png", "/var/www/html/jonbobcar.com/public_html/economy.png")
    # shutil.copy("/home/jonathon/neptune/industry.png", "/var/www/html/jonbobcar.com/public_html/industry.png")
    # shutil.copy("/home/jonathon/neptune/science.png", "/var/www/html/jonbobcar.com/public_html/science.png")
    print("Ran the job")
    
schedule.every().hour.at(":54").do(job)
# schedule.every(20).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(5)
    
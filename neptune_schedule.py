import time
import schedule
import shutil

# cron job to copy index.html:
# */5 * * * * cp /home/jonathon/neptune/index.html /var/www/html/jonbobcar.com/public_html/

def job():
    import neptune
    import stats_plotter
    import neptune_to_html
    print("Ran the job")

    shutil.move("/home/jonathon/neptune/index.html", "/var/www/html/jonbobcar.com/public_html/index.html")
    shutil.move("/home/jonathon/neptune/stars.png", "/var/www/html/jonbobcar.com/public_html/stars.png")
    shutil.move("/home/jonathon/neptune/ships.png", "/var/www/html/jonbobcar.com/public_html/ships.png")
    shutil.move("/home/jonathon/neptune/economy.png", "/var/www/html/jonbobcar.com/public_html/economy.png")
    shutil.move("/home/jonathon/neptune/industry.png", "/var/www/html/jonbobcar.com/public_html/industry.png")
    shutil.move("/home/jonathon/neptune/science.png", "/var/www/html/jonbobcar.com/public_html/science.png")
    

schedule.every().hour.at(":54").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
    
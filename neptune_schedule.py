import time
import schedule

# cron job to copy index.html:
# */5 * * * * cp /home/jonathon/neptune/index.html /var/www/html/jonbobcar.com/public_html/

def job():
    import neptune
    import stats_plotter
    import neptune_to_html
    print("Ran the job")

schedule.every().hour.at(":54").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)

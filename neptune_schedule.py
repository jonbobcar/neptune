import time
import schedule
import shutil
import os

print(os.environ)

def job():
    import neptune
    import stats_plotter
    import neptune_to_html
    import neptune_move
    print("Ran the job")
    
schedule.every().hour.at(":54").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
    
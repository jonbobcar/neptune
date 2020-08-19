import time
import schedule
import shutil
import os
import neptune
import stats_plotter
import neptune_to_html
import neptune_move

def job():
    neptune.nep_get()
    stats_plotter.nep_plot()
    neptune_to_html.nep_html()
    neptune_move.nep_copy()
    
    print("Ran the job")
    
schedule.every().hour.at(":54").do(job)
# schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
    